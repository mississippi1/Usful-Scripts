# Comp 2020 summer (קיץ) moed B — Part II, Q5-Q6 (11 pts each): classifying languages in RE/coRE/R

Note: Q5's screenshot had no visible exam header (just "חלק II (26 נק') / 5. (11 נק')"), but
given identical point values, consecutive numbering, and Q6 explicitly headed
"שאלת סיווג מחלקות (מועד ב' קיץ 2020)", Q5 is very likely Part II Q5 of the same
"2020 summer moed B" exam as the MARK questions (see the "Q2-Q3 (MARK closure both
directions).md" note) — filed here on that assumption; correct if wrong. This exam PDF is
not present in this repo's "2017-2025 Exams" folder either way.

## Q5 (11 pts): L = {⟨M1,M2⟩ : ∀w∈Σ*, (M1 accepts w within 1000 steps) → (w∈L(M2))}

**Question.** To which class does L belong?

### Reading the logical structure

Define S = { w : M1 accepts w within 1000 steps }. The statement
"∀w, A(w)→B(w)" is exactly the standard translation of the subset relation S ⊆ L(M2):
∀x(x∈S → x∈T) means S⊆T. Per-word truth table: A(w)→B(w) is false in exactly one case —
A(w) true, B(w) false, i.e. w∈S but w∉L(M2). So ⟨M1,M2⟩∉L exactly when M1 accepts some w
quickly that M2 doesn't accept at all.

### Why "1000 steps" specifically

This bound makes A(w) = "M1 accepts w within 1000 steps" DECIDABLE (bounded simulation,
always halts). But decidable does NOT mean S is finite: M1 = "immediately accept every
input" gives S = Σ* (infinite). So S ranges over all decidable sets achievable this way,
including infinite/cofinite ones, while L(M2) is an arbitrary RE language. That combination
— ∀w over a possibly-infinite decidable set, checking membership in a merely-RE language —
is what pushes this out of both RE and coRE.

### Classification: L is neither RE nor coRE

Fix M1★ = the trivial machine that accepts every input in 1 step. Then

    ⟨M1★, M2⟩ ∈ L  ⟺  ∀w (true → w∈L(M2))  ⟺  L(M2) = Σ*  ⟺  ⟨M2⟩ ∈ ALL_TM

So f(⟨M2⟩) = ⟨M1★, M2⟩ is a mapping reduction ALL_TM ≤m L. ALL_TM = {⟨M⟩ : L(M)=Σ*} is a
classical example that is neither RE nor coRE:

- **ALL_TM ∉ RE**: reduce co-A_TM (∉RE) to it. Given ⟨M,w⟩, build M' that on input x
  simulates M on w for |x| steps and accepts x iff M has NOT yet accepted w within that
  many steps. If M never accepts w, M' accepts every x (L(M')=Σ*). If M accepts w at step
  t, M' rejects every x with |x|≥t (L(M')≠Σ*). So co-A_TM ≤m ALL_TM ⟹ ALL_TM ∉ RE.
- **ALL_TM ∉ coRE**: reduce A_TM (∉coRE) to it. Given ⟨M,w⟩, build M'' that on input x
  ignores x and simulates M on w; if/when M accepts w, M'' accepts x. If M accepts w,
  L(M'')=Σ*; if not, L(M'')=∅≠Σ*. So A_TM ≤m ALL_TM ⟹ ALL_TM ∉ coRE.

Since ALL_TM ≤m L (via the fixed M1★ embedding) and ALL_TM is neither RE nor coRE:

    L ∉ RE   and   L ∉ coRE

## Q6 (11 pts): L3 = {⟨M⟩ : M halts on every w∈Σ* within |w| steps}

**Question.** Which class does L3 belong to: complement(RE∪coRE), coRE\R, RE\R, or R?

