# MINDMESH Edition 03 — Build and Audit Report

## Audit scope

This release is a ground-up application rebuild around the audited 160-card bank. The main goal was not another cosmetic theme. It was to make the interface feel authored, improve the game model, remove misleading measurement language, harden accessibility and local play, and reduce exploitable answer-choice patterns.

## 1. Product and visual redesign

The previous neon/glass dashboard language was replaced with an **editorial field-atlas** system:

- warm paper and ink instead of generic dark gradients;
- vermillion and ultramarine used as meaningful editorial marks;
- a custom 16-node human-signal map rather than stock illustration;
- route tickets, ruled sheets, margin notes, chapter traces, and field reports;
- deliberate serif/sans/monospace hierarchy using system fonts only;
- no external visual assets or dependencies;
- a restrained night edition rather than a mechanically inverted theme.

The result is a single-file application that remains usable offline and does not depend on a framework or CDN.

## 2. Deck integrity

Final bank totals:

| Measure | Result |
|---|---:|
| Questions | 160 |
| Chapters | 16 |
| Questions per chapter | 10 |
| Research sources | 100 |
| Average sources per question | 1.3125 |
| Duplicate prompts | 0 |
| Questions containing duplicate options | 0 |
| HTTPS source links | 100 / 100 |
| Stored answer positions | 40 A · 40 B · 40 C · 40 D |

Difficulty distribution:

| Difficulty | Cards |
|---|---:|
| Signal 1 — Applied core | 21 |
| Signal 2 — Analytical | 48 |
| Signal 3 — Advanced | 54 |
| Signal 4 — Research edge | 37 |

Choices are shuffled at runtime in addition to the source-position balance.

## 3. Answer-length leakage audit

The v2 expansion still had a detectable length cue. Twenty distractors were rewritten without changing the correct answers, explanations, evidence, or learning objectives.

| Metric | v2 | v3 |
|---|---:|---:|
| Correct option tied for longest | 67/160 · 41.88% | 47/160 · 29.38% |
| Correct option uniquely longest | 58/160 · 36.25% | 38/160 · 23.75% |
| Expected accuracy of “choose a longest option”* | 38.85% | 26.35% |
| Expected accuracy of “choose a shortest option”* | 22.50% | 22.50% |
| Mean correct-minus-distractor length gap | +1.594 chars | +0.169 chars |
| Median gap | +2.000 chars | +0.667 chars |

\*Ties are resolved uniformly at random. Chance performance in a four-option item is 25%.

The residual longest-option heuristic is now approximately chance rather than a viable meta-strategy. This is not a claim that every possible linguistic cue has been eliminated; it is a specific, reproducible audit of option length.

## 4. Game-system corrections

### Calibration

The earlier app presented `1 − mean Brier loss` as a calibration score. That was removed. Edition 03 reports separate quantities:

- **accuracy** — observed correctness;
- **average confidence** — mean pre-feedback forecast;
- **confidence gap** — confidence minus accuracy;
- **expected calibration error** — weighted absolute confidence/accuracy deviation across the four confidence bins;
- **Brier loss** — squared probability error, labeled as a combined probability-quality measure rather than calibration alone;
- **calibration plot** — confidence versus observed accuracy, with sample counts.

Timed-out unanswered cards are excluded from confidence-only calculations because no forecast was logged; they remain incorrect for accuracy and scoring.

### Session construction

Balanced routes now balance both chapter and difficulty. Reproducible session codes use deterministic shuffling. Weak-area and unseen-first routes use local history while retaining variety. No session can contain duplicate cards.

### Team play

Team scores, streaks, accuracy, and turn ownership are independent. A protected handoff dialog prevents the next answer from being exposed while the device changes hands.

### Study mode

Open-notebook mode removes score pressure and timers while preserving hints, explanations, field moves, boundary conditions, notes, and evidence.

## 5. Accessibility and interaction audit

Implemented and browser-tested:

- semantic buttons and headings;
- skip link;
- radiogroup semantics with a single roving `tabindex` target;
- Up/Down/Left/Right navigation and selection within answers;
- visible keyboard focus;
- modal focus containment and return to the invoking control;
- `Escape` dismissal for ordinary dialogs;
- protected team handoff behavior;
- status/live-region announcements;
- progressbar semantics;
- reduced-motion behavior;
- forced-colors support;
- no horizontal overflow at a 390 × 844 viewport.

This is a practical implementation audit, not formal accessibility certification. No claim is made that every browser/screen-reader combination has been independently certified.

## 6. Automated regression results

The final file passed the following Chromium/Playwright flows:

| Flow | Result |
|---|---|
| JavaScript syntax check | Pass |
| Solo 12-card session through report | Pass |
| Answer ledger count | Pass — 12 |
| Calibration plot rendering | Pass |
| Keyboard answer selection | Pass |
| Keyboard confidence adjustment | Pass |
| Evidence search dialog | Pass |
| Dialog focus return and Escape | Pass |
| Two-team relay and handoff | Pass |
| Per-team streak isolation | Pass |
| Open-notebook score/timer rules | Pass |
| Night edition switch | Pass |
| 30-second timeout auto-lock behavior | Pass |
| Unanswered timeout confidence handling | Pass — `null` |
| 24-card balanced routes across four seeds | Pass |
| Unique cards per route | Pass |
| Desktop runtime/page errors | None observed |
| Mobile runtime/page errors | None observed |
| Mobile horizontal overflow | None observed |
| Duplicate HTML element IDs | 0 |
| External script/style dependencies | 0 |

For balanced 24-card test routes, each chapter appeared one or two times. Three tested seeds produced exactly six cards at each difficulty; one produced a 5/7/6/6 distribution because the eligible source bank and category quotas constrained an exact allocation.

## 7. Remaining caveats

- A knowledge game cannot infer personality, empathy, leadership quality, or real-world EQ from a short sample.
- Calibration estimates are noisy in short sessions; bin counts are shown for this reason.
- Research findings have boundary conditions, which the cards state, but no card can encode every methodological dispute or later replication.
- Source URLs can move even when the underlying paper remains available.
- Browser policies for local storage under locally opened files vary. The game catches storage failures and remains playable, but persistence may not be available in every configuration.
- Formal third-party accessibility tooling and assistive-technology certification remain outside this audit.

## 8. Reproducibility

The package includes the standalone HTML and source JSON. The application embeds the same versioned JSON bank (`3.0.0`, build date `2026-08-23`). A session export records the app version, deck version, route code, settings, responses, correctness, confidence, hint usage, timing, explanations, and evidence IDs.
