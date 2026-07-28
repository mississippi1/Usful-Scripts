# L = { ⟨M₁,M₂⟩ : L(M₁) ≤m L(M₂) } is outside RE ∪ coRE (source exam unidentified)

**Question.** Let L ≝ { ⟨M₁,M₂⟩ : L(M₁) ≤m L(M₂) }. Show L ∈ $\overline{RE ∪ coRE}$.

*(No exam file identified; likely a תרגיל / תרגול item. Rename/merge this doc if the source turns
up.)*

---

## Answer

One reduction does both halves. Reduce from **ALL_TM** = { ⟨M⟩ : L(M) = Σ* }, which is
Π⁰₂-complete and therefore lies in $\overline{RE ∪ coRE}$ (formula sheet, page-4 table; the
standard witnesses are Ā_TM ≤m ALL_TM and A_TM ≤m ALL_TM).

### Construction

f(⟨M⟩) = ⟨M₁, M₂⟩ where

**M₁** (fixed, does not depend on M) on input x:
1. parse x as ⟨T,w⟩; reject if malformed;
2. simulate T on w; accept if it halts.

So **L(M₁) = HALT**.

**M₂** on input x:
1. parse x as ⟨T,w⟩; reject if malformed;
2. for every word u with |u| ≤ |x| (finitely many), simulate M on u until it accepts — continue only
   if *all* of them are accepted;
3. simulate T on w; accept if it halts.

So L(M₂) = { ⟨T,w⟩ : T halts on w **and** M accepts every u with |u| ≤ |⟨T,w⟩| }.

### Correctness

- **⟨M⟩ ∈ ALL_TM.** Step 2 always passes, so L(M₂) = HALT = L(M₁). The identity map witnesses
  HALT ≤m HALT ⇒ ⟨M₁,M₂⟩ ∈ L ✓
- **⟨M⟩ ∉ ALL_TM.** Let u₀ be a *shortest* word M does not accept, n = |u₀|. Every input x with
  |x| ≥ n makes step 2 hang on u₀, so M₂ accepts nothing of length ≥ n:

      L(M₂) ⊆ { x : |x| < n }  is **finite**, hence decidable.

  If HALT = L(M₁) ≤m L(M₂) held, HALT would be decidable — contradiction. So ⟨M₁,M₂⟩ ∉ L ✓

**Computability of f.** It only writes two programs, plugging the fixed string ⟨M⟩ into a template.
No simulation at reduction time.

### Both non-memberships at once

ALL_TM ≤m L, and ≤m pushes membership downward:

- L ∈ RE ⇒ ALL_TM ∈ RE — false;
- L ∈ coRE ⇒ ALL_TM ∈ coRE — false.

Hence L ∈ $\overline{RE ∪ coRE}$. ∎

---

## Pitfalls

### 1. Intersecting with L(M) does not control the m-degree

The tempting version: L(M₁) = HALT and **M₂ on ⟨T,w⟩: simulate M on the input; if M accepts, simulate
T on w** — i.e. L(M₂) = L(M) ∩ HALT.

The ALL case is fine (L(M₂) = HALT, identity reduction). The **non-ALL case fails**:

> Let M accept every word except one word x₀ = ⟨T₀,w₀⟩ where T₀ **loops** on w₀. Then ⟨M⟩ ∉ ALL_TM,
> but L(M₂) = L(M) ∩ HALT = HALT = L(M₁), so ⟨M₁,M₂⟩ ∈ L. A no-instance maps to a yes-instance.

Not even equality is needed to break it: for any x₀, HALT ∖ {x₀} is still HALT-hard (map x ↦ x for
x ≠ x₀ and x₀ ↦ a fixed element of HALT ∖ {x₀}), so almost any "one missing word" scenario keeps the
reduction alive.

**Root cause.** `L(M₁) ≤m L(M₂)` depends only on the **m-degree** of L(M₂). "L(M) ≠ Σ*" gives you a
*generic* subset of HALT, and generic subsets of an RE-complete set stay RE-complete. To make the
reduction fail you must drive L(M₂) into a **trivially low** degree — finite/decidable, or ∅/Σ*.

### 2. Which trivial target to aim for

Watch the polarity when picking the "collapsed" language, because ∅ and Σ* behave asymmetrically:

| collapsed L(M₂) | does HALT ≤m it? | usable? |
|---|---|---|
| finite (or any decidable set) | no — would decide HALT | ✓ **this is the one** |
| ∅ | no — A ≤m ∅ iff A = ∅ | ✓ |
| Σ* | no — A ≤m Σ* iff A = Σ* | ✓, but only if L(M₁) ≠ Σ* |
| a nonempty finite set, with **L(M₁) = Σ*** | **yes** — constant map | ✗ trap |

So the pairing matters: with L(M₁) = HALT a finite target is safe, but if you had set L(M₁) = Σ* the
same finite target would be reducible via a constant function and the proof would collapse.

### 3. The length-threshold gadget, reused with the opposite moral

Step 2 above ("M accepts all u with |u| ≤ |x|") is the same gadget as in the Ā_TM ≤m ALL_TM proof and
in `L(M) in R is coRE-hard`. There it was *useless*, because the finite language it produces **is
decidable** and so lands on the same side of "∈ R" as Σ*. Here that is exactly what is wanted: a
finite set has a trivial m-degree, so HALT cannot reduce into it.

> Same gadget, opposite verdict — it depends entirely on whether the target property can *see* a
> finite language.

### 4. One reduction suffices for both classes

ALL_TM is outside RE **and** outside coRE, so a single ALL_TM ≤m L settles both. No need for a
separate reduction from HALT and from Ā_TM. (If a question demands coRE-hardness or RE-hardness
specifically, then reduce from the complete sets instead — ALL_TM is *not* complete for either.)

---

## Issues log

- **Full question** — Attempted ALL_TM ≤m L with L(M₁) = HALT and M₂ computing **L(M) ∩ HALT**
  (M₂ on ⟨T,w⟩ simulates M on the input and, if M accepts, simulates T on w). Correctly suspected it
  was wrong. Resolved: the ALL case is fine but the **non-ALL case fails** — take M accepting
  everything except a single x₀ = ⟨T₀,w₀⟩ with T₀ looping on w₀; then L(M) ∩ HALT = HALT = L(M₁), so
  a no-instance maps to a yes-instance. More generally, deleting a word from HALT leaves an
  RE-complete (hence still HALT-hard) set, so "L(M) ≠ Σ*" carries no usable information about the
  m-degree of L(M) ∩ HALT. Fix keeps the same shape but replaces "M accepts x" with the
  **length-threshold** check "M accepts every u with |u| ≤ |x|": in the non-ALL case, with u₀ the
  shortest non-accepted word, M₂ hangs on every input of length ≥ |u₀|, so L(M₂) is **finite** hence
  decidable, and HALT ≤m L(M₂) would decide HALT. Key lesson recorded in Pitfall 1: `≤m` is a
  property of the whole m-degree, so the no-case must collapse the target to a trivial degree
  (finite/∅/Σ*), not merely shrink it.
