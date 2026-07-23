# Comp 2025-1 moed A — Q5, Q6, Q8 (study notes)

*(Source: `Complexity/2017-2025 Exams/Comp 2025-1 moed A.pdf`, exam date 16.2.2025, מועד א.
Questions labeled "שאלה 5", "שאלה 6", "שאלה 8".)*

These are multiple-choice classification questions: pick the computability/complexity
class of the given language (Q5, Q6) or the truth-value of a claim (Q8), and prove it.

---

## Q5 (11 pts) — reversal-equality of two TMs

L = { ⟨M₁, M₂⟩ : M₁ and M₂ are TMs such that **L(M₁) = rev(L(M₂))** }

where rev(σ₁σ₂⋯σ_k) = σ_k⋯σ₂σ₁ and rev(K) = { rev(w) : w ∈ K } for a language K ⊆ Σ*.

**Answer: L ∉ RE ∪ coRE** (i.e. the option $\overline{RE ∪ coRE}$).

This is `EQ_TM` in disguise: rev is a computable involution on Σ*, so "L(M₁) = rev(L(M₂))"
is a language-equality condition, exactly as hard as equality of two recognized languages.
Both reductions below use a **trivial M₂** for which rev does nothing (rev(Σ*) = Σ*, rev(∅) = ∅),
so the reversal never even complicates the argument.

**L ∉ coRE — reduce A_TM ≤m L.**
Given ⟨M, w⟩, output ⟨M₁, M₂⟩ where
- M₁ on input x: erase x, simulate M on w, accept if M accepts. So L(M₁) = Σ* if M accepts w, else ∅.
- M₂ = accept-everything machine. L(M₂) = Σ*, so rev(L(M₂)) = Σ*.

Then ⟨M₁,M₂⟩ ∈ L ⟺ L(M₁) = Σ* ⟺ M accepts w. So A_TM ≤m L. Since A_TM ∉ coRE, **L ∉ coRE**.

**L ∉ RE — reduce Ā_TM ≤m L.**
Same M₁, but M₂ = reject-everything machine. L(M₂) = ∅, rev(L(M₂)) = ∅.
Then ⟨M₁,M₂⟩ ∈ L ⟺ L(M₁) = ∅ ⟺ M does **not** accept w. So Ā_TM ≤m L.
Since Ā_TM ∉ RE, **L ∉ RE**.

Both reductions are computable, so L ∉ RE and L ∉ coRE, hence **L ∉ RE ∪ coRE**. ∎

---

## Q6 (11 pts) — "accepts all words of some length n"

L = { ⟨M⟩ : M is a TM and **there exists n ≥ 0 such that M accepts all words of length n** }

**Answer: L ∈ RE ∖ R** (semi-decidable but not decidable).

**L ∈ RE — dovetail over n and over the finitely many words per length.**
Recognizer for ⟨M⟩: for n = 0, 1, 2, …, and for increasing step budgets, simulate M on **all**
|Σ|ⁿ words of length n in a dovetailed fashion; **accept ⟨M⟩ the moment, for some n, every one of the
|Σ|ⁿ words of length n has accepted.** "M accepts all words of length n" is a *finite* conjunction of
RE conditions (finite ∩ of RE is RE); "∃n" is a countable disjunction of RE conditions (∃/countable ∪
of RE is RE, via dovetailing). So L ∈ RE.

