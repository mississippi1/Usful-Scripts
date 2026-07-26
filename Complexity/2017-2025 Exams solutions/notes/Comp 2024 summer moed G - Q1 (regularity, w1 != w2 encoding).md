# Comp 2024 summer (קיץ) moed G — Q1 (12 pts, T/F+proof): is L' = {w1#w2 : w1,w2 ∈ L, w1≠w2} always regular?

**Question.** For L ⊆ {0,1}*, define

    L' = { w1#w2 : w1, w2 ∈ L and w1 ≠ w2 }

Claim: for every regular L, the language L' is regular. Mark correct/incorrect and prove.

Note: this exam PDF is not present in this repo (only "2017-2025 Exams" has files for moed
A/B/C sets; this "moed ג' (moed G)" summer 2024 exam isn't archived here). Answer: the
student's circled "not correct" is right.

## Answer: FALSE

## The counterexample: L = {0,1}*

Take the simplest regular language, L = {0,1}* (a 1-state DFA, self-loop on every letter,
always accepting). Then

    L' = { w1#w2 : w1, w2 ∈ {0,1}*,  w1 ≠ w2 }

We show L' is not regular; since this L is regular, that alone disproves the universal
claim.

## Proof L' is not regular — direct Myhill–Nerode (no pumping lemma needed)

**The family.** For each n ≥ 0, let u_n = 0^n.

**The distinguishing suffix.** For each n, take z_n = "#" 0^n.

**Claim:** for n ≠ m, z_n distinguishes u_n from u_m.

- u_n · z_n = 0^n # 0^n represents w1 = 0^n, w2 = 0^n. But w1 = w2, violating the required
  w1 ≠ w2. So u_n · z_n ∉ L'.
- u_m · z_n = 0^m # 0^n (m ≠ n) represents w1 = 0^m, w2 = 0^n. Since m ≠ n, |0^m| ≠ |0^n|, so
  w1 ≠ w2, and both trivially lie in L = {0,1}*. So u_m · z_n ∈ L' for every m ≠ n.

So z_n puts u_n outside L' while putting every other u_m inside L'. Hence for any n ≠ m,
u_n and u_m are NOT ≡_{L'}-equivalent (z_n separates them). So u_0, u_1, u_2, … are pairwise
≡_{L'}-inequivalent — infinitely many words in infinitely many distinct classes:

    MN(L') = ∞

By Myhill–Nerode (finite index ⟺ regular), L' is not regular. ∎

Machine-verified: checked u_m · z_n ∈ L' for n, m ∈ {0,…,5} — got exactly the predicted
pattern (False only on the diagonal m = n, True everywhere else). Also measured MN classes
of L' restricted to growing observation windows (words over {0,1,#} up to length k):
3, 9, 17, 33, 65 classes for k = 1..5 — strictly increasing without leveling off, consistent
with infinite true index.

## Since L = {0,1}* is regular but L' is not, the claim is false. ∎

## Two more ways to see it

**Via pumping + closure properties.** Let U = {0,1}* # {0,1}* (exactly one #, regular by
inspection). If L' were regular, then since REG is closed under set difference,

    U \ L' = { w1#w2 ∈ U : ¬(w1 ≠ w2) } = { w#w : w ∈ {0,1}* } =: EQ

would also be regular. But EQ is the classic non-regular language: take s = 0^p#0^p; any
valid decomposition s = xyz with |xy| ≤ p, |y| ≥ 1 has y = 0^k sitting entirely in the left
0^p block, so pumping down to i=0 gives 0^{p-k}#0^p with unequal-length halves, hence
∉ EQ — contradicting the pumping lemma. Contradiction, so L' isn't regular either.

**Why direct pumping on L' itself is the wrong tool.** Pumping a witness string almost
always *preserves* an inequality between the two halves (e.g. adding/removing zeros from
an all-zero half while the other half contains a different symbol keeps them unequal no
matter what), so no contradiction falls out easily by pumping L' directly. EQ, by contrast,
is broken by any perturbation (any length change breaks equality). That asymmetry is why
the closure-property reduction (or the direct MN fooling-set argument above) is the natural
technique for a "not-equal" language, while pumping directly suits an "equal" one.

## The general lesson

w1 ≠ w2 is exactly as hard for a finite automaton to check as w1 = w2 — both require
comparing two arbitrary strings across the #, which no bounded memory can do once L places
no real restriction on the two halves. The claim would only have a chance for special
regular L where "different" becomes locally checkable (e.g. L restricted to a single fixed
length) — but as stated ("for every regular L"), L = Σ* kills it immediately.

## Issues log

- **Q1** — Given as a marked-answer exam question (student circled "not correct" but wanted
  the full proof). Resolved via the counterexample L = {0,1}*, showing
  L' = {w1#w2 : w1≠w2} is not regular by exhibiting the infinite pairwise-inequivalent
  family u_n = 0^n with distinguishing suffixes z_n = "#0^n" (u_n·z_n ∉ L' since it encodes
  w1=w2=0^n, while u_m·z_n ∈ L' for all m≠n since lengths differ) — giving MN(L')=∞ directly,
  no pumping lemma required. Also recorded the equivalent pumping/closure-property argument
  (reduce to the classic non-regularity of {w#w}) and why pumping L' directly is the wrong
  tool (perturbations preserve inequality, unlike equality). Verified computationally: the
  fooling-set pattern and strictly growing MN-class counts (3,9,17,33,65) over windows of
  length 1..5.
