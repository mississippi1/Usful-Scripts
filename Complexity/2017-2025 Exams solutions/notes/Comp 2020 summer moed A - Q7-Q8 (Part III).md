# Comp 2020 summer (קיץ) Moed A — חלק III, Questions 7-8 (study notes)

Source exam: `Complexity/2017-2025 Exams/Comp 2020 moed A.pdf` (dated 29.7.2020 — this is the
**summer** moed A; a screenshot captioned "מועד א חורף 2020" was mislabeled, the Q7/Q8 text matches
this PDF verbatim), חלק III, Q7-Q8 (7 pts each).
Official solution: `Complexity/2017-2025 Exams solutions/Comp 2020 moed A solution.pdf`.

חלק III instructions: for each claim mark נכונה / לא נכונה / נכונותה לא ידועה; if "לא ידוע", circle
every one of P=NP, P≠NP, NP=coNP, NP=NL, P=PSPACE that would follow if the claim were proved true.
Justify your answer and every implication you circled — no need to justify the ones you left unmarked.
(Q9 of the same part, CLIQUE ≤p PATH, is not covered here.)

## Q7 — the claim

> **Claim:** PATH ≤p HAMCYCLE
>
> PATH = { ⟨G,s,t⟩ : G is a directed graph containing a path from s to t }
> HAMCYCLE = { ⟨G⟩ : G is a directed graph containing a Hamiltonian cycle }

Answer format: mark **נכונה / לא נכונה / לא ידוע**, and if "לא ידוע", circle which of
P=NP, P≠NP, NP=coNP, NP=NL, P=PSPACE would follow from the claim being true.

## Answer

**נכונה (TRUE), unconditionally.** Nothing is circled — no assumption is needed, since the claim is
provable outright.

## Proof 1 (the "textbook" one-liner)

- PATH ∈ NL ⊆ P ⊆ **NP**. (Reachability: BFS/DFS from s, accept iff t is reached.)
- HAMCYCLE is **NP-hard** (known theorem from the course).
- By definition of NP-hardness, **every** L ∈ NP satisfies L ≤p HAMCYCLE. In particular PATH ≤p HAMCYCLE. ∎

## Proof 2 (explicit reduction — the one worth writing on the exam)

**Lemma.** If A ∈ P and B is *non-trivial* (i.e. B ≠ ∅ and B ≠ Σ*), then A ≤p B.

*Proof.* Since B is non-trivial, fix once and for all two constant strings y_yes ∈ B and y_no ∉ B.
Define

  f(x) = y_yes if x ∈ A,  f(x) = y_no if x ∉ A.

f is computable in polynomial time: run the poly-time decider for A on x, then print one of two
**hard-coded constant** strings (constants, so printing them costs O(1)). And x ∈ A ⟺ f(x) ∈ B by
construction. ∎

**Applying it here.**

- A = PATH ∈ P: on ⟨G,s,t⟩ run BFS/DFS from s in O(|V|+|E|) time and check whether t is reached.
- B = HAMCYCLE is non-trivial:
  - **yes-instance** G_yes = the 2-cycle: V = {1,2}, E = {(1,2),(2,1)}. The cycle 1→2→1 visits every
    vertex exactly once, so ⟨G_yes⟩ ∈ HAMCYCLE. (Using a 2-cycle rather than a single self-loop
    vertex avoids any quibble about whether a self-loop counts as a cycle.)
  - **no-instance** G_no = V = {1,2}, E = ∅. No edges at all, so no cycle, so ⟨G_no⟩ ∉ HAMCYCLE.

So the reduction, spelled out, is: **on input x**
1. If x is not a well-formed encoding ⟨G,s,t⟩ of a directed graph with two marked vertices, output ⟨G_no⟩.
2. Otherwise run BFS from s in G.
3. If t was reached, output ⟨G_yes⟩; else output ⟨G_no⟩.

Runs in polynomial (in fact linear) time, and x ∈ PATH ⟺ f(x) ∈ HAMCYCLE. ∎

## Why this is not "cheating", and why no assumption is needed

The trap in the question is the intuition *"PATH is easy and HAMCYCLE is hard, so surely you can't
reduce one to the other without P=NP."* That gets the direction of a Karp reduction backwards:

- A ≤p B means **"A is no harder than B"**. Reducing an *easy* language to a *hard* one is the
  harmless direction and is always fine.
- The direction that would be explosive is the other one: **HAMCYCLE ≤p PATH** would put an
  NP-complete language in P (PATH ∈ P and P is closed under ≤p), giving **P = NP**. *That* is the
  claim where you'd mark "לא ידוע" and circle P = NP.

Also note the definition of a Karp reduction places no restriction on the reduction "doing the work"
itself — f may decide A internally. That is exactly why every language in P reduces to every
non-trivial language, and it is a standard, accepted argument.

Two degenerate cases the lemma legitimately excludes (worth a sentence if you want full rigor):
B = ∅ and B = Σ* have no reduction *into* them from any non-trivial A. HAMCYCLE is neither, as
witnessed by G_yes and G_no above.