**L ∉ coRE — reduce A_TM ≤m L (so also L ∉ R).**
Given ⟨M, w⟩, output ⟨M'⟩ where M' on input x: simulate M on w, and accept x iff M accepts w.
- M accepts w ⇒ L(M') = Σ* ⇒ M' accepts all words of every length ⇒ ⟨M'⟩ ∈ L.
- M does not accept w ⇒ L(M') = ∅ ⇒ for every n (including n = 0, the single word ε) not all
  words of length n are accepted ⇒ ⟨M'⟩ ∉ L.

So A_TM ≤m L; since A_TM ∉ coRE, **L ∉ coRE**, hence L ∉ R.

Therefore **L ∈ RE ∖ R** — *not* $\overline{RE ∪ coRE}$. The existential "∃n … accepts all length-n
words" is exactly the shape that dovetailing recognizes, which pulls the language into RE. ∎

---

## Q8 — true / false / unknown claims (mark and prove all correct answers)

### Q8.א (9 pts) — claim: ALL_NFA ≤p PATH

ALL_NFA = { ⟨A⟩ : A is an NFA and L(A) = Σ* } is **PSPACE-complete** (NFA universality).
PATH (directed s–t reachability, STCON) is **NL-complete**, in particular PATH ∈ P.

**Answer: נכונותה לא ידועה (truth unknown) — the claim is *equivalent* to P = PSPACE.**

The claim is not merely *sufficient* for a collapse; it is **logically equivalent** to P = PSPACE:

> **ALL_NFA ≤p PATH ⟺ ALL_NFA ∈ P ⟺ P = PSPACE.**

**(⇒) claim ⇒ P = PSPACE.** A ≤p reduction to PATH puts **ALL_NFA ∈ P**: decide ⟨A⟩ by computing f(⟨A⟩)
in poly time, then solving PATH in poly time (PATH ∈ NL ⊆ P; P closed under ≤p). ALL_NFA is
PSPACE-complete, so every L ∈ PSPACE has L ≤p ALL_NFA ∈ P ⇒ L ∈ P ⇒ PSPACE ⊆ P, i.e. **P = PSPACE**.

**(⇐) P = PSPACE ⇒ claim.** Then ALL_NFA ∈ PSPACE = P. Key fact about **poly-time** reductions: to reduce
*any* B ∈ P to PATH, let f(x) = "decide x ∈ B in poly time, then output a fixed **yes**-instance of PATH
if yes, a fixed **no**-instance if no." That is poly-time and correct, so B ≤p PATH. With B = ALL_NFA,
the claim holds. (General phenomenon: ≤p is strong enough to *solve* the source and emit a canned
answer, so `A ≤p (any nontrivial P-language)` just means `A ∈ P` — PATH only needs one yes- and one
no-instance, which it has.)

P = PSPACE is open (believed false, unproven), so the claim's truth is **unknown**. It cascades
(P ⊆ NP ⊆ PSPACE = P): the claim entails **P = PSPACE ⇒ P = NP ⇒ NP = coNP ⇒ NP = PSPACE**. It does
**not** entail L = NL, and it is inconsistent with **P ≠ NP**.

**Why the Space-Hierarchy "impossibility" argument is wrong — and where it is right.** The tempting wrong
proof: "PATH is NL-ish, ALL_NFA needs poly space, and NL ⊊ PSPACE by the Space Hierarchy Theorem, so the
reduction is impossible ⇒ false." The flaw: **a ≤p reduction is time-bounded, not space-bounded** — it may
use poly space and need not respect either problem's space complexity. The Space Hierarchy Theorem
separates *space* classes (giving NL ⊊ PSPACE unconditionally) but says nothing about whether a
poly-*time* map between two problems exists; that is a time-vs-space question (P vs PSPACE), left open.
The instinct **is correct for the logspace version of the claim**:

| Claim | Truth | Why |
|---|---|---|
| **ALL_NFA ≤_L PATH** (logspace reduction) | **provably FALSE** | ≤_L to PATH ⇒ ALL_NFA ∈ NL; but ALL_NFA is PSPACE-complete and NL ⊊ PSPACE (Space Hierarchy) — contradiction. |
| **ALL_NFA ≤p PATH** (poly-time reduction) | **unknown** | ⟺ ALL_NFA ∈ P ⟺ P = PSPACE (open). |

So the whole question turns on the **reduction's resource bound**: under ≤_L the space separation forces
"false"; under ≤p a poly-time reduction can absorb the NL/P computation and the only barrier left is the
open P vs PSPACE question.

**"But doesn't reducing to the low-space PATH *solve* the space bound?" — No; nothing bypasses the
hierarchy.** The mechanism is how far membership travels across a reduction:

> If A ≤ᵣ B and B ∈ 𝒞, then A ∈ 𝒞 **only when 𝒞 is closed under ≤ᵣ**.

P is closed under ≤p; **NL is not**. So from ALL_NFA ≤p PATH and PATH ∈ NL ⊆ P you may only infer
ALL_NFA ∈ **P** — *not* ALL_NFA ∈ NL. PATH's low space does **not** propagate backward across a
poly-*time* reduction. Trace the actual cost: to decide ALL_NFA you (1) run f to *build* the PATH
instance ⟨G,s,t⟩, then (2) solve PATH. Step 2 is cheap *in |G|*, but step 1 runs in poly time and may
**write a poly-size G using poly work space** — you cannot ignore that cost. Composed, the procedure is
poly time **and poly space**. So it certifies ALL_NFA ∈ P (a poly-*space* class it already lived in — no
contradiction), adding only a *time* bound; no PSPACE computation is ever crammed into logspace. That is
why the consequence is P = PSPACE (time = space), never NL = PSPACE. Under **≤_L**, by contrast, NL *is*
closed, so PATH's cheapness *does* travel all the way down (ALL_NFA ∈ NL ⇒ NL = PSPACE), which is exactly
the contradiction that makes the logspace version provably false.

### Q8.ג (9 pts) — claim: K ∈ LOGSPACE

K = { ⟨A₁, A₂⟩ : A₁, A₂ are DFAs and there is a word in L(A₁)·L(A₂) } (· = concatenation).

**Answer: נכונותה לא ידועה (truth unknown) — the claim holds iff L = NL.**

Concatenation L(A₁)·L(A₂) is nonempty **iff both L(A₁) ≠ ∅ and L(A₂) ≠ ∅** (pick one word from each
and concatenate; if either factor is empty the product is empty). So
K = { ⟨A₁,A₂⟩ : L(A₁) ≠ ∅ **and** L(A₂) ≠ ∅ } — just DFA non-emptiness on both machines.

DFA non-emptiness = "is an accepting state reachable from the start state in the DFA's transition
graph" = directed reachability = **PATH**, which is **NL-complete**. So K is NL-complete (NL is closed
under the AND of two reachability checks). Hence **K ∈ LOGSPACE ⟺ L = NL**, which is an open problem —
so the truth is **unknown**.

**The containment direction that matters:** L ⊆ NL (deterministic logspace is *contained in*
nondeterministic logspace); equality is open. It is **not** the other way around — NL is not known to be
inside L, and an NL-complete problem sitting in L is exactly the statement L = NL.

---

## Issues log

- **Q5** — Answer bucket ($\overline{RE ∪ coRE}$) was correct, but the **problem was misread**: I thought
  the condition was "M₂ writes on its tape the reverse of what M₁ writes" (a per-run tape/output
  relationship), rather than the intended **language** condition L(M₁) = rev(L(M₂)), where
  rev(K) = { rev(w) : w ∈ K } reverses every accepted word. Resolved: this is `EQ_TM` up to a
  computable involution (rev), so ∉ RE ∪ coRE; the two reductions (A_TM ≤m L via accept-all M₂ ⇒ ∉coRE;
  Ā_TM ≤m L via reject-all M₂ ⇒ ∉RE) use a trivial M₂ where rev(Σ*) = Σ* and rev(∅) = ∅, so the reversal
  is irrelevant to the hardness.

- **Q6** — Answered $\overline{RE ∪ coRE}$; **correct is RE ∖ R**. Mistake: treated "∃n such that M
  accepts all words of length n" as if it were as hard as an ALL_TM-style property (outside RE ∪ coRE).
  Resolved: it is **recognizable** — "M accepts all |Σ|ⁿ length-n words" is a finite ∩ of RE conditions,
  and "∃n" is a countable ∪ of RE conditions, so dovetailing over n and over the words recognizes L ⇒
  L ∈ RE. A_TM ≤m L (M' accepts everything iff M accepts w) shows L ∉ coRE, so L ∈ RE ∖ R. Takeaway:
  an **existential** "∃n / ∃w …" over a semi-decidable condition usually lands in RE, not outside it.

- **Q8.א** — Answered **"false" (ב)**, arguing from the **Space Hierarchy Theorem**: PATH is NL-complete
  (logspace-ish), ALL_NFA needs polynomial space, so "the reduction can't happen." **This is wrong.**
  Resolved: ALL_NFA ≤p PATH is a poly-**time** reduction, so it would only give ALL_NFA ∈ P, and since
  ALL_NFA is PSPACE-complete that means **P = PSPACE** — an *open* problem, so the claim's truth is
  **unknown** (answer ג), and it would entail P = PSPACE (cascading to P = NP, NP = coNP, NP = PSPACE).
  The Space Hierarchy Theorem separates *space* classes (NL ⊊ PSPACE) and never rules out a poly-time
  map between problems; conflating the reduction's time budget with the problems' space complexity was
  the error.

- **Q8.א (follow-up)** — Asked for a deeper walkthrough. Two clarifications added to the Q8.א section:
  (1) the claim is not just *sufficient* for a collapse — it is **equivalent** to P = PSPACE
  (ALL_NFA ≤p PATH ⟺ ALL_NFA ∈ P ⟺ P = PSPACE), because a poly-time reduction can internally decide
  any P-language and map to a fixed yes/no PATH instance, so `A ≤p (nontrivial P-language)` ⟺ `A ∈ P`;
  (2) the space-hierarchy instinct is actually **correct for the logspace version**: ALL_NFA ≤_L PATH is
  *provably false* (it would give ALL_NFA ∈ NL, contradicting NL ⊊ PSPACE), whereas ALL_NFA ≤p PATH is
  *unknown*. The trap is the reduction's resource bound — ≤_L forces "false", ≤p leaves it open at P vs
  PSPACE.

- **Q8.א (follow-up 2)** — "How does the poly reduction *solve* the space constraint?" It doesn't — the
  confusion is expecting PATH's low space to transfer back to ALL_NFA. Resolved: membership transfers
  across A ≤ᵣ B only when the target class is **closed under ≤ᵣ**. P is closed under ≤p, **NL is not**,
  so ALL_NFA ≤p PATH yields only ALL_NFA ∈ **P**, never ALL_NFA ∈ NL. Building the PATH instance already
  costs poly time and poly space, so the composed decider is poly-space (a class ALL_NFA was always in —
  no contradiction) plus a new poly-*time* bound ⇒ P = PSPACE, not NL = PSPACE. The Space Hierarchy
  (NL ⊊ PSPACE) is never touched. Only under ≤_L (NL *is* closed) does PATH's cheapness reach NL and
  trigger the contradiction — which is why the logspace version is provably false.

- **Q8.ג** — Got the **L vs NL containment backwards**: I thought "LOGSPACE contains NL." The correct
  direction is **L ⊆ NL** (deterministic logspace ⊆ nondeterministic logspace), with equality open.
  Resolved: K reduces to DFA non-emptiness of both automata (L(A₁)·L(A₂) ≠ ∅ ⟺ both factors nonempty),
  and DFA non-emptiness = directed reachability = PATH = NL-complete. So K is NL-complete and
  **K ∈ LOGSPACE ⟺ L = NL** — truth unknown.
