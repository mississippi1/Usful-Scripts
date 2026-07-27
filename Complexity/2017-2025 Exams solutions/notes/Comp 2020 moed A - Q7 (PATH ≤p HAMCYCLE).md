# Comp 2020 Moed A (חורף) — Question 7 (study notes)

Source exam: `Complexity/2017-2025 Exams/Comp 2020 moed A.pdf`, חלק III, Q7 (7 pts).
Official solution: `Complexity/2017-2025 Exams solutions/Comp 2020 moed A solution.pdf`.

## Q7 — the claim

> **Claim:** PATH ≤p HAMCYCLE
>
> PATH = { ⟨G,s,t⟩ : G is a directed graph containing a path from s to t }
> HAMCYCLE = { ⟨G⟩ : G is a directed graph containing a Hamiltonian cycle }

Answer format: mark **נכונה / לא נכונה / לא ידוע**, and if "לא ידוע", circle which of
P=NP, P≠NP, NP=coNP, NP=NL, P=PSPACE would follow from the claim being true.

## Answer

**נכונה (TRUE), unconditionally.** Nothing is circled — no assumption is needed, since the claim is
provable outright.

## Proof 1 (the "textbook" one-liner)

- PATH ∈ NL ⊆ P ⊆ **NP**. (Reachability: BFS/DFS from s, accept iff t is reached.)
- HAMCYCLE is **NP-hard** (known theorem from the course).
- By definition of NP-hardness, **every** L ∈ NP satisfies L ≤p HAMCYCLE. In particular PATH ≤p HAMCYCLE. ∎

## Proof 2 (explicit reduction — the one worth writing on the exam)

**Lemma.** If A ∈ P and B is *non-trivial* (i.e. B ≠ ∅ and B ≠ Σ*), then A ≤p B.

*Proof.* Since B is non-trivial, fix once and for all two constant strings y_yes ∈ B and y_no ∉ B.
Define

  f(x) = y_yes if x ∈ A,  f(x) = y_no if x ∉ A.

f is computable in polynomial time: run the poly-time decider for A on x, then print one of two
**hard-coded constant** strings (constants, so printing them costs O(1)). And x ∈ A ⟺ f(x) ∈ B by
construction. ∎

**Applying it here.**

- A = PATH ∈ P: on ⟨G,s,t⟩ run BFS/DFS from s in O(|V|+|E|) time and check whether t is reached.
- B = HAMCYCLE is non-trivial:
  - **yes-instance** G_yes = the 2-cycle: V = {1,2}, E = {(1,2),(2,1)}. The cycle 1→2→1 visits every
    vertex exactly once, so ⟨G_yes⟩ ∈ HAMCYCLE. (Using a 2-cycle rather than a single self-loop
    vertex avoids any quibble about whether a self-loop counts as a cycle.)
  - **no-instance** G_no = V = {1,2}, E = ∅. No edges at all, so no cycle, so ⟨G_no⟩ ∉ HAMCYCLE.

So the reduction, spelled out, is: **on input x**
1. If x is not a well-formed encoding ⟨G,s,t⟩ of a directed graph with two marked vertices, output ⟨G_no⟩.
2. Otherwise run BFS from s in G.
3. If t was reached, output ⟨G_yes⟩; else output ⟨G_no⟩.

Runs in polynomial (in fact linear) time, and x ∈ PATH ⟺ f(x) ∈ HAMCYCLE. ∎

## Why this is not "cheating", and why no assumption is needed

The trap in the question is the intuition *"PATH is easy and HAMCYCLE is hard, so surely you can't
reduce one to the other without P=NP."* That gets the direction of a Karp reduction backwards:

- A ≤p B means **"A is no harder than B"**. Reducing an *easy* language to a *hard* one is the
  harmless direction and is always fine.
- The direction that would be explosive is the other one: **HAMCYCLE ≤p PATH** would put an
  NP-complete language in P (PATH ∈ P and P is closed under ≤p), giving **P = NP**. *That* is the
  claim where you'd mark "לא ידוע" and circle P = NP.

Also note the definition of a Karp reduction places no restriction on the reduction "doing the work"
itself — f may decide A internally. That is exactly why every language in P reduces to every
non-trivial language, and it is a standard, accepted argument.

Two degenerate cases the lemma legitimately excludes (worth a sentence if you want full rigor):
B = ∅ and B = Σ* have no reduction *into* them from any non-trivial A. HAMCYCLE is neither, as
witnessed by G_yes and G_no above.

## Exam checklist for this item

- [x] Mark **נכונה**; circle nothing among P=NP / P≠NP / NP=coNP / NP=NL / P=PSPACE.
- [x] Justify: PATH ∈ P (BFS), HAMCYCLE non-trivial → constant-output reduction; or PATH ∈ NP +
      HAMCYCLE NP-hard.
- [x] Exhibit the two concrete constants G_yes, G_no — don't just assert non-triviality.
- [x] Say explicitly that the reduction runs in poly time.

---

## Issues log

Track here which parts gave trouble, and how they were resolved.

- **Q7 (PATH ≤p HAMCYCLE — true, false, or unknown?):** Resolved as **נכונה, unconditionally**,
  with nothing circled. Confusion came from reading ≤p as "same difficulty" and expecting that
  linking an easy language to an NP-complete one must need P=NP. Clarified: A ≤p B means A is *no
  harder than* B, so easy→hard is always allowed. Two proofs recorded: (1) PATH ∈ NL ⊆ P ⊆ NP and
  HAMCYCLE is NP-hard, so every NP language reduces to it; (2) explicit reduction — decide PATH by
  BFS in poly time and output one of two hard-coded constants, ⟨G_yes⟩ = 2-cycle on {1,2} or
  ⟨G_no⟩ = two vertices with no edges — which relies only on HAMCYCLE being non-trivial. Contrast
  noted for the mirror-image exam item: **HAMCYCLE ≤p PATH** is the one that is "לא ידוע" and would
  imply **P = NP**.
