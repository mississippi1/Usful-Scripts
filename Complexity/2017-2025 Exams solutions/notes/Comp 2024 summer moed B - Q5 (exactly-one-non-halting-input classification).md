# Comp 2024 summer (קיץ) moed B — Q5 (12 pts, class classification): "exactly one non-halting input"

**Question.** Let L be the language of encodings of Turing machines that halt on almost all
inputs, except exactly one. That is:

    L = { ⟨M⟩ : M is a TM and there exists exactly one w ∈ Σ* s.t. M does not halt on w }

Which computability class does L belong to: R, RE\R, coRE\R, or complement(RE∪coRE)?

Note: this exam PDF is likely "Comp 2024-2 moed B.pdf" in this repo's "2017-2025 Exams"
folder (matching "2024-2" = second exam period = summer, by analogy with
"Comp 2025-1 moed A/B/C" = winter 2024-2025), but that PDF is a scan with no extractable
text layer and no PDF rendering tooling was available to confirm the exact question — filed
under a descriptive name instead.

## Answer: complement(RE∪coRE) — neither RE nor coRE (student's circled answer is correct)

## Unpacking the quantifier structure

    L = { ⟨M⟩ : ∃w (¬Halt(M,w)  ∧  ∀w'≠w, Halt(M,w')) }

The inner part, ∀w'≠w, Halt(M,w'), is a universal quantifier over Halt(M,w') — which is only
RE, not decidable (it's literally the halting problem). This is the "∀w [RE predicate]"
pattern — the same core as TOTAL_TM = {⟨M⟩ : M halts on every input}, which is neither RE
nor coRE by the same style of argument as ALL_TM (see the "2020 summer moed B - Q5-Q6" and
"2024 winter moed B" notes for the ALL_TM-style proof pattern). Wrapping an additional ∃w
around an already-outside-both-classes core doesn't pull it back in — confirmed directly
below via two reductions, rather than relying on hierarchy heuristics alone.

## Two reductions, one for each direction

Reserve one input, ε, as a permanent "sacrificial" exception.

### L ∉ coRE — reduce HALT_TM to L

Given ⟨M0,w0⟩, build M'₁:

    M'₁ on input y:
      if y = ε:  loop forever (hardcoded)
      else:      simulate M0 on w0, unbounded (ignore y itself);
                 halt as soon as M0 halts on w0

- M0 halts on w0 (at some fixed step t, same for every y): M'₁ eventually halts on every
  y≠ε (each after ~t internal steps, regardless of y). Non-halting inputs = {ε} exactly
  (size 1) ⟹ ⟨M'₁⟩ ∈ L.
- M0 never halts on w0: M'₁ never halts on any y≠ε either (stuck in the simulation
  forever). Non-halting inputs = all of Σ* — infinite, not 1 ⟹ ⟨M'₁⟩ ∉ L.

So ⟨M0,w0⟩ ∈ HALT_TM ⟺ ⟨M'₁⟩ ∈ L. Since HALT_TM ∉ coRE (standard), L ∉ coRE.

### L ∉ RE — reduce co-HALT_TM to L

Given ⟨M0,w0⟩, build M'₂:

    M'₂ on input y:
      if y = ε:  loop forever (hardcoded)
      else:      simulate M0 on w0 for exactly |y| steps;
                 if M0 has NOT halted within that budget → halt;
                 if M0 HAS halted within that budget     → loop forever

- M0 never halts on w0: for every y≠ε and every budget |y|, the simulation never sees a
  halt, so M'₂ always takes the "halt" branch. Non-halting inputs = {ε} exactly
  ⟹ ⟨M'₂⟩ ∈ L.
- M0 halts on w0 at step t: for y≠ε with |y|<t, M'₂ halts (budget too small to detect it);
  for |y|≥t, M'₂ loops (detects it, deliberately fails). Non-halting inputs =
  {ε} ∪ {y≠ε : |y|≥t} — infinite ⟹ ⟨M'₂⟩ ∉ L.

So ⟨M0,w0⟩ ∈ co-HALT_TM ⟺ ⟨M'₂⟩ ∈ L. Since co-HALT_TM ∉ RE (standard), L ∉ RE.

## Combining

L ∉ RE and L ∉ coRE, so L ∈ complement(RE ∪ coRE). ∎

## The extended quantifier-pattern cheat sheet

| Quantifier shape | Class |
|---|---|
| decidable (finite object, e.g. DFA) — any ∃/∀ combo | R |
| ∃z (RE predicate) | RE (possibly RE\R) |
| ∀w (decidable predicate) | coRE (possibly coRE\R) |
| ∀w (decidable → RE) | generically neither (ALL_TM-style) |
| ∀w (RE predicate, unconditional) | generically neither (TOTAL_TM) |
| ∃w (¬RE ∧ ∀w'≠w RE) — this question | still neither — the ∀-over-RE core dominates |

Consistent lesson: once a ∀ sits directly over a merely-RE (not decidable) predicate — with
no decidable "gate" in front of it — the language generically lands outside both RE and
coRE, and an outer ∃ doesn't rescue it.

## Issues log

- **Q5** — Given as a marked-answer classification question (student circled
  complement(RE∪coRE)). Confirmed correct via two explicit reductions: HALT_TM ≤m L (using
  an unbounded-simulation machine with a single hardcoded non-halting input at ε, giving
  L∉coRE) and co-HALT_TM ≤m L (using a budget-bounded-by-|y| simulation with the same
  hardcoded exception, giving L∉RE). Both reductions hinge on the same "sacrificial ε input"
  trick: force exactly one guaranteed non-halting input by fiat, then make ALL other inputs'
  halting behavior track the hard problem uniformly, so "exactly one exception" becomes
  synonymous with the target problem's truth value. Extended the running quantifier-pattern
  cheat sheet from the "2020 summer moed B Q5-Q6" and prior notes with this example
  (∀ over a bare RE predicate, even wrapped in an outer ∃, stays outside RE∪coRE).
