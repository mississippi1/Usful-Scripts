# Study guide — which classes are closed under which reductions

Companion to `Guide - how to answer any reduction claim.md` and the Q8.א anatomy in
`Comp 2025-1 moed A - Q5-Q8.md`. Sources: `Complexity/PROOFS_REFERENCE.md` (E-section reduction
theorems, F/G complexity sections), `lessons/lesson 10.pdf`, `תרגול 12 (4).pdf`.

Closure under reduction is a property of a **class**, not of an individual language:

> **𝒞 is closed under ≤ᵣ** ⟺ ( `A ≤ᵣ B` and `B ∈ 𝒞` ) ⟹ `A ∈ 𝒞`.

It is the *only* bridge from "a reduction exists" to a membership statement, and it is a theorem that
must be proved per (class, reduction) pair — never assumed.

---

## 1. The rule that generates every entry in the tables

Closure is proved by composing "run `f`, then run `B`'s decider" and checking the composition fits
**𝒞's own budget**. Hence:

> **𝒞 can be closed under ≤ᵣ only if 𝒞 is at least as powerful as the reduction itself.**

**Theorem (the forcing direction).** If 𝒞 is closed under ≤ᵣ and contains a nontrivial language `B`
(one yes-instance, one no-instance), then every language decidable inside ≤ᵣ's budget lies in 𝒞.

*Proof.* Let `A` be decidable within the reduction's budget. Define `f(x)` = "decide `x ∈ A`; output a
fixed yes-instance of `B` if yes, a fixed no-instance if no." `f` is computable inside the budget, so
`A ≤ᵣ B`, and closure gives `A ∈ 𝒞`. ∎

Instantiations, each of which explains a whole column of ✘'s:

| Reduction | Its budget | Closure forces |
|---|---|---|
| `≤_L` | logspace | `L ⊆ 𝒞` |
| `≤p` | poly time | `P ⊆ 𝒞` |
| `≤m` | any computable function | `R ⊆ 𝒞` |

**Slogan.** *A reduction transfers a bound only as low as the reduction's own budget.*
Corollary: `A ≤ᵣ (nontrivial B ∈ 𝒟_r)` where `𝒟_r` is the reduction's own class degenerates to
`A ∈ 𝒟_r` — the target's identity becomes irrelevant.

---

## 2. Computability

| Class | `≤m` (computable many-one) | `≤T` (Turing / oracle) |
|---|---|---|
| **R** | ✔ | ✔ |
| **RE** | ✔ | ✘ **provably** |
| **coRE** | ✔ | ✘ provably |
| REG, CFL | ✘ | ✘ |

- **R, RE, coRE under ≤m** ✔ — compose `f` with the decider/recognizer. coRE follows from
  `A ≤m B ⟺ Ā ≤m B̄`.
- **RE under ≤T** ✘ — `Ā_TM ≤T A_TM` (query the oracle, flip the answer), but `A_TM ∈ RE` while
  `Ā_TM ∉ RE`. **This is why the course reduces with ≤m and not with oracles:** ≤m preserves RE,
  ≤T does not.
- **REG under ≤m** ✘ — `{aⁿbⁿ} ≤m {a}` by the canned-answer trick; closure would force `R ⊆ REG`.

---

## 3. Complexity

| Class | `≤_L` | `≤p` (Karp) | `≤m` (computable) |
|---|---|---|---|
| REG, CFL | ✘ | ✘ | ✘ |
| **L** | ✔ | ✘ — *equivalent to* `L = P` | ✘ |
| **NL** | ✔ | ✘ — *equivalent to* `NL = P` | ✘ |
| **P** | ✔ | ✔ | ✘ |
| **NP** | ✔ | ✔ | ✘ |
| **coNP** | ✔ | ✔ | ✘ |
| **PSPACE** | ✔ | ✔ | ✘ |
| **EXP, EXPSPACE** | ✔ | ✔ | ✘ |
| **R, RE, coRE** | ✔ | ✔ | ✔ |
| `TIME(nᵏ)`, `SPACE(nᵏ)`, fixed `k` | ✘ | ✘ | ✘ |

