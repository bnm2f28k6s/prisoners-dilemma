# Strategic games: foundations and additional resources

Research date: 2026-10-21. This is a development note, not a replacement lesson or a published site page.

## What we already have

Reviewed the repository's `README.md`, `docs/README.md`, and site configuration before searching. The existing lesson already explains:

- The prisoner's dilemma matrix, dominance comparisons, `T > R > P > S`, and the optional repeated-play condition `2R > T + S`.
- Moves versus strategies, fixed versus uncertain horizons, and the finite prisoner's dilemma backward-induction argument.
- Observations, retained memory, tit for tat, grim trigger, and a worked match.
- A proposed rules/decision-process decomposition and later directions involving noise, forgiveness, and populations.

Those topics do not need another introductory treatment. The current source is Stanford Encyclopedia of Philosophy's *Prisoner's Dilemma*. The resources below add a general game definition, contrasting payoff structures, sharper model boundaries, and material for exercises.

## Main recommendation

Keep the proposed teaching sequence:

1. **Level 0: a one-shot game.** Identify players, available actions, and each player's preferences over joint outcomes. Compare several payoff structures before specializing in prisoner's dilemma.
2. **Level 1: repeat the same stage game.** Keep the players, actions, and stage payoff functions fixed. Explicitly specify observation of past play, the horizon, and how round payoffs form an overall payoff. Strategies can now prescribe different actions after different histories.
3. **Later extensions: change one further assumption.** Treat observation errors, action errors, memory limits, learning, changing opponents, and changing environmental states as separate branches, not a compulsory linear hierarchy.

These levels are our teaching labels, not a standard taxonomy. In particular, they are not levels of recursive reasoning about another player's reasoning.

The central sentence should be: **the stage game stays constant; the repeated game is a new, larger game.** The distinction is directly supported by MIT Lecture 5, slides 6–7 [S5].

## Additions that would improve the foundation

### 1. Define the general object before introducing the square

For the initial deterministic one-shot setting, describe a game by:

- A set of players.
- A set of available actions for each player.
- A payoff function for each player, assigning a value to every joint action profile.

Formally, write `G = (N, (A_i), (u_i))`, with `u_i` taking the whole action profile as input. The notation is a compact summary, not a prerequisite for reading a matrix. Payoffs represent what that player values, which need not be money or selfish material gain [S1, S2].

A two-by-two matrix is one small case. Strategic games need not have two players, two actions, symmetry, or even a finite action set. Also distinguish the definition of the game from assumptions used to analyze it, such as rational payoff maximization or common knowledge of its rules [S1, S2].

**Terminology boundary:** strategic form or normal form is a representation, not a synonym for one-shot interaction. A dynamic game can also have a normal-form representation, whose strategies are complete contingent plans. MIT Lecture 4 explicitly constructs such a representation on slide 12 [S4]. Prefer the heading "one-shot simultaneous-move games" for our initial restricted setting.

### 2. Show that different matrices create different strategic problems

Yale Lecture 1 is unusually well matched to this project: its overview explicitly changes plausible payoffs to move from a prisoner's dilemma to a coordination problem. Lecture 5 develops multiple equilibria and coordination failure [S3].

For a future comparison exercise, keep the row/column layout and change only payoffs. The following are **constructed teaching examples**, not empirical measurements or matrices copied from a source. Cells contain `(Row payoff, Column payoff)`.

| Game | (C, C) | (C, D) | (D, C) | (D, D) | Pure-strategy Nash equilibria |
| --- | --- | --- | --- | --- | --- |
| Prisoner's dilemma, existing baseline | (3, 3) | (0, 5) | (5, 0) | (1, 1) | (D, D) |
| Stag hunt, a coordination problem | (4, 4) | (0, 3) | (3, 0) | (2, 2) | (C, C), (D, D) |
| Chicken, an anti-coordination problem | (3, 3) | (1, 5) | (5, 1) | (0, 0) | (C, D), (D, C) |
| Harmony, aligned dominant incentives | (5, 5) | (2, 3) | (3, 2) | (0, 0) | (C, C) |

The table's equilibrium claims were checked by enumerating unilateral deviations. It is a small selection, not a classification of every two-by-two game. C and D here are consistent action labels, not moral judgments.

Teaching questions:

- **Prisoner's dilemma:** why do individual incentives conflict with mutual improvement?
- **Stag hunt:** why might a player choose the safer action despite both preferring mutual C?
- **Chicken:** why does a player's best response switch to the action opposite the opponent's?
- **Harmony:** what disappears when individual incentives already favor mutual C?

