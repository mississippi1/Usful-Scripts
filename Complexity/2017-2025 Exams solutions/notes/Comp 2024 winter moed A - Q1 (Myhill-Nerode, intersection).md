# Comp 2024 winter (חורף) moed A — Q1 (25 pts): Myhill–Nerode, and C ∩ C' under intersection

**Question.** Let Σ be an alphabet.
(a) Define the Myhill–Nerode equivalence relation for a language L ⊆ Σ*.
(b) Let L, L' ⊆ Σ* be languages and let C, C' be Myhill–Nerode equivalence classes of
    L, L' respectively. Prove that any two words u, v ∈ C ∩ C' are Myhill–Nerode
    equivalent with respect to the language L ∩ L'.

## (a) The definition

For u, v ∈ Σ*:

    u ≡_L v   ⟺   ∀ z ∈ Σ* :  u·z ∈ L ⟺ v·z ∈ L

"No suffix can tell u and v apart": every extension z takes both into L or both out of L.

The exam answer written in the box (∀z ∈ Σ*, u·z ∈ L ⟺ v·z ∈ L) is exactly right; the only
slip was writing Σ^# instead of Σ* (all finite words over Σ, ε included).

Points that cost marks:

- **z ranges over all of Σ*, ε included.** z = ε gives the special case u ∈ L ⟺ v ∈ L, which
  is a *consequence*, not the definition.
- **The quantifier is outside the biconditional**: ∀z: (uz ∈ L ⟺ vz ∈ L), *not*
  (∀z: uz ∈ L) ⟺ (∀z: vz ∈ L).
- **The relation depends on L** — hence the subscript.

**It is an equivalence relation:** reflexive (uz ∈ L ⟺ uz ∈ L); symmetric (⟺ is symmetric);
transitive (chain the biconditionals for each z). So ≡_L partitions Σ* into classes; write
MN(L) for their number and [u] for the class of u.

**Why it matters (context for (b)).** ≡_L is a right congruence: u ≡_L v ⇒ ua ≡_L va for
every a ∈ Σ*, since the suffixes of ua are exactly the words a·z. Myhill–Nerode theorem:
L is regular ⟺ MN(L) < ∞, and then the minimal DFA has exactly MN(L) states — the states
*are* the classes, and reading u lands in the state [u].

## (b) Solution

### Step 1: two words lying in a common class are equivalent

Let u, v ∈ C ∩ C'. In particular u, v ∈ C, and C is a class of ≡_L, i.e.
C = [w]_{≡_L} = { t : t ≡_L w } for some representative w. So u ≡_L w and v ≡_L w, hence by
symmetry and transitivity (part (a)):

    u ≡_L v

Identically, from u, v ∈ C' and C' being a class of ≡_{L'}:

    u ≡_{L'} v

This step is short but it is the one being tested: the hypothesis is *not* "u and v are
equivalent", it is "u and v lie in a common class of each relation", and classes consist of
pairwise-equivalent words.

### Step 2: unfold the definition for L ∩ L'

Let z ∈ Σ* be arbitrary. Then

    u·z ∈ L ∩ L'
     ⟺ u·z ∈ L  and  u·z ∈ L'      (definition of ∩)
     ⟺ v·z ∈ L  and  u·z ∈ L'      (Step 1: u ≡_L v, applied to this z)
     ⟺ v·z ∈ L  and  v·z ∈ L'      (Step 1: u ≡_{L'} v, applied to the same z)
     ⟺ v·z ∈ L ∩ L'                (definition of ∩)

z was arbitrary, so ∀z ∈ Σ*: uz ∈ L ∩ L' ⟺ vz ∈ L ∩ L', i.e. u ≡_{L ∩ L'} v. ∎

The engine of the proof: ≡_L and ≡_{L'} are ∀z statements, so the *same* z can be plugged
into both. Nothing has to be constructed or searched for.

Degenerate cases need no separate treatment: if C ∩ C' is empty or a singleton the claim is
vacuous, and the proof never assumed otherwise.

## Why the exam asks this: the state-count corollary

The blocks C ∩ C' (over all classes C of ≡_L and C' of ≡_{L'}) form a partition of Σ* —
each word lies in exactly one class of each relation. Part (b) says every block sits inside
a *single* class of ≡_{L ∩ L'}, i.e. that partition **refines** the ≡_{L ∩ L'} partition, so
each ≡_{L ∩ L'} class is a union of blocks. Counting:

    MN(L ∩ L')  ≤  #{nonempty blocks C ∩ C'}  ≤  MN(L) · MN(L')

So if L, L' are regular then MN(L ∩ L') < ∞ and L ∩ L' is regular: this is the
Myhill–Nerode proof that REG is closed under intersection, and it re-derives the
product-automaton bound n₁·n₂ without constructing the automaton. It is exactly the tool
for 2023-2 moed B Q3 ("can MN(L₁)·MN(L₂) < MN(L₁ ∩ L₂)?" — no, by this inequality).

Keep straight:

- **Tight case:** L = even #0's, L' = even #1's ⇒ 2·2 = 4 = MN(L ∩ L').
- **Strict case / converse is false:** L = {w : |w| even}, L' = {w : |w| odd} have MN = 2
  each, but L ∩ L' = ∅ has MN = 1. So u ≡_{L ∩ L'} v does *not* imply u ≡_L v, and C ∩ C'
  need not **be** a class of ≡_{L ∩ L'} — only be contained in one. Claiming equality is the
  standard way to lose points. (Both examples machine-checked, plus the refinement property
  on random language pairs.)

## Free generalization

The proof used only that membership of w in the target language is determined by the bit
pair (w ∈ L, w ∈ L'). So for any binary Boolean operation f, the language
L_f = { w : f(w ∈ L, w ∈ L') = 1 } satisfies the same statement — union, difference,
symmetric difference, … — with MN(L_f) ≤ MN(L)·MN(L'). Just replace the middle line of
Step 2 by f(uz ∈ L, uz ∈ L') = f(vz ∈ L, vz ∈ L').

For a single language, complement is even better: uz ∈ Σ*\L ⟺ ¬(uz ∈ L), so ≡_L and
≡_{Σ*\L} are the *same* relation and MN(Σ*\L) = MN(L) exactly.

## Issues log

- **Q1(a)** — Checking the handwritten definition. Resolved: ∀z ∈ Σ*, u·z ∈ L ⟺ v·z ∈ L is
  correct (Σ^# was a typo for Σ*). Emphasised that z ranges over all of Σ* including ε, that
  the ∀z must sit outside the biconditional, and that ≡_L is an equivalence relation and a
  right congruence whose classes are the states of the minimal DFA.
- **Q1(b)** — How to get from "u, v ∈ C ∩ C'" to equivalence w.r.t. L ∩ L'. Resolved in two
  steps: (1) words in a common class of ≡_L are ≡_L-equivalent (via a representative w plus
  symmetry/transitivity), same for ≡_{L'}; (2) for an arbitrary z, rewrite
  uz ∈ L ∩ L' ⟺ uz ∈ L ∧ uz ∈ L' and swap u for v in each conjunct using the *same* z.
  Key insight: both hypotheses are ∀z statements, so one z serves both.
- **Q1(b) follow-up** — What the claim is for. Resolved: it shows the {C ∩ C'} partition
  refines the ≡_{L ∩ L'} partition, hence MN(L ∩ L') ≤ MN(L)·MN(L') (closure of REG under
  intersection, Myhill–Nerode version of the product automaton). Warning recorded: C ∩ C' is
  only *contained in* a class, not equal to one — L = even length, L' = odd length gives
  2·2 classes collapsing to 1.
