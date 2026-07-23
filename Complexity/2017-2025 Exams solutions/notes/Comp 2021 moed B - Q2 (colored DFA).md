# Comp 2021 moed B — Q2 (colored DFA / k-צבעוני)

*(From the unified study booklet; the question is labeled "שאלה 2". Same DFA-topic
cluster as the Part-I DFA question.)*

## Definitions

A **k-colored DFA** A = ⟨Q, Σ, δ, q₀, f⟩ is an ordinary DFA except the last component
is a coloring f : Q → [k] instead of a set of accepting states.
A run r = q₀,q₁,…,qₙ is **accepting** iff it visits **every** color at least once:
∀ c ∈ [k] ∃ i with f(qᵢ) = c. (Runs are still deterministic → one run per word.)
Example given: a 2-colored DFA for a·b·(a+b)*.

## Part א — 3-colored DFA for L = {w : both a and b appear in w}, minimal #states

**Minimal #states = 3.** With ≤ 2 states there are ≤ 2 distinct colors in the whole
machine, so no run can collect all 3 colors ⇒ empty language. So ≥ 3 states needed; 3 works:

| state | color | on a | on b |
|---|---|---|---|
| q₀ (start) | 1 | q_a | q_b |
| q_a | 2 | q_a | q_b |
| q_b | 3 | q_a | q_b |

Uniform rule: every state sends a → q_a and b → q_b.

**Why:** current state after w is q_a if last letter a, q_b if last letter b. Over the run:
color 1 always visited (start q₀); color 2 (q_a) visited iff some a occurs;
color 3 (q_b) visited iff some b occurs. So colors visited = {1,2,3} iff w has both a and b = L.
(ε, a*, b* each miss a color → rejected.) Note: ordinary minimal DFA for L needs 4 states;
coloring saves one.

## Transforming a k-colored DFA → ordinary DFA

Colored-acceptance depends on the **set of colors seen so far** along the run, so remember
that set inside the state (subset construction over [k]).

Given A = ⟨Q, Σ, δ, q₀, f⟩, build A' = ⟨Q', Σ, δ', q₀', F⟩:
- States: Q' = Q × P([k])   — (current state, set of colors visited so far)
- Start:  q₀' = (q₀, {f(q₀)})
- δ'((q,C), σ) = (δ(q,σ), C ∪ {f(δ(q,σ))})
- F = {(q,C) : C = [k]}   — accept once all k colors collected

**Correctness (induction on |w|):** after w, A' is in (q,C) with q = δ*(q₀,w) and
C = exact set of colors on A's run over w. So w ∈ L(A) ⇔ C = [k] ⇔ (q,C) ∈ F ⇔ w ∈ L(A').
**Size:** |Q'| = |Q|·2^k (can merge all C = [k] states into one accepting sink).
Corollary: k-colored DFAs recognize exactly the regular languages.

## Issues log

- **Q2.א** — How to design a *3-colored* minimal-state DFA and, generally, convert colored
  DFAs to ordinary ones. Resolved: 3 states colored 1/2/3 with every state sending a→q_a,
  b→q_b; run collects all 3 colors iff both letters appear. Minimality: <3 states can't hold
  3 colors. General transform: augment each state with the subset of colors seen so far
  (Q×P([k])), accept when the subset = [k]; blowup |Q|·2^k.
