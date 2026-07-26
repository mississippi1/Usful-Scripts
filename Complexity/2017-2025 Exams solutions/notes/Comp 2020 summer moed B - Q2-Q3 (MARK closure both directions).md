# Comp 2020 summer (קיץ) moed B — Q2-Q3 (11 pts each, T/F+proof): REG and MARK(L), both directions

**Question (Q2).** For L ⊆ {a,b}*, define

    MARK(L) = { a·w : w ∈ L and |w| is even } ∪ { b·w : w ∈ L and |w| is odd }

Examples given:
    MARK({a,ab,aba}) = {aab, ba, baba}
    MARK({aⁿbⁿ | n≥0}) = {aⁿ⁺¹bⁿ | n≥0}

Claim: for every L ⊆ {a,b}*, if L ∈ REG then MARK(L) ∈ REG. Mark correct/incorrect and
prove.

**Question (Q3, same worksheet, the converse).** Claim: for every L ⊆ {a,b}*, if
MARK(L) ∈ REG then L ∈ REG. Mark correct/incorrect and prove.

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

## Q3 — the converse: MARK(L) ∈ REG ⟹ L ∈ REG — also CORRECT

## The key tool: closure under left quotient by a fixed symbol

**Fact.** If L1 ∈ REG and c ∈ Σ is a fixed symbol, then c⁻¹L1 := {w : c·w ∈ L1} ∈ REG.

Proof: let A = (Q, Σ, δ, q0, F) be a DFA for L1. Build A' = (Q, Σ, δ, δ(q0,c), F) — same
automaton, only the start state shifted to δ(q0,c). Then for any w:

    w ∈ L(A')  ⟺  δ*(δ(q0,c), w) ∈ F  ⟺  δ*(q0, c·w) ∈ F  ⟺  c·w ∈ L1  ⟺  w ∈ c⁻¹L1

so L(A') = c⁻¹L1, a finite automaton, hence regular. ∎

## The key identity: MARK can be exactly undone

**Claim.** For every L ⊆ {a,b}* (no regularity assumption needed here):

    L  =  a⁻¹MARK(L)  ∪  b⁻¹MARK(L)

Proof: recall MARK(L) = a·(L∩EVEN) ∪ b·(L∩ODD) (the Q2 identity), and the two pieces are
automatically disjoint by first letter. So a⁻¹MARK(L) = {w : a·w ∈ MARK(L)}: since a word
starting with a can only come from the first piece (a·(L∩EVEN), never b·(L∩ODD)),
a·w ∈ MARK(L) ⟺ w ∈ L∩EVEN. So a⁻¹MARK(L) = L∩EVEN exactly. Symmetrically
b⁻¹MARK(L) = L∩ODD exactly. Therefore:

    a⁻¹MARK(L) ∪ b⁻¹MARK(L) = (L∩EVEN) ∪ (L∩ODD) = L ∩ (EVEN∪ODD) = L ∩ Σ* = L

using that every word's length is either even or odd. ∎ (Verified by brute force: recovered
L exactly from MARK(L) via this quotient identity on 2000 random finite languages.)

## Closing the Q3 proof

If MARK(L) ∈ REG, then by the quotient fact, a⁻¹MARK(L) and b⁻¹MARK(L) are both regular. By
the identity, their union IS L. REG is closed under union, so L ∈ REG. ∎

## Why this makes MARK an "iff", and the contrast with squaring

Combined, Q2+Q3 show L ∈ REG ⟺ MARK(L) ∈ REG — regularity of L and of MARK(L) are
equivalent, stronger than either direction alone. This makes sense structurally: MARK
doesn't throw away or garble information about L — it tags each word with a marker letter
determined by a property (|w|'s parity) that is itself always regular, and the tagging is
invertible by a single fixed-string left quotient. Contrast with an operation like
w ↦ w#w (squaring): recovering w from the squared form is not a finite-state operation —
exactly why {w#w} is the classic non-regular example, unlike MARK.

## Issues log

- **Q2** — Given as a marked-answer exam question (student circled "correct", wanted the
  proof). Resolved with an explicit product-with-parity DFA: states (q,p,X) track A's run
  on the suffix w, the parity of symbols of w consumed, and which marker symbol (a/b)
  started the string, with acceptance requiring both the correct final A-state and the
  parity matching the marker. |Q'|=1+4|Q| is finite whenever L is regular. Verified against
  both worked examples in the question (including reproducing MARK({a,ab,aba}) exactly via
  a concrete trie-DFA simulation), plus a bounded exhaustive check.
- **Q2 follow-up** — Asked whether this can also be solved via closure under
  intersection/union (as the Majority question was), instead of a custom automaton.
  Resolved: yes — MARK(L) = a·(L∩EVEN) ∪ b·(L∩ODD) with EVEN, ODD trivially regular, so the
  claim follows from REG's closure under intersection, concatenation (with the singleton
  languages {a}, {b}), and union alone, with no automaton construction needed. Verified the
  identity by brute force on 2000 random finite languages. Kept the explicit automaton as an
  alternate proof, noting it's just this closure argument unfolded into concrete states.
- **Q3** — The converse claim (MARK(L)∈REG ⟹ L∈REG), given without a marked answer.
  Resolved: also correct, via the exact identity L = a⁻¹MARK(L) ∪ b⁻¹MARK(L) (a set identity
  true for every L, regularity-independent) plus closure of REG under left quotient by a
  fixed symbol (shift the DFA's start state along that symbol). So L ∈ REG ⟺ MARK(L) ∈ REG —
  MARK preserves regularity losslessly in both directions, unlike an operation like
  w ↦ w#w whose inverse isn't finite-state. Verified the recovery identity by brute force on
  2000 random finite languages.
