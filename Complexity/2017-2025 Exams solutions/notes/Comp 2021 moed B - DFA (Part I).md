# Comp 2021 moed B — DFA question (Part I / חלק I)

**Language.** Σ = {0,1}.
L = { w : |w| is **odd** AND #₀(w) is **even** }
(all words whose length is odd and whose number of 0's is even).
Examples: `010 ∈ L` (len 3 odd, two 0's even); `01010 ∉ L` (len 5 odd, but three 0's — odd).

Part I.1 (7 pts): draw a **minimal DFA** for L (and, here, prove minimality).

## Solution

Track two independent parity bits: (length parity, #₀ parity) ∈ {E,O}×{e,o} → 4 states.
Reading a symbol always flips length parity; it flips #₀ parity only on `0`.

| state | meaning | reached by |
|---|---|---|
| A | (len Even, #₀ even) — **start** | ε |
| B | (len Odd, #₀ even) — **accepting** | 1 |
| C | (len Even, #₀ odd) | 01 |
| D | (len Odd, #₀ odd) | 0 |

Transitions — on `0`: flip both parities; on `1`: flip length parity only.

| state | on 0 | on 1 |
|---|---|---|
| A=(E,e) | D | B |
| B=(O,e) ✓ | C | A |
| C=(E,o) | B | D |
| D=(O,o) | A | C |

Start A, unique accepting state B. This matches the DFA drawn in the exam.
Trace `010`: A→D→C→B (accept ✓). Trace `01010`: A→D→C→B→A→D (reject ✓).

## Minimality (Myhill–Nerode)

Representatives x_A=ε, x_B=1, x_C=01, x_D=0 lie in 4 distinct ∼_L classes.
Distinguishing suffixes z (u ∈ L iff |u| odd and #₀(u) even):

| pair | z | word1·z | word2·z |
|---|---|---|---|
| A,B | ε | ε ∉ L | 1 ∈ L |
| B,C | ε | 1 ∈ L | 01 ∉ L |
| B,D | ε | 1 ∈ L | 0 ∉ L |
| A,C | 1 | 1 ∈ L | 011 ∉ L (len 3, #₀=1) |
| A,D | 1 | 1 ∈ L | 01 ∉ L (len 2) |
| C,D | 0 | 010 ∈ L (len 3, #₀=2) | 00 ∉ L (len 2) |

All 6 pairs separated ⇒ ≥ 4 states required. Our DFA has exactly 4 reachable states,
so it is minimal (and unique up to renaming by Myhill–Nerode). ∎

## Issues log

- **Part I.1** — Confusion over reading the language definition and confirming the drawn 4-state DFA is minimal. Resolved: L = {odd length AND even #₀}; build the product of two parity automata (length parity × #₀ parity) = 4 states, accepting state = (odd length, even #₀). Proved minimality by exhibiting 4 pairwise-distinguishable Myhill–Nerode representatives (ε, 1, 01, 0), giving a matching lower bound of 4 states.
