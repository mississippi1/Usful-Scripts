# Study guide — empty-language traps (when {⟨M⟩ : P(M)} is secretly ∅ or Σ*)

A recurring exam pattern: a classification question is dressed up in undecidability vocabulary
(coRE, "does not halt", Rice-shaped semantic property), you start building a reduction — and the
correct answer is **R**, because **no machine at all satisfies the condition** (so L = ∅) or
**every machine does** (so L = Σ*).

Both ∅ and Σ* are decidable by a constant machine. No reduction, no Rice, no dovetailing.

**The one question to ask before anything else:**

> Can I exhibit a single machine satisfying the property? Can I exhibit one violating it?
> If I cannot produce both, the language is probably trivial — and trivial means **R**.

---

## Family 1 — class-slice contradictions (the L(M) ∈ coRE ∖ R trap)

This is the most common form. It rests on two facts that are each one line, and lethal together.

### Fact 1: L(M) is **always** in RE

**Definitions.** L(M) = { w : M accepts w }. A language K is in **RE** iff there exists a TM that
**recognizes** it — i.e. accepts every w ∈ K, and does not accept any w ∉ K.

**Proof that L(M) ∈ RE.** The machine M itself recognizes L(M). By construction M accepts exactly
the words of L(M): if w ∈ L(M) then M accepts w (that is what membership means), and if w ∉ L(M)
then M does not accept w. So M is a recognizer for L(M), hence **L(M) ∈ RE**. ∎

It is that immediate — a definition unfolding, not a theorem.

> **The misconception that hides this.** Students think "but M might loop forever on some inputs, so
> it's not a *good* machine". Irrelevant. **Recognition never requires halting on non-members.** A
> recognizer must accept the members; on non-members it may reject *or run forever*, and both are
> fine. That looseness is exactly the difference between RE and R. So no matter how badly behaved M
> is — loops on half its inputs, never halts at all — the set of words it *does* accept is an RE
> language.

**Consequence (worth memorizing).** The set of languages of the form L(M) is *exactly* RE:

  **{ L(M) : M is a TM } = RE**

(⊆ is the fact above; ⊇ is the definition of RE — a language in RE has a recognizer M, and that M
has L(M) equal to it.) So a question about `L(M) ∈ 𝒞` is really a question about **𝒞 ∩ RE**.

### Fact 2: RE ∩ coRE = R

Recall coRE = { K : K̄ ∈ RE }.

**(⊇) R ⊆ RE ∩ coRE.** Let D be a decider for K — it halts on every input. Then D recognizes K, so
K ∈ RE. Swapping D's accept and reject states gives a decider for K̄ (legitimate precisely because D
always halts), so K̄ ∈ RE, i.e. K ∈ coRE. ∎

**(⊆) RE ∩ coRE ⊆ R.** Let M₁ recognize K and M₂ recognize K̄. Build D on input w:

> Run M₁ and M₂ **in parallel** — dovetail them, one step of M₁ then one step of M₂, alternating.
> If M₁ accepts, **accept**. If M₂ accepts, **reject**.

Every w lies in exactly one of K, K̄. If w ∈ K, then M₁ accepts w after finitely many steps, so the
interleaving reaches that point and D accepts. If w ∉ K then w ∈ K̄, so M₂ accepts after finitely
many steps and D rejects. Either way **D halts on every input**, and it answers correctly. So
K ∈ R. ∎

> **Why parallel simulation is essential.** Running M₁ to completion *first* and only then starting
> M₂ does not work: if w ∉ K, M₁ may run forever and M₂ never gets a turn. The dovetailing is the
> entire content of the proof — it is what converts "one of the two will halt" into "the combined
> machine always halts".

### The contradiction

Suppose some ⟨M⟩ satisfied **L(M) ∈ coRE ∖ R**. Then:

- L(M) ∈ coRE (given), and
- L(M) ∈ RE (Fact 1 — free, for every machine),

so by Fact 2, L(M) ∈ RE ∩ coRE = **R**. But `coRE ∖ R` explicitly excludes R. Contradiction. ∎

Equivalently, in one line:

  **RE ∩ (coRE ∖ R) = (RE ∩ coRE) ∖ R = R ∖ R = ∅**

So `{ ⟨M⟩ : L(M) ∈ coRE ∖ R } = ∅ ∈ R`.

The intuition to carry: **inside RE, "coRE" and "R" are the same thing.** The slice `coRE ∖ R` is
non-empty as a class of languages in general (Ā_TM lives there), but it becomes empty the moment you
restrict to languages that are somebody's L(M) — and every language named `L(M)` is.

### Master table — L = { ⟨M⟩ : L(M) ∈ 𝒞 } for the usual 𝒞

Compute 𝒞 ∩ RE first; everything follows.

| condition on L(M) | 𝒞 ∩ RE | resulting L | verdict |
|---|---|---|---|
| L(M) ∈ **RE** | RE | Σ* (all encodings) | **trivial → R** |
| L(M) ∈ **RE ∪ coRE** | RE | Σ* | **trivial → R** |
| L(M) ∈ **coRE ∖ R** | ∅ | ∅ | **trivial → R** ⚠ *the trap* |
| L(M) ∉ **RE** | ∅ | ∅ | **trivial → R** |
| L(M) ∈ **$\overline{RE ∪ coRE}$** | ∅ | ∅ | **trivial → R** |
| L(M) ∈ **R** | R | — | **hard** — coRE-hard, in fact Σ⁰₃-complete |
| L(M) ∈ **coRE** | R | same as the row above | **hard** (⟺ L(M) ∈ R) |
| L(M) ∈ **RE ∩ coRE** | R | same again | **hard** |
| L(M) ∈ **RE ∖ R** | RE ∖ R | "L(M) is undecidable" | **hard** (complement of the R row) |

