# NP verifier characterization — Q3(a), 25 pts (study notes)

Source exam: **not identified.** The screenshot shows "שאלת משחק עם ההגדרות", question 3 (25 נק'),
part (א). A text search over every PDF in `Complexity/2017-2025 Exams/` and
`Complexity/2017-2025 Exams solutions/` found no match for this wording, so these notes are written
from the standard theorem rather than from an official solution. Update this header if the exam
turns up.

## The question

> Complete the following theorem to a **correct** statement: let Σ be an alphabet and L ⊆ Σ*.
> Then **L ∈ NP if and only if there exists a language L^π ∈ P with the following properties:**
> [box to fill]

## The completion

1. **L^π is a language of pairs:** L^π ⊆ { ⟨x, π⟩ : x, π ∈ Σ* }, under some poly-time computable
   pairing/encoding (Σ extended with a separator symbol).
2. **There is a polynomial p such that for every x ∈ Σ*:**

     x ∈ L  ⟺  ∃π ∈ Σ* with **|π| ≤ p(|x|)** and ⟨x, π⟩ ∈ L^π.

π is the certificate / witness — the letter stands for *proof*. L^π is the **verifier language**:
the set of (claim, proof) pairs in which the proof is valid.

Harmless WLOGs if a later part needs them: may require |π| = p(|x|) exactly (pad), and π ∈ {0,1}*.

## Why each clause is load-bearing (drop one → the theorem becomes false)

- **Drop the length bound |π| ≤ p(|x|), keep L^π ∈ P → the statement characterizes RE, not NP.**
  For any L ∈ RE recognized by M, let π be the *entire accepting computation history* of M on x.
  Checking a history is polynomial in the history's own length, so L^π ∈ P — yet L may be
  undecidable. The polynomial bound on the certificate is the sole thing pinning the class at NP.
- **Weaken L^π ∈ P to L^π ∈ R → the statement characterizes R.** With poly-bounded certificates one
  can enumerate all π with |π| ≤ p(|x|) and test each, so L is decidable; conversely any decidable L
  is captured with π = ε. Verification must be *efficient*, not merely effective.
- **Replace ∃π by ∀π** → that is the coNP-shaped statement, not NP.
- **Weaken ⟺ to ⟹** → trivially satisfied by L^π = Σ* × Σ*. The ⟸ direction is **soundness**: when
  x ∉ L, *no* π may be accepted. This is the half most often omitted, and where the points are.

## Proof of the equivalence (for the likely part (b))

**(⟹) L ∈ NP gives the verifier.** Let N be an NTM deciding L within p(n) steps, WLOG with branching
factor 2. Define

  L^π = { ⟨x, π⟩ : π ∈ {0,1}*, and the computation of N on x following the choice sequence π accepts }.

Each nondeterministic step consumes one bit of π, so |π| ≤ p(|x|). Simulating N on x along a **fixed**
choice sequence is deterministic and polynomial, so L^π ∈ P. Finally x ∈ L iff some branch of N
accepts iff such a π exists. ∎

**(⟸) The verifier gives an NTM.** On input x: nondeterministically write a string π of length
≤ p(|x|) (≤ p(|x|) steps), then run the poly-time decider of L^π on ⟨x, π⟩ and output its answer.
Total time polynomial; some branch accepts iff a valid certificate exists iff x ∈ L. ∎

Note how the two properties are consumed: the **length bound** makes the guessing phase polynomial,
and **L^π ∈ P** makes the checking phase polynomial.

## Exam checklist for this item

- [x] Say L^π is a language of **pairs** ⟨x, π⟩.
- [x] Quantify the certificate: **∃π**, with **|π| ≤ p(|x|)** for a polynomial p — state p explicitly.
- [x] Make it an **iff** (both completeness and soundness), not a one-way implication.
- [x] L^π ∈ P is given in the statement — don't restate it as "decidable".

---

## Issues log

Track here which parts gave trouble, and how they were resolved.

- **Q3(a) (how to complete "L ∈ NP iff ∃L^π ∈ P with the following properties"):** Resolved as the
  standard verifier/certificate characterization: L^π is a language of pairs ⟨x, π⟩, and there is a
  polynomial p with x ∈ L ⟺ ∃π, |π| ≤ p(|x|), ⟨x, π⟩ ∈ L^π. Points confirmed: the equivalence must be
  two-way (the ⟸ half is soundness — no certificate may be accepted for x ∉ L); the polynomial length
  bound is what keeps the class at NP (without it, computation histories as certificates make the
  statement characterize **RE**); and efficiency of the verifier is what keeps it below R (with L^π
  merely decidable, the statement characterizes **R**). Proof of both directions recorded: choice
  sequence of the NTM as certificate; guess-then-verify for the converse. Source exam could not be
  located in the repo.
