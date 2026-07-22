# Comp 2022-2, Moed B — Question 6 (study notes)

Source exam: `Complexity/2017-2025 Exams/Comp 2022-2 moed B.pdf`
Official solution: `Complexity/2017-2025 Exams solutions/Comp 2022-2 moed B solution.pdf`

## Q6 (12 pts)

Using the language defined in Q5 (f : {0,1}* → {0,1}* computable):

L_{f,TM} = { ⟨M⟩ | on every input x ∈ {0,1}*, M halts with f(x) written on the tape }.

Claim: **L_{f,TM} ∈ RE.**

**Answer: FALSE (לא נכונה).** In fact L_{f,TM} ∉ RE. (Combined with Q5, which shows
L_{f,TM} ∉ coRE, the language is ∉ RE ∪ coRE.)

To show ∉ RE, reduce a non-RE language A ≤m L_{f,TM}: if L_{f,TM} were in RE then A would be
too (RE is closed downward under ≤m), a contradiction. Two valid reductions:

### Official proof — reduce { ⟨M⟩ : M does not halt on ε } ≤m L_{f,TM}

(The non-halting-on-ε language is coRE-complete, hence ∉ RE.) Let M_f compute f. Given ⟨M⟩,
output M' that on input w:
- simulates M on ε for exactly |w| steps (a bounded simulation, so M' always halts);
- if M halted within |w| steps: print f(w) **plus one extra letter** (output ≠ f(w));
- otherwise (M did not halt within |w| steps): print exactly f(w).

Correctness:
- M loops on ε ⟹ for every w, M is not caught within |w| steps ⟹ M' prints exactly f(w) ⟹
  ⟨M'⟩ ∈ L_{f,TM}.
- M halts on ε in n steps ⟹ for every w with |w| ≥ n, M is caught ⟹ M' prints the wrong word ⟹
  ⟨M'⟩ ∉ L_{f,TM}.

The elegance: M' always halts; the reduction only controls whether the *output* equals f(w).

### Alternative proof (validated) — reduce ALL_TM ≤m L_{f,TM}

ALL_TM = { ⟨M⟩ : L(M) = Σ* } ∉ RE. Given ⟨M⟩, output M' that on input x:
- **keep a copy of x** (simulation can overwrite the tape), then simulate M on x;
- if M accepts: erase and write exactly f(x), halt;
- if M rejects: write f(x)·1 (which ≠ f(x), different length), halt;
- if M loops on x: M' loops (never halts).
- (Inputs ∉ {0,1}* are a don't-care — the language only quantifies over {0,1}*.)

Correctness:
- ⟨M⟩ ∈ ALL_TM ⟹ M accepts every x ⟹ M' writes exactly f(x) and halts on every x ⟹
  ⟨M'⟩ ∈ L_{f,TM}.
- ⟨M⟩ ∉ ALL_TM ⟹ some x₀ is not accepted:
  - M rejects x₀ ⟹ M' halts with f(x₀)·1 ≠ f(x₀) ⟹ ⟨M'⟩ ∉ L_{f,TM};
  - M loops on x₀ ⟹ M' doesn't halt on x₀ ⟹ ⟨M'⟩ ∉ L_{f,TM}.

So ⟨M⟩ ∈ ALL_TM ⟺ ⟨M'⟩ ∈ L_{f,TM}; the map is computable ⟹ L_{f,TM} ∉ RE.

**Contrast:** the official M' always halts and fails membership via a *wrong output*; the ALL_TM
version instead lets M' inherit M's *looping* to fail the "halts on every input" clause. Both
valid; the ALL_TM reduction is more direct because ALL_TM already packages "accepts everything,"
removing the need for the |w|-step timing gadget.

---

## Issues log

Track here which parts gave trouble, and how they were resolved.

- **Q6 (alternative reduction validated):** Solved the "L_{f,TM} ∈ RE?" claim (answer: FALSE) with
  a self-devised reduction **ALL_TM ≤m L_{f,TM}** instead of the official
  non-halting-on-ε reduction. Confirmed correct: M' simulates M on x and writes f(x) on accept,
  f(x)·1 on reject, and inherits M's looping otherwise — so ⟨M⟩ ∈ ALL_TM ⟺ M' halts with f(x) on
  every input. Two points flagged for rigor: (1) f(x)·1 ≠ f(x) always (so the reject branch is a
  genuinely wrong output), and (2) M' must keep a copy of x before simulating M in order to compute
  f(x) afterward. Also noted the language is ∉ RE ∪ coRE (Q5 gives ∉ coRE).
