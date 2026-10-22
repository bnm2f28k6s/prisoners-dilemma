---
title: "Sources and teaching choices"
---

# Sources and teaching choices

[Walkthrough](/) | [Combined conceptual model](/conceptual-model)

The numbered levels and their order are this project's teaching design, not a standard taxonomy. They are not levels of recursive reasoning about other minds. All worked numerical examples and traces are constructed teaching examples, not empirical measurements or reported simulation results.

The existing development research is retained in the repository at `research/strategic-game-foundations.md`. It records source locators, access limitations, and what was actually reviewed. This walkthrough uses that research and adds the official OpenSpiel and PettingZoo concept pages as background for a broader process description. No game library is selected or required.

## Foundations

- Asya Magazinnik, [MIT 17.810 Lecture 2: Games in Strategic Form and Nash Equilibrium](https://ocw.mit.edu/courses/17-810-game-theory-spring-2021/mit17_810s21_lec2.pdf), Spring 2021. Slides 2 and 7-8 introduce the basic game elements; later sections discuss dominance and Nash equilibrium.
- Giacomo Bonanno, [Game Theory, third edition](https://faculty.econ.ucdavis.edu/faculty/bonanno/PDF/GT_book.pdf), 2024. Sections 2.1, 2.2, and 2.6 cover strategic games, dominance, and Nash equilibrium. Section 5.2 and Sections 6.1-6.2 distinguish ordinal utility, lottery comparisons, and mixed strategies. Printed page numbers and access limitations are recorded in the development research. We explain in our own words rather than reproduce the book's figures or exercises.
- Ben Polak, Yale ECON 159, [Lecture 1](https://oyc.yale.edu/economics/econ-159/lecture-1) and [Lecture 5](https://oyc.yale.edu/economics/econ-159/lecture-5), Fall 2007. The official overviews motivate comparisons of prisoner's dilemma, coordination, and multiple equilibria. Full videos were not reviewed for the development research.
- Steven Kuhn, [Prisoner's Dilemma](https://plato.stanford.edu/entries/prisoner-dilemma/), Stanford Encyclopedia of Philosophy. Background for the starting square and the distinction between individual incentives and mutual improvement.

These sources support Levels 0, 3, 6, 7, and 8. The contribution formulas and asymmetric alteration of the starting square are ours.

## Repetition

- Magazinnik, [MIT Lecture 5: Repeated Games](https://ocw.mit.edu/courses/17-810-game-theory-spring-2021/mit17_810s21_lec5.pdf). Slides 6-7 define the stage/repeated-game bridge, histories, and aggregation; slides 8-15 discuss the finite-horizon distinction; slide 22 treats infinite discounted repetition.
- Polak, [Yale Lecture 21: Repeated Games: Cooperation vs. the End Game](https://oyc.yale.edu/economics/econ-159/lecture-21). The official overview contrasts the finite prisoner's dilemma with repeated games having multiple stage equilibria.
- Kuhn, [finite iteration](https://plato.stanford.edu/entries/prisoner-dilemma/#FiniIter) and [indefinite iteration](https://plato.stanford.edu/entries/prisoner-dilemma/#IndeIter).

These support Levels 1 and 2. Our q = 0.75 example and the q >= 0.5 incentive comparison use the specified square and independent continuation rule. They are derived examples, not tournament evidence.

## Information and dynamics

- Magazinnik, [MIT Lecture 4: Extensive Form Games with Complete Information](https://ocw.mit.edu/courses/17-810-game-theory-spring-2021/mit17_810s21_lec4.pdf). Slide 2 separates information concepts; slides 10-12 discuss contingent strategies and normal-form representation. Normal form is a representation, not a synonym for one-shot interaction.
- OpenSpiel, [Concepts](https://openspiel.readthedocs.io/en/latest/concepts.html) and [Introduction](https://openspiel.readthedocs.io/en/latest/intro.html), living documentation. The concept page distinguishes game descriptions from states and trajectories, explains chance nodes, and discusses representing simultaneous moves through turns. The introduction lists supported information, timing, and payoff categories. Both pages were retrieved for this walkthrough.
- PettingZoo, [AEC concepts](https://pettingzoo.farama.org/api/aec/), living documentation. Read for changing turn order, variable agent populations, legal-action masks, and the distinction between parallel choices and sequential updates. These are design references, not a claim that our proposed schema has been implemented or formally proved equivalent to either library.

These inform Levels 5 and 9-16. Sensor, stock, private-cost, and membership examples are ours. Later levels reuse earlier mechanisms; they are not all strictly larger mathematical game classes.

## Experiments

- Nicky Case, [The Evolution of Trust](https://ncase.me/trust/) and its [text version](https://ncase.me/trust/words), 2017. Separates individual games, repeated games, tournaments, population changes, and mistakes. Useful for predict-first teaching design, not universal strategy rankings. The prior research read the text and opened the landing page; it did not reproduce the full interactive.
- Axelrod project, [library documentation](https://axelrod.readthedocs.io/en/stable/), living documentation. Background for matches, noise, history use, tournaments, and population experiments. No package was installed and no library experiments are reported here.

These inform Levels 4, 15, and 17, with the important distinction that following a fixed history-dependent rule is not the same explanation as updating a learned parameter. Level 18's voting/subsidy example and the combined conceptual schema are our proposals. They use state and action concepts rather than assert a new game-theoretic result.