## Variant: what if the reduction had to be **log-space** (PATH ≤L HAMCYCLE)?

**Bottom line: the claim stays TRUE and still needs no assumption — but Proof 2 dies and Proof 1
becomes the only route, in a strengthened form.**

**Why Proof 2 breaks.** The constant-output lemma generalizes verbatim, but with P replaced by L:

  *If A ∈ **L** and B is non-trivial, then A ≤L B.*

(Printing a hard-coded constant costs O(1) workspace, so the output step is fine — the write-only
output tape never counts against the space bound. The expensive part is the decision.) To use it here
we would need **PATH ∈ L**. But PATH is **NL-complete** under log-space reductions, so

  PATH ∈ L ⟺ **L = NL**,

which is *open*. (Reingold 2005 put *undirected* reachability USTCON in L; the directed case is
exactly the L vs NL question.) So the "just decide it and print a constant" trick is unavailable —
BFS needs a queue of up to n vertices, i.e. linear space, not O(log n).

**Why the claim is nonetheless still true.** Proof 1 survives, provided you use the sharper fact:

- PATH ∈ NL ⊆ P ⊆ **NP**;
- HAMCYCLE is **NP-hard under log-space reductions** — Cook–Levin and the whole classical chain
  (SAT → 3SAT → … → HAMCYCLE) are computable in log space (in fact in AC⁰/FO for most links);
- hence every L ∈ NP satisfies L ≤L HAMCYCLE, PATH included. ∎

So on an exam the answer is still **נכונה**, but the justification has to lean on log-space
NP-hardness rather than on "PATH is easy, so decide it inside the reduction". If your course only
states NP-hardness with respect to ≤p, say explicitly that the standard reductions are log-space
computable — that is the one load-bearing extra claim.

**Other things that change.**

- **Strength.** Log-space ⟹ poly time, so ≤L ⊆ ≤p: a log-space reduction is a *stronger* statement
  and implies the original claim. Output length is automatically polynomial.
- **Transitivity still holds**, but the proof is not "run f, then g" — the intermediate string f(x)
  can be polynomially long and cannot be stored. The standard fix is to run g and, whenever it wants
  the i-th symbol of f(x), re-run f from scratch keeping only a counter.
- **The reverse claim gets a stronger consequence.** HAMCYCLE ≤L PATH would put HAMCYCLE in NL
  (NL is closed under ≤L), giving NP ⊆ NL ⊆ P — so both **P = NP** and **NP = NL**. (With ≤p it
  only gives P = NP.)
- **Why the course bothers with ≤L at all:** precisely because of the degeneracy exhibited by Proof 2.
  Under ≤p every non-trivial language in P is "complete" for NL, P, and every class inside P, so ≤p
  is useless for classifying anything below P. NL-completeness of PATH is only meaningful with
  respect to ≤L.

## Exam checklist for this item

- [x] Mark **נכונה**; circle nothing among P=NP / P≠NP / NP=coNP / NP=NL / P=PSPACE.
- [x] Justify: PATH ∈ P (BFS), HAMCYCLE non-trivial → constant-output reduction; or PATH ∈ NP +
      HAMCYCLE NP-hard.
- [x] Exhibit the two concrete constants G_yes, G_no — don't just assert non-triviality.
- [x] Say explicitly that the reduction runs in poly time.

---

# Q8 (7 pts) — the claim

> **Claim:** TQBF ∈ P
>
> Reminder: TQBF is the language of all boolean formulas in which **every variable is quantified**,
> and the quantified formula is **true**.

## Answer

**נכונותה לא ידועה (UNKNOWN).** Circle **P = NP**, **NP = coNP**, **P = PSPACE**.
Do **not** circle P ≠ NP (it is contradicted) and do **not** circle NP = NL (it is *refuted* — see below).

## Why the status is unknown

TQBF is **PSPACE-complete** (Stockmeyer–Meyer). So "TQBF ∈ P" is not merely *related to* P = PSPACE —
it **is** that open question restated, exactly as "SAT ∈ P" is P = NP restated. Widely believed false.

Easy half, worth one line on the exam: **TQBF ∈ PSPACE** — evaluate the quantifier tree recursively,
reusing space between the two recursive calls; recursion depth ≤ #variables, so O(n) bits suffice.

## The implications, each justified

- **P = PSPACE.** Let L ∈ PSPACE be arbitrary. TQBF is PSPACE-complete, so L ≤p TQBF; by assumption
  TQBF ∈ P; P is closed under ≤p; hence L ∈ P. So PSPACE ⊆ P, and P ⊆ PSPACE always. ∎
- **P = NP.** P ⊆ NP ⊆ PSPACE = P. (NP ⊆ PSPACE: enumerate certificates one at a time, reusing the
  space; or NP ⊆ NPSPACE = PSPACE by Savitch.) ∎
- **NP = coNP.** From P = NP plus closure of P under complement: coNP = co(P) = P = NP. ∎

## Why NP = NL must NOT be circled

