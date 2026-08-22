## The Human Edge

High-consequence trivia questions.

## Open the game

**Launch the interactive single-file web app by downloading the HTML file!**

It runs entirely in the browser. No installation, account, server, external JavaScript, web font, or internet connection is required. Internet is needed only when opening one of the optional source links.

The bundle contains the app as `index.html`, the structured data, readable answer key, complete audit, editable Python source, and verification script.

| Measure                    |             Result |
| -------------------------- | -----------------: |
| Total questions            |            **120** |
| Original concepts retained |       **49 of 50** |
| New questions              |             **71** |
| Domains                    |             **12** |
| Progressive hints          | **3 per question** |
| Challenging                |             **36** |
| Hard                       |             **48** |
| Very Hard                  |             **36** |
| Source entries             |             **87** |

There is deliberately no ordinary “easy” tier. **Challenging** is the floor.

The source policy privileges primary papers, authoritative reviews, official standards, and transparent derivations. Representative anchors include Nash’s original equilibrium paper, the Karpicke–Roediger retrieval-practice experiment, the ASA’s p-value statement, and current NIST, OWASP, and CISA security guidance.

## The 12 domains

The expanded set covers:
1. Strategy & Negotiation
2. Judgment & Decision-Making
3. Learning & Memory
4. Brain, Attention & Perception
5. Social Dynamics & Networks
6. Probability & Statistical Literacy
7. Causality & Scientific Reasoning
8. Finance & Economics
9. Mathematics, Information & Computation
10. Organizations, Operations & Systems
11. Rhetoric, Logic & Communication
12. Digital Self-Defense & Adversarial Thinking

Emphasis on causality, systems, rhetoric, and security is intentional: these domains directly affect whether someone learns efficiently, interprets evidence correctly, coordinates people, communicates risk, designs incentives, avoids manipulation, and protects important information.

## App functionality

The app includes:
* Click-the-card and button-based answer reveal
* Three progressively more revealing hints
* Hint-based point deductions
* Solo and host modes
* Two to four editable teams
* Team scoring and turn rotation
* Optional 30-, 60-, or 90-second timer
* Search and multi-domain filtering
* Difficulty filtering
* Random-unseen-card selection
* A visual atlas of all 120 cards
* Saved and mastered states
* Local progress persistence
* Progress export
* Focus and fullscreen presentation modes
* Keyboard shortcuts
* Per-card assumptions and evidence classification
* Practical “why this matters” explanations
* Direct source links
* Responsive desktop and mobile layouts
* Reduced-motion accessibility support
* Print-friendly answer rendering

For group play, the strongest rule is to award full credit only when a player supplies both **the answer and the mechanism**. After revealing the card, ask which assumption is doing the most work and how the conclusion would change if it failed.

## Supporting files

* **Complete editorial audit and original-50 mapping**: `THE_HUMAN_EDGE_AUDIT.md`
* **Readable 120-question answer key: `THE_HUMAN_EDGE_QUESTION_BANK.md`
* **Structured JSON question bank**: `human_edge_questions.json`

The final build passed 27 independent numerical checks, structural validation of all 120 cards and 360 hints, automated interaction tests for hints, answers, sources, team creation and scoring, and question-atlas rendering. It was also checked at desktop and mobile dimensions with no JavaScript console errors or mobile horizontal overflow.

Sources: To see the list of sources, open the HTML/game.