(`≤_L ⊆ ≤p ⊆ ≤m` as *classes of reductions*, so closure under a **weaker** reduction is implied by
closure under a stronger one — that is why the ✔'s form an upper-left staircase.)

### The three cells worth understanding

**P / NP / PSPACE under ≤p ✔.** `f` runs in `p(n)`, so `|f(x)| ≤ p(n)` (a TM writes at most one symbol
per step); the decider costs `q(p(n))`; **polynomials are closed under composition**. NP guesses after
the mapping; PSPACE/EXP identical accounting.

**NP under ≤m ✘ — the same trap as NL-under-≤p, one floor up.** A computable reduction may run for
`2^{2ⁿ}` steps, decide the source outright, and emit a canned SAT instance. Closure would force
`R ⊆ NP`, false since `NP ⊆ EXP ⊊ R` (time hierarchy). So `A ≤m SAT` yields nothing beyond `A ∈ R`.

**L / NL under ≤_L ✔ but under ≤p ✘.**

| | why |
|---|---|
| `≤_L` ✔ | You cannot **store** `f(x)` (poly-size). Instead **recompute on demand**: rerun `f` from scratch whenever the target's algorithm requests its `i`-th input bit, keeping only a counter. `O(log n)` for `f` + `O(log n)` counter + `O(log\|f(x)\|) = O(log n)` for the target. |
| `≤p` ✘ | The composed machine must **write** a poly-size intermediate string — that alone breaks the logspace budget. And closure here is *equivalent to* `NL = P` (resp. `L = P`): for nontrivial `A ∈ P`, `A ≤p PATH`, so closure ⇒ `P ⊆ NL ⊆ P`. |

---

## 4. Different axis — closure under complement (commonly confused with the above)

| | R | RE | coRE | L | NL | P | NP | coNP | PSPACE | EXP |
|---|---|---|---|---|---|---|---|---|---|---|
| complement | ✔ | ✘ | ✘ | ✔ | ✔ (Immerman–Szelepcsényi) | ✔ | open | open | ✔ | ✔ |

Deterministic classes are closed by flipping the decider's answer; RE is not (else `RE ∩ coRE = R`
would collapse `A_TM`); NL is a theorem (IS), not an obvious fact.

---

## 5. How the closure facts get used

1. **Transfer membership.** `A ≤ᵣ B`, `B ∈ 𝒞`, 𝒞 closed under ≤ᵣ ⟹ `A ∈ 𝒞`.
2. **Transfer hardness (contrapositive).** `A ∉ 𝒞` and `A ≤ᵣ B` ⟹ `B ∉ 𝒞`. Shape of every
   "show `L ∉ RE`" answer: `Ā_TM ≤m L`.
3. **Completeness lemma.** If `A` is 𝒞-complete under ≤ᵣ and `A ∈ 𝒟` with 𝒟 ⊆ 𝒞 closed under ≤ᵣ,
   then `𝒞 = 𝒟`. Engine behind `SAT ∈ P ⇒ P = NP`, `TQBF ∈ NP ⇒ NP = PSPACE`,
   `ALL_NFA ≤p PATH ⇒ P = PSPACE`.
4. **Refuting a reduction** needs the full chain — closure is the link people skip:

```
reduction exists --[𝒞 closed under ≤ᵣ]--> A ∈ 𝒞 --[A is 𝒞'-complete]--> 𝒞' ⊆ 𝒞 --[hierarchy]--> ⊥
```

**Procedure.** (i) Name the reduction's budget. (ii) Name the target's class. (iii) Look up the cell —
if the class is closed, transfer; if the reduction is the stronger of the two, the claim degenerates to
"source ∈ (reduction's own class)". (iv) Only then reach for a hierarchy theorem.
