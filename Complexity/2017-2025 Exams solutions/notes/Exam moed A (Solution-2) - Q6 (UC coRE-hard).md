# Exam moed A (Solution-2) — Question 6 (study notes)

Source exam: `Exam_moed_A_Solution-2.pdf` (⚠ exam identity unconfirmed — assumed same file as this
exam's Q8 notes because the screenshot formatting matches; rename if it belongs to a different exam).

## Q6 (12 pts)

**Definition (closed-from-above / upward-closed).** A language L is *closed-from-above* if for all
words x, y: if x ∈ L then also x∘y ∈ L. (Once a word is in L, every extension of it is in L.)

**Language.** UC = { ⟨M⟩ : L(M) is closed-from-above }.

**Task.** Prove UC is **coRE-hard**.

### The complement (the object you complement for a coRE-hardness proof)

  UC-bar = { ⟨M⟩ : L(M) is NOT closed-from-above }
         = { ⟨M⟩ : ∃ x, y such that x ∈ L(M) and x∘y ∉ L(M) }.

In words: M accepts some word x but fails to accept some extension x∘y of it. (Negation of
∀x,y(x∈L ⟹ xy∈L): ∃x,y(x∈L ∧ xy∉L).)

**One-symbol reformulation.** L is upward-closed ⟺ ∀ z∈L, ∀ symbol b∈Σ: zb∈L. (Walk along
x, xa₁, xa₁a₂, …, xy; membership flips from in to out at some adjacent pair z, zb.) Hence
UC-bar = { ⟨M⟩ : ∃ z∈L(M), ∃ b∈Σ, zb∉L(M) }.

Encoding caveat: invalid ⟨M⟩ strings are a decidable set — fold into either side (standard: invalid
codes ∉ UC); does not affect hardness.

### Why the complement matters

Reductions transfer under complement: A ≤m B ⟺ Ā ≤m B̄. So
  UC is coRE-hard ⟺ UC-bar is RE-hard.
Standard route: reduce an RE-hard language (A_TM or HALT) **to UC-bar** — construct M' whose language
*fails* upward-closure exactly when M accepts / halts on w; the "∃ x∈L(M'), xy∉L(M')" shape is the
failure you engineer. (Equivalently, reduce the coRE-complete Ā_TM **to UC** directly.)

---

## Issues log

Track here which parts gave trouble, and how they were resolved.

- **Q6 (what is the complement of UC?):** Clarified. UC-bar = { ⟨M⟩ : L(M) is not closed-from-above }
  = { ⟨M⟩ : ∃ x,y with x ∈ L(M) and x∘y ∉ L(M) } — M accepts a word but not some extension of it.
  Obtained by negating the definition ∀x,y(x∈L ⟹ xy∈L). Noted the one-symbol reformulation (suffices
  to have z∈L, b∈Σ with zb∉L) and the encoding-validity caveat. Connected it to the proof: since
  A ≤m B ⟺ Ā ≤m B̄, proving UC coRE-hard is the same as proving UC-bar RE-hard, so the natural plan
  is to reduce A_TM / HALT to UC-bar (build M' whose language fails upward-closure iff M accepts w).
  Also distinguished from the string-level dual: the complement of a generic upward-closed *string*
  language is *prefix-closed* (z∉L ⟹ all prefixes of z ∉ L) — not the object needed here.
