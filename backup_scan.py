#!/usr/bin/env python3
"""
Scan a drive before a PC migration and report what is worth backing up.

Reads only filesystem metadata - names, sizes, timestamps. It never opens a
file, never reads file contents, and never deletes, moves or modifies
anything. The output is a prioritised report, not an action.

The classification is a heuristic based on paths and extensions, so it is
deliberately biased toward keeping things: when a file is ambiguous it lands
in REVIEW rather than SKIP. Backing up junk wastes disk space; skipping the
one folder that mattered loses it permanently. Treat the SKIP tier as a
suggestion to eyeball, not a verdict.

Usage:
  python backup_scan.py                          # scan your home directory
  python backup_scan.py /path/to/drive
  python backup_scan.py --csv manifest.csv       # full per-file manifest
  python backup_scan.py --top 40                 # show more per tier
  python backup_scan.py --client-pattern acme --client-pattern "q3 report"
"""

import argparse
import csv
import os
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

# --- Tiers, most important first -------------------------------------------

KEEP = "KEEP"        # unique and unrecoverable if lost
REVIEW = "REVIEW"    # ambiguous, decide by hand
SKIP = "SKIP"        # regenerable or re-downloadable
CLIENT = "CLIENT"    # client data reports - flagged, per your instruction

TIER_ORDER = [KEEP, REVIEW, CLIENT, SKIP]

TIER_BLURB = {
    KEEP: "Unique and unrecoverable. Back these up.",
    REVIEW: "Ambiguous. Look at this list yourself before deciding.",
    CLIENT: "Matched a client-report pattern. Low priority, but check the list.",
    SKIP: "Regenerable or re-downloadable. Listed so nothing vanishes silently.",
}

# --- Classification tables -------------------------------------------------

# Directory names whose entire subtree is regenerable.
SKIP_DIRS = {
    "node_modules", "__pycache__", ".venv", "venv", "env", ".tox",
    ".mypy_cache", ".pytest_cache", ".ruff_cache", ".gradle", ".cache",
    ".npm", ".nuget", ".yarn", ".pnpm-store", "site-packages",
    ".next", ".nuxt", ".parcel-cache", ".turbo", ".terraform",
    "bower_components", "vendor", "Pods", "DerivedData",
    "$RECYCLE.BIN", "System Volume Information", "Windows", "WinSxS",
    "Program Files", "Program Files (x86)", "ProgramData",
}

# Same idea, but matched on a path fragment rather than a single component.
SKIP_PATH_FRAGMENTS = (
    os.path.join("Library", "Caches"),
    os.path.join("AppData", "Local", "Temp"),
    os.path.join("AppData", "Local", "Microsoft", "Windows", "INetCache"),
    os.path.join(".local", "share", "Trash"),
    os.path.join(".git", "objects"),
)

TRASH_DIRS = {".Trash", ".Trash-1000", "Trash", "RecycleBin"}

# Build output. Only skipped when the directory sits inside a project, which
# is checked at match time - a bare "build" folder in Documents is not junk.
BUILD_DIRS = {"build", "dist", "target", "out", "obj", ".build"}

PROJECT_MARKERS = {
    ".git", "package.json", "pyproject.toml", "setup.py", "Cargo.toml",
    "pom.xml", "build.gradle", "Makefile", "CMakeLists.txt", "go.mod",
    ".csproj", ".sln",
}

KEEP_EXTS = {
    # documents
    ".doc", ".docx", ".odt", ".rtf", ".pdf", ".txt", ".md", ".tex", ".bib",
    ".pages", ".epub", ".one", ".wpd",
    # spreadsheets and slides
    ".xls", ".xlsx", ".xlsm", ".ods", ".csv", ".tsv", ".ppt", ".pptx",
    ".odp", ".key", ".numbers",
    # images
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".heic", ".heif", ".webp",
    ".tif", ".tiff", ".svg", ".psd", ".ai", ".xcf", ".sketch", ".fig",
    # camera raw
    ".raw", ".cr2", ".cr3", ".nef", ".arw", ".dng", ".orf", ".rw2", ".raf",
    # audio and video
    ".mp3", ".m4a", ".aac", ".flac", ".wav", ".ogg", ".opus", ".aiff",
    ".mp4", ".mov", ".avi", ".mkv", ".wmv", ".m4v", ".webm",
    # source code and notebooks
    ".py", ".ipynb", ".js", ".jsx", ".ts", ".tsx", ".java", ".kt", ".c",
    ".cpp", ".cc", ".h", ".hpp", ".cs", ".go", ".rs", ".rb", ".php",
    ".swift", ".scala", ".sh", ".bash", ".zsh", ".ps1", ".pl", ".lua",
    ".r", ".m", ".sql", ".html", ".css", ".scss", ".vue", ".ml", ".hs",
    # keys, certificates, password vaults
    ".pem", ".key", ".ppk", ".gpg", ".asc", ".kdbx", ".kdb", ".p12",
    ".pfx", ".crt", ".cer", ".jks", ".keystore", ".ovpn", ".enc",
    # mail and local databases
    ".pst", ".ost", ".mbox", ".eml", ".msg", ".db", ".sqlite", ".sqlite3",
    # design, CAD, research
    ".dwg", ".dxf", ".stl", ".step", ".blend", ".sav", ".dta", ".rdata",
}

