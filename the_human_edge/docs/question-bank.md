# The Human Edge — Complete 120-Question Bank

This is the readable companion to the interactive app. Answers are visible here; use the HTML app for spoiler-free play, progressive hints, scoring, filtering, and saved progress.

## ♜ Strategy & Negotiation

Equilibria, auctions, bargaining, voting, and strategic information.

### STR-01 · Challenging · 2 points

**Question.** A finite strategic-form game has no pure-strategy Nash equilibrium. In what enlarged strategy space is an equilibrium nevertheless guaranteed to exist?

**Assumptions.** Finite numbers of players and pure actions; expected-utility payoffs.

**Hints.**
1. Enlarge each player’s choices from actions to probability distributions over actions.
2. The equilibrium need not assign probability 1 to any single move.
3. The relevant phrase begins with ‘mixed’.

**Answer.** The space of mixed strategies.

**Explanation.** Nash’s existence theorem guarantees at least one equilibrium for every finite game once players may randomize over their pure actions.

**Practical takeaway.** Randomness can be an equilibrium discipline, not indecision; predictability itself may be exploitable.

**Evidence type.** Theorem  
**Sources.** [PNAS](https://www.pnas.org/doi/10.1073/pnas.36.1.48)  
**Audit status.** Retained; wording tightened

---

### STR-02 · Challenging · 2 points

**Question.** In matching pennies, Player A wins when the coins match and Player B wins when they differ. In Nash equilibrium, with what probability should each player choose Heads?

**Hints.**
1. The goal is to make the opponent indifferent between Heads and Tails.
2. Suppose A used Heads more than half the time; B could exploit that.
3. The equilibrium mixture is symmetric.

**Answer.** Each chooses Heads with probability 1/2.

**Explanation.** Any bias away from one-half gives the opponent a profitable pure response. A 50–50 mixture makes the opponent indifferent.

**Practical takeaway.** A strategy can be optimal precisely because no adversary can predict it better than chance.

**Evidence type.** Game-theoretic derivation  
**Sources.** [PNAS](https://www.pnas.org/doi/10.1073/pnas.36.1.48)  
**Audit status.** Retained

---

### STR-03 · Challenging · 2 points

**Question.** Two fully rational players play a prisoner’s dilemma exactly 100 times. The horizon, payoffs, and rationality are common knowledge, and defection is the unique equilibrium action in the one-shot game. What does backward induction prescribe in round 1?

**Assumptions.** Known finite horizon; unique one-shot Nash outcome; common knowledge of rationality and payoffs.

**Hints.**
1. Begin at round 100, not round 1.
2. Ask whether cooperation in the penultimate round can change the final-round action.
3. The last-round logic propagates backward through all 100 rounds.

**Answer.** Defect in round 1—and in every round.

**Explanation.** Round 100 has the one-shot equilibrium. Once round 100 cannot reward cooperation, the same argument applies to round 99, and recursively to every earlier round.

**Practical takeaway.** Finite horizons can unravel reputational incentives; real cooperation often depends on uncertainty, repeated relationships, norms, or incomplete information absent here.

**Evidence type.** Model result  
**Sources.** [PNAS](https://www.pnas.org/doi/10.1073/pnas.36.1.48)  
**Audit status.** Retained; assumptions made explicit

---

### STR-04 · Hard · 3 points

**Question.** In a standard sealed-bid second-price auction, your private value is v, utility is quasi-linear, and there are no externalities. What bid is weakly dominant?

**Assumptions.** Known private value; quasi-linear utility; standard second-price rules; no budget constraints or externalities. Independence of values is not required for the dominance result.

**Hints.**
1. Conditional on winning, your own bid usually does not set the price.
2. Compare what happens when the top rival bid is just below your value.
3. Neither shading down nor inflating up can improve every case.

**Answer.** Bid exactly v, your true value.

**Explanation.** Your bid determines whether you win, while the highest competing bid determines the price. Overbidding can make you buy above value; underbidding can make you lose a profitable purchase.

**Practical takeaway.** Mechanism design can make honesty strategically optimal—but only under the mechanism’s stated private-value assumptions.

**Evidence type.** Theorem  
**Sources.** [Journal of Finance](https://www.cs.princeton.edu/courses/archive/spr09/cos444/papers/vickrey61.pdf)  
**Audit status.** Retained; assumptions tightened

---

### STR-05 · Hard · 3 points

**Question.** There are n risk-neutral bidders in a first-price sealed-bid auction. Values are i.i.d. uniform on [0,1]. In the symmetric equilibrium, what does a bidder with value v bid?

**Assumptions.** Risk-neutral bidders; independent private values uniform on [0,1]; symmetric equilibrium.

**Hints.**
1. Unlike a second-price auction, your own bid sets the payment.
2. The equilibrium bid is a constant fraction of v.
3. As n grows, competition makes that fraction approach 1.

**Answer.** b(v) = ((n−1)/n)·v.

**Explanation.** A bidder shades below value because winning requires paying one’s own bid. With n−1 rivals and uniform values, the symmetric equilibrium bid is the expected highest rival value conditional on it being below v: (n−1)v/n.

**Practical takeaway.** The optimal amount of strategic shading depends on competition and the value distribution; ‘always bid your value’ is mechanism-specific.

**Evidence type.** Theorem / derivation  
**Sources.** [Nobel Prize](https://www.nobelprize.org/prizes/economic-sciences/2020/popular-information/)  
**Audit status.** New

---

### STR-06 · Hard · 3 points

**Question.** An oil lease has roughly the same unknown value to every bidder. Each bidder gets an unbiased but noisy estimate. Conditional on learning that your estimate was the highest, should you revise the estimate upward or downward? Name the phenomenon.

**Assumptions.** Common-value environment with noisy private signals; symmetric bidders; winning means submitting the highest estimate/bid.

**Hints.**
1. Winning is not merely good news; it tells you something about your signal’s rank.
2. Ask why your estimate beat every competing estimate.
3. The correction goes against the selection that made you win.

**Answer.** Downward. The phenomenon is the winner’s curse.

**Explanation.** Winning is evidence that your signal was unusually optimistic relative to others. A rational common-value bid conditions on the information contained in winning.

**Practical takeaway.** Whenever selection favors the most optimistic estimate—auctions, hiring, acquisitions, forecasts—condition on the selection process.

**Evidence type.** Auction-theory result  
**Sources.** [Nobel Prize](https://www.nobelprize.org/prizes/economic-sciences/2020/popular-information/)  
**Audit status.** Retained; common-value conditions clarified

---

### STR-07 · Hard · 3 points

**Question.** In the classical secretary problem, candidates arrive in uniformly random order, rejected candidates cannot be recalled, and success means choosing the single best candidate. Approximately what fraction should you reject before accepting the next record-breaker? What is the limiting success probability?

**Assumptions.** Known n, random order, no recall, only relative ranks observed, objective is the unique best.

**Hints.**
1. The threshold is a famous mathematical constant, not one-half.
2. The same constant appears in both the observation fraction and success probability.
3. It is approximately 0.367879.

**Answer.** Reject about 1/e ≈ 36.8%; the limiting success probability is also 1/e ≈ 36.8%.

**Explanation.** The optimal asymptotic rule uses the first 1/e of the sequence to set a benchmark, then accepts the next candidate better than all previously seen.

**Practical takeaway.** Optimal stopping rules are powerful, but only when their assumptions match reality; recall, uncertain pool size, and utility for near-best candidates change the answer.

**Evidence type.** Theorem  
**Sources.** [Statistical Science](https://projecteuclid.org/journals/statistical-science/volume-4/issue-3/Who-Solved-the-Secretary-Problem/10.1214/ss/1177012493.full)  
**Audit status.** Retained; caveat strengthened

---

### STR-08 · Very Hard · 5 points

**Question.** Two negotiators can split 100 units. If bargaining fails, each receives 10. Under the symmetric Nash bargaining solution, how is the surplus allocated?

**Assumptions.** Feasible frontier x+y=100; symmetric bargaining weights; disagreement point (10,10).

**Hints.**
1. Do not split the total from zero; account for disagreement payoffs first.
2. Maximize the product of each side’s gain above 10.
3. Symmetry applies to the 80-unit cooperative surplus.

**Answer.** Each receives 50 total—10 from the disagreement baseline plus 40 of the cooperative surplus.

**Explanation.** The solution maximizes the product of gains over disagreement: (x−10)(90−x), where the other party gets 100−x. The maximum occurs at x=50, splitting the 80-unit surplus equally.

**Practical takeaway.** A credible outside option changes bargaining power because the relevant object is surplus above disagreement, not the headline pie.

**Evidence type.** Axiomatic solution / calculation  
**Sources.** [Econometrica](https://www.cs.princeton.edu/courses/archive/fall13/cos597E/papers/nash50.pdf)  
**Audit status.** New

---

### STR-09 · Very Hard · 5 points

**Question.** Three voters rank A>B>C, B>C>A, and C>A>B. Under pairwise majority rule, who wins A versus B, B versus C, and C versus A? What is the pattern called?

**Hints.**
1. Count each pair separately.
2. Two voters prefer A to B; two prefer B to C.
3. The remaining comparison closes a cycle rather than producing a champion.

**Answer.** A beats B; B beats C; C beats A. This is a Condorcet cycle.

**Explanation.** Each pair has a 2–1 majority, yet the collective relation cycles. Individual transitivity does not guarantee transitive majority preferences.

**Practical takeaway.** Group preference can depend on agenda order even when every person’s ranking is internally consistent.

**Evidence type.** Social-choice derivation  
**Sources.** [Nobel Prize](https://www.nobelprize.org/prizes/economic-sciences/1972/arrow/facts/)  
**Audit status.** Retained

---

### STR-10 · Very Hard · 5 points

**Question.** With at least three alternatives, can a rank-order voting rule always produce a complete, transitive social ranking while satisfying unrestricted preferences, Pareto unanimity, independence of irrelevant alternatives, and non-dictatorship?

**Assumptions.** At least three alternatives; ordinal individual rankings; the listed Arrow axioms.

**Hints.**
1. The result concerns simultaneously satisfying a package of axioms.
2. At least one attractive property must be relaxed.
3. The theorem is named for Kenneth Arrow.

**Answer.** No. Arrow’s impossibility theorem proves that no such rule exists.

**Explanation.** Under Arrow’s conditions, every aggregation rule must sacrifice at least one desirable property. This is not a claim that voting is futile; it identifies unavoidable tradeoffs in rule design.

**Practical takeaway.** Institutional design is tradeoff management: no voting rule can be judged without specifying which failures are acceptable.

**Evidence type.** Theorem  
**Sources.** [Nobel Prize](https://www.nobelprize.org/prizes/economic-sciences/1972/arrow/facts/)  
**Audit status.** Retained; interpretation narrowed

---

## ◇ Judgment & Decision-Making

Bayes, biases, value of information, framing, and choice under uncertainty.

### DEC-01 · Challenging · 2 points

**Question.** A disease affects 1% of a population. A test has 90% sensitivity and 95% specificity. A randomly selected person tests positive. What is the probability the person has the disease?

**Assumptions.** Random sampling from the stated population; sensitivity and specificity apply to this population.

**Hints.**
1. Imagine 10,000 people rather than percentages.
2. About 90 diseased people and 495 healthy people test positive.
3. Divide true positives by all positives: 90/(90+495).

**Answer.** About 15.38%.

**Explanation.** Bayes’ rule gives 0.90×0.01 / [0.90×0.01 + 0.05×0.99] = 0.009/0.0585 ≈ 0.1538.

**Practical takeaway.** Base rates can dominate apparently impressive test characteristics; always ask how common the target condition was before the evidence arrived.

**Evidence type.** Bayesian derivation  
**Sources.** [Science / PubMed](https://pubmed.ncbi.nlm.nih.gov/17835457/)  
**Audit status.** Retained

---

### DEC-02 · Challenging · 2 points

**Question.** In the standard Monty Hall problem, you choose one of three doors. The host knows where the prize is, always opens a different losing door, and always offers a switch. What is your probability of winning if you switch?

**Assumptions.** The host always follows the stated protocol and never opens the prize door.

**Hints.**
1. Your first choice does not become more likely merely because a door opens.
2. Switching wins exactly when the initial choice was wrong.
3. The initial choice is wrong two-thirds of the time.

**Answer.** 2/3.

**Explanation.** Your initial choice is correct with probability 1/3 and wrong with probability 2/3. Whenever it is wrong, the host’s constrained reveal leaves the prize behind the only other closed door.

**Practical takeaway.** Information depends on the process that generated it; a reveal made under constraints is not equivalent to a random reveal.

**Evidence type.** Probability derivation  
**Sources.** Direct derivation from the assumptions stated on the card  
**Audit status.** New

---

### DEC-03 · Challenging · 2 points

**Question.** Which probability must be at least as large: P(A) or P(A and B)?

**Hints.**
1. Think of sets: one event is contained inside the other.
2. Adding a condition cannot create more qualifying cases.
3. ‘Bank teller and activist’ is a subset of ‘bank teller’.

**Answer.** P(A) must be at least as large: P(A) ≥ P(A∩B).

**Explanation.** Every outcome in A∩B is already contained in A, so adding the extra requirement B cannot increase probability. Violating this is the conjunction fallacy.

**Practical takeaway.** A vivid, coherent story can feel more probable while being mathematically less probable.

**Evidence type.** Probability axiom  
**Sources.** Direct derivation from the assumptions stated on the card  
**Audit status.** New

---

### DEC-04 · Hard · 3 points

**Question.** A company has irreversibly spent $1 million on a project. Completion now costs $200,000 and produces a certain $300,000 payoff, with no other relevant effects or opportunity costs. Should it complete the project?

**Assumptions.** The $1 million is truly unrecoverable; payoff and completion cost are certain; no omitted strategic effects.

**Hints.**
1. Compare only consequences that differ between ‘complete’ and ‘stop’. 
2. The past expenditure cannot be recovered under either option.
3. The forward-looking net value is positive.

**Answer.** Yes. Completion adds a net $100,000 from this point forward.

**Explanation.** The sunk $1 million is identical under both current choices. The incremental decision is $300,000 − $200,000 = +$100,000.

**Practical takeaway.** Past sacrifice is not a reason to continue—or stop. Decide using future marginal costs and benefits.

**Evidence type.** Economic derivation  
**Sources.** Direct derivation from the assumptions stated on the card  
**Audit status.** Retained

---

### DEC-05 · Hard · 3 points

**Question.** You prefer $100 today to $110 next week, but prefer $110 in 53 weeks to $100 in 52 weeks. What class of time-discounting model can generate this preference reversal?

**Hints.**
1. A stationary exponential discounter would rank the one-week tradeoff consistently at both dates.
2. The reversal is driven by an extra premium on ‘now’. 
3. The model’s name refers to a non-exponential discount curve.

**Answer.** Hyperbolic or quasi-hyperbolic discounting.

**Explanation.** Present-biased discounting gives immediacy disproportionate weight. As both outcomes move into the future, the extra week matters less than when one option is available now.

**Practical takeaway.** Commitment devices can be rational responses to predictable conflict between present and future selves.

**Evidence type.** Behavioral model  
**Sources.** [Harvard DASH](https://dash.harvard.edu/handle/1/4481499)  
**Audit status.** Retained

---

### DEC-06 · Hard · 3 points

**Question.** An urn contains 30 red balls and 60 balls that are black or yellow in an unknown mix. Many people prefer betting on red over black, yet prefer betting on black-or-yellow over red-or-yellow. What preference pattern does this reveal?

**Assumptions.** Standard Ellsberg two-urn-style preferences and equal payoffs for winning colors.

**Hints.**
1. Distinguish risk with known probabilities from uncertainty about probabilities.
2. The choices cannot both be explained by a single additive subjective probability over colors.
3. The paradox is named after Daniel Ellsberg.

**Answer.** Ambiguity aversion, as illustrated by the Ellsberg paradox.

**Explanation.** The known red probability is 1/3; black’s probability is unknown. The paired choices favor known probabilities in a way that violates Savage’s sure-thing principle.

**Practical takeaway.** People often pay to avoid poorly specified uncertainty; contracts and forecasts should separate measurable risk from model ambiguity.

**Evidence type.** Experimental regularity / paradox  
**Sources.** [Quarterly Journal of Economics](https://academic.oup.com/qje/article-abstract/75/4/643/1905197)  
**Audit status.** New

---

### DEC-07 · Hard · 3 points

**Question.** Two states, High and Low, are equally likely. Action A pays 100 in High and 0 in Low; Action B pays 60 in either state. What is the expected value of perfect information before choosing?

**Assumptions.** Risk-neutral objective; information is perfectly accurate and arrives before an irreversible choice.

**Hints.**
1. First compute the best expected payoff without information.
2. Then choose the best action separately within each state.
3. Subtract 60 from the informed expected payoff of 80.

**Answer.** $20.

**Explanation.** Without information, choose B for expected value 60 rather than A’s 50. With perfect information, choose A in High and B in Low, yielding (100+60)/2=80. EVPI=80−60=20.

**Practical takeaway.** The value of information is the improvement in decisions it enables, not the amount of data collected.

**Evidence type.** Decision-theory derivation  
**Sources.** Direct derivation from the assumptions stated on the card  
**Audit status.** New

---

### DEC-08 · Very Hard · 5 points

**Question.** People first spin a visibly arbitrary wheel, then estimate the percentage of African countries in the United Nations. Their estimates move toward the wheel’s number. What effect is this?

**Hints.**
1. The wheel contains no valid information about the target quantity.
2. The bias concerns dependence on an initial reference value.
3. The term begins with ‘anchor’.

**Answer.** The anchoring effect, specifically insufficient adjustment from an arbitrary anchor.

**Explanation.** Even an irrelevant starting value can shift subsequent numerical judgments. The classic result does not imply every anchor always works or that adjustment is the only mechanism.

**Practical takeaway.** In negotiation and forecasting, whoever supplies the first plausible number may reshape the comparison scale.

**Evidence type.** Experimental finding  
**Sources.** [Science / PubMed](https://pubmed.ncbi.nlm.nih.gov/17835457/)  
**Audit status.** New

---

### DEC-09 · Very Hard · 5 points

**Question.** In a 600-person epidemic, Program A is described as saving 200 people. Program B gives a 1/3 chance that all 600 are saved and a 2/3 chance that none are saved. What are their expected lives saved, and what classic bias is shown when preferences reverse under equivalent loss wording?

**Assumptions.** The programs have exactly the stated outcome distributions; the alternative wording is mathematically equivalent.

**Hints.**
1. Compute the expected value of the probabilistic option.
2. The two descriptions can encode the same outcome distribution.
3. The bias is named for how a choice is presented.

**Answer.** Both have an expected value of 200 lives; preference reversal is a framing effect.

**Explanation.** Program B’s expectation is (1/3)×600=200. Describing equivalent outcomes as gains versus losses often changes risk preference, contrary to description invariance.

**Practical takeaway.** Demand absolute outcome tables, not merely persuasive gain/loss wording, before comparing policies.

**Evidence type.** Experimental finding / calculation  
**Sources.** [Econometrica](https://www.princeton.edu/~kahneman/docs/Publications/prospect_theory.pdf)  
**Audit status.** New

---

### DEC-10 · Very Hard · 5 points

**Question.** In prospect theory, what three features characterize the value function around its reference point?

**Hints.**
1. Outcomes are evaluated as changes, not only final wealth.
2. Curvature differs on opposite sides of zero.
3. A loss of x typically has greater magnitude than an equal gain of x.

**Answer.** It is reference-dependent, generally concave for gains, convex for losses, and steeper for losses than for gains.

**Explanation.** The shape captures diminishing sensitivity away from the reference point and loss aversion near it. It describes observed choice patterns, not a universal law for every person and context.

**Practical takeaway.** Manage reference points and downside framing carefully: psychologically equal-dollar gains and losses are not usually equal-impact.

**Evidence type.** Behavioral model  
**Sources.** [Econometrica](https://www.princeton.edu/~kahneman/docs/Publications/prospect_theory.pdf)  
**Audit status.** New

---

## ⌁ Learning & Memory

How durable knowledge is encoded, retrieved, distorted, and strengthened.

### LRN-01 · Challenging · 2 points

**Question.** Patient H.M. improved at mirror tracing across sessions yet reported no memory of doing the task before. What major distinction did this establish?

**Hints.**
1. Separate knowing how from remembering that an episode occurred.
2. Performance improved even though conscious recollection did not.
3. The preserved system is often called procedural memory.

**Answer.** Procedural/nondeclarative learning can be preserved despite profound impairment of new declarative memory.

**Explanation.** H.M. acquired a motor skill without conscious episodic recollection of practice, demonstrating that memory is not a single unitary faculty.

**Practical takeaway.** A feeling of familiarity is not required for learning, and conscious understanding does not guarantee procedural skill.

**Evidence type.** Neuropsychological case evidence  
**Sources.** [Journal of Neuroscience / PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2807224/)  
**Audit status.** Retained

---

### LRN-02 · Challenging · 2 points

**Question.** Under conditions intended to prevent rehearsal and strategic chunking, approximately how many chunks did Nelson Cowan propose as the central capacity of working memory?

**Assumptions.** Controlled laboratory tasks limiting rehearsal and chunking; adult central capacity.

**Hints.**
1. The answer is smaller than seven.
2. It is a single-digit number close to the number of suits in a deck.
3. The paper’s title calls it a ‘magical number’.

**Answer.** About four chunks—often summarized as roughly three to five.

**Explanation.** Cowan’s estimate is lower than the famous ‘seven plus or minus two’ when rehearsal and grouping are controlled. It is an approximate central tendency, not a universal hard ceiling.

**Practical takeaway.** Externalize complex tasks, reduce simultaneous dependencies, and teach chunk structures rather than overloading active memory.

**Evidence type.** Review / empirical estimate  
**Sources.** [Behavioral and Brain Sciences / PubMed](https://pubmed.ncbi.nlm.nih.gov/11515286/)  
**Audit status.** Retained; universality caveat added

---

### LRN-03 · Challenging · 2 points

**Question.** After initial study, which usually produces better delayed retention: repeatedly rereading material or repeatedly retrieving it from memory with feedback?

**Assumptions.** Comparable study time; delayed test; feedback or sufficiently successful retrieval; appropriate materials.

**Hints.**
1. The better method feels harder during practice.
2. It requires producing an answer before looking.
3. It is also called the testing effect.

**Answer.** Repeated retrieval practice, under the usual testing-effect conditions.

**Explanation.** Attempting recall strengthens later accessibility more than equivalent additional exposure, especially when retrieval is effortful but successful and feedback corrects errors.

**Practical takeaway.** Replace passive review with low-stakes recall: practice the act you will need at performance time.

**Evidence type.** Replicated experimental finding  
**Sources.** [Science / PubMed](https://pubmed.ncbi.nlm.nih.gov/18276894/)  
**Audit status.** New

---

### LRN-04 · Hard · 3 points

**Question.** For the same total study time, which generally improves long-term retention more: massing repetitions together or distributing them across time?

**Assumptions.** Same or comparable total exposure; goal is delayed retention; spacing intervals are not so long that every retrieval fails.

**Hints.**
1. Cramming can improve immediate fluency without maximizing delayed recall.
2. The key variable is the interval between encounters.
3. The effect is named after spacing.

**Answer.** Distributed, spaced practice.

**Explanation.** A large literature finds that spacing repetitions improves retention relative to massing. The optimal gap is not fixed; it tends to increase with the desired retention interval.

**Practical takeaway.** Schedule review according to when knowledge must survive, not according to what feels smooth today.

**Evidence type.** Meta-analytic finding  
**Sources.** [Psychological Bulletin / PubMed](https://pubmed.ncbi.nlm.nih.gov/16719566/)  
**Audit status.** New

---

### LRN-05 · Hard · 3 points

**Question.** Students practice four kinds of problems. One group blocks each type; another mixes the types while holding spacing roughly constant. Which group often performs worse during practice but better on a delayed test requiring method selection?

**Assumptions.** Related categories benefit from comparison; test requires choosing the right procedure; spacing is controlled or acknowledged.

**Hints.**
1. Immediate practice fluency can point in the wrong direction.
2. The learner must identify which procedure applies before executing it.
3. The better delayed schedule mixes related problem types.

**Answer.** The interleaved-practice group.

**Explanation.** Interleaving forces learners to discriminate among problem types and select a strategy, while blocked practice gives away the method by repetition. Benefits depend on the task and what is interleaved.

**Practical takeaway.** Practice should train diagnosis and selection, not only execution after the method has been announced.

**Evidence type.** Experimental finding  
**Sources.** [Applied Cognitive Psychology](https://digitalcommons.usf.edu/psy_facpub/1760/)  
**Audit status.** New

---

### LRN-06 · Hard · 3 points

**Question.** People either read the paired word ‘rapid–fast’ or generate ‘fast’ from ‘rapid–f___’. Which condition usually produces better later memory for the target? What is the effect called?

**Hints.**
1. The stronger condition requires completing information rather than receiving it.
2. Active production is the critical manipulation.
3. The effect’s name is almost a direct description of that manipulation.

**Answer.** Generating the target usually produces better memory—the generation effect.

**Explanation.** Self-production recruits additional item-specific and relational processing compared with merely reading the completed target.

**Practical takeaway.** Answers you reconstruct are often more durable than answers you merely recognize.

**Evidence type.** Experimental finding  
**Sources.** [Journal of Verbal Learning and Verbal Behavior](https://doi.org/10.1016/S0022-5371(78)80009-7)  
**Audit status.** New

---

### LRN-07 · Hard · 3 points

**Question.** A word is encoded with a particular cue. At test, which cue is generally most effective: the cue with the strongest generic association to the word, or the cue that was present during encoding?

**Hints.**
1. Think match, not absolute cue strength.
2. A cue can be weak in general but diagnostic of this learning episode.
3. The principle joins encoding conditions to retrieval conditions.

**Answer.** The cue present during encoding can be more effective, even if it is a weaker generic associate. This is encoding specificity.

**Explanation.** Retrieval depends on overlap between information available at encoding and at test. Cue effectiveness is relational, not simply an intrinsic property of a cue.

**Practical takeaway.** Study with the kinds of cues, contexts, and prompts you will actually have when you must use the knowledge.

**Evidence type.** Experimental principle  
**Sources.** [Psychological Review](https://doi.org/10.1037/h0020071)  
**Audit status.** New

---

### LRN-08 · Very Hard · 5 points

**Question.** A consolidated fear memory is reactivated, becomes temporarily labile under suitable conditions, and then is stored again. What is this restabilization process called?

**Assumptions.** The retrieval episode actually destabilizes the memory; reconsolidation boundary conditions are met.

**Hints.**
1. The memory was already consolidated once.
2. Reactivation can require a second stabilization process.
3. Add the prefix ‘re-’ to the original storage process.

**Answer.** Reconsolidation.

**Explanation.** Some retrieved memories require protein-dependent restabilization and can be modified during a limited window. Retrieval alone does not guarantee destabilization; boundary conditions matter.

**Practical takeaway.** Recall can update memory, but ‘every recollection rewrites everything’ is an overstatement; modification depends on mismatch, timing, and memory conditions.

**Evidence type.** Experimental neuroscience finding  
**Sources.** [Nature / PubMed](https://pubmed.ncbi.nlm.nih.gov/10963596/)  
**Audit status.** Retained; boundary conditions added

---

### LRN-09 · Very Hard · 5 points

**Question.** Witnesses asked how fast cars were moving when they ‘smashed’ rather than ‘hit’ later gave higher estimates and more often reported nonexistent broken glass. What phenomenon does this illustrate?

**Hints.**
1. The misleading information arrives after the witnessed event.
2. The later question changes reported recollection.
3. The effect’s name contains ‘misinformation’.

**Answer.** The misinformation effect and reconstructive memory.

**Explanation.** Post-event wording can alter later reports and sometimes the remembered representation. The study demonstrates susceptibility, not that every memory is equally unreliable.

**Practical takeaway.** Separate contemporaneous notes from later discussion; repeated retelling can contaminate evidence.

**Evidence type.** Experimental finding  
**Sources.** [Journal of Verbal Learning and Verbal Behavior](https://doi.org/10.1016/S0022-5371(74)80011-3)  
**Audit status.** Retained; claim narrowed

---

### LRN-10 · Very Hard · 5 points

**Question.** In immediate free recall, people often remember the first and last list items best. A 30-second filled delay before recall disproportionately removes which component?

**Assumptions.** Classic immediate free-recall design with an interpolated distractor task before recall.

**Hints.**
1. The affected items are those still most available at the end of presentation.
2. The beginning and end peaks have different sensitivities to an interpolated task.
3. The answer is the final-position advantage.

**Answer.** The recency effect; the primacy effect is much less affected.

**Explanation.** A distractor-filled delay displaces or makes less accessible the most recent items, flattening the end of the serial-position curve while leaving the beginning advantage comparatively intact.

**Practical takeaway.** What is currently accessible can masquerade as what was learned durably; test after delay and interference.

**Evidence type.** Experimental finding  
**Sources.** [Journal of Verbal Learning and Verbal Behavior](https://doi.org/10.1016/S0022-5371(66)80044-0)  
**Audit status.** New

---

## ◉ Brain, Attention & Perception

What awareness, attention, prediction, and sensory measurement actually do.

### BRN-01 · Challenging · 2 points

**Question.** In the classic temporal-difference account, a dopamine burst shifts from an unexpected reward to a cue that predicts it; omission of the expected reward produces a dip. What quantity is the phasic signal approximating?

**Assumptions.** The classic reward-learning interpretation of phasic midbrain dopamine; not a claim about every dopamine neuron or function.

**Hints.**
1. It is not simply the amount of pleasure received.
2. The sign depends on surprise relative to expectation.
3. Actual outcome minus predicted outcome is the core intuition.

**Answer.** A signed reward-prediction error: received reward plus updated future value minus prior expected value.

**Explanation.** The signal is positive for better-than-predicted outcomes, near zero for fully predicted outcomes, and negative for worse-than-predicted outcomes.

**Practical takeaway.** Motivation and learning respond strongly to violated expectations; managing predictions can matter as much as managing outcomes.

**Evidence type.** Neuroscience model supported by experiments  
**Sources.** [Science](https://www.science.org/doi/10.1126/science.275.5306.1593)  
**Audit status.** Retained; scope restricted

---

### BRN-02 · Challenging · 2 points

**Question.** A large feature of a scene changes across two images separated by a brief blank, yet an observer repeatedly fails to notice. What is this called?

**Hints.**
1. The observer can see both versions clearly.
2. The failure concerns detecting a difference across views.
3. Its name combines ‘change’ with a visual-awareness failure.

**Answer.** Change blindness.

**Explanation.** The blank masks the visual transient that would normally capture attention. Detailed visual access does not imply a complete, continuously compared internal picture.

**Practical takeaway.** Critical changes in interfaces, documents, and environments need explicit attention cues; visibility alone is insufficient.

**Evidence type.** Experimental finding  
**Sources.** [Psychological Science](https://doi.org/10.1111/j.1467-9280.1997.tb00427.x)  
**Audit status.** Retained

---

### BRN-03 · Challenging · 2 points

**Question.** A person carefully counts basketball passes and fails to notice a highly visible unexpected figure crossing the scene. What is this called?

**Hints.**
1. The stimulus is visible but unexpected.
2. Attention is occupied by another task.
3. The effect’s name joins inattention with blindness.

**Answer.** Inattentional blindness.

**Explanation.** A demanding focal task can prevent conscious awareness of an unexpected but visible stimulus. This differs from ordinary acuity failure.

**Practical takeaway.** Checking harder is not the same as checking broadly; assign separate attention to rare, high-cost anomalies.

**Evidence type.** Experimental finding  
**Sources.** [Perception / PubMed](https://pubmed.ncbi.nlm.nih.gov/10694957/)  
**Audit status.** Retained

---

### BRN-04 · Hard · 3 points

**Question.** A person’s just-noticeable weight difference is 2 g near 100 g. Assuming a constant Weber fraction in this range, what should the just-noticeable difference be near 500 g?

**Assumptions.** Weber’s law is approximately valid over the specified stimulus range.

**Hints.**
1. Use a relative rather than absolute threshold.
2. First compute 2/100.
3. Apply the same 2% fraction to 500 g.

**Answer.** 10 g.

**Explanation.** The Weber fraction is ΔI/I=2/100=0.02. Therefore ΔI=0.02×500=10 g.

**Practical takeaway.** Human sensitivity often tracks proportional change, which is why percentage differences can matter more than equal absolute differences.

**Evidence type.** Psychophysical law / calculation  
**Sources.** [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7038823/)  
**Audit status.** Retained; approximation caveat retained

---

### BRN-05 · Hard · 3 points

**Question.** Two radiologists have the same ability to discriminate tumors from normal images, but one calls far more scans positive. In signal-detection theory, which parameter differs if sensitivity is truly equal?

**Assumptions.** Standard equal-variance signal-detection framing; underlying sensitivity is equal by stipulation.

**Hints.**
1. Accuracy alone mixes perceptual ability with willingness to say yes.
2. One parameter measures separation of signal and noise; another sets the cutoff.
3. The differing parameter is the criterion.

**Answer.** Their decision criterion (response bias), not d′ sensitivity.

**Explanation.** Signal-detection theory separates discriminability, commonly measured by d′, from the threshold used to say ‘signal present.’ Moving the criterion trades false alarms against misses.

**Practical takeaway.** When errors have asymmetric costs, choose a threshold deliberately rather than treating every false alarm as evidence of poor perception.

**Evidence type.** Formal measurement model  
**Sources.** [Behavior Research Methods](https://doi.org/10.3758/BF03207704)  
**Audit status.** New

---

### BRN-06 · Hard · 3 points

**Question.** A person with damage to primary visual cortex reports no conscious vision in part of the field but can guess stimulus location or orientation above chance. What syndrome is this?

**Hints.**
1. The patient denies seeing the stimulus.
2. Forced-choice performance is nevertheless above chance.
3. The name suggests vision without sight.

**Answer.** Blindsight.

**Explanation.** Residual visual pathways can support discrimination without ordinary acknowledged visual awareness, demonstrating a dissociation between performance and conscious seeing.

**Practical takeaway.** Conscious confidence is not a perfect readout of information available to the nervous system.

**Evidence type.** Neuropsychological finding  
**Sources.** [Current Opinion in Neurobiology / PubMed](https://pubmed.ncbi.nlm.nih.gov/8725963/)  
**Audit status.** New

---

### BRN-07 · Hard · 3 points

**Question.** In a classic split-brain patient with left-hemisphere speech dominance, an object is flashed only to the left visual field. Can the person typically name it aloud, and which hand can often select the matching object?

**Assumptions.** Classic complete callosotomy case with typical left-hemisphere language dominance; individual variation exists.

**Hints.**
1. Visual fields project contralaterally.
2. The right hemisphere controls the left hand.
3. Speech is usually left-lateralized in these classic cases.

**Answer.** They typically cannot name it aloud, but the left hand can often select it.

**Explanation.** The left visual field projects initially to the right hemisphere, which controls the left hand. With the corpus callosum severed, the information cannot reach the usual left-hemisphere speech system.

**Practical takeaway.** A unified verbal report is not identical to all processing occurring in the brain; access pathways determine what can be reported.

**Evidence type.** Neuropsychological finding  
**Sources.** [Nobel Prize](https://www.nobelprize.org/prizes/medicine/1981/sperry/lecture/)  
**Audit status.** New

---

### BRN-08 · Very Hard · 5 points

**Question.** Which opioid antagonist reduced placebo analgesia in the classic postoperative-pain experiment, implicating endogenous opioid mechanisms?

**Hints.**
1. It is used clinically to reverse opioid effects.
2. The drug blocks opioid receptors rather than stimulating them.
3. Its name begins with ‘nal-’.

**Answer.** Naloxone.

**Explanation.** Patients receiving naloxone reported more pain than those receiving placebo after placebo analgesia had been induced, supporting an opioid-mediated component in that setting.

**Practical takeaway.** Expectation can recruit real physiological pathways, but placebo effects are mechanism- and context-specific, not evidence that every condition is ‘all in the mind.’

**Evidence type.** Clinical experiment  
**Sources.** [Lancet / PubMed](https://pubmed.ncbi.nlm.nih.gov/80579/)  
**Audit status.** Retained; scope caveat added

---

### BRN-09 · Very Hard · 5 points

**Question.** After repeated safe exposure to a conditioned fear cue, does standard extinction learning usually erase the original fear association, or create new inhibitory learning that competes with it?

**Assumptions.** Standard Pavlovian extinction; some interventions may alter or update original memories under special conditions.

**Hints.**
1. Ask why fear can return outside the extinction context.
2. The old association may remain while a new ‘cue means safety’ relation is learned.
3. The answer is competition, not simple erasure.

**Answer.** It usually creates new inhibitory/safety learning that competes with the original association.

**Explanation.** Extinguished fear can return through renewal, spontaneous recovery, or reinstatement, which is difficult to explain if the original trace were simply deleted.

**Practical takeaway.** Relapse after successful exposure does not prove nothing was learned; safety learning often needs retrieval across contexts.

**Evidence type.** Learning-theory finding  
**Sources.** [NIH / PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4214179/)  
**Audit status.** New

---

### BRN-10 · Very Hard · 5 points

**Question.** What paired structure in the anterior hypothalamus is the principal circadian pacemaker in mammals, and what environmental cue is its dominant synchronizer?

**Hints.**
1. The structure sits above the optic chiasm.
2. Its abbreviation is three letters.
3. The dominant cue reaches it through a retinal pathway.

**Answer.** The suprachiasmatic nucleus (SCN); the light–dark cycle is the dominant zeitgeber.

**Explanation.** Retinal input entrains SCN cellular clocks, which coordinate rhythms across physiology and behavior. Other time cues matter, but light is primary for human circadian phase.

**Practical takeaway.** Timing light exposure is a direct way to shift sleep and alertness; willpower cannot fully override circadian phase.

**Evidence type.** Neuroscience consensus  
**Sources.** [PubMed](https://pubmed.ncbi.nlm.nih.gov/10548871/)  
**Audit status.** New

---

## ⌘ Social Dynamics & Networks

How local incentives and network structure create collective outcomes.

### SOC-01 · Challenging · 2 points

**Question.** Let K be the number of friends of a randomly selected person in an undirected network. What is the expected number of friends of a person reached by following a uniformly random friendship edge?

**Assumptions.** Undirected finite network; select an edge endpoint uniformly; degrees are positive for sampled endpoints.

**Hints.**
1. An individual with twice as many friends can be reached by twice as many edges.
2. The edge-sampled degree distribution is size-biased by K.
3. Use E[K²]/E[K].

**Answer.** E[K²]/E[K] = E[K] + Var(K)/E[K], which is at least E[K] and larger when degree varies.

**Explanation.** Following edges samples people in proportion to their degree, so highly connected people are overrepresented. This is the friendship paradox.

**Practical takeaway.** Local social samples systematically overrepresent popular, active, and highly connected people—distorting perceived norms and success rates.

**Evidence type.** Theorem  
**Sources.** [American Journal of Sociology](https://www.cs.umd.edu/~gasarch/Feld-FriendsFriends-1991.pdf)  
**Audit status.** Retained; sampling scheme specified

---

### SOC-02 · Challenging · 2 points

**Question.** Regions with higher immigrant shares have higher average literacy. Someone concludes that immigrants are more literate than non-immigrants. What inferential error may have occurred?

**Hints.**
1. The data unit is a region, but the conclusion is about individuals.
2. Between-group and within-group relationships are not interchangeable.
3. The error’s name refers to aggregate or ecological data.

**Answer.** The ecological fallacy.

**Explanation.** An association between group-level aggregates need not equal the within-group individual association and may even have the opposite sign.

**Practical takeaway.** Match the level of evidence to the level of the claim; aggregate dashboards cannot automatically answer individual questions.

**Evidence type.** Statistical inference principle  
**Sources.** [UC Berkeley](https://statistics.berkeley.edu/sites/default/files/tech-reports/549.pdf)  
**Audit status.** Retained

---

### SOC-03 · Challenging · 2 points

**Question.** Most members of a group privately reject a norm, but each mistakenly believes most others accept it, so everyone publicly complies. What is this called?

**Hints.**
1. The group is not privately unanimous.
2. Each person misreads others’ public compliance as genuine support.
3. The term combines plurality with ignorance.

**Answer.** Pluralistic ignorance.

**Explanation.** Private beliefs and perceived group beliefs diverge. Public conformity then supplies misleading evidence that perpetuates the false perception.

**Practical takeaway.** Anonymous polling and visible dissent can dissolve norms that survive mainly because everyone misestimates everyone else.

**Evidence type.** Social-psychological phenomenon  
**Sources.** [Stanford GSB](https://www.gsb.stanford.edu/faculty-research/publications/pluralistic-ignorance-perpetuation-social-norms-unwitting-actors)  
**Audit status.** Retained

---

### SOC-04 · Hard · 3 points

**Question.** In a Schelling segregation model, agents move only when fewer than one-third of nearby agents share their type. Can this relatively tolerant local rule still generate highly segregated neighborhoods?

**Assumptions.** Schelling-style spatial model and relocation dynamics; result is model-based, not a complete empirical causal account.

**Hints.**
1. Track the feedback from one person’s move to neighbors’ satisfaction.
2. Mild thresholds can cascade.
3. Micro-level tolerance does not guarantee integrated macro outcomes.

**Answer.** Yes.

**Explanation.** Small local preferences can interact through repeated moves to create a strongly segregated macro-pattern. The model demonstrates a mechanism, not proof that this mechanism explains every real city.

**Practical takeaway.** Judge systems by emergent outcomes as well as stated individual intentions; benign local rules can compound into harmful patterns.

**Evidence type.** Agent-based model result  
**Sources.** [Journal of Mathematical Sociology](https://doi.org/10.1080/0022250X.1971.9989794)  
**Audit status.** Retained; model-to-world boundary emphasized

---

### SOC-05 · Hard · 3 points

**Question.** In Granovetter’s network account, why can a weak acquaintance be more useful than a close friend for finding novel job information?

**Hints.**
1. Compare redundant information within a clique with information crossing between cliques.
2. Tie strength and structural position are different variables.
3. The key word is bridge.

**Answer.** Weak ties more often bridge otherwise separate social clusters and therefore carry nonredundant information.

**Explanation.** Close friends tend to know one another and share similar information. A bridge to a different cluster can expose a person to opportunities unavailable within the dense local circle.

**Practical takeaway.** Maintain some cross-boundary relationships; network diversity can matter more than adding another tie inside the same circle.

**Evidence type.** Network theory with empirical evidence  
**Sources.** [American Journal of Sociology / Stanford](https://www.cs.umd.edu/~golbeck/INST633o/granovetterTies.pdf)  
**Audit status.** New

---

### SOC-06 · Hard · 3 points

**Question.** A behavior is rare in the whole population but concentrated among highly connected people. Many individuals nonetheless see it among most of their neighbors. What network phenomenon is this?

**Hints.**
1. Local neighborhoods are not uniform samples of the population.
2. Highly connected nodes are seen disproportionately often.
3. The name describes a false local impression of prevalence.

**Answer.** The majority illusion.

**Explanation.** Because high-degree nodes appear in many neighborhoods, a globally rare state can be locally overrepresented, especially when degree correlates with the state.

**Practical takeaway.** Virality and apparent consensus may reflect who is visible, not how many people actually agree or behave that way.

**Evidence type.** Network-model result  
**Sources.** [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0147617)  
**Audit status.** New

---

### SOC-07 · Hard · 3 points

**Question.** People make sequential choices after observing earlier choices but not earlier private signals. After enough identical early choices, later people rationally ignore their own signals. What is this called?

**Assumptions.** Sequential Bayesian decision model with bounded private signals and observation of predecessors’ actions.

**Hints.**
1. The phenomenon is not necessarily irrational imitation.
2. Actions are public while underlying signals are hidden.
3. Once the sequence starts, information can cascade.

**Answer.** An informational cascade.

**Explanation.** Observed actions can summarize accumulated evidence strongly enough to swamp a later person’s private signal. Cascades can be correct or wrong and can be fragile because little new private information enters afterward.

**Practical takeaway.** Independent estimates should be collected before discussion when group members possess private evidence.

**Evidence type.** Game-theoretic model  
**Sources.** [Journal of Political Economy](https://doi.org/10.1086/261849)  
**Audit status.** New

---

### SOC-08 · Very Hard · 5 points

**Question.** When people pull a rope in a group and individual contributions are hard to identify, average effort per person falls as group size rises. What is this called?

**Hints.**
1. The total group output may rise while output per person falls.
2. Individual effort is pooled and less visible.
3. The term uses a word meaning idling.

**Answer.** Social loafing, historically related to the Ringelmann effect.

**Explanation.** Diffused identifiability and responsibility can reduce effort on pooled tasks, though coordination loss and task design also matter.

**Practical takeaway.** Make ownership and contributions legible; ‘the team will handle it’ is a weak accountability mechanism.

**Evidence type.** Experimental finding  
**Sources.** [Journal of Personality and Social Psychology](https://doi.org/10.1037/0022-3514.37.6.822)  
**Audit status.** New

---

### SOC-09 · Very Hard · 5 points

**Question.** In an ambiguous emergency, the presence of more passive bystanders can make each observer less likely to intervene partly because responsibility is spread across the group. What mechanism is this?

**Assumptions.** Ambiguous or shared-responsibility setting; many contextual moderators affect real helping behavior.

**Hints.**
1. Each person can imagine someone else taking action.
2. The relevant quantity is perceived personal responsibility.
3. The mechanism’s name says that responsibility is spread out.

**Answer.** Diffusion of responsibility, a mechanism in the bystander effect.

**Explanation.** Each observer feels less personally obligated when others could act. Ambiguity and pluralistic ignorance can compound the effect; it is not an iron law that crowds always reduce helping.

**Practical takeaway.** In emergencies, assign a named person a concrete action—‘You in the blue shirt, call emergency services’—rather than addressing the crowd.

**Evidence type.** Experimental finding  
**Sources.** [Journal of Personality and Social Psychology](https://doi.org/10.1037/h0025589)  
**Audit status.** New

---

### SOC-10 · Very Hard · 5 points

**Question.** A person connects two groups that otherwise have few ties between them. In Ronald Burt’s terminology, what network feature does the person span, and what advantage can it create?

**Hints.**
1. The advantage comes from separation between the groups, not simply having many contacts.
2. The person occupies a bridge or broker position.
3. Burt’s phrase refers to a ‘hole’ in social structure.

**Answer.** They span a structural hole, which can provide brokerage access to diverse information and coordination opportunities.

**Explanation.** Disconnected clusters contain less redundant information. The broker can translate, combine, or control flows between them, although brokerage also carries maintenance and trust costs.

**Practical takeaway.** Career leverage often comes from connecting domains that do not naturally communicate, then earning trust on both sides.

**Evidence type.** Network theory with empirical research  
**Sources.** [University of Chicago](https://press.uchicago.edu/ucp/books/book/chicago/S/bo3634314.html)  
**Audit status.** New

---

## ∴ Probability & Statistical Literacy

Base rates, uncertainty, sampling, testing, and counterintuitive waiting times.

### PRO-01 · Challenging · 2 points

**Question.** A correctly calculated p-value is 0.03. Does that mean there is a 3% probability the null hypothesis is true? What does it mean?

**Assumptions.** The test, stopping rule, and model assumptions are correctly specified.

**Hints.**
1. Distinguish P(data | hypothesis) from P(hypothesis | data).
2. The null is assumed during the calculation.
3. The probability describes hypothetical data, not the truth status of H₀.

**Answer.** No. It is the probability, assuming the null and the rest of the statistical model, of a result at least as incompatible with the null as the observed result.

**Explanation.** A p-value is P(data as or more extreme | model including H₀), not P(H₀ | data). Reversing those conditionals is a serious error.

**Practical takeaway.** Treat p-values as one diagnostic, not a posterior probability, effect size, replication probability, or decision rule by themselves.

**Evidence type.** Definition / statistical standard  
**Sources.** [American Statistical Association](https://www.tandfonline.com/doi/full/10.1080/00031305.2016.1154108)  
**Audit status.** Retained

---

### PRO-02 · Challenging · 2 points

**Question.** What is the correct frequentist interpretation of a 95% confidence interval?

**Assumptions.** Repeated sampling under the same model and interval construction.

**Hints.**
1. Imagine repeating the whole sampling procedure many times.
2. The intervals vary from sample to sample; the parameter is fixed.
3. Ninety-five percent is a property of the procedure.

**Answer.** Across repeated samples, 95% of intervals generated by the stated procedure would cover the fixed true parameter.

**Explanation.** Once a particular interval is computed, the parameter is not random in the frequentist model; the 95% refers to the long-run coverage of the procedure.

**Practical takeaway.** An interval’s interpretation depends on the procedure and assumptions that produced it; confidence is not automatic certainty about this one realized range.

**Evidence type.** Definition  
**Sources.** [NIST/SEMATECH e-Handbook](https://www.itl.nist.gov/div898/handbook/prc/section1/prc14.htm)  
**Audit status.** Retained

---

### PRO-03 · Challenging · 2 points

**Question.** You conduct 20 independent tests, every null is true, and each uses α=0.05. What is the probability of at least one nominally significant result?

**Assumptions.** Independent tests; all null hypotheses true; fixed α=0.05 for each.

**Hints.**
1. Calculate the complement first.
2. All 20 must avoid a false positive for there to be none.
3. Use 1−(1−0.05)^20.

**Answer.** 1−0.95²⁰ ≈ 64.15%.

**Explanation.** The probability of no false positives is 0.95²⁰. Taking the complement gives about 0.6415.

**Practical takeaway.** A single ‘significant’ result among many undisclosed opportunities can be ordinary noise.

**Evidence type.** Probability derivation  
**Sources.** Direct derivation from the assumptions stated on the card; [American Statistical Association](https://www.tandfonline.com/doi/full/10.1080/00031305.2016.1154108)  
**Audit status.** Retained

---

### PRO-04 · Hard · 3 points

**Question.** Ignoring leap days and assuming birthdays are equally distributed across 365 days, what is the probability that at least two people share a birthday in a group of 23?

**Assumptions.** Independent uniformly distributed birthdays; 365 possible days.

**Hints.**
1. Count pairs indirectly by calculating no collision.
2. Multiply the shrinking number of unused days for each new person.
3. The answer is just above one-half.

**Answer.** About 50.73%.

**Explanation.** The complement is that all birthdays differ: 365/365×364/365×…×343/365 ≈ 0.4927. Therefore a match has probability ≈0.5073.

**Practical takeaway.** Collision risk grows with the number of pairs, roughly quadratically, not merely with the number of people.

**Evidence type.** Probability derivation  
**Sources.** Direct derivation from the assumptions stated on the card  
**Audit status.** New

---

### PRO-05 · Hard · 3 points

**Question.** A fair coin is tossed until the first Heads. If Heads first occurs on toss n, you receive $2ⁿ. What is the expected monetary payoff?

**Assumptions.** Unbounded casino solvency and payoff; fair independent tosses; no entry or time constraints.

**Hints.**
1. Write the expectation as a sum over n.
2. Probability and payoff exactly cancel for each term.
3. The resulting series is 1+1+1+…

**Answer.** Infinite.

**Explanation.** P(N=n)=2⁻ⁿ, so each n contributes 2⁻ⁿ×2ⁿ=$1 to expectation. Summing $1 over all positive integers diverges.

**Practical takeaway.** Expected money alone can be a poor guide under unbounded payoffs, finite wealth, risk constraints, and diminishing utility.

**Evidence type.** Probability derivation  
**Sources.** Direct derivation from the assumptions stated on the card  
**Audit status.** Retained

---

### PRO-06 · Hard · 3 points

**Question.** Buses repeat alternating gaps of 5 and 15 minutes. You arrive at a uniformly random clock time over many cycles. What is the expected wait for the next bus?

**Assumptions.** Perfectly repeating gaps; arrival time uniform and independent of schedule.

**Hints.**
1. Long gaps occupy more of the clock and are sampled more often.
2. Weight each gap by its length, not equally.
3. The conditional residual waits are half of 5 and half of 15.

**Answer.** 6.25 minutes.

**Explanation.** You land in the 5-minute gap with probability 1/4 and wait 2.5 minutes on average, or in the 15-minute gap with probability 3/4 and wait 7.5. Thus ¼×2.5+¾×7.5=6.25.

**Practical takeaway.** Random-time samples are length-biased: you disproportionately encounter long meetings, delays, queues, and lifetimes.

**Evidence type.** Renewal-process derivation  
**Sources.** Direct derivation from the assumptions stated on the card  
**Audit status.** Retained

---

### PRO-07 · Hard · 3 points

**Question.** A cereal promotion has 100 equally likely coupon types, drawn independently with replacement. What is the expected number of boxes needed to collect all types?

**Assumptions.** Independent draws; exactly uniform coupon probabilities; replacement.

**Hints.**
1. Break the process into waiting times for the 1st, 2nd, …, 100th new type.
2. The last missing type alone takes 100 boxes on average.
3. Use the harmonic number H₁₀₀.

**Answer.** 100·H₁₀₀ ≈ 518.74 boxes.

**Explanation.** After k distinct types are collected, the chance the next box is new is (100−k)/100, so the expected wait for the next new type is 100/(100−k). Summing gives 100H₁₀₀.

**Practical takeaway.** Complete coverage is disproportionately expensive; the last few edge cases dominate testing, hiring, discovery, and inventory variety.

**Evidence type.** Probability theorem  
**Sources.** Direct derivation from the assumptions stated on the card  
**Audit status.** Retained

---

### PRO-08 · Very Hard · 5 points

**Question.** A forensic pattern occurs in only 1 in a million innocent people. A prosecutor says a matching defendant therefore has only a 1-in-a-million chance of being innocent. What error is this?

**Hints.**
1. Reverse the direction of the conditional probability.
2. You still need a prior probability of guilt and the alternative likelihood.
3. It is a named courtroom version of the inverse fallacy.

**Answer.** The prosecutor’s fallacy: confusing P(match | innocent) with P(innocent | match).

**Explanation.** Posterior innocence also depends on prior odds and the probability of a match if guilty. A rare random match rate is not by itself the probability of innocence after a match.

**Practical takeaway.** Whenever evidence is presented as ‘one in X,’ ask one in X of what conditional event—and compare both hypotheses.

**Evidence type.** Bayesian reasoning principle  
**Sources.** [American Statistical Association](https://www.tandfonline.com/doi/full/10.1080/00031305.2016.1154108)  
**Audit status.** New

---

### PRO-09 · Very Hard · 5 points

**Question.** Prior odds for a hypothesis are 1:9. New evidence has likelihood ratio 6 in favor of the hypothesis. What are the posterior odds and posterior probability?

**Hints.**
1. Do not multiply the prior probability directly by six.
2. Use odds form of Bayes’ theorem.
3. Convert 2:3 odds into 2 out of 5 total parts.

**Answer.** Posterior odds are 6:9 = 2:3; posterior probability is 2/(2+3)=40%.

**Explanation.** Bayes in odds form is posterior odds = prior odds × likelihood ratio. Multiplying 1/9 by 6 gives 2/3 odds, equivalent to probability 0.4.

**Practical takeaway.** Strong evidence need not make a hypothesis probable when the prior odds are sufficiently low.

**Evidence type.** Bayesian derivation  
**Sources.** Direct derivation from the assumptions stated on the card  
**Audit status.** New

---

### PRO-10 · Very Hard · 5 points

**Question.** A fair coin has landed Heads five times in a row. Assuming independent tosses and that the coin is known to be fair, what is P(Heads on the next toss), and what mistake predicts a compensating Tail?

**Assumptions.** The coin’s fairness is known, tosses are independent, and no hidden selection or mechanical change exists.

**Hints.**
1. The coin has no memory.
2. Distinguish long-run proportions from a force correcting the next observation.
3. The named fallacy is associated with gamblers.

**Answer.** P(Heads)=1/2. Predicting Tail because outcomes must ‘balance soon’ is the gambler’s fallacy.

**Explanation.** Independence means the conditional probability of the next toss is unchanged by the finite history. Long-run balance does not impose short-run correction.

**Practical takeaway.** Before inferring mean reversion, identify a real mechanism; randomness alone does not promise immediate compensation.

**Evidence type.** Probability axiom  
**Sources.** [Science / PubMed](https://pubmed.ncbi.nlm.nih.gov/17835457/)  
**Audit status.** New

---

## ↯ Causality & Scientific Reasoning

Confounding, selection, experiments, identification, and research integrity.

### CAU-01 · Challenging · 2 points

**Question.** Treatment A succeeds in 81/87 mild cases and 192/263 severe cases. Treatment B succeeds in 234/270 mild cases and 55/80 severe cases. Which treatment is better within each severity group, and which is better after pooling?

**Assumptions.** The table is descriptive; causal interpretation still requires assumptions about treatment assignment and confounding.

**Hints.**
1. Compute four within-stratum percentages before combining anything.
2. Then compare 273/350 with 289/350.
3. The reversal is driven by different severity mixes.

**Answer.** A is better in both groups; B is better after pooling. This is Simpson’s paradox.

**Explanation.** Mild: A≈93.1% vs B≈86.7%. Severe: A≈73.0% vs B=68.75%. Pooled: A=273/350=78.0%; B=289/350≈82.6%. B treated a much larger share of mild cases.

**Practical takeaway.** Aggregate rates can reverse causal-looking comparisons; stratify by variables that affected assignment and outcome.

**Evidence type.** Arithmetic paradox  
**Sources.** [NIH / PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8870532/)  
**Audit status.** Retained

---

### CAU-02 · Challenging · 2 points

**Question.** Talent and family connections are initially independent, and both raise the chance of elite admission. Among admitted students only, what association can appear between talent and connections, and why?

**Assumptions.** Talent and connections are independent before selection; both causally affect admission.

**Hints.**
1. Draw arrows Talent→Admission←Connections.
2. The selected variable is a common effect, not a common cause.
3. Conditioning on a collider opens a noncausal path.

**Answer.** A spurious negative association can appear because admission is a collider and conditioning on it induces selection bias.

**Explanation.** Within the selected group, having less of one cause often requires more of the other to cross the admission threshold.

**Practical takeaway.** Comparing only winners, employees, customers, survivors, or published papers can manufacture relationships absent in the source population.

**Evidence type.** Causal-DAG result  
**Sources.** [NIH / PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2846442/)  
**Audit status.** Retained

---

### CAU-03 · Challenging · 2 points

**Question.** A team is selected for coaching immediately after an unusually bad performance. Its next performance improves even if coaching has no effect. What statistical phenomenon can create this pattern?

**Hints.**
1. Selection happened because the first measurement was extreme.
2. Temporary noise is unlikely to repeat at the same magnitude.
3. The next value tends toward the population mean.

**Answer.** Regression to the mean.

**Explanation.** Extreme observations often combine a stable component with temporary noise. On remeasurement, the noise is unlikely to be equally extreme, so results tend to move toward the average.

**Practical takeaway.** Before crediting an intervention aimed at extreme cases, compare against an appropriate control or expected natural reversion.

**Evidence type.** Statistical phenomenon  
**Sources.** [Science / PubMed](https://pubmed.ncbi.nlm.nih.gov/17835457/)  
**Audit status.** New

---

### CAU-04 · Hard · 3 points

**Question.** What key property does random assignment create, in expectation, that allows a treatment–control outcome difference to estimate a causal effect?

**Assumptions.** Proper randomization, well-defined treatment, no problematic interference, and valid outcome measurement.

**Hints.**
1. Randomization does not guarantee identical groups in one finite sample.
2. Its key benefit concerns the assignment mechanism.
3. Treatment becomes independent of pre-treatment causes in expectation.

**Answer.** It makes treatment assignment independent of pre-treatment potential outcomes and confounders, balancing them in expectation.

**Explanation.** Randomization breaks systematic links between assignment and factors that would otherwise affect the outcome. Execution problems such as attrition, noncompliance, interference, or bad measurement can still compromise interpretation.

**Practical takeaway.** Causal credibility comes from how exposure was assigned, not from sophisticated analysis alone.

**Evidence type.** Experimental-design principle  
**Sources.** [PubMed](https://pubmed.ncbi.nlm.nih.gov/29085540/)  
**Audit status.** New

---

### CAU-05 · Hard · 3 points

**Question.** In a randomized trial with noncompliance, which primary analysis preserves the original randomization by comparing participants according to assigned group rather than treatment actually received?

**Assumptions.** Outcome follow-up is adequate; estimand is the effect of assignment/policy; missingness still needs handling.

**Hints.**
1. Do not move crossovers into the treatment they ultimately chose.
2. Keep participants in their randomized arms.
3. The analysis name begins ‘intention’.

**Answer.** Intention-to-treat (ITT) analysis.

**Explanation.** Analyzing by assignment preserves the baseline comparability generated by randomization and estimates the effect of assignment or treatment policy. It may differ from the effect of actually receiving treatment.

**Practical takeaway.** Changing groups after seeing behavior can reintroduce the selection bias randomization was meant to eliminate.

**Evidence type.** Clinical-trial standard  
**Sources.** [PubMed](https://pubmed.ncbi.nlm.nih.gov/29085540/)  
**Audit status.** New

---

### CAU-06 · Hard · 3 points

**Question.** What central identifying assumption lets a basic difference-in-differences design interpret the treated group’s change minus the control group’s change as causal?

**Assumptions.** No anticipation or spillovers and a suitable parallel-trends condition for the estimand and design.

**Hints.**
1. The assumption concerns an unobserved counterfactual trend.
2. Pre-treatment similarity of levels is not required.
3. The word ‘parallel’ is part of the answer.

**Answer.** Parallel trends: absent treatment, the groups’ average outcomes would have changed in parallel.

**Explanation.** Difference-in-differences subtracts baseline group differences, but it cannot remove differential time trends that would have occurred without treatment.

**Practical takeaway.** Before using before–after comparisons with a control group, defend why their untreated trajectories would have moved similarly.

**Evidence type.** Causal-identification assumption  
**Sources.** [NBER](https://www.nber.org/papers/w31184)  
**Audit status.** New

---

### CAU-07 · Hard · 3 points

**Question.** Name the three core conditions for a variable Z to serve as a valid instrument for treatment X’s causal effect on outcome Y; what extra condition is commonly used for a LATE interpretation?

**Assumptions.** Standard potential-outcomes IV framework; precise conditions depend on estimand and model.

**Hints.**
1. The first condition requires a first-stage effect.
2. The second and third block backdoor and direct paths to Y.
3. The LATE condition rules out people who always move opposite the instrument.

**Answer.** Relevance, independence/exogeneity, and exclusion restriction; monotonicity is additionally used for LATE.

**Explanation.** Z must affect X, be as-if independent of unmeasured causes of Y, and affect Y only through X. With heterogeneous effects, monotonicity rules out ‘defiers’ and identifies a local average treatment effect for compliers.

**Practical takeaway.** An instrument is credible because of a causal story, not because software can run two-stage least squares.

**Evidence type.** Causal-identification theorem  
**Sources.** [NIH / PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5776781/)  
**Audit status.** New

---

### CAU-08 · Very Hard · 5 points

**Question.** Under classical independent measurement error, the true correlation between X and Y is 0.80. X has reliability 0.64 and Y is measured perfectly. What observed correlation is expected?

**Assumptions.** Classical additive errors independent of true scores and each other; linear correlation setting.

**Hints.**
1. Measurement error usually shrinks correlation toward zero under the classical model.
2. Take the square root of the product of reliabilities.
3. Multiply 0.80 by 0.80.

**Answer.** 0.64.

**Explanation.** Attenuation gives r_observed = r_true·√(reliability_X·reliability_Y) = 0.80·√(0.64·1)=0.80·0.80=0.64.

**Practical takeaway.** Weak observed relationships can reflect noisy measurement rather than weak underlying association; improve measurement before overinterpreting coefficients.

**Evidence type.** Measurement-theory derivation  
**Sources.** Direct derivation from the assumptions stated on the card  
**Audit status.** New

---

### CAU-09 · Very Hard · 5 points

**Question.** If studies with statistically significant or positive results are more likely to appear in journals than null studies, what distortion results?

**Hints.**
1. The selection occurs between completed research and the public record.
2. Null results disproportionately disappear.
3. The bias is named for the publication process.

**Answer.** Publication bias, a form of selective reporting.

**Explanation.** The visible literature becomes an outcome-dependent sample of all conducted studies, inflating apparent evidence and effect sizes. Funnel-plot asymmetry can be suggestive but is not uniquely diagnostic.

**Practical takeaway.** Treat the literature as a selected dataset; search registries, protocols, and unpublished results when stakes are high.

**Evidence type.** Research-methods phenomenon  
**Sources.** [Cochrane Handbook](https://training.cochrane.org/handbook/current/chapter-13)  
**Audit status.** New

---

### CAU-10 · Very Hard · 5 points

**Question.** A researcher discovers a pattern after analyzing data, then writes the paper as though the hypothesis had been specified beforehand. What is this called?

**Hints.**
1. The problem is not generating a new hypothesis from data.
2. The problem is misrepresenting when the hypothesis was formed.
3. The acronym begins with Hypothesizing After…

**Answer.** HARKing—Hypothesizing After the Results are Known.

**Explanation.** Exploration is legitimate, but presenting a post-hoc hypothesis as a priori hides the extra search process and makes the evidence appear more confirmatory than it is.

**Practical takeaway.** Label exploration honestly and use preregistration or holdout data when claiming a confirmatory test.

**Evidence type.** Research-integrity concept  
**Sources.** [PubMed](https://pubmed.ncbi.nlm.nih.gov/15647155/)  
**Audit status.** New

---

## ∆ Finance & Economics

Compounding, leverage, risk, incentives, discounting, and capital allocation.

### FIN-01 · Challenging · 2 points

**Question.** An investment rises 50% in year 1 and falls 50% in year 2. What are its cumulative two-year return and annualized geometric return?

**Hints.**
1. Apply the returns multiplicatively, not additively.
2. 1.5×0.5=0.75.
3. For annualization, take the square root of 0.75.

**Answer.** Cumulative return: −25%. Annualized geometric return: √0.75−1 ≈ −13.40% per year.

**Explanation.** Starting from 1, wealth becomes 1.5 then 0.75. Percentage gains and losses act on different bases; arithmetic averaging gives a misleading 0%.

**Practical takeaway.** Evaluate wealth paths with geometric compounding; average percentages can conceal capital destruction.

**Evidence type.** Financial arithmetic  
**Sources.** Direct derivation from the assumptions stated on the card  
**Audit status.** Retained

---

### FIN-02 · Challenging · 2 points

**Question.** An investment earns a nominal 10% while the price level rises 8%. What is the exact real return?

**Hints.**
1. Use multiplicative growth factors.
2. Divide 1.10 by 1.08.
3. The result is slightly below 2%.

**Answer.** 1.10/1.08−1 ≈ 1.8519%.

**Explanation.** Real growth is the ratio of nominal wealth growth to price-level growth. Subtracting inflation is only a first-order approximation.

**Practical takeaway.** Track purchasing power, not account balance alone; inflation compounds too.

**Evidence type.** Economic arithmetic  
**Sources.** Direct derivation from the assumptions stated on the card  
**Audit status.** Retained

---

### FIN-03 · Challenging · 2 points

**Question.** A bond has modified duration 6. Yields rise by 0.50 percentage points. Ignoring convexity, what approximate price change should you expect?

**Assumptions.** Small parallel yield change; modified duration applies; convexity and credit-spread changes ignored.

**Hints.**
1. Convert 0.50 percentage points to 0.005.
2. Duration gives percentage price sensitivity per one-point yield change.
3. The sign is opposite the yield change.

**Answer.** About −3%.

**Explanation.** The first-order approximation is ΔP/P≈−D_mod·Δy=−6×0.005=−0.03.

**Practical takeaway.** A ‘safe’ fixed payment can still have material market-price risk when duration is long.

**Evidence type.** Financial approximation  
**Sources.** [FINRA](https://www.finra.org/investors/insights/bonds-interest-rate-changes-duration)  
**Audit status.** Retained

---

### FIN-04 · Hard · 3 points

**Question.** Which type of investment risk can broad diversification largely eliminate: systematic risk or idiosyncratic risk?

**Assumptions.** Sufficiently broad diversification across imperfectly correlated assets; diversification does not guarantee against loss.

**Hints.**
1. A product recall at one company is the relevant kind of shock.
2. Owning more companies cannot remove a recession affecting all of them.
3. The diversifiable risk is also called unsystematic.

**Answer.** Idiosyncratic, company-specific risk.

**Explanation.** Independent or weakly correlated firm-specific shocks tend to offset in a broad portfolio. Market-wide systematic shocks remain shared across holdings.

**Practical takeaway.** Do not expect compensation for risks you could cheaply diversify away; concentration needs a deliberate justification.

**Evidence type.** Portfolio-theory result  
**Sources.** [Investor.gov](https://www.investor.gov/introduction-investing/investing-basics/glossary/diversification)  
**Audit status.** Retained

---

### FIN-05 · Hard · 3 points

**Question.** You can repeatedly make an even-money bet that wins with probability 0.60 and loses with probability 0.40. Under the Kelly criterion, what fraction of wealth maximizes long-run expected logarithmic growth?

**Assumptions.** Known stationary probabilities, repeated independent bets, even payoff odds, logarithmic-growth objective.

**Hints.**
1. For even odds, subtract loss probability from win probability.
2. The edge is 0.20.
3. The criterion does not say to bet 60%.

**Answer.** 20% of wealth.

**Explanation.** For an even-money bet, f*=p−q=0.60−0.40=0.20. Betting more increases drawdown and eventually reduces logarithmic growth; betting all risks ruin.

**Practical takeaway.** Position size is as important as having an edge; estimation error is why practitioners often use fractional Kelly.

**Evidence type.** Optimization theorem  
**Sources.** [Bell System Technical Journal](https://onlinelibrary.wiley.com/doi/10.1002/j.1538-7305.1956.tb03809.x)  
**Audit status.** Retained

---

### FIN-06 · Hard · 3 points

**Question.** At a 7% annual discount rate, what is the present value of a guaranteed $100,000 payment ten years from now?

**Assumptions.** Annual compounding at a constant 7% rate; payment is certain and in the same nominal units.

**Hints.**
1. Use 1.07 to the tenth power.
2. The result is a little more than half of $100,000.
3. Compute 100,000/1.967151…

**Answer.** $100,000/1.07¹⁰ ≈ $50,834.93.

**Explanation.** Discounting reverses compounding: present value is future value divided by the growth factor over ten periods.

**Practical takeaway.** Small changes in discount rate or time horizon can radically change the economic value of distant promises.

**Evidence type.** Financial arithmetic  
**Sources.** Direct derivation from the assumptions stated on the card  
**Audit status.** Retained

---

### FIN-07 · Hard · 3 points

**Question.** A retiree starts with $100 and withdraws $10 at each year-end. Sequence A returns +20%, then −10%; Sequence B returns −10%, then +20%. What is ending wealth in each case?

**Assumptions.** Returns occur before each year-end withdrawal; no taxes or fees.

**Hints.**
1. Apply each return before that year’s withdrawal.
2. Without cash flows, multiplication would make order irrelevant.
3. The early loss leaves less capital for the later gain.

**Answer.** Sequence A ends at $89; Sequence B ends at $86.

**Explanation.** A: 100×1.20−10=110; 110×0.90−10=89. B: 100×0.90−10=80; 80×1.20−10=86. Withdrawals make return order matter.

**Practical takeaway.** When withdrawing or contributing, average return is not enough; path and timing become financially consequential.

**Evidence type.** Financial arithmetic  
**Sources.** [Charles Schwab](https://www.schwab.com/learn/story/timing-matters-understanding-sequence-returns-risk)  
**Audit status.** Retained

---

### FIN-08 · Very Hard · 5 points

**Question.** A project has cash flows −100 at t=0, +230 at t=1, and −132 at t=2. How many internal rates of return does it have, and what are they?

**Assumptions.** Deterministic annual cash flows and the conventional IRR definition.

**Hints.**
1. Nonconventional sign changes can produce multiple roots.
2. Multiply the NPV equation by (1+r)².
3. Factor 100x²−230x+132.

**Answer.** Two IRRs: 10% and 20%.

**Explanation.** Setting NPV to zero and x=1+r gives 100x²−230x+132=0=(10x−11)(10x−12). Thus x=1.1 or 1.2.

**Practical takeaway.** IRR can be ambiguous; for nonconventional cash flows, inspect the full NPV profile and opportunity-cost discount rate.

**Evidence type.** Financial derivation  
**Sources.** [ACCA](https://www.accaglobal.com/gb/en/student/exam-support-resources/foundation-level-study-resources/ffm/ffm-technical-articles/the-internal-rate-of-return.html)  
**Audit status.** Retained

---

### FIN-09 · Very Hard · 5 points

**Question.** A company owns $100 of assets financed by $50 debt and $50 equity. Asset value falls by 50% while debt remains $50. What percentage of equity is lost?

**Assumptions.** Debt face value is fixed and senior; no new capital, taxes, or bankruptcy frictions.

**Hints.**
1. Equity is the residual: assets minus debt.
2. Debt does not absorb the first loss in this simplified capital structure.
3. New equity = 50−50.

**Answer.** 100%.

**Explanation.** Assets fall to $50. After the fixed $50 debt claim, residual equity is zero. Leverage magnifies the asset loss onto the smaller equity base.

**Practical takeaway.** A moderate fall in enterprise value can wipe out owners when the equity cushion is thin.

**Evidence type.** Balance-sheet arithmetic  
**Sources.** Direct derivation from the assumptions stated on the card  
**Audit status.** Retained

---

### FIN-10 · Very Hard · 5 points

**Question.** What is the distinction between adverse selection and moral hazard in contracting or insurance?

**Hints.**
1. One problem exists at selection; the other after incentives change.
2. Ask whether the hidden variable is a type or an action.
3. Before = adverse selection; after = moral hazard.

**Answer.** Adverse selection is hidden information or type before contracting; moral hazard is hidden action or changed behavior after contracting.

**Explanation.** A high-risk buyer disproportionately choosing insurance is adverse selection. Taking less care because one is insured is moral hazard.

**Practical takeaway.** Design screening for hidden types and incentives/monitoring for hidden actions; they are different failures requiring different remedies.

**Evidence type.** Contract-theory distinction  
**Sources.** [Nobel Prize](https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/)  
**Audit status.** New

---

## ∞ Mathematics, Information & Computation

Convexity, entropy, infinity, computability, and distributions with heavy tails.

### MTH-01 · Challenging · 2 points

**Question.** If f is convex and X is a random variable with finite expectations, which is larger: E[f(X)] or f(E[X])? Name the theorem.

**Assumptions.** f is convex on the support of X and the relevant expectations exist.

**Hints.**
1. Convex curves bow below their chords.
2. Randomness can raise the expectation of a convex payoff.
3. The theorem is named after Jensen.

**Answer.** E[f(X)] ≥ f(E[X]); Jensen’s inequality.

**Explanation.** A chord of a convex function lies above the function. Averaging transformed values therefore exceeds or equals transforming the average.

**Practical takeaway.** Variability is costly under convex loss and valuable under convex payoff; averages alone omit the curvature effect.

**Evidence type.** Theorem  
**Sources.** [Encyclopedia of Mathematics](https://encyclopediaofmath.org/wiki/Jensen_inequality)  
**Audit status.** Retained

---

### MTH-02 · Challenging · 2 points

**Question.** What is the Shannon entropy, in bits, of a binary source that emits one symbol with probability 0.9 and the other with probability 0.1?

**Hints.**
1. Use H(p)=−p log₂p−(1−p)log₂(1−p).
2. The answer is below 0.5 bits.
3. Numerically it is about 0.468996.

**Answer.** −0.9 log₂0.9 − 0.1 log₂0.1 ≈ 0.469 bits per symbol.

**Explanation.** Entropy measures average uncertainty. A highly imbalanced binary source carries less than the one bit of a fair source.

**Practical takeaway.** Predictability is compressible: information depends on surprise, not merely the number of possible symbols.

**Evidence type.** Information-theory calculation  
**Sources.** [Bell System Technical Journal](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)  
**Audit status.** Retained

---

### MTH-03 · Challenging · 2 points

**Question.** Can a lossless compressor make every possible n-bit file shorter than n bits?

**Hints.**
1. A lossless compressor must map distinct inputs to distinct compressed strings.
2. Count all binary strings shorter than n.
3. Apply the pigeonhole principle.

**Answer.** No.

**Explanation.** There are 2ⁿ n-bit strings but only 2ⁿ−1 binary strings of length less than n. An injective lossless mapping cannot fit all inputs into fewer outputs.

**Practical takeaway.** Compression works by exploiting structure in some inputs; any universal gain must be paid for by unchanged or expanded others.

**Evidence type.** Counting proof  
**Sources.** [Bell System Technical Journal](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)  
**Audit status.** Retained

---

### MTH-04 · Hard · 3 points

**Question.** Is there an algorithm that examines every arbitrary program–input pair and always determines correctly whether the program eventually halts?

**Hints.**
1. Assume such a decider exists and make a program react opposite to its prediction about itself.
2. The contradiction uses self-reference and diagonalization.
3. The problem is called the halting problem.

**Answer.** No. The halting problem is undecidable.

**Explanation.** Turing-style diagonalization constructs a contradiction from any purported universal halting decider. Specific restricted programs can be analyzed; the impossibility is for all programs.

**Practical takeaway.** No tool can perfectly certify every arbitrary program; practical verification succeeds by restricting languages, properties, or assumptions.

**Evidence type.** Undecidability theorem  
**Sources.** [Proceedings of the London Mathematical Society](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf)  
**Audit status.** Retained

---

### MTH-05 · Hard · 3 points

**Question.** What does Gödel’s first incompleteness theorem imply for any consistent, effectively axiomatized formal system capable of expressing sufficient arithmetic?

**Assumptions.** Classical conditions of Gödel’s theorem, including consistency and sufficient arithmetic strength.

**Hints.**
1. The system must be sufficiently expressive and effectively axiomatized.
2. Consistency cannot coexist with proving every sentence or its negation.
3. The missing property is completeness.

**Answer.** It is incomplete: some statements expressible in the system are neither provable nor disprovable within it.

**Explanation.** Gödel constructs a sentence whose provability would conflict with consistency. The theorem is precise and does not imply that every difficult question is unknowable.

**Practical takeaway.** Formal rigor has limits that are themselves formally demonstrable; use the theorem precisely, not as a metaphor for ordinary uncertainty.

**Evidence type.** Theorem  
**Sources.** [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/goedel-incompleteness/)  
**Audit status.** Retained; scope caveat strengthened

---

### MTH-06 · Hard · 3 points

**Question.** Which of these sets have the same cardinality: the integers, rational numbers, and real numbers?

**Hints.**
1. Density on the number line does not determine cardinality.
2. Both positive and negative integers can be put in one sequence.
3. Cantor diagonalization separates the reals from countable sets.

**Answer.** Integers and rationals are both countably infinite; reals are uncountable and strictly larger.

**Explanation.** A diagonal enumeration lists every rational despite density. Cantor’s diagonal argument shows no list can contain every real number.

**Practical takeaway.** Intuition built for finite collections often fails for infinity; specify the mapping, not merely ‘more densely packed.’

**Evidence type.** Set-theoretic theorem  
**Sources.** [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/set-theory/)  
**Audit status.** Retained

---

### MTH-07 · Hard · 3 points

**Question.** Is there a general algorithm that computes, for every finite string, the exact length of the shortest program that outputs it?

**Assumptions.** A fixed universal description language; complexity measured up to an additive language constant.

**Hints.**
1. The quantity asks for the shortest program over all programs.
2. Searching longer is not enough because some candidate programs may never halt.
3. The result is tied to the halting problem.

**Answer.** No. Exact Kolmogorov complexity is uncomputable in general.

**Explanation.** If exact shortest-description length were computable, it could solve problems equivalent to halting and create Berry-style contradictions. Compressors can find descriptions but cannot universally certify optimality.

**Practical takeaway.** There is no universal, computable certificate that an explanation or compression is the simplest possible one.

**Evidence type.** Uncomputability theorem  
**Sources.** [arXiv](https://arxiv.org/abs/2002.07674)  
**Audit status.** Retained

---

### MTH-08 · Very Hard · 5 points

**Question.** A fair random walk starts at wealth i and moves +1 or −1 with equal probability until hitting 0 or N. What is the probability it reaches N before ruin? What is it for i=3, N=10?

**Assumptions.** Fair independent ±1 steps; absorbing boundaries; stopping occurs almost surely.

**Hints.**
1. The process has no drift.
2. Use expected wealth at the stopping boundary.
3. Solve i=Np.

**Answer.** i/N; for i=3 and N=10, the probability is 0.3.

**Explanation.** The current wealth is a martingale. At stopping, expected terminal wealth is N·P(hit N)+0·P(hit 0)=i, so P(hit N)=i/N.

**Practical takeaway.** A fair game can still have a high ruin probability when the loss boundary is much closer than the success boundary.

**Evidence type.** Martingale theorem / derivation  
**Sources.** Direct derivation from the assumptions stated on the card  
**Audit status.** New

---

### MTH-09 · Very Hard · 5 points

**Question.** For a Pareto distribution with tail parameter α, when are the mean and variance finite?

**Assumptions.** Standard continuous Pareto Type I distribution with positive scale.

**Hints.**
1. Moments fail one by one as the tail gets heavier.
2. The k-th raw moment exists only when α>k.
3. Apply k=1 and k=2.

**Answer.** The mean is finite iff α>1; the variance is finite iff α>2.

**Explanation.** Pareto tails decay as a power law. Integrating x times the density requires α>1; integrating x² requires α>2.

**Practical takeaway.** In heavy-tailed domains, averages and standard deviations may be unstable or undefined; ordinary risk intuition can fail catastrophically.

**Evidence type.** Distribution theorem  
**Sources.** Direct derivation from the assumptions stated on the card  
**Audit status.** New

---

### MTH-10 · Very Hard · 5 points

**Question.** If X₁,…,Xₙ are independent Uniform[0,1] variables, what is E[max Xᵢ]? What is it for n=9?

**Assumptions.** Independent, identically distributed continuous Uniform[0,1] draws.

**Hints.**
1. Find the cumulative distribution of the maximum first.
2. All n observations must be at most x.
3. Differentiate xⁿ, then integrate x times the density.

**Answer.** n/(n+1); for n=9, 0.9.

**Explanation.** P(max≤x)=xⁿ, so the maximum has density nxⁿ⁻¹. Integrating x·nxⁿ⁻¹ from 0 to 1 gives n/(n+1).

**Practical takeaway.** Selection alone creates impressive extremes; the best of many noisy candidates is predictably optimistic.

**Evidence type.** Probability derivation  
**Sources.** Direct derivation from the assumptions stated on the card  
**Audit status.** New

---

## ⚙ Organizations, Operations & Systems

Queues, bottlenecks, reliability, projects, incentives, and feedback amplification.

### SYS-01 · Challenging · 2 points

**Question.** A stable process completes 20 cases per day, and the average case spends 5 days in the system. What is average work-in-process?

**Assumptions.** Long-run stable averages; consistent boundary for arrivals, departures, and time in system.

**Hints.**
1. Multiply throughput by flow time.
2. Units are cases/day × days.
3. Use L=λW.

**Answer.** 100 cases.

**Explanation.** Little’s Law states L=λW. Thus 20 cases/day × 5 days = 100 cases in the system on average.

**Practical takeaway.** Inventory, queues, and cycle time are linked; reducing work-in-process can reduce delay when throughput is constrained.

**Evidence type.** Theorem  
**Sources.** [INFORMS](https://pubsonline.informs.org/doi/10.1287/opre.9.3.383)  
**Audit status.** New

---

### SYS-02 · Challenging · 2 points

**Question.** In an M/M/1 queue, service rate μ=10 per hour. What is mean time in the system when arrival rate λ=8, and when λ=9?

**Assumptions.** Poisson arrivals, exponential independent service times, one server, infinite buffer, steady state with λ<μ.

**Hints.**
1. Use the gap between service and arrival rates, not their ratio alone.
2. The formula is 1/(μ−λ).
3. As λ approaches μ, the denominator approaches zero.

**Answer.** At λ=8: 1/(10−8)=0.5 hour. At λ=9: 1/(10−9)=1 hour.

**Explanation.** For a stable M/M/1 queue, W=1/(μ−λ). Increasing utilization from 80% to 90% doubles mean system time; waiting grows nonlinearly near full capacity.

**Practical takeaway.** Operating near 100% utilization can destroy responsiveness even when nominal capacity still exceeds average demand.

**Evidence type.** Queueing theorem  
**Sources.** [MathWorks](https://www.mathworks.com/help/simevents/ug/m-m-1-queuing-system.html)  
**Audit status.** New

---

### SYS-03 · Challenging · 2 points

**Question.** If 90% of a program can be parallelized and the remaining 10% is inherently serial, what is the maximum speedup even with infinitely many processors?

**Assumptions.** Fixed workload; 10% truly serial; no communication or parallel overhead.

**Hints.**
1. Only the serial fraction remains in the infinite-processor limit.
2. The runtime floor is 10% of the original.
3. Speedup is the reciprocal of that fraction.

**Answer.** 10×.

**Explanation.** Amdahl’s Law gives speedup 1/[(1−p)+p/s]. As s→∞ and p=0.9, the limit is 1/0.1=10.

**Practical takeaway.** Optimize the bottleneck fraction; enormous investment in the already-fast part has a hard ceiling.

**Evidence type.** Performance law  
**Sources.** [ACM](https://dl.acm.org/doi/10.1145/1465482.1465560)  
**Audit status.** New

---

### SYS-04 · Hard · 3 points

**Question.** A project has tasks: A=4 days; after A, B=5 and C=3 can run in parallel; D=4 follows B; E=8 follows C; project completion requires both D and E. What is the minimum duration and critical path?

**Assumptions.** Deterministic durations, stated precedence constraints, unlimited resources, no crashing side effects.

**Hints.**
1. Enumerate each start-to-finish path.
2. Parallel branches do not add to each other; the longer branch governs.
3. Compare 13 with 15.

**Answer.** 15 days; critical path A→C→E.

**Explanation.** Path A-B-D takes 4+5+4=13 days. Path A-C-E takes 4+3+8=15 days, so the latter determines completion.

**Practical takeaway.** Accelerating a noncritical task may create no project-level benefit; manage the path that controls finish time.

**Evidence type.** Scheduling derivation  
**Sources.** Direct derivation from the assumptions stated on the card; [Project Management Institute](https://www.pmi.org/learning/library/critical-path-method-calculations-scheduling-8040)  
**Audit status.** New

---

### SYS-05 · Hard · 3 points

**Question.** A serial production line has stage capacities of 10, 7, and 12 units per hour. Ignoring variability and downtime, what is maximum steady throughput?

**Assumptions.** Serial flow, no yield loss or rework, stable operation, unlimited buffers.

**Hints.**
1. Every completed unit must pass all three stages.
2. The fastest stages cannot compensate for the slowest serial stage.
3. Take the minimum capacity.

**Answer.** 7 units per hour.

**Explanation.** Flow through every serial stage cannot exceed the smallest capacity. The 7-unit stage is the bottleneck.

**Practical takeaway.** Improving non-bottlenecks can increase idle inventory rather than output; find the constraint first.

**Evidence type.** Capacity derivation  
**Sources.** Direct derivation from the assumptions stated on the card  
**Audit status.** New

---

### SYS-06 · Hard · 3 points

**Question.** Three independent components with reliability 0.99 are required in series. What is system reliability? If instead two independent 0.90 components are redundant in parallel and either can succeed, what is reliability?

**Assumptions.** Component outcomes independent; series requires all; parallel succeeds if either succeeds.

**Hints.**
1. For series, calculate the probability all succeed.
2. For parallel, calculate one minus the probability all fail.
3. Independence permits multiplication.

**Answer.** Series: 0.99³=0.970299. Parallel: 1−0.10²=0.99.

**Explanation.** A series system fails if any required component fails, so reliabilities multiply. A parallel system fails only if both redundant components fail.

**Practical takeaway.** Adding required dependencies reduces reliability; well-designed redundancy can increase it—but correlated failures undermine the gain.

**Evidence type.** Reliability derivation  
**Sources.** Direct derivation from the assumptions stated on the card  
**Audit status.** New

---

### SYS-07 · Hard · 3 points

**Question.** A company owner cannot fully observe a manager’s effort, and their objectives differ. What class of organizational problem is this?

**Hints.**
1. One party acts on behalf of another.
2. The action is imperfectly observable.
3. The words ‘principal’ and ‘agent’ name the relationship.

**Answer.** A principal–agent problem with hidden action.

**Explanation.** The principal delegates to an agent whose action is costly to monitor and whose incentives are not perfectly aligned. Contracts trade off incentives, risk, measurement, and gaming.

**Practical takeaway.** Do not assume delegation preserves goals; align incentives while anticipating what cannot be measured cleanly.

**Evidence type.** Contract-theory model  
**Sources.** [Nobel Prize](https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/)  
**Audit status.** New

---

### SYS-08 · Very Hard · 5 points

**Question.** Small fluctuations in retail demand become larger swings in distributor orders and still larger swings upstream. What is this called?

**Hints.**
1. The pattern grows as it travels backward through a supply chain.
2. Orders become more variable than underlying consumption.
3. The metaphor is the tip of a whip moving farther than the handle.

**Answer.** The bullwhip effect.

**Explanation.** Forecast updating, order batching, price promotions, rationing games, and delays can amplify variability as information moves upstream.

**Practical takeaway.** Share end-demand data, reduce batching and delays, and avoid incentives that turn local rationality into system-wide instability.

**Evidence type.** Operations phenomenon and model  
**Sources.** [Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.1040.0305)  
**Audit status.** New

---

### SYS-09 · Very Hard · 5 points

**Question.** What principle warns that when a measure becomes a target, it often ceases to be a good measure?

**Assumptions.** An aphoristic regularity rather than a universal mathematical theorem; effect depends on incentives and adaptivity.

**Hints.**
1. The problem appears after incentives attach to a metric.
2. The proxy is optimized rather than the underlying objective.
3. The law is named after economist Charles Goodhart.

**Answer.** Goodhart’s law.

**Explanation.** Once rewards depend on a proxy, people optimize the proxy—including by shifting effort, exploiting loopholes, or changing the relationship between the metric and the true goal.

**Practical takeaway.** Use multiple measures, audits, and outcome checks; every high-stakes metric invites adaptation and gaming.

**Evidence type.** Institutional principle  
**Sources.** [Bank of England](https://www.bankofengland.co.uk/quarterly-bulletin/2021/why-does-goodharts-law-matter)  
**Audit status.** New

---

### SYS-10 · Very Hard · 5 points

**Question.** Four thousand drivers travel from S to T. Roads S→A and B→T take x/100 minutes with x users; A→T and S→B take 45 minutes. What is equilibrium time before adding a zero-minute A→B road, and after adding it?

**Assumptions.** Nonatomic selfish routing, stated latency functions, 4,000 identical drivers, Wardrop equilibrium.

**Hints.**
1. First solve the symmetric split without the shortcut.
2. After adding A→B, test the route containing both congestion-sensitive links.
3. The added option changes equilibrium incentives, not physical capacity alone.

**Answer.** Before: 65 minutes. After: 80 minutes.

**Explanation.** Before, traffic splits 2,000/2,000: 20+45=65. With A→B, all drivers choose S-A-B-T: 40+0+40=80; a unilateral switch would take 85. This is Braess’s paradox.

**Practical takeaway.** More options can worsen decentralized outcomes; evaluate equilibrium behavior after a policy change, not just engineering capacity.

**Evidence type.** Congestion-game result  
**Sources.** [Cornell Networks Textbook](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch08.pdf)  
**Audit status.** Retained; moved to systems

---

## ¶ Rhetoric, Logic & Communication

Validity, implication, hidden premises, persuasion, and honest risk communication.

### RHE-01 · Challenging · 2 points

**Question.** What is the difference between a valid deductive argument and a sound one?

**Hints.**
1. One property is structural; the other adds factual correctness.
2. Soundness implies validity, but validity does not imply soundness.
3. A sound argument is valid plus true premises.

**Answer.** Valid: true premises could not yield a false conclusion. Sound: valid and all premises are actually true.

**Explanation.** Validity concerns logical form; soundness adds factual truth of premises. A valid argument can be unsound and even have a false conclusion if a premise is false.

**Practical takeaway.** Logic preserves truth but does not supply true premises; audit evidence and inference separately.

**Evidence type.** Formal definition  
**Sources.** [Internet Encyclopedia of Philosophy](https://iep.utm.edu/val-snd/)  
**Audit status.** New

---

### RHE-02 · Challenging · 2 points

**Question.** Translate ‘P only if Q’ into symbolic logic. Which condition is necessary, and which is sufficient?

**Hints.**
1. Try: ‘You graduate only if you pass.’
2. Passing is required, though not necessarily enough.
3. The arrow points from P to Q.

**Answer.** P→Q. Q is necessary for P; P is sufficient for Q.

**Explanation.** ‘Only if’ introduces a requirement: whenever P holds, Q must hold. It does not assert Q→P.

**Practical takeaway.** Many policy and contract disputes are disguised errors about necessary versus sufficient conditions.

**Evidence type.** Formal semantics  
**Sources.** [Internet Encyclopedia of Philosophy](https://iep.utm.edu/val-snd/)  
**Audit status.** New

---

### RHE-03 · Challenging · 2 points

**Question.** What is wrong with the argument: ‘If the server is down, the status page is red. The status page is red. Therefore the server is down’?

**Hints.**
1. A conditional does not say its consequent has only one cause.
2. The form is P→Q, Q, therefore P.
3. The fallacy’s name starts with ‘affirming’.

**Answer.** It affirms the consequent and is invalid.

**Explanation.** Other causes could make the status page red. From P→Q and Q, P does not follow; the valid related form is modus tollens using not-Q.

**Practical takeaway.** Diagnostic indicators need likelihoods and alternatives; an effect does not uniquely identify its favored cause.

**Evidence type.** Formal-logic result  
**Sources.** [Internet Encyclopedia of Philosophy](https://iep.utm.edu/val-snd/)  
**Audit status.** New

---

### RHE-04 · Hard · 3 points

**Question.** Does the sentence ‘Some guests left’ logically entail that not all guests left? If not, what commonly conveys that interpretation?

**Hints.**
1. Test whether ‘Some, in fact all’ is contradictory.
2. Distinguish literal truth conditions from pragmatic inference.
3. The technical term is scalar implicature.

**Answer.** No. Semantically, ‘some’ is compatible with ‘all’; ‘not all’ is commonly conveyed by a scalar conversational implicature.

**Explanation.** A cooperative listener reasons that the speaker would have used the stronger ‘all’ if warranted. Context can cancel the implication: ‘Some—indeed all—left.’

**Practical takeaway.** Good communication distinguishes what was asserted from what listeners predictably inferred.

**Evidence type.** Linguistic analysis  
**Sources.** [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/implicature/)  
**Audit status.** New

---

### RHE-05 · Hard · 3 points

**Question.** An argument states a conclusion and one premise but leaves another premise for the audience to supply. What is this rhetorical form called?

**Hints.**
1. It is sometimes called a rhetorical syllogism.
2. The missing material is presumed obvious to the audience.
3. The word begins with ‘en-’ and ends with ‘-meme’.

**Answer.** An enthymeme.

**Explanation.** Everyday persuasion often omits a shared or strategically hidden premise. Reconstructing it makes the inference and its vulnerability explicit.

**Practical takeaway.** When an argument feels compelling, write the missing bridge premise; that is often where disagreement actually lives.

**Evidence type.** Rhetorical definition  
**Sources.** [Purdue OWL](https://owl.purdue.edu/owl/general_writing/common_writing_assignments/argument_papers/body_paragraphs.html)  
**Audit status.** New

---

### RHE-06 · Hard · 3 points

**Question.** In Toulmin’s model, what component explains why the stated data or grounds support the claim?

**Hints.**
1. It is not the evidence itself or the conclusion.
2. It licenses the move from grounds to claim.
3. The term also means authorization.

**Answer.** The warrant.

**Explanation.** The warrant is the inferential bridge, often implicit. Backing supports the warrant; qualifiers limit strength; rebuttals state exceptions.

**Practical takeaway.** Strong communicators expose warrants so audiences can evaluate the actual inference, not just the evidence and conclusion.

**Evidence type.** Argumentation framework  
**Sources.** [Purdue OWL](https://owl.purdue.edu/owl/general_writing/academic_writing/historical_perspectives_on_argumentation/toulmin_argument.html)  
**Audit status.** New

---

### RHE-07 · Hard · 3 points

**Question.** Repeated exposure to a claim can increase its judged truth even when repetition supplies no new evidence. What is this called?

**Hints.**
1. The claim becomes easier to process.
2. Familiarity is mistaken for evidence.
3. The effect’s name contains ‘truth’.

**Answer.** The illusory truth effect.

**Explanation.** Repetition increases processing fluency and familiarity, which people can misattribute to accuracy. Prior knowledge helps but does not always eliminate the effect.

**Practical takeaway.** Do not let repetition count as corroboration; trace claims to independent evidence and sources.

**Evidence type.** Replicated experimental finding  
**Sources.** [NIH / PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8116821/)  
**Audit status.** New

---

### RHE-08 · Very Hard · 5 points

**Question.** What persuasion method builds resistance by warning that an attitude is vulnerable and presenting weakened counterarguments with refutations before a stronger attack?

**Hints.**
1. The metaphor comes from immunology.
2. Exposure is preemptive and uses a weakened challenge.
3. The technique’s name is the same as vaccination.

**Answer.** Inoculation.

**Explanation.** Analogous to a vaccine, an inoculation message induces threat awareness and counterarguing practice. It differs from merely repeating support for the existing belief.

**Practical takeaway.** Teach people how manipulation works before exposure; pre-bunking can be more durable than chasing every falsehood afterward.

**Evidence type.** Persuasion theory with experimental evidence  
**Sources.** [NIH / PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4746429/)  
**Audit status.** New

---

### RHE-09 · Very Hard · 5 points

**Question.** Experts systematically underestimate how difficult their explanations are for novices because they cannot fully ignore what they already know. What is this bias called?

**Hints.**
1. Knowing makes it hard to simulate not knowing.
2. The bias affects teaching, negotiation, and product design.
3. Its name describes knowledge as a curse.

**Answer.** The curse of knowledge.

**Explanation.** Information available to the communicator contaminates predictions of an uninformed listener’s beliefs and comprehension.

**Practical takeaway.** Test explanations on real novices, define hidden prerequisites, and ask receivers to paraphrase rather than merely nod.

**Evidence type.** Experimental finding  
**Sources.** [CaltechAUTHORS](https://authors.library.caltech.edu/records/zgwcn-vap73)  
**Audit status.** New

---

### RHE-10 · Very Hard · 5 points

**Question.** A treatment lowers risk from 2% to 1%. What are the relative risk reduction, absolute risk reduction, and number needed to treat?

**Assumptions.** Comparable populations and time horizons; NNT based on the stated constant absolute risk difference.

**Hints.**
1. Report both a ratio and a difference.
2. Use risks as decimals for NNT.
3. The reciprocal of 0.01 is 100.

**Answer.** RRR=50%; ARR=1 percentage point; NNT=100.

**Explanation.** Relative reduction is (2−1)/2=50%. Absolute reduction is 0.02−0.01=0.01. NNT=1/0.01=100.

**Practical takeaway.** Relative effects can sound dramatic while absolute benefit is modest; communicate both, with time horizon and harms.

**Evidence type.** Risk-communication calculation  
**Sources.** [Oxford Centre for Evidence-Based Medicine](https://www.cebm.ox.ac.uk/resources/ebm-tools/number-needed-to-treat-nnt)  
**Audit status.** New

---

## ⬡ Digital Self-Defense & Adversarial Thinking

Authentication, cryptography, injection, backups, and threat-model discipline.

### SEC-01 · Challenging · 2 points

**Question.** Which security principle says a cryptosystem should remain secure even if everything about the system except the secret key is public?

**Hints.**
1. The algorithm may be public.
2. Only a small, replaceable secret must remain unknown.
3. The principle is named after Auguste Kerckhoffs.

**Answer.** Kerckhoffs’s principle.

**Explanation.** Security should rest on manageable secret keys, not obscurity of algorithms or architecture. Public designs can be analyzed, tested, and replaced without pretending implementation details stay hidden forever.

**Practical takeaway.** Assume adversaries will learn how a system works; protect secrets and design for compromise rather than depending on obscurity.

**Evidence type.** Cryptographic design principle  
**Sources.** [Cryptologia](https://doi.org/10.1080/0161-118591863745)  
**Audit status.** New

---

### SEC-02 · Challenging · 2 points

**Question.** Under what conditions does a one-time pad provide perfect secrecy?

**Hints.**
1. The key cannot be shorter and expanded by an ordinary deterministic generator if perfect secrecy is required.
2. Its name contains ‘one-time’ for a reason.
3. Random, message-length, secret, used once.

**Answer.** The key must be truly random, at least as long as the message, kept secret, and never reused.

**Explanation.** With those conditions, every plaintext of the same length is equally compatible with a ciphertext. Reusing a pad or using predictable key material destroys the guarantee.

**Practical takeaway.** Strong cryptography is conditional: violating key-generation or reuse assumptions can nullify a mathematically perfect construction.

**Evidence type.** Information-theoretic theorem  
**Sources.** [Bell System Technical Journal](https://pages.cs.wisc.edu/~rist/642-spring-2014/shannon-secrecy.pdf)  
**Audit status.** New

---

### SEC-03 · Challenging · 2 points

**Question.** For an ideal 128-bit hash output, after roughly how many random inputs does a collision become likely on the order of 50%?

**Assumptions.** Ideal uniformly distributed independent hash outputs; generic collision attack.

**Hints.**
1. This is a collision question, not a preimage question.
2. Use the birthday paradox.
3. Take the square root of 2^128.

**Answer.** On the order of 2⁶⁴ inputs.

**Explanation.** The birthday bound makes collision work scale as the square root of the output space: √(2¹²⁸)=2⁶⁴, up to a constant near 1.177 for 50% probability.

**Practical takeaway.** Security bits depend on the attack goal: an n-bit hash offers about n/2 bits of generic collision resistance.

**Evidence type.** Probability / cryptography derivation  
**Sources.** Direct derivation from the assumptions stated on the card  
**Audit status.** New

---

### SEC-04 · Hard · 3 points

**Question.** A passphrase consists of four independently and uniformly selected words from a 7,776-word list. Approximately how much entropy does the selection have?

**Assumptions.** Exactly uniform independent word selection and no information leakage about the choices.

**Hints.**
1. Entropy adds for independent uniform choices.
2. 7,776=6^5, the Diceware list size.
3. Compute four times log₂7,776.

**Answer.** 4·log₂(7,776) ≈ 51.7 bits.

**Explanation.** There are 7,776⁴ equally likely phrases. Entropy is log₂ of that count, or four times about 12.925 bits per word.

**Practical takeaway.** Password strength comes from the selection process, not how random the result looks; human-chosen words are not equivalent to uniform dice rolls.

**Evidence type.** Information-theory calculation  
**Sources.** [Electronic Frontier Foundation](https://www.eff.org/dice)  
**Audit status.** New

---

### SEC-05 · Hard · 3 points

**Question.** A login asks for two different passwords. Is that two-factor authentication?

**Hints.**
1. Count categories, not prompts.
2. Password and PIN are both knowledge factors.
3. A second factor might be a hardware authenticator or biometric.

**Answer.** No. Both are the same factor type: something you know.

**Explanation.** Multiple factors require distinct categories, such as knowledge, possession, or inherence. Two secrets may be two steps, but not two independent factor classes.

**Practical takeaway.** Extra steps are not automatically extra security; ask whether compromise of one channel also compromises the other.

**Evidence type.** Authentication standard  
**Sources.** [NIST SP 800-63B](https://pages.nist.gov/800-63-4/sp800-63b.html)  
**Audit status.** New

---

### SEC-06 · Hard · 3 points

**Question.** Why is WebAuthn/FIDO authentication generally phishing-resistant while a time-based one-time code can be relayed by a real-time phishing site?

**Assumptions.** Correct WebAuthn implementation and trusted client; TOTP used without additional transaction/origin binding.

**Hints.**
1. The difference is not merely code length.
2. One credential output is scoped to a verifier identity.
3. The other can be copied and replayed during its validity window.

**Answer.** WebAuthn cryptographically binds the authenticator response to the legitimate relying-party identity/origin; a TOTP code is a bearer value not inherently bound to that site.

**Explanation.** An impostor origin cannot obtain a valid WebAuthn assertion for the real domain. A phishing proxy can ask for a TOTP code and immediately forward it to the real service.

**Practical takeaway.** Prefer phishing-resistant authenticators for high-value accounts; generic OTP MFA can still fail against adversary-in-the-middle attacks.

**Evidence type.** Technical standard / official guidance  
**Sources.** [NIST SP 800-63B](https://pages.nist.gov/800-63-4/sp800-63b.html); [W3C](https://www.w3.org/TR/webauthn-3/)  
**Audit status.** New

---

### SEC-07 · Hard · 3 points

**Question.** In public-key digital signatures, which key signs and which key verifies?

**Hints.**
1. The signing key must remain secret.
2. Anyone who needs to verify may possess the other key.
3. Private signs; public verifies.

**Answer.** The private key signs; the corresponding public key verifies.

**Explanation.** The signer proves possession of the private key without revealing it. Verification establishes integrity and key-based authenticity, subject to trust in the public-key binding.

**Practical takeaway.** A valid signature proves a key produced it, not automatically that the human identity, device, or surrounding claim is trustworthy.

**Evidence type.** Cryptographic definition  
**Sources.** [NIST FIPS 186-5](https://csrc.nist.gov/pubs/fips/186-5/final)  
**Audit status.** New

---

### SEC-08 · Very Hard · 5 points

**Question.** What programming technique is the primary defense against SQL injection when inserting untrusted values into a query?

**Assumptions.** The database driver genuinely parameterizes values; query structure is not built from untrusted concatenated fragments.

**Hints.**
1. Escaping strings manually is more fragile.
2. Separate code from data at the database interface.
3. Bind values to placeholders.

**Answer.** Prepared statements with parameterized queries.

**Explanation.** Parameters keep data separate from SQL syntax, so attacker-controlled text is not parsed as executable query structure. Allow-list validation remains important for identifiers or syntax that cannot be parameterized.

**Practical takeaway.** Security improves when dangerous interpretation is structurally impossible, not when every developer must remember perfect sanitization.

**Evidence type.** Secure-coding guidance  
**Sources.** [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)  
**Audit status.** New

---

### SEC-09 · Very Hard · 5 points

**Question.** How should a server store user passwords: reversible encryption, a fast unsalted hash, or a unique salt plus a slow memory-hard password hash/KDF?

**Hints.**
1. The server should not need to recover the original password.
2. Fast general-purpose hashes help attackers guess faster.
3. OWASP’s preferred modern choice is Argon2id.

**Answer.** A unique salt plus a slow, memory-hard password hashing function/KDF such as Argon2id, with appropriate parameters.

**Explanation.** Salts defeat precomputed tables and ensure equal passwords have different stored values. Deliberately expensive hashing raises the cost of each offline guess after a database breach.

**Practical takeaway.** Design for database compromise: password storage should make offline guessing expensive and isolate each user’s hash.

**Evidence type.** Current secure-coding guidance  
**Sources.** [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)  
**Audit status.** New

---

### SEC-10 · Very Hard · 5 points

**Question.** What does the 3-2-1 backup rule prescribe?

**Hints.**
1. The first number counts total copies.
2. The second counts media types.
3. The last requires separation from the primary site.

**Answer.** Keep 3 copies of important data, on 2 different types of storage media, with 1 copy off-site; for ransomware resilience, at least one protected/offline copy is prudent.

**Explanation.** Multiple copies reduce single-device loss, media diversity reduces common-mode failure, and geographic or logical separation protects against local disasters and account compromise.

**Practical takeaway.** A synchronized copy is not necessarily a backup; test restoration and keep at least one copy outside the attacker’s ordinary reach.

**Evidence type.** Operational security guideline  
**Sources.** [CISA](https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/back-up-business-data)  
**Audit status.** New

---