Stronger than "does not follow" — the assumption **refutes** it:

- Under the assumption NP = P = PSPACE.
- But **NL ⊊ PSPACE unconditionally**: NL ⊆ SPACE(log²n) by Savitch, and SPACE(log²n) ⊊ PSPACE by the
  space hierarchy theorem.
- Hence NP = PSPACE ≠ NL.

Related fact worth carrying: we *can* prove **TQBF ∉ L** (L ⊊ PSPACE by the space hierarchy theorem,
and TQBF is PSPACE-complete under log-space reductions), yet we cannot prove TQBF ∉ P. Hierarchy
theorems separate classes measured in the *same* resource; P vs PSPACE crosses time against space,
which is where the tools run out.

## Exam checklist for this item

- [x] Mark **נכונותה לא ידועה**; circle exactly P = NP, NP = coNP, P = PSPACE.
- [x] State TQBF is PSPACE-complete — that is the engine for the whole item.
- [x] Justify each circled implication (the exam explicitly requires it); the chain is
      P = PSPACE ⟹ P = NP ⟹ NP = coNP.
- [x] Do not reflexively circle NP = NL just because other collapses hold.

---

## Issues log

Track here which parts gave trouble, and how they were resolved.

- **Q7 (PATH ≤p HAMCYCLE — true, false, or unknown?):** Resolved as **נכונה, unconditionally**,
  with nothing circled. Confusion came from reading ≤p as "same difficulty" and expecting that
  linking an easy language to an NP-complete one must need P=NP. Clarified: A ≤p B means A is *no
  harder than* B, so easy→hard is always allowed. Two proofs recorded: (1) PATH ∈ NL ⊆ P ⊆ NP and
  HAMCYCLE is NP-hard, so every NP language reduces to it; (2) explicit reduction — decide PATH by
  BFS in poly time and output one of two hard-coded constants, ⟨G_yes⟩ = 2-cycle on {1,2} or
  ⟨G_no⟩ = two vertices with no edges — which relies only on HAMCYCLE being non-trivial. Contrast
  noted for the mirror-image exam item: **HAMCYCLE ≤p PATH** is the one that is "לא ידוע" and would
  imply **P = NP**.
- **Q7 (why is a mapping reduction called "mapping"?):** Because the reduction *is* a function —
  a total computable f : Σ* → Σ* with x ∈ A ⟺ f(x) ∈ B — as opposed to a Turing reduction, which is
  an oracle *procedure* (many queries, may negate the answer). The map must preserve both polarities:
  A → B and Ā → B̄, which is why A ≤m B does **not** give Ā ≤m B. The synonym "many-one" (≤m) records
  that f need not be injective; the injective version is a one-one reduction (≤1), so the hierarchy
  is ≤1 ⊂ ≤m ⊂ ≤T. Q7's own reduction is the extreme illustration of "many-one": infinitely many
  PATH instances collapse onto the single string ⟨G_yes⟩.
- **Q7 (what if the reduction had to be log-space, PATH ≤L HAMCYCLE?):** Still **true and
  unconditional**, but the proof changes — see the "Variant" section above. The constant-output
  argument breaks, because it would need PATH ∈ L, and PATH is NL-complete, so that is exactly the
  open **L = NL** question (BFS needs linear space for its queue). What rescues the claim is that
  HAMCYCLE is NP-hard **under log-space reductions** (Cook–Levin and the classical chain are all
  log-space computable), and PATH ∈ NL ⊆ NP. Side facts confirmed: ≤L ⊆ ≤p so the log-space claim is
  strictly stronger; transitivity of ≤L needs the recompute-f-on-demand trick rather than storing the
  intermediate string; and HAMCYCLE ≤L PATH would give NP ⊆ NL, i.e. both P = NP and NP = NL.
- **Q8 (TQBF ∈ P — true, false, or unknown?):** Resolved as **לא ידוע**, circling P = NP, NP = coNP,
  P = PSPACE. Key move: TQBF is PSPACE-complete, so the claim *is* the open P = PSPACE question
  restated (the SAT ∈ P ⟺ P = NP pattern one level up). Implication chain recorded:
  P = PSPACE ⟹ P = NP (since P ⊆ NP ⊆ PSPACE) ⟹ NP = coNP (P closed under complement). The trap
  confirmed: **NP = NL is not merely unimplied but refuted**, because NL ⊆ SPACE(log²n) ⊊ PSPACE
  (Savitch + space hierarchy) while the assumption makes NP = PSPACE. Also noted that TQBF ∉ L *is*
  provable while TQBF ∉ P is not — hierarchy theorems only separate within one resource.
- **Note bookkeeping:** the source PDF `Comp 2020 moed A.pdf` is dated 29.7.2020, i.e. the **summer**
  moed A, and contains both Q7 and Q8 of חלק III verbatim; an earlier screenshot caption saying
  "מועד א חורף 2020" was wrong. File renamed from `Comp 2020 moed A - Q7 (PATH ≤p HAMCYCLE).md` to
  match the repo's "summer/winter" naming convention.
