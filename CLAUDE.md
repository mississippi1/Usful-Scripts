# Writing Style: Avoid AI-Sounding Patterns

All text written in this repo (docs, comments, commit messages, READMEs, replies) must avoid
the patterns below. They are the documented tells of AI-generated writing, compiled from
Wikipedia's "Signs of AI writing" guide (WikiProject AI Cleanup), the tropes.fyi pattern
directory, and stylometric research. Write like a person: concrete, direct, uneven, and
willing to repeat the clearest word.

## 1. Banned vocabulary (always replace)

| Avoid | Use instead |
|---|---|
| delve / delve into, deep dive | look at, examine, dig into |
| landscape, realm, tapestry, ecosystem (metaphor) | field, area, industry — or name the actual thing |
| leverage, utilize, harness | use |
| robust, seamless, cutting-edge, state-of-the-art | strong, smooth, latest — or a concrete spec |
| pivotal, crucial, paramount | important, key (sparingly) |
| testament to, underscores, highlights | shows, proves |
| meticulous, intricate, nuanced, multifaceted | careful, complex, detailed |
| foster, bolster, facilitate, empower, streamline | help, support, simplify |
| embark, commence | start, begin |
| vibrant, thriving, nestled, boasts | plain description with verifiable details |
| game-changer, watershed moment, paradigm shift | say specifically what changed |
| holistic, actionable, impactful, learnings, synergy | complete, practical, effective, lessons |
| myriad, plethora | many, or a number |
| in order to, due to the fact that | to, because |
| ever-evolving, enduring, burgeoning, nascent | changing, lasting, growing, new |

Cluster rule: even legitimate words (navigate, elevate, resonate, cultivate, illuminate,
cornerstone, poised, quintessential, overarching) read as AI when several appear together.
Two or more in one paragraph — rewrite.

## 2. Banned sentence templates

- **Negative parallelism**: "It's not X — it's Y", "not just X, but Y", "This isn't about X.
  It's about Y." State the positive claim directly.
- **Rule-of-three compulsion**: "innovative, scalable, and transformative." Use one, two, or
  four items when that's what the content has; never pad to three.
- **"The X? A Y."** self-posed rhetorical questions, and openers like "But what does this mean
  for you?" — if you know the answer, just say it.
- **False ranges**: "from the Big Bang to dark matter." List actual items or pick one.
- **Copula avoidance**: "serves as", "stands as", "functions as", "represents", "features",
  "boasts", "marks" in place of "is/has." Say "is" and "has."
- **Superficial -ing analysis**: tacking "highlighting...", "showcasing...", "reflecting...",
  "underscoring its importance..." onto sentence ends. Inanimate facts can't "emphasize"
  anything. Replace with a specific fact or cut.
- **"Despite challenges, X continues to thrive"** and other concede-then-dismiss formulas.
  Name the actual challenge and the actual response, or cut.
- **Hedge stacking**: "could potentially", "may eventually", "might ultimately." One hedge max.
- **Speculative openers**: "Imagine a world where...", "Picture a future in which..."
- **Drama fragments**: "The catch?", "Here's the kicker:", "Here's the thing." State the thing.

## 3. Banned filler and transitions

- "It is important/worth noting that", "Notably", "Interestingly", "Significantly" — delete;
  let the fact speak.
- "Moreover", "Furthermore", "Additionally" as sentence openers — use "and", "also", or nothing.
- "In today's fast-paced world", "in the digital age", "in an era where..." — cut.
- "In conclusion", "In summary", signposted conclusions — end when done; don't announce it.
- "Let's dive in", "Let's break this down", "Let's explore" — start with the content.
- "When it comes to", "at the end of the day", "that being said" — cut or use "but."
- Generic closers: "The future looks bright", "Only time will tell", "Whether you're a beginner
  or an expert..." — these contain no testable content; delete.

## 4. Tone rules

- **No sycophancy**: never open with "Great question!", "Excellent point!", "You're absolutely
  right!" or validate before correcting ("That's an interesting perspective, however..."). If
  something is wrong, say it's wrong in the first sentence.
- **No significance inflation**: don't call routine work "a pivotal moment", "a vital role", or
  "a rich heritage." State what happened; the reader judges importance.
- **No promotional voice**: no travel-brochure or press-release phrasing. Use plain description,
  numbers, and verifiable details.
- **No vague attribution**: never "experts argue", "studies show", "observers have noted",
  "industry reports" without naming the source. Name it or drop the claim.
- **No false balance**: "While X is impressive, Y remains a challenge" — make both halves
  specific or take a side.
- **Have a position**: humans show opinions and preferences. Relentless neutrality is a tell.

## 5. Formatting rules

- **Em dashes**: at most 1–2 per page of text (human norm), not one per paragraph. Prefer
  commas, periods, or parentheses.
- **Bold**: rarely; never bold every list label or every occurrence of a term.
- **Bullets**: only for genuinely list-like content (steps, options). Never 8+ bullets in a
  short doc, never lists of bare noun phrases with no verbs, never "**Label:** text that
  restates the label."
- **Headings**: sentence case, not Title Case. Don't add headers to short text — more than 3
  headings in 300 words is a tell. No formulaic "Overview / Key Points / Conclusion" scaffolds.
- **No emoji** in headings or as list markers. No decorative Unicode arrows (→) in prose.
- **No fractal summaries**: don't summarize at every level (intro summary + section summaries +
  closing summary). Say each thing once.

## 6. Rhythm and structure

- **Vary sentence length** deliberately: mix short sentences (3–8 words) with long ones (20+).
  Uniform medium-length sentences read as machine output.
- **Vary paragraph length**: one-sentence paragraphs are allowed. Not every paragraph is 3–5
  sentences.
- **Repeat the clearest word** instead of synonym-cycling ("developers... engineers...
  practitioners"). Elegant variation is an AI tell.
- **Each paragraph must add something new.** If a paragraph restates the premise in fresh
  words, cut it. Test: if you can shuffle the paragraphs without breaking the piece, it's a
  list, not an argument.
- **Lead with the point**, not broad context-setting. No throat-clearing openings.
- Deliberate fragments and sentences starting with "And" or "But" are fine — over-polished
  grammar everywhere is itself a tell.

## 7. Chatbot artifacts (never emit)

- "I hope this helps!", "Certainly!", "Feel free to reach out", "Let me know if you need
  anything else", "Great question!"
- "As an AI language model...", "As of my last knowledge update...", "While specific details
  are limited...", knowledge-cutoff disclaimers of any kind.
- Restating the prompt back: "You're asking about...", "To answer your question..."
- Reasoning scaffolds: "Let me think step by step", "To approach this systematically."
- Placeholder text: `[Your Name]`, `[INSERT SOURCE]`, unfilled dates.
- Citation-markup leaks (`oaicite`, `citeturn0search0`, `contentReference`) and AI tracking
  params in URLs (`utm_source=chatgpt.com`, `utm_source=claude.ai`).

## 8. Quick self-check before finishing any prose

1. Any word from the banned table? Replace it.
2. Any "not just X but Y", triple list, or "serves as"? Rewrite.
3. Count em dashes and bold spans; cut to near zero.
4. Delete the first sentence if it's context-setting — does the text improve? Usually yes.
5. Read it aloud: if every sentence has the same length and cadence, break the rhythm.
6. Is every claim concrete and attributable? Kill vague attributions and empty superlatives.