REVIEW_EXTS = {
    ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".tgz",
    ".json", ".xml", ".yaml", ".yml", ".ini", ".cfg", ".conf", ".toml",
    ".bak", ".old", ".vmdk", ".vdi", ".qcow2", ".ova", ".img",
}

SKIP_EXTS = {
    ".tmp", ".temp", ".log", ".cache", ".swp", ".swo", ".part", ".crdownload",
    ".pyc", ".pyo", ".pyd", ".o", ".a", ".obj", ".class", ".lock",
    ".iso", ".dmg", ".exe", ".msi", ".pkg", ".deb", ".rpm", ".appimage",
    ".dll", ".so", ".dylib", ".lib", ".map", ".dSYM",
}

NOISE_NAMES = {".DS_Store", "Thumbs.db", "desktop.ini", "._.DS_Store"}

DEFAULT_CLIENT_PATTERNS = [
    "client report", "client_report", "client-report",
    "clientreport", "client data", "client_data",
]

# Directories under the scan root that are usually pure gold.
HIGH_VALUE_DIRS = {
    "documents", "desktop", "pictures", "photos", "movies", "music",
    "projects", "code", "src", "dev", "workspace", "repos",
}


def human(size):
    """Format a byte count."""
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024 or unit == "TB":
            return f"{size:.1f} {unit}" if unit != "B" else f"{size} B"
        size /= 1024


def is_inside_project(directory):
    """True if this directory or a parent looks like a source project."""
    current = directory
    for _ in range(6):  # don't walk all the way to /
        try:
            names = set(os.listdir(current))
        except OSError:
            return False
        if names & PROJECT_MARKERS:
            return True
        if any(n.endswith((".csproj", ".sln")) for n in names):
            return True
        parent = os.path.dirname(current)
        if parent == current:
            return False
        current = parent
    return False


def should_prune(dirname, full_path):
    """Whether to skip descending into a directory entirely."""
    if dirname in SKIP_DIRS or dirname in TRASH_DIRS:
        return True
    if any(frag in full_path for frag in SKIP_PATH_FRAGMENTS):
        return True
    if dirname in BUILD_DIRS and is_inside_project(os.path.dirname(full_path)):
        return True
    return False


def classify(path, name, client_patterns):
    """Return (tier, reason) for one file, using its name and path only."""
    lowered = name.lower()
    lowered_path = path.lower()
    ext = os.path.splitext(lowered)[1]

    if name in NOISE_NAMES:
        return SKIP, "OS metadata file"

    for pattern in client_patterns:
        if pattern in lowered or pattern in lowered_path:
            return CLIENT, f"matched client pattern {pattern!r}"

    if ext in SKIP_EXTS:
        return SKIP, f"{ext} is regenerable or re-downloadable"

    if ext in KEEP_EXTS:
        return KEEP, f"{ext} is user-created content"

    if ext in REVIEW_EXTS:
        return REVIEW, f"{ext} could be either - check by hand"

    if lowered.startswith(".") and ext == "":
        return REVIEW, "dotfile - config, may be worth keeping"

    if any(f"{os.sep}{d}{os.sep}" in lowered_path for d in HIGH_VALUE_DIRS):
        return REVIEW, "unknown type in a high-value folder"

    if ext == "":
        return REVIEW, "no extension - unidentifiable without opening it"

    return REVIEW, f"unrecognised type {ext}"


def scan(root, client_patterns, follow_symlinks=False):
    """Walk the tree, collecting metadata only. Returns (files, stats)."""
    files = []
    stats = {"dirs": 0, "pruned": 0, "errors": 0}
    root = os.path.abspath(root)

    for dirpath, dirnames, filenames in os.walk(
        root, topdown=True, followlinks=follow_symlinks
    ):
        stats["dirs"] += 1

        kept_dirs = []
        for d in dirnames:
            if should_prune(d, os.path.join(dirpath, d)):
                stats["pruned"] += 1
            else:
                kept_dirs.append(d)
        dirnames[:] = kept_dirs

        for filename in filenames:
            full = os.path.join(dirpath, filename)
            try:
                info = os.lstat(full)
            except OSError:
                stats["errors"] += 1
                continue

            # Skip symlinks: the target gets counted where it actually lives.
            if os.path.islink(full):
                continue

            tier, reason = classify(full, filename, client_patterns)
            files.append({
                "path": full,
                "size": info.st_size,
                "modified": datetime.fromtimestamp(info.st_mtime),
                "tier": tier,
                "reason": reason,
            })

    return files, stats