Then add **matching pennies** as a boundary case: Row wants the choices to match; Column wants them to differ. It has no pure-strategy Nash equilibrium. This demonstrates why randomization is a useful separate topic and why not every game fits the symmetric C/D payoff template. Bonanno gives the example in Section 2.6, pp. 45–46 [S2].

The symmetric parameter ordering from our lesson distinguishes the examples above: prisoner's dilemma has `T > R > P > S`; the chosen stag hunt has `R > T > P > S`; chicken has `T > R > S > P`; the chosen harmony example has `R > T > S > P`. These are the orderings of these examples, not exhaustive definitions of every named family.

### 3. Separate three questions about outcomes

Before tournament rankings, introduce:

- **Strict dominance:** is one of my actions better than another against every opponent action?
- **Nash equilibrium:** given everyone else's choices, can any player improve by changing only their own choice?
- **Pareto efficiency:** is there another feasible outcome that makes someone better off without making anyone worse off?

They do not mean the same thing. In our prisoner's dilemma, `(D, D)` is an equilibrium but is Pareto dominated by `(C, C)`. Nash equilibrium does not mean the highest total score, fairness, or a prediction that people must behave this way. Define whether efficiency is being evaluated over the displayed pure outcomes or a larger set that includes lotteries [S1–S3].

**Suggested exercise:** mark each player's best response in every column/row, find the cells where both marks meet, then separately identify improvements that require both players to change.

### 4. Clarify when the actual numbers matter

The existing lesson correctly uses payoff ordering to identify the prisoner's dilemma. Add one boundary sentence: **preserving the order preserves pure-action comparisons, but need not preserve comparisons of lotteries or multi-round payoff streams.**

An ordinal representation only ranks outcomes. Expected-payoff calculations require cardinal utility information. Under expected utility, positive affine transformations preserve preferences over lotteries; arbitrary increasing transformations need not. Bonanno explains this explicitly in Section 5.2, especially p. 183, and Sections 6.1–6.2 [S2].

For repeated play, the aggregation rule is additional structure. If we add or discount stage payoffs, payoff gaps can affect incentives even when `T > R > P > S` remains true. Do not say that every numerical prisoner's dilemma produces identical repeated-game behavior. The existing `2R > T + S` discussion already gives one reason rankings alone do not settle comparisons across rounds.

This needs a short warning now, not an expected-utility chapter. Also avoid summing different players' utility numbers as an objective welfare measure unless interpersonal comparability is explicitly assumed.

### 5. Make the transition to repetition precise without redoing the memory lesson

For the initial repeated model, specify:

| Keep fixed | Add explicitly |
| --- | --- |
| Same players and action sets | A sequence of rounds |
| Same payoff function in each round | A rule for observing completed rounds |
| Simultaneous choices within each round | A stopping rule or horizon |
| Same stage incentives | A rule for combining stage payoffs |
| | Strategies defined over possible histories |

A standard first model reveals both actions after each round. That is perfect monitoring of past actions, not advance visibility of the opponent's current move. Do not call a simultaneous-move game a perfect-information game just because completed rounds are observed. MIT Lecture 4, slide 2, defines the information distinction; Lecture 5, slides 6–7, states the repeated observation/history setup [S4, S5].

Our existing "add memory" section can remain a teaching step, but its role should be clear: once history-dependent strategies are allowed, subsequent memory restrictions describe what the player retains or can implement. Memory is not automatically learning. Tit for tat can follow a fixed rule without updating that rule or estimating an opponent model.

**An important new contrast:** finite repetition does not force the same outcome for every stage game. The standard finite prisoner's dilemma result depends on its unique stage-game equilibrium. With multiple stage-game equilibria, credible future rewards and punishments can support other earlier behavior in some finitely repeated games. Yale Lecture 21 gives this contrast directly; MIT Lecture 5, slides 8–15, supplies a worked example and the unique-equilibrium result [S5, S6]. Keep this adjacent to the existing finite-horizon caveat, rather than repeat its proof.

### 6. Organize later lessons by what changes

| Extension | What changes | What not to conflate it with |
| --- | --- | --- |
| Bounded memory | Retained information or implementable decision rules | Whether the rules of the game reveal past actions |
| Action errors | Intended action versus executed action | A mistaken observation |
| Imperfect monitoring | Signals about completed play | Unknown preferences/payoffs |
| Learning | Updating estimates or decision rules | Merely executing a fixed history-dependent strategy |
| Tournament or rematching | Opponent selection and scoring across matches | A fixed pair's repeated game |
| Evolutionary dynamics | Population composition under a specified selection rule | An individual learning within a match |
| State-dependent/stochastic game | Environmental transitions and state-dependent opportunities/payoffs | Repeating an unchanged stage game |

