# Comp 2020 summer (קיץ) moed B — Q2 (11 pts, T/F+proof): REG closed under MARK(L)

**Question.** For L ⊆ {a,b}*, define

    MARK(L) = { a·w : w ∈ L and |w| is even } ∪ { b·w : w ∈ L and |w| is odd }

Examples given:
    MARK({a,ab,aba}) = {aab, ba, baba}
    MARK({aⁿbⁿ | n≥0}) = {aⁿ⁺¹bⁿ | n≥0}

Claim: for every L ⊆ {a,b}*, if L ∈ REG then MARK(L) ∈ REG. Mark correct/incorrect and
prove.

Note: this exam PDF is not present in this repo's "2017-2025 Exams" folder.

## Answer: CORRECT (student's circled "נכונה" is right)

## Proof — via closure properties alone (intersection, concatenation, union)

No custom automaton needed. Let EVEN = {w : |w| even}, ODD = {w : |w| odd} — both
trivially regular: EVEN = ((a+b)(a+b))*, ODD = (a+b)((a+b)(a+b))*.

**Identity.**

    MARK(L) = a·(L ∩ EVEN) ∪ b·(L ∩ ODD)

Proof of the identity: a·w ∈ {a·w : w∈L, |w| even} iff w∈L and |w| even, i.e. iff
w ∈ L∩EVEN — so {a·w : w∈L,|w|even} = a·(L∩EVEN) (prepend a to every word of L∩EVEN).
Symmetrically {b·w : w∈L,|w|odd} = b·(L∩ODD). Union of the two gives MARK(L). (Verified by
brute force against 2000 random finite languages — no mismatch.)

**Closing the proof, purely via closure properties:**
1. EVEN, ODD ∈ REG (explicit regexes above).
2. L ∈ REG by hypothesis ⟹ L∩EVEN, L∩ODD ∈ REG (REG closed under intersection).
3. {a}, {b} ∈ REG (finite languages) ⟹ a·(L∩EVEN), b·(L∩ODD) ∈ REG (REG closed under
   concatenation).
4. Their union ∈ REG (REG closed under union), and by the identity that union IS MARK(L). ∎

This mirrors how Q3 (Majority) reduces to intersection/union alone — no automaton needs to
be built by hand; standard closure properties applied to L and two trivially-regular parity
languages finish the job.

## Alternate proof — explicit product-with-parity automaton

Unfolding the closure-based proof into an explicit automaton (the (q,p,X) state below is
literally tracking membership in L, parity, and which branch — i.e. the product-with-
EVEN/ODD structure made concrete) gives the following construction directly, useful if a
question specifically asks for a DFA rather than a closure argument.

Let A = (Q, {a,b}, δ, q0, F) be a (complete) DFA for L. Build A' = (Q', {a,b}, δ', q0', F'):

    Q'  = {s} ∪ (Q × {0,1} × {A,B})            (s = fresh initial state)
    δ'(s, a) = (q0, 0, A)          δ'(s, b) = (q0, 0, B)
    δ'((q,p,X), σ) = (δ(q,σ), 1−p, X)          for X ∈ {A,B}, σ ∈ {a,b}
    F'  = { (q,0,A) : q ∈ F } ∪ { (q,1,B) : q ∈ F }

Reading of state (q,p,X): X records which "mode" the first symbol triggered (A = first
symbol was a, needs the rest to have even length; B = first symbol was b, needs odd
length). q is where A's run on the suffix w (read so far) currently sits. p is the parity
of how many symbols of w have been read so far (flips on every step after the first).

**Correctness.** For input u of length n ≥ 1, write u = c·w with c the first symbol and w
the rest (|w| = n−1). After reading u, A' is in state (δ*(q0,w), parity(|w|), X) where
X = A if c=a, X = B if c=b. This is accepting iff:
- X=A and δ*(q0,w) ∈ F and parity(|w|)=0 — i.e. c=a, w∈L, |w| even — exactly a·w ∈ MARK(L).
- X=B and δ*(q0,w) ∈ F and parity(|w|)=1 — i.e. c=b, w∈L, |w| odd — exactly b·w ∈ MARK(L).

For u = ε, A' is stuck at s ∉ F', correctly rejecting (MARK(L) never contains ε, since
every element starts with a or b). So L(A') = MARK(L) exactly, and |Q'| = 1 + 4|Q| is
finite. ∎

Machine-verified: built the actual trie-DFA for L = {a, ab, aba}, ran this exact
construction through it, and it reproduces {aab, ba, baba} — matching the exam's own
example — and matches the general formula MARK_via_formula on a bounded exhaustive check
up to length 6. Also confirmed MARK({aⁿbⁿ}) = {aⁿ⁺¹bⁿ} for n=0..4 directly from the
definition (this L is not itself regular — the example just pins down what the operator
computes; it is not a counterexample, since the claim only concerns regular L).

## Why the reverse direction isn't the claim

The construction only used L ∈ REG to get a finite Q; it doesn't lean on any special
structure of the marking rule. The converse (MARK(L) ∈ REG ⟹ L ∈ REG) also happens to hold
by a similar per-parity argument, but that's not what was asked — only the forward
direction (L regular ⟹ MARK(L) regular) is claimed and proven above.

## Issues log

- **Q2** — Given as a marked-answer exam question (student circled "correct", wanted the
  proof). Resolved with an explicit product-with-parity DFA: states (q,p,X) track A's run
  on the suffix w, the parity of symbols of w consumed, and which marker symbol (a/b)
  started the string, with acceptance requiring both the correct final A-state and the
  parity matching the marker. |Q'|=1+4|Q| is finite whenever L is regular. Verified against
  both worked examples in the question (including reproducing MARK({a,ab,aba}) exactly via
  a concrete trie-DFA simulation), plus a bounded exhaustive check.
- **Q2 follow-up** — Asked whether this can also be solved via closure under
  intersection/union (as Q3/Majority was), instead of a custom automaton. Resolved: yes —
  MARK(L) = a·(L∩EVEN) ∪ b·(L∩ODD) with EVEN, ODD trivially regular, so the claim follows
  from REG's closure under intersection, concatenation (with the singleton languages {a},
  {b}), and union alone, with no automaton construction needed. Verified the identity by
  brute force on 2000 random finite languages. Kept the explicit automaton as an alternate
  proof, noting it's just this closure argument unfolded into concrete states.