**Read the table carefully — the near-misses are the point.** `L(M) ∈ coRE ∖ R` is empty, but
`L(M) ∈ coRE` is *not* trivial at all: it silently means `L(M) ∈ R`, one of the hardest properties
in the course. Removing "∖ R" flips the answer from a one-line R to a Σ⁰₃-complete monster. Similarly
`L(M) ∉ RE` is empty while `L(M) ∉ R` (= `L(M) ∈ RE ∖ R`) is hard.

*(The Σ⁰₃ claims are beyond course scope — see
`L(M) in R is coRE-hard - part (ג) (exam unidentified).md` for the coRE-hardness proof that is in
scope.)*

---

## Family 2 — bounded-computation contradictions

A clause that constrains a computation to **t steps** cannot see arbitrarily far into the input.

> **Lemma.** A TM head starts on cell 1 and moves one cell per step, so during t steps it reads only
> cells **1 … t**. Hence the configuration after t steps — in particular whether the machine has
> accepted — depends **only on the first t cells of the tape**.

So any property demanding that a t-step computation distinguish two inputs agreeing on their first
t cells is **unsatisfiable**.

**Canonical instance (Comp 2024 summer moed A, Q6).**

  L = { ⟨M⟩ : ∃σ such that M **accepts σσ in one step** but **does not halt on σσσσ** }

With t = 1 the outcome depends on cell 1 alone. Inputs σσ and σσσσ both have σ in cell 1. So if M
accepts σσ in one step — meaning q₀ = q_accept, or δ(q₀,σ) = (q_accept, γ, d) — then M accepts
*every* input beginning with σ within one step, σσσσ included. It therefore **halts** on σσσσ,
contradicting the second clause. No ⟨M⟩ qualifies: **L = ∅ ∈ R.**

The dressing ("does not halt on …") looks co-RE and invites a reduction. The step bound kills it
first.

---

## Family 3 — the dual trap: every machine qualifies

Same lesson, opposite side. If the property holds vacuously for all machines, L = Σ* ∈ R.

- `L(M) ∈ RE` — Fact 1, always true.
- `L(M) ⊆ Σ*` — always true.
- `M halts on w or M does not halt on w` — tautology; a disjunction that exhausts the cases.
- `|L(M)| ≥ 0`, `L(M) ∩ ∅ = ∅` — degenerate arithmetic/set conditions.

Check for this whenever a condition looks suspiciously easy to satisfy by *any* construction you try.

---

## The Rice connection — this is exactly Rice's missing hypothesis

**Rice's theorem.** If P is a **non-trivial semantic** property of TMs, then L_P = { ⟨M⟩ : L(M) ∈ P }
is **not** decidable.

"Non-trivial" means: **some** machine has the property and **some** machine lacks it. That hypothesis
is not decoration — it is precisely what these traps violate:

| situation | Rice applies? | answer |
|---|---|---|
| no machine has the property | **no** — trivial | L = ∅ ∈ **R** |
| every machine has it | **no** — trivial | L = Σ* ∈ **R** |
| property is **syntactic** (about δ, states, step counts — not about L(M)) | **no** — not semantic | usually decidable; check directly |
| some do, some don't, and it's about L(M) | **yes** | L ∉ R — then classify RE / coRE / neither |

So **verifying Rice's hypothesis and detecting the trap are literally the same check.** If you are
about to invoke Rice, you must exhibit M_yes and M_no anyway. Do that *first*, and the trap can
never catch you: the moment you fail to build one of them, you have your answer.

Note Family 2 fails *both* hypotheses at once — "accepts σσ in one step" is syntactic (it is about
δ and a step count, not about the language L(M)), and the property is also empty.

---

## Exam checklist

Before classifying any `{ ⟨M⟩ : … }` or `{ ⟨M,w⟩ : … }`:

1. **Build M_yes.** Actually try to write a machine satisfying the property. If every attempt
   self-destructs, look for a proof that none exists → **L = ∅ ∈ R**.
2. **Build M_no.** If every machine satisfies it → **L = Σ* ∈ R**.
3. **Intersect the named class with RE.** For any `L(M) ∈ 𝒞` condition, replace 𝒞 by 𝒞 ∩ RE and use
   `RE ∩ coRE = R`. Slices like `coRE ∖ R`, `$\overline{RE ∪ coRE}$`, `∉ RE` collapse to ∅.
4. **Unfold step bounds.** For any "in t steps" clause, remember it can only see cells 1…t; check
   whether the inputs being compared differ there at all.
5. **Only then** reach for Rice, reductions, or dovetailing.

Step 3 costs about ten seconds and is worth the full 7–14 points on these questions.

---

## Worked instances in this archive

| exam | question | property | why trivial | answer |
|---|---|---|---|---|
| **Comp 2025-2026 winter moed A** | Q5 | L(M) ∈ coRE ∖ R | RE ∩ coRE = R, and L(M) ∈ RE always | **R** (= ∅) |
| **Comp 2024 summer moed A** | Q6 | accepts σσ in 1 step, diverges on σσσσ | 1 step sees only cell 1; σσ and σσσσ agree there | **R** (= ∅) |

And the near-misses that are *genuinely* hard, for contrast:

| language | answer |
|---|---|
| { ⟨M⟩ : L(M) ∈ R } | coRE-hard; far outside RE ∪ coRE |
| { ⟨M⟩ : L(M) ∈ RE ∖ R } | hard (complement of the above) |
| { ⟨M,w⟩ : M accepts w and \|L(M)\| ≥ 2026 } | **RE ∖ R** (Comp 2025-2026 moed A Q6) — a real RE property, no collapse |
