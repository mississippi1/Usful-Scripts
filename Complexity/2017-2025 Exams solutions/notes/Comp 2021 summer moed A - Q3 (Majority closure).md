# Comp 2021 summer (קיץ) moed A — Q3 (9 pts, T/F+proof): REG closed under Majority(L1,L2,L3)

**Question.** For three languages L1, L2, L3 over Σ, define

    Majority(L1,L2,L3) = { w ∈ Σ* : at least two of L1, L2, L3 contain w }

Claim: the regular languages are closed under Majority, i.e. if L1, L2, L3 are regular then
Majority(L1,L2,L3) is regular. Mark correct/incorrect and prove.

Note: this exam PDF is not present in this repo's "2017-2025 Exams" folder.

## Answer: CORRECT (student's circled "נכונה" is right)

## Proof — reduce to known closure properties via a set identity

**Key identity.**

    Majority(L1, L2, L3) = (L1 ∩ L2) ∪ (L1 ∩ L3) ∪ (L2 ∩ L3)

Proof of the identity: fix w ∈ Σ* and let k = |{ i : w ∈ Li }| (how many of the three
contain w).
- If k ≥ 2: some pair {i,j} both contain w (pigeonhole on 3 sets with ≥2 hits), so
  w ∈ Li ∩ Lj, hence w is in the RHS.
- If k ≤ 1: no pair can both contain w (that would need k ≥ 2), so w is in none of the three
  pairwise intersections, hence not in the RHS.

So RHS membership holds exactly when k ≥ 2 — precisely the definition of Majority. ∎
(Brute-force verified against 2000 random triples of finite languages over {0,1}: no
mismatch between Majority(L1,L2,L3) and (L1∩L2)∪(L1∩L3)∪(L2∩L3).)

**Closing the proof.** L1, L2, L3 ∈ REG and REG is closed under intersection, so
L1∩L2, L1∩L3, L2∩L3 ∈ REG. REG is closed under union, so their union — which by the
identity IS Majority(L1,L2,L3) — is regular. ∎

## Equivalent explicit construction (product automaton)

Let A1=(Q1,Σ,δ1,q1,F1), A2=(Q2,Σ,δ2,q2,F2), A3=(Q3,Σ,δ3,q3,F3) be DFAs for L1,L2,L3. Build

    A = (Q1×Q2×Q3, Σ, δ, (q1,q2,q3), F)
    δ((p1,p2,p3), σ) = (δ1(p1,σ), δ2(p2,σ), δ3(p3,σ))
    F = { (p1,p2,p3) : at least two of p1∈F1, p2∈F2, p3∈F3 hold }

Running w through A computes (δ1*(q1,w), δ2*(q2,w), δ3*(q3,w)) — the three individual
acceptance verdicts, in parallel — and F accepts exactly when at least two of those
verdicts are "accept". So L(A) = Majority(L1,L2,L3), with |Q| = |Q1|·|Q2|·|Q3|, giving

    MN(Majority(L1,L2,L3)) ≤ MN(L1)·MN(L2)·MN(L3)

— the natural 3-way generalization of the MN(L1∩L2) ≤ MN(L1)·MN(L2) bound from the
2024-winter and 2025-summer MN worksheets (see the other "Comp ... - Q1 (Myhill-Nerode..."
and "(MN product bound...)" notes).

## Issues log

- **Q3** — Given as a marked-answer exam question (student circled "correct", wanted the
  proof). Resolved via the set identity
  Majority(L1,L2,L3) = (L1∩L2) ∪ (L1∩L3) ∪ (L2∩L3), reducing to REG's closure under
  intersection and union — no new construction strictly needed, though the explicit
  3-way product automaton (accepting states = triples where ≥2 components are accepting)
  gives the same result directly and the bound MN(Majority) ≤ MN(L1)·MN(L2)·MN(L3).
  Verified the set identity by brute force on 2000 random finite-language triples.
