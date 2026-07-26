# Comp 2025 summer (קיץ) moed A — Q1 (12 pts, MN worksheet): can MN(L1)=MN(L2)=10 give MN(L1∩L2)=2025?

**Question.** Claim: there exist languages L1, L2 such that each has 10 Myhill–Nerode
equivalence classes, and the intersection L1 ∩ L2 has 2025 Myhill–Nerode equivalence
classes. Is the claim correct? Prove your answer.

Note: this exam PDF is not present in this repo (only "2017-2025 Exams" has a "Comp 2025-1
moed A/B/C" set, dated 2025.2.16 — winter, not summer). Filed alongside
"Comp 2025 summer moed A - Q3 (MN, finite-or-infinite dichotomy).md" from the same
"MN (קיץ 2025, מועד א')" worksheet.

## Answer: the claim is FALSE

## The tool: MN(L1 ∩ L2) ≤ MN(L1) · MN(L2)

Same fact used in "Comp 2024 winter moed A - Q1 (Myhill-Nerode, intersection).md" parts (b)
and (c) — restated self-contained here.

**Lemma.** For any L1, L2 ⊆ Σ*, MN(L1 ∩ L2) ≤ MN(L1) · MN(L2).

*Proof.* Let m = MN(L1), m' = MN(L2). Define

    Φ : Σ* → (Σ*/≡_{L1}) × (Σ*/≡_{L2}),   Φ(u) = ( [u]_{L1} , [u]_{L2} )

— at most m·m' possible outputs. If Φ(u) = Φ(v), then u, v lie together in some class C of
≡_{L1} and together in some class C' of ≡_{L2}, i.e. u, v ∈ C ∩ C'. For arbitrary z ∈ Σ*:

    uz ∈ L1 ∩ L2  ⟺ uz ∈ L1 ∧ uz ∈ L2  ⟺ vz ∈ L1 ∧ uz ∈ L2  ⟺ vz ∈ L1 ∧ vz ∈ L2  ⟺ vz ∈ L1 ∩ L2

(swap u for v in each conjunct via u ≡_{L1} v and u ≡_{L2} v, both true since u, v share a
class of each relation). So u ≡_{L1∩L2} v. Hence Φ determines the ≡_{L1∩L2} class: the map
(C, C') ↦ [u]_{L1∩L2} (any u ∈ C ∩ C') is a well-defined surjection from Image(Φ) onto
Σ*/≡_{L1∩L2}. A surjection cannot increase cardinality, so MN(L1 ∩ L2) ≤ m·m'. ∎

## Applying it

MN(L1) = MN(L2) = 10 forces MN(L1 ∩ L2) ≤ 10 · 10 = 100. Since 2025 > 100, it is impossible
for MN(L1) = MN(L2) = 10 and MN(L1 ∩ L2) = 2025 to hold simultaneously, for ANY choice of
L1, L2 — the lemma is unconditional (no regularity or other structural assumption needed).
**The claim is false.** ∎

## Why the bound is tight (so the disproof is really about arithmetic, not structure)

100 is achievable, not merely an upper limit. Over Σ = {a,b}:

    L1 = { w : |w| ≡ 0 (mod 10) }        (length-counter language, 10 classes)
    L2 = { w : #a(w) ≡ 0 (mod 10) }      (a-counter language, 10 classes)

Each has exactly 10 MN classes (minimal DFA = a 10-state counting cycle). L1 ∩ L2 tracks two
*independent* counters — |w| mod 10 and #a(w) mod 10 — because appending b changes only the
first, appending a changes both by 1 (letting either coordinate be corrected freely). All
10×10 = 100 combined states are reachable and pairwise distinguishable, so
MN(L1 ∩ L2) = 100 exactly.

Machine-verified with the analogous mod-3 construction (brute force, words up to length 8):
MN(L1) = 3, MN(L2) = 3, MN(L1 ∩ L2) = 9 = 3·3 — confirms the bound is achieved exactly, not
just an inequality.

So 100 is the *maximum* possible value of MN(L1 ∩ L2) once MN(L1) = MN(L2) = 10, and 2025
sits far above anything the construction can reach.

## Common wrong moves

- Trying to engineer L1, L2 to hit 2025 directly — impossible regardless of construction,
  since the lemma holds unconditionally for all L1, L2.
- Citing the bound but skipping the actual arithmetic check (10·10 = 100 < 2025) — the whole
  disproof is exactly that one inequality.
- The identical lemma and disproof (swap ∧ for the relevant connective in the unfolding step)
  disposes of the same claim if ∩ were replaced by ∪ or symmetric difference.

## Issues log

- **Q1** — Was unable to solve; needed to identify which tool applies. Resolved by reusing
  the product bound MN(L1 ∩ L2) ≤ MN(L1)·MN(L2) proved on the winter 2024 moed A MN
  worksheet (see "Comp 2024 winter moed A - Q1" notes): with MN(L1)=MN(L2)=10 this caps
  MN(L1 ∩ L2) at 100, and 2025 > 100 makes the claim false — no construction can evade an
  unconditional inequality. Confirmed the bound is tight (not just an upper limit) via a
  two-independent-counters construction, verified by brute force at modulus 3
  (MN(L1)=MN(L2)=3, MN(L1∩L2)=9).