**Answer: coRE\R** (student's circled answer is correct).

### Step 1 — L3 ∈ coRE

For fixed M, w, the predicate C(w) := "M halts on w within |w| steps" is decidable (|w| is
computable, so simulate for exactly that many steps). L3 = {⟨M⟩ : ∀w, C(w)}.

complement(L3) = {⟨M⟩ : ∃w, ¬C(w)} — an existential over a decidable predicate, always RE:
enumerate all w, decide ¬C(w) directly for each (always terminates), halt-accept on the
first witness. So complement(L3) ∈ RE, hence L3 ∈ coRE.

### Step 2 — L3 ∉ RE (so L3 ∉ R too, since R ⊆ RE)

Reduce co-A_TM = {⟨M,w⟩ : M does not accept w} (∉ RE) to L3.

Construction: given ⟨M,w0⟩, build M' that on input x: simulate M on w0 for |x| steps; if
that simulation shows M has ALREADY reached an accepting halt within |x| steps, M' loops
forever; otherwise (still running, or already halted-rejecting, or looping — all mean "not
yet accepted"), M' halts immediately. (Small edge-case input lengths get a hardcoded fast
halt, standard for this style of proof — the argument is about asymptotic behavior.)

- If ⟨M,w0⟩ ∈ co-A_TM (M never accepts w0): for every x the simulation never shows an
  accepting halt, so M' always halts. M' halts on every input within ~|x| steps, so
  ⟨M'⟩ ∈ L3.
- If ⟨M,w0⟩ ∉ co-A_TM (M accepts w0 at step t): for every x with |x|≥t, the simulation
  does see the accepting halt, so M' loops forever on all those x — M' fails to halt on
  infinitely many inputs, so ⟨M'⟩ ∉ L3.

Valid reduction co-A_TM ≤m L3; since co-A_TM ∉ RE, L3 ∉ RE.

### Combining

L3 ∈ coRE and L3 ∉ RE ⟹ (since R = RE∩coRE) L3 ∉ R. So L3 ∈ coRE\R. ∎

### Why Q6 lands in coRE but Q5 escapes RE∪coRE entirely — the key contrast

- **Q5's pattern**: ∀w (decidable(w) → RE(w)) — an RE predicate sits INSIDE the universal
  quantifier. This generically escapes BOTH RE and coRE (Π2-like, same shape as ALL_TM).
- **Q6's pattern**: ∀w [decidable(w)] — NO RE predicate inside the universal at all; just
  "for all w, a decidable check passes." This is ALWAYS coRE (negation is a plain
  existential over a decidable predicate, hence RE). Whether it's FURTHER decidable
  (landing in R) or not (coRE\R) then needs a separate reduction — Step 2 above.

So the presence or absence of a genuinely-RE-only condition (like w∈L(M2) in Q5) inside the
universal quantifier is what decides whether the language can even land inside coRE, versus
falling outside RE∪coRE entirely.

## Issues log

- **Q5** — Confusion about the logical meaning of "∀w, (M1 accepts w within 1000 steps) →
  w∈L(M2)" — the if-then connective seemed off. Resolved: it's the standard translation of
  a subset relation S⊆L(M2) where S={w : M1 accepts w within 1000 steps}; the 1000-step
  bound makes S decidable (via bounded simulation) but NOT necessarily finite (e.g. an M1
  that instantly accepts everything gives S=Σ*). Classified L as neither RE nor coRE via a
  mapping reduction from ALL_TM (fixing M1 to the trivial always-accept machine), with
  ALL_TM's own non-RE/non-coRE status established via two standard reductions
  (co-A_TM ≤m ALL_TM and A_TM ≤m ALL_TM).
- **Q6** — Given as a marked-answer classification question (student circled coRE\R).
  Resolved: L3 ∈ coRE because "∀w [decidable C(w)]" always has an RE complement (∃w ¬C(w),
  existential over a decidable predicate); L3 ∉ RE via a reduction from co-A_TM using a
  machine M' that halts iff a bounded simulation of M on a fixed w0 has NOT yet detected an
  accepting halt, forcing M' to loop on all sufficiently long inputs exactly when M does
  accept w0. Highlighted the structural contrast with Q5: an RE-only condition mixed inside
  a ∀ escapes RE∪coRE entirely, while a purely-decidable condition under a ∀ always stays
  inside coRE.