This organization is our proposed lesson design, not a theorem or a claim that all game theory must be built from repeated two-action games. Sequential one-shot games and incomplete-information games are also independent directions [S4, S8]. Use the interactive and software resources below for examples of tournament, noise, and population settings, not as authority for a universal winning strategy [S7, S9].

## Annotated source guide

### S1. MIT: a concise formal foundation

Asya Magazinnik, **17.810 Game Theory, Lecture 2: Games in Strategic Form and Nash Equilibrium**, Spring 2021.

[Direct PDF](https://ocw.mit.edu/courses/17-810-game-theory-spring-2021/mit17_810s21_lec2.pdf)

- Start with slides 2 and 7–8 for static complete-information games, the elements of a game, and normal-form notation. Continue to the dominance and Nash equilibrium sections as needed.
- **New value:** an explicit general definition to place before our existing square.
- **Limit:** lecture slides, not a fully self-contained beginner textbook. Their initial identification of actions with strategies belongs to the static setting.
- **Verification:** PDF retrieved; relevant definitions read.

### S2. Bonanno: the best detailed reference for this pass

Giacomo Bonanno, **Game Theory**, third edition, 2024.

[Author-hosted PDF](https://faculty.econ.ucdavis.edu/faculty/bonanno/PDF/GT_book.pdf)

- Section 2.1, p. 19 onward: game frames, preferences, and strategic-form games.
- Section 2.2, p. 26 onward: strict and weak dominance.
- Section 2.6, p. 41 onward: Nash equilibrium; matching pennies on pp. 45–46.
- Section 5.2, especially p. 183: ordinal versus cardinal utility and positive affine transformations.
- Sections 6.1–6.2, pp. 203–210: cardinal strategic-form games and mixed strategies.
- **New value:** separates outcome rankings from lottery comparisons instead of silently treating payoff labels as quantities that can always be averaged.
- **Limit:** long and more formal than our lesson. Free access does not imply unrestricted adaptation; the copyright page restricts commercial use and derivative reuse. Link and explain in our own words rather than copy exercises or figures.
- **Verification:** downloaded PDF, checked its third-edition/2024 title material, and read the relevant passages. Locators refer to this edition.

### S3. Yale: the closest match to the proposed one-shot lesson

Ben Polak, **ECON 159**, Fall 2007.

[Lecture 1: Introduction: Five First Lessons](https://oyc.yale.edu/economics/econ-159/lecture-1) · [Lecture 5: Nash Equilibrium: Bad Fashion and Bank Runs](https://oyc.yale.edu/economics/econ-159/lecture-5)

- Lecture 1's overview explicitly contrasts a prisoner's dilemma with a coordination problem obtained by changing plausible payoffs.
- Lecture 5 covers multiple equilibria, coordination failure, and why communication may help a coordination problem differently from a prisoner's dilemma.
- **New value:** classroom framing for comparing strategic situations before introducing repeated play.
- **Limit:** examples and course material, not empirical evidence that every real-world trust problem has one particular matrix.
- **Verification:** official lecture overviews read; full videos not watched for this pass.

### S4. MIT: representation and information boundaries

Asya Magazinnik, **Lecture 4: Extensive Form Games with Complete Information**, Spring 2021.

[Direct PDF](https://ocw.mit.edu/courses/17-810-game-theory-spring-2021/mit17_810s21_lec4.pdf)

- Slide 2: complete information versus perfect/imperfect information.
- Slides 5 and 10–12: actions versus contingent strategies and conversion from extensive to normal form.
- **New value:** evidence against equating normal form with one-shot timing.
- **Limit:** much of the lecture is beyond the initial lesson; use these passages as author background.
- **Verification:** PDF retrieved; relevant passages read, including the explicit normal-form conversion on slide 12.

### S5. MIT: the precise repeated-game bridge

Asya Magazinnik, **Lecture 5: Repeated Games**, Spring 2021.

[Direct PDF](https://ocw.mit.edu/courses/17-810-game-theory-spring-2021/mit17_810s21_lec5.pdf)

- Slides 6–7: stage game, finite repetition, observed histories, summed payoffs, and contingent strategies.
- Slides 8–15: finite repetition with multiple stage equilibria versus a unique stage equilibrium.
- Slide 22: infinite discounted repetition.
- **New value:** makes "same game, played again" precise and supplies a contrast beyond finite prisoner's dilemma.
- **Limit:** do not turn the slide deck's broad motivation about expanded equilibrium possibilities into a claim that every repeated game gains cooperative equilibria. Its own finite-horizon examples qualify that motivation.
- **Verification:** PDF retrieved; definitions and finite-horizon contrast read.

### S6. Yale: finite repetition beyond prisoner's dilemma

Ben Polak, **Lecture 21: Repeated Games: Cooperation vs. the End Game**, Fall 2007.

[Lecture page](https://oyc.yale.edu/economics/econ-159/lecture-21)

- The official overview explains both finite prisoner's dilemma unraveling and how multiple stage equilibria can provide credible rewards and punishments in other finitely repeated games.
- **New value:** a direct counterexample to overgeneralizing our existing finite prisoner's dilemma result.
- **Limit:** overlaps with the current lesson on grim trigger and uncertain endings. Use selectively.
- **Verification:** official overview read; full video not watched.

### S7. Nicky Case: an interaction-design reference

Nicky Case, **The Evolution of Trust**, July 2017.

[Interactive](https://ncase.me/trust/) · [Text version](https://ncase.me/trust/words)

- The text explicitly separates One Game, Repeated Game, One Tournament, Repeated Tournament, mistakes, and sandbox exploration.
- **New value:** a concrete example of predict-first, play, inspect the result, then change the rules. Particularly useful for distinguishing a repeated match from a tournament and population dynamics.
- **Limit:** its introductory prisoner's dilemma material duplicates ours. Its specific tournament winners depend on its rules and entrants; its social narrative is not a general equilibrium theorem. Its coin-payoff example also differs from ours.
- **Verification:** interactive landing page opened in a browser and text version read. The full interactive was not played through or independently reproduced.

### S8. Osborne and Rubinstein: a formal reading map

Martin J. Osborne and Ariel Rubinstein, **A Course in Game Theory**, MIT Press, 1994.

[Author's table of contents](https://www.economics.utoronto.ca/osborne/cgt/TOC.html) · [Free-download access information](https://books.osborne.economics.utoronto.ca/)

- Section 2.1, p. 11: strategic games; Section 2.2, p. 14: Nash equilibrium.
- Section 6.4, p. 103: interpretation of a strategy.
- Sections 8.1–8.4, pp. 133–142: repeated games, definitions, and strategies as machines; Section 8.10, p. 155: finite repetition.
- Chapter 9, p. 163 onward: complexity considerations in repeated games, useful background for later memory/implementation restrictions.
- **New value:** connects our memory-state picture to a formal literature and shows that strategic form, sequential play, incomplete information, and repetition are separate topics.
- **Limit:** the author-hosted free full-book download requires registration. No account was created. Use Bonanno and MIT for immediately accessible definitions.
- **Verification:** contents and access conditions checked, not the full book. Chapter locators are a reading map, not evidence of a full-text review.

### S9. Axelrod-Python: a later experimental reference

Axelrod project, **Axelrod Python library documentation**, undated living documentation.

[Documentation and quick start](https://axelrod.readthedocs.io/en/stable/)

- Documents head-to-head matches, round-robin tournaments, noisy settings, probabilistic match lengths, and population models.
- Classifies strategies by stochasticity, history use, and dependence on game or match information.
- **New value:** a reference for future experiment settings and for distinguishing strategies by their information requirements.
- **Limit:** focused on iterated prisoner's dilemma, not a general game-theory engine. A tournament ranking is not automatically an equilibrium or a universal superiority result. Documentation examples were not executed in this research pass.
- **Verification:** documentation overview and quick-start page read. No package installed and no simulation results claimed.

## Smallest useful next revision

1. Add a short "What is a strategic game?" introduction, using S1 and S2.
2. Add a one-shot comparison exercise, guided by Yale Lecture 1, with our own small matrices.
3. Introduce best response, Nash equilibrium, and Pareto improvement before asking which strategy wins.
4. Add the one-sentence ordinal/cardinal warning near the existing parameterized matrix.
5. Tighten the transition to repetition using S5, with the stage game/repeated game distinction and explicit observation/scoring rules.
6. Preserve the existing memory examples and process diagram. Organize later topics by the assumption they change.

No simulator, new dependency, lesson rewrite, or publication is needed to use these findings. The highest-priority sources are S1 for the definition, S3 for the comparison lesson, S2 for payoff interpretation, and S5 for repetition.
