# Comp 2021 (קיץ 2021) moed A — Q6 (8 pts, T/F+proof): does A≤_mB imply B̄≤_mĀ?

Source exam: `Complexity/2017-2025 Exams/Comp 2021 Moed A.pdf` (page 7)
Official solution: `Complexity/2017-2025 Exams solutions/Comp 2021 moed A solution.pdf` (page 7)

**Question.** For a language L, write L̄ = Σ*\L. Let A,B be languages over Σ. Claim: if
there is a mapping reduction from A to B, then there is a mapping reduction from B̄ to Ā.
That is, if A≤_mB then B̄≤_mĀ. Prove or disprove.

Note on transcription: an initial reading of the screenshot misread the claim's direction as
"Ā≤_mB̄" (same-direction complementing, which would be trivially TRUE). Re-checking against
the exam and solution PDFs (rendered via pymupdf) confirmed the actual claim swaps sides:
"B̄≤_mĀ" — the target's complement reduces to the source's complement, roles reversed. That
swap is the entire point of the question.

## Answer: FALSE (student's circled "לא נכונה" is correct)

## Why the naively-true version doesn't apply

If the claim were "A≤_mB ⟹ Ā≤_mB̄" (same direction), it would be trivially true: A≤_mB
means some computable g satisfies w∈A ⟺ g(w)∈B; negating both sides of that biconditional
gives w∉A ⟺ g(w)∉B, i.e. w∈Ā ⟺ g(w)∈B̄ — the SAME g works, no new construction needed.

But the actual claim asks for B̄≤_mĀ — reversed direction. There's no reason the original
g:Σ*→Σ* (mapping A-instances to B-instances) should say anything about mapping
B-instances back to A-instances. Reductions are inherently asymmetric ("at least as hard
as"), and complementing both sides doesn't make that asymmetry reversible.

## Proof — counterexample using R and RE\R

Let A be any language in R (decidable — e.g. A=∅), and B any non-trivial language in RE\R
(e.g. B=A_TM).

**Step 1: A≤_mB holds** (standard fact). Since A∈R, decide w∈A directly. Since B is
non-trivial (B≠∅, B≠Σ*), fix w1∈B and w0∉B. Define:

    g(w) = w1   if w ∈ A
         = w0   if w ∉ A

g is computable (uses A's decision procedure) and w∈A ⟺ g(w)∈B by construction. So A≤_mB.

**Step 2: assume the claim holds — derive a contradiction.** The claim would give B̄≤_mĀ.

Since A∈R and R is closed under complement, Ā∈R. By the reduction theorem (X≤_mY and Y∈R
⟹ X∈R), B̄≤_mĀ with Ā∈R gives B̄∈R.

But R is closed under complement too, so B̄∈R ⟹ B∈R. This contradicts B∈RE\R (B∉R, by
choice). ∎

So the claim is false.

## Alternate proof (from the official solution) — using ALL_TM

A_TM≤_m ALL_TM is the standard reduction used in class to show ALL_TM∉RE∪coRE. If the
claim held, this would give (ALL_TM)̄ ≤_m (A_TM)̄.

RE∪coRE is closed under complement (X∈RE∪coRE ⟺ X̄∈RE∪coRE — complementing an RE set
gives a coRE set and vice versa, both inside RE∪coRE), and the reduction theorem applies to
RE∪coRE as a whole (X≤_mY, Y∈RE∪coRE ⟹ X∈RE∪coRE, splitting into the RE or coRE case for
Y). So the derived reduction (ALL_TM)̄≤_m(A_TM)̄ combined with (ALL_TM)̄∉RE∪coRE (since
ALL_TM∉RE∪coRE, by the complement-symmetry above) forces (A_TM)̄∉RE∪coRE, hence
A_TM∉RE∪coRE (again by symmetry).

But A_TM∈RE⊆RE∪coRE — contradiction. ∎

## Takeaway

Complementing both sides while keeping the same direction is free (just re-read the same
reduction function backwards). Complementing while also swapping which side reduces to
which is not — that would require the reduction to run in reverse, which nothing about
A≤_mB guarantees, and the R/RE\R asymmetry (decidable languages reduce TO undecidable ones,
never the other way) gives a clean, general counterexample.

## Issues log

- **Q6** — Own transcription error: initially misread the claim's direction from the
  screenshot as "Ā≤_mB̄" (same-direction complementing), which is trivially TRUE by simply
  negating both sides of the defining biconditional with the same reduction function.
  Re-verified against the exam and solution PDFs (rendered as images via pymupdf, since text
  extraction proved unreliable again) and confirmed the real claim is the direction-swapped
  "B̄≤_mĀ", which is FALSE — matching the circled answer. Proved via a clean R/RE\R
  counterexample (A∈R, B∈RE\R non-trivial: A≤_mB always holds via decide-and-map, but
  B̄≤_mĀ would force B∈R via the reduction theorem and R's closure under complement,
  contradicting B∉R), plus the official solution's alternate ALL_TM/A_TM-based proof.
