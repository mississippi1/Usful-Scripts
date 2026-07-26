# Comp 2023-2 (קיץ 2023) moed A — Q6 (12 pts, T/F+proof): does L∈RE reduce to f(L)?

Source exam: `Complexity/2017-2025 Exams/Comp 2023-2 moed A.pdf` (page 7)
Official solution: `Complexity/2017-2025 Exams solutions/Comp 2023-2 moed A solution.pdf` (page 7)

**Question.** Let f:Σ*→Σ* be a computable function and L⊆Σ* satisfy f(L)≠Σ*.
Claim: if L∈RE then L≤_m f(L). Mark correct/incorrect and prove.

Note on transcription: an initial pypdf text-layer extraction of the exam PDF dropped the
"E" and read the hypothesis as "L∈R" — WRONG. Rendering the page as an image (pypdf's text
layer for this PDF is unreliable for Hebrew math text) confirmed the hypothesis is
genuinely "L∈RE", matching the screenshot exactly, including the in-exam clarification
("הבהרה במבחן") that restates it the same way.

## Answer: FALSE (the official solution circles "לא נכונה")

If a screenshot of this question shows "נכונה" (correct) circled, that does not match the
official solution — flagged directly, per the pattern used elsewhere in these notes when a
transcribed/circled answer conflicts with a verified source.

## The counterexample

Take L = A_TM (the acceptance problem, {⟨M,w⟩ : M accepts w}) — the canonical RE\R language
(RE but not decidable). Take f to be the constant function f(x) = ε.

Then f(A_TM) = {ε} (image of a nonempty set under a constant function), and {ε} ≠ Σ*, so
both hypotheses of the claim hold: A_TM ∈ RE and f(A_TM) ≠ Σ*.

If the claim were true, A_TM ≤_m f(A_TM) = {ε} would have to hold. But {ε} ∈ R (finite,
trivially decidable). By the reduction theorem (A ≤_m B and B∈R ⟹ A∈R), this would force
A_TM ∈ R. But A_TM ∉ R (the acceptance/halting problem is undecidable — the foundational
fact of the course). Contradiction.

So A_TM ≤_m f(A_TM) = {ε} does NOT hold, even though A_TM ∈ RE and f(A_TM) ≠ Σ*. This
directly falsifies the claim. ∎

## Why this generalizes

The real content is just the contrapositive of the reduction theorem: an undecidable
language can never ≤_m-reduce to a decidable one. So the claim fails for any L ∈ RE\R paired
with any f whose image f(L) happens to be decidable and ≠Σ* — the constant function is just
the simplest way to force f(L) to be decidable (a single point). The hypothesis f(L)≠Σ* is
there to rule out a different degenerate failure mode, not to prevent this one.

## Contrast — why the same claim WOULD be true if the hypothesis were L∈R

Worth presenting side by side, since it pinpoints exactly where the RE version breaks.

If L ∈ R (decidable), fix any z0 ∉ f(L) (exists since f(L)≠Σ*). Define:

    g(w) = f(w)   if w ∈ L    (decide this — always halts, since L∈R)
         = z0     if w ∉ L

g is computable (deciding L always terminates). Correctness: w∈L ⟹ g(w)=f(w)∈f(L)
(trivially, by definition of image); w∉L ⟹ g(w)=z0∉f(L) (by choice of z0). So
w∈L ⟺ g(w)∈f(L) exactly — a valid reduction L≤_m f(L). This proof genuinely works when
L∈R.

The only place it breaks for L∈RE: the first step, "decide w∈L", requires L decidable. For
merely-RE L (like A_TM), there's no way to always halt that decision — you can
semi-decide it (run forever if w∉L), but a mapping-reduction function g must be TOTAL
(halt on every input, including non-members). Losing that one guarantee is exactly what
breaks the construction — and the counterexample shows the gap is real, not just a
limitation of this specific proof attempt.

## Follow-up — what if the "f(L)≠Σ*" hypothesis were dropped?

The claim breaks even harder, and even for the L∈R version, for a reason that has nothing
to do with decidability at all.

**General fact.** A ≤_m B means: computable g with w∈A ⟺ g(w)∈B. If B = Σ*, then g(w)∈Σ* is
tautologically true for every w (just the definition of g's codomain — it carries zero
information). So A ≤_m Σ* forces w∈A ⟺ TRUE for every w, i.e. A = Σ* exactly. No wiggle
room: if A misses even one string, the reduction is impossible. (Symmetrically, A ≤_m ∅
forces A = ∅.) Σ* and ∅ are the two "trivial" targets in reduction theory for exactly this
reason.

**Concrete counterexample, even for L∈R.** Let Σ={0,1}, L = 0* = {ε,0,00,000,…} — clearly
decidable (L∈R, regular even). Let e:ℕ→Σ* be the standard enumeration of Σ*
(e(0)=ε, e(1)=0, e(2)=1, e(3)=00, …, a computable bijection). Define:

    f(0^n) = e(n)     for w = 0^n ∈ L
    f(w)   = ε        for any w ∉ 0*  (arbitrary elsewhere)

f is computable (checking w∈0* is decidable). Since e is a bijection onto Σ*,
f(L) = f(0*) = {e(n) : n≥0} = Σ* — the full language. But L = 0* ≠ Σ* (e.g. "1"∉L).

So even though L∈R (which should otherwise guarantee L≤_m f(L) by the construction in the
previous section), f(L)=Σ* now, and by the general fact above L≤_mΣ* is impossible unless
L=Σ*, which it isn't. The earlier proof doesn't even get started: there is no z0∉f(L) to
divert rejected inputs to, since f(L) is everything.

**Takeaway.** f(L)≠Σ* isn't a patch for one corner case of the RE counterexample — it's
load-bearing for the whole problem, R version included. Dropping it kills the claim for a
reason that has nothing to do with the RE/R distinction: Σ* is simply an information-free
reduction target. That's exactly why the exam bakes this hypothesis into the statement
rather than leaving it implicit — it isolates the genuinely interesting question (does L's
decidability status matter?) from this much more basic obstruction.

## Issues log

- **Q6** — Screenshot showed "L∈RE" as the hypothesis with "נכונה" (correct) circled.
  Resolved: confirmed via image-rendered official solution (not just text extraction, which
  had mis-read "RE" as "R" on a first pass) that the hypothesis is indeed L∈RE, and the
  correct answer is "לא נכונה" (incorrect) — the circled answer in the screenshot does not
  match the official solution. Counterexample: L=A_TM (∈RE\R), f(x)=ε constant, giving
  f(A_TM)={ε}∈R; if A_TM≤_m{ε} held, the reduction theorem would force A_TM∈R, contradicting
  A_TM∉R. Also worked out why the same claim IS true if the hypothesis were L∈R instead
  (decide membership, then route through f(w) or a fixed non-image witness z0), to pin down
  exactly which step of that construction needs decidability and fails for merely-RE L.
- **Q6 follow-up** — Asked what changes if f(L) were allowed to equal Σ*. Resolved: the
  claim breaks even for L∈R, for a reason unrelated to decidability — A≤_mΣ* forces A=Σ*
  exactly (g(w)∈Σ* is tautological, carries no information), so any f achieving f(L)=Σ*
  with L≠Σ* is an immediate counterexample regardless of L's class. Concrete instance:
  L=0*∈R, f a bijection from 0* onto Σ* via the standard enumeration (elsewhere arbitrary),
  giving f(L)=Σ*≠L. Confirms f(L)≠Σ* is load-bearing for the whole problem, not just a
  patch for the RE counterexample.