def find_git_repos(root):
    """Locate git working copies so the user can confirm they are pushed."""
    repos = []
    for dirpath, dirnames, _ in os.walk(root, topdown=True):
        if ".git" in dirnames:
            repos.append(dirpath)
            dirnames[:] = []  # don't descend into a repo we've found
            continue
        dirnames[:] = [
            d for d in dirnames if not should_prune(d, os.path.join(dirpath, d))
        ]
    return repos


def report(files, stats, root, top_n, git_repos):
    """Print the prioritised summary."""
    by_tier = defaultdict(list)
    for entry in files:
        by_tier[entry["tier"]].append(entry)

    total_size = sum(f["size"] for f in files)

    print("=" * 72)
    print(f"Backup scan of {root}")
    print(f"{len(files):,} files, {human(total_size)} across "
          f"{stats['dirs']:,} directories")
    print(f"{stats['pruned']:,} regenerable directories pruned, "
          f"{stats['errors']:,} unreadable entries skipped")
    print("Metadata only - no file contents were read.")
    print("=" * 72)

    for tier in TIER_ORDER:
        entries = by_tier.get(tier, [])
        if not entries:
            continue
        tier_size = sum(e["size"] for e in entries)
        print(f"\n{tier}  -  {len(entries):,} files, {human(tier_size)}")
        print(f"  {TIER_BLURB[tier]}")

        # Roll up to folders: a per-file list is unreadable at this scale.
        folders = defaultdict(lambda: {"size": 0, "count": 0})
        for entry in entries:
            folder = os.path.dirname(entry["path"])
            folders[folder]["size"] += entry["size"]
            folders[folder]["count"] += 1

        ranked = sorted(
            folders.items(), key=lambda kv: kv[1]["size"], reverse=True
        )
        for folder, data in ranked[:top_n]:
            shown = os.path.relpath(folder, root)
            print(f"    {human(data['size']):>10}  "
                  f"{data['count']:>6} files  {shown}")
        if len(ranked) > top_n:
            print(f"    ... and {len(ranked) - top_n:,} more folders")

    if git_repos:
        print(f"\nGIT REPOSITORIES  -  {len(git_repos)} found")
        print("  Confirm each is committed and pushed before you wipe the "
              "old machine.")
        print("  Uncommitted work and unpushed branches exist only here.")
        for repo in git_repos[:top_n]:
            print(f"    {os.path.relpath(repo, root)}")
        if len(git_repos) > top_n:
            print(f"    ... and {len(git_repos) - top_n} more")

    print("\n" + "-" * 72)
    print("Not covered by any file scan - collect these by hand:")
    print("  - Browser profiles: bookmarks, saved passwords, open tabs")
    print("  - 2FA authenticator seeds (re-enrol before wiping the old PC)")
    print("  - Software licence keys and account logins")
    print("  - Application settings that live in the cloud or the registry")
    print("  - SSH keys and cloud CLI credentials (~/.ssh, ~/.aws, ~/.config)")
    print("-" * 72)
    print("Nothing was deleted, moved or modified by this scan.")


def write_csv(files, root, csv_path):
    """Write the full per-file manifest."""
    with open(csv_path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["tier", "size_bytes", "modified", "reason", "path"])
        for entry in sorted(
            files, key=lambda e: (TIER_ORDER.index(e["tier"]), -e["size"])
        ):
            writer.writerow([
                entry["tier"],
                entry["size"],
                entry["modified"].isoformat(timespec="seconds"),
                entry["reason"],
                os.path.relpath(entry["path"], root),
            ])
    print(f"\nFull manifest written to {csv_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Report which files are worth backing up before a PC "
                    "migration. Read-only, metadata only.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "root", nargs="?", default=str(Path.home()),
        help="directory to scan (default: your home directory)",
    )
    parser.add_argument(
        "--csv", metavar="FILE",
        help="also write a full per-file manifest to this CSV",
    )
    parser.add_argument(
        "--top", type=int, default=20, metavar="N",
        help="folders to list per tier (default: 20)",
    )
    parser.add_argument(
        "--client-pattern", action="append", default=None, metavar="TEXT",
        help="filename/path substring marking a client data report; repeat "
             "to add several (default: several 'client report' variants)",
    )
    parser.add_argument(
        "--follow-symlinks", action="store_true",
        help="follow symlinks (off by default - risks loops and double counts)",
    )
    args = parser.parse_args()

    if not os.path.isdir(args.root):
        print(f"Error: '{args.root}' is not a directory.")
        sys.exit(1)

    patterns = [
        p.lower() for p in (args.client_pattern or DEFAULT_CLIENT_PATTERNS)
    ]

    print(f"Scanning {os.path.abspath(args.root)} ... "
          "(large drives take a few minutes)")
    files, stats = scan(args.root, patterns, args.follow_symlinks)

    if not files:
        print("No files found.")
        return

    git_repos = find_git_repos(os.path.abspath(args.root))
    report(files, stats, os.path.abspath(args.root), args.top, git_repos)

    if args.csv:
        write_csv(files, os.path.abspath(args.root), args.csv)


if __name__ == "__main__":
    main()
