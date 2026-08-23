# The Human Edge — Editorial Audit and Methodology
**Edition:** 1.0  
**Audit date:** 2026-08-18  
**Scope:** the original 50-question set plus the expanded 120-card edition and its interactive app.
## Executive verdict
I found **no fatal answer-key or numerical error** in the original 50. Its weaknesses were mainly editorial and epistemic rather than arithmetic: hidden assumptions, empirical findings phrased too universally, uneven source quality, and an imbalance toward elegant puzzles over immediately transferable skills.
- **49 of 50 original concepts were retained.** Sixteen were materially tightened, scoped, reclassified, or moved.
- **One concept was removed:** the finite centipede game, because it repeated the backward-induction lesson already tested by the finite prisoner’s dilemma while offering less practical transfer.
- **71 new cards were added**, producing **120 questions in 12 domains**.
- Difficulty distribution: **36 Challenging, 48 Hard, 36 Very Hard**. “Challenging” is the floor; there is deliberately no ordinary easy tier.
- Every card has **three progressive hints, explicit assumptions where needed, an evidence-type label, an explanation, a practical takeaway, and source metadata**.
## What was changed
### 1. Assumptions became part of the question
Answers in game theory, causal inference, finance, and probability often flip when the data-generating process changes. The revised wording therefore states protocol details rather than hiding them in the answer. Examples include Monty Hall’s host policy, the finite-horizon/common-knowledge assumptions in repeated games, the common-value structure behind the winner’s curse, the random-arrival assumption in the bus problem, and the no-externality/quasi-linear conditions for truthful bidding in a second-price auction.
### 2. Theorem, model, experiment, and current guidance were separated
A proof is not an empirical frequency, and an experimental regularity is not a universal law. Cards now identify whether an answer is a theorem, a transparent derivation, a model result, a neuropsychological case, an experimental finding, a meta-analytic conclusion, or a current technical guideline. This prevents “the model predicts X” from silently becoming “people always do X.”
### 3. Empirical claims were narrowed
The dopamine card refers to the **classic reward-prediction-error account**, not every function of dopamine. Working-memory capacity is an approximate central estimate under controlled conditions, not a hard human constant. Reconsolidation and extinction cards state boundary conditions. Placebo analgesia is tied to the mechanism demonstrated in the cited setting rather than generalized to every placebo response.
### 4. Sources were upgraded and made inspectable
The source hierarchy was: (1) primary theorem or paper; (2) official standard or government/standards-body guidance; (3) authoritative peer-reviewed review or meta-analysis; (4) a transparent derivation from the card’s assumptions. Direct calculations are labeled as such instead of citing an adjacent paper as though it derived the number. Tracking parameters were removed from links.
- [Nash’s equilibrium theorem — PNAS](https://www.pnas.org/doi/10.1073/pnas.36.1.48)
- [Vickrey’s auction result — Journal of Finance](https://www.cs.princeton.edu/courses/archive/spr09/cos444/papers/vickrey61.pdf)
- [Retrieval-practice evidence — Science / PubMed](https://pubmed.ncbi.nlm.nih.gov/18276894/)
- [ASA p-value statement — American Statistical Association](https://www.tandfonline.com/doi/full/10.1080/00031305.2016.1154108)
- [NIST authentication guidance — NIST SP 800-63B](https://pages.nist.gov/800-63-4/sp800-63b.html)
- [OWASP password-storage guidance — OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### 5. Practical transfer became an inclusion criterion
A card had to do more than surprise. It had to improve at least one of: strategic judgment, resistance to statistical error, learning efficiency, attention design, social coordination, causal reasoning, capital allocation, systems thinking, argument analysis, risk communication, or digital self-defense.
## Why the five added areas belong
| Added emphasis | Direct use |
|---|---|
| **Learning science** | Build durable knowledge through retrieval, spacing, generation, interleaving, and cue design. |
| **Causal inference** | Avoid treating selection, regression, measurement error, or pre-trends as causal effects. |
| **Organizations and systems** | Diagnose queues, bottlenecks, critical paths, metric gaming, incentive failures, and feedback amplification. |
| **Rhetoric, logic, and communication** | Distinguish validity from truth, expose hidden premises, understand implicature, resist repetition effects, and communicate risk honestly. |
| **Digital self-defense** | Use phishing-resistant authentication, safe password storage, parameterized queries, strong backup structure, and correct cryptographic mental models. |
## Inclusion and exclusion rubric
A question was included only when all of the following were true:
1. **Objective answer:** a theorem, calculation, formal definition, named empirical effect with a checkable setup, or current official technical recommendation.
2. **Nontrivial:** a college graduate should need recall plus reasoning, not mere cultural trivia.
3. **Reusable:** the mechanism transfers to decisions beyond the example.
4. **Compact:** enough information fits on one card without relying on unstated conventions.
5. **Sourceable:** the answer can be checked against a primary/official source or reconstructed directly.
6. **Non-philosophical:** no questions whose “correct” answer depends primarily on values, taste, identity, or metaphysical commitments.
Excluded or avoided: personality-type folklore, broad “left-brain/right-brain” claims, simplistic neurotransmitter slogans, investment predictions, political opinion questions, brittle current-events trivia, and claims that cannot be operationalized.
## High-impact corrections to the original set
| Original idea | Audit issue | Revision |
|---|---|---|
| Finite repeated prisoner’s dilemma | Backward induction depends on a known finite horizon, stage-game equilibrium, and common knowledge. | Those conditions are now in the prompt. |
| Second-price auction | Independence was treated as central; it is not required for the weak-dominance truth-telling result. | The card now states private value, quasi-linear utility, standard rules, and no externalities/budget constraints. |
| Winner’s curse | The result is specific to common-value or affiliated-value selection, not all auctions. | Common value and noisy signals are explicit. |
| Secretary problem | Easy to overgeneralize to ordinary hiring or dating. | Random order, known pool, no recall, relative ranks, and “single best” objective are explicit. |
| Dopamine | “Dopamine equals reward/pleasure” is too broad. | The card asks about the classic phasic reward-prediction-error signal. |
| Working memory | “Four” can sound like an immutable biological cap. | The answer is framed as an approximate central estimate under controlled conditions. |
| Reconsolidation | Retrieval does not make every memory modifiable in every situation. | “Under suitable conditions” and restabilization are explicit. |
| Weber’s law | It is an approximation over a range, not an exact universal law. | The valid-range assumption is included. |
| Friendship paradox | The sampling procedure determines the formula. | Uniform edge-endpoint sampling is stated. |
| P-values and confidence intervals | Correct answers require the inferential procedure and model assumptions. | Those conditioning statements are now in the answer/assumptions. |
| Gödel incompleteness | Often overextended to any difficult or unprovable claim. | The formal-system requirements are explicit. |
| Braess’s paradox | Better understood as a systems/congestion lesson than isolated game trivia. | Moved to Organizations, Operations & Systems. |
## Original 50 → revised deck mapping
| # | Original concept | Revised card | Status |
|---:|---|---|---|
| 1 | Mixed-strategy Nash equilibrium | STR-01 | Retained; wording tightened |
| 2 | Finite repeated prisoner’s dilemma | STR-03 | Retained; assumptions exposed |
| 3 | Second-price auction truth-telling | STR-04 | Retained; dominance conditions corrected |
| 4 | Winner’s curse | STR-06 | Retained; common-value conditioning made explicit |
| 5 | Matching pennies | STR-02 | Retained |
| 6 | Finite centipede game | — | Removed: duplicated the backward-induction lesson with lower practical transfer |
| 7 | Secretary problem | STR-07 | Retained; classical assumptions emphasized |
| 8 | Braess’s paradox | SYS-10 | Retained; moved to systems |
| 9 | Condorcet cycle | STR-09 | Retained |
| 10 | Arrow impossibility | STR-10 | Retained; interpretation narrowed |
| 11 | Dopamine prediction error | BRN-01 | Retained; limited to the classic account |
| 12 | H.M. and memory systems | LRN-01 | Retained |
| 13 | Working-memory capacity | LRN-02 | Retained; approximate, task-dependent estimate |
| 14 | Memory reconsolidation | LRN-08 | Retained; boundary conditions added |
| 15 | Misinformation effect | LRN-09 | Retained; claim narrowed |
| 16 | Change blindness | BRN-02 | Retained |
| 17 | Inattentional blindness | BRN-03 | Retained |
| 18 | Naloxone and placebo analgesia | BRN-08 | Retained; mechanism not universalized |
| 19 | Hyperbolic discounting | DEC-05 | Retained |
| 20 | Weber’s law | BRN-04 | Retained; approximation stated |
| 21 | Friendship paradox | SOC-01 | Retained; sampling scheme specified |
| 22 | Ecological fallacy | SOC-02 | Retained |
| 23 | Pluralistic ignorance | SOC-03 | Retained |
| 24 | Schelling segregation model | SOC-04 | Retained; model/world boundary emphasized |
| 25 | Simpson’s paradox | CAU-01 | Retained |
| 26 | Collider bias | CAU-02 | Retained |
| 27 | P-value interpretation | PRO-01 | Retained |
| 28 | Confidence-interval interpretation | PRO-02 | Retained |
| 29 | Multiple-testing familywise risk | PRO-03 | Retained |
| 30 | Base-rate/Bayes calculation | DEC-01 | Retained |
| 31 | Gain/loss compounding | FIN-01 | Retained |
| 32 | Exact real return | FIN-02 | Retained |
| 33 | Bond duration | FIN-03 | Retained |
| 34 | Diversifiable risk | FIN-04 | Retained |
| 35 | Kelly criterion | FIN-05 | Retained |
| 36 | Present value | FIN-06 | Retained |
| 37 | Sequence-of-returns risk | FIN-07 | Retained |
| 38 | Multiple IRRs | FIN-08 | Retained |
| 39 | Leverage and equity loss | FIN-09 | Retained |
| 40 | Sunk cost | DEC-04 | Retained |
| 41 | Jensen’s inequality | MTH-01 | Retained; source corrected |
| 42 | Binary Shannon entropy | MTH-02 | Retained |
| 43 | Universal lossless compression impossibility | MTH-03 | Retained |
| 44 | Halting problem | MTH-04 | Retained |
| 45 | Gödel incompleteness | MTH-05 | Retained; formal scope strengthened |
| 46 | Countable vs. uncountable infinity | MTH-06 | Retained |
| 47 | St. Petersburg paradox | PRO-05 | Retained |
| 48 | Inspection paradox / bus wait | PRO-06 | Retained |
| 49 | Coupon collector | PRO-07 | Retained |
| 50 | Kolmogorov complexity | MTH-07 | Retained |

## Quality assurance performed
- **Content structure:** 120 unique IDs, exactly 10 cards per domain, exactly three hints per card, and no missing category/source references.
- **Numerical verification:** 27 independent programmatic checks cover Bayes, EVPI, multiple testing, birthdays, inspection waiting time, coupon collection, compounding, exact real return, duration, Kelly sizing, present value, sequence risk, IRR roots, entropy, gambler’s ruin, order statistics, Little’s law, M/M/1 delay, Amdahl’s law, reliability, and passphrase entropy.
- **Application behavior:** tested in a Chromium automation run for initial render, hint progression, answer reveal, source rendering, solo/host switching, team creation, and all 120 atlas cards. No JavaScript console errors were observed.
- **Responsive layout:** tested at 1440×1100 and 390×844; the final mobile build had no horizontal overflow.
- **Privacy/offline behavior:** the app contains no external JavaScript, web fonts, trackers, analytics, accounts, or network dependency. Only optional source links require internet access. Progress is stored locally when the browser permits local storage.
## Limitations
- Difficulty is necessarily approximate and depends on background, although the answers themselves are objective.
- Empirical psychology and social-science findings are conditional on task, population, implementation, and measurement; a card is not a guarantee about every person or setting.
- Security guidance can change. The app records this edition’s audit date and links to live official guidance so it can be rechecked.
- The finance cards teach mechanics and decision principles, not personalized investment advice. Medical examples teach inference or mechanisms, not diagnosis or treatment.
- A 120-card deck cannot cover every high-value mental model. Selection favored conceptual breadth, teachability, and direct personal relevance.
## Recommended play rule
Award full points only when the player gives both the answer **and the mechanism**. A correct label without an explanation earns at most half credit. After revealing the answer, ask: “Which assumption is doing the most work, and how would the answer change if it failed?” That turns trivia into transferable judgment.
