---
title: "Putting the levels together"
---

# Putting the levels together

[Previous: Level 18](/levels/18-rules) | [Walkthrough](/) | [Sources](/sources)

The result is a configurable description of an interaction, not a simulator design or a universal solution method. Earlier games become special settings of this description. Many later choices are independent, so a model need not switch on every extension.

## Four things to keep separate

| Part | What it describes | Examples |
| --- | --- | --- |
| Rules | What may happen and who can know it | Legal choices, event order, transition and observation laws |
| World | What is actually the case now | Stock, active participants, private types, institutional settings |
| Controllers | How players choose and update retained information | Tit for tat, beliefs, learning parameters, memory limits |
| Evaluation | What a specified comparison measures | Each player's utility, cooperation frequency, resource survival |

A player's utility criterion belongs to the game being analyzed. An external report can measure something else, but must not silently replace that utility or leak evaluator-only information to players. A tournament score is not automatically a player's strategic objective.

## The conceptual settings

These are descriptive slots, not proposed classes, data types, or library interfaces.

| Setting | Questions that must be answered | Introduced or exposed at |
| --- | --- | --- |
| Participants and identities | Who exists? Which identities persist across encounters? | 0, 8, 16 |
| Legal actions | What may each participant choose at this point? | 0, 7, 11 |
| Outcomes and payoffs | How does a resolved event affect each participant? Are utilities comparable only within a player? | 0, 6 |
| Duration | Fixed horizon, stochastic stopping, terminal condition, or an infinite model? | 1, 2 |
| Utility over time | Sum, discounted stream, average criterion, terminal utility, or another explicitly defined preference? | 1, 2 |
| Decision rule | What distribution over legal choices follows from a player's permitted information and controller state? | 1, 3 |
| Execution | How do intended actions become executed actions? | 4 |
| Information | Which signals, payoffs, legal-action notices, and identities does each player learn, and when? | 1, 5, 13 |
| Schedule | Who acts together? Which events resolve before the next decision? | 9 |
| Communication | Who sends what to whom, at what time and cost, with what binding effect? | 10 |
| Environment | What persists, and how do actions affect it? | 11 |
| Chance | What distributions govern initial conditions and subsequent outcomes? Which random effects are correlated? | 2, 3, 4, 5, 12 |
| Private parameters | Which types affect incentives or capabilities? What do players initially know or believe? | 14 |
| Interaction structure | Which groups meet, which relationships are possible, and what resets? | 15 |
| Membership | When do players arrive or depart, and how are their information and utilities initialized or settled? | 16 |
| Controller update | What is retained, forgotten, estimated, or adapted after permitted experience? | 1, 17 |
| Institutional choices | Which rule settings may players change under which outer rules? | 18 |
| Comparison protocol | Which controllers, initial conditions, repetitions, and metrics are being compared? | Separate experiment specification |

A sum over a finite match is straightforward. Infinite-horizon criteria require conditions under which utility exists. A reported average, an expected discounted utility, and one realized score answer different questions.

## A process in conceptual pseudocode

An **event** is the next specified decision, chance, delivery, membership, or settlement point. Events need not be evenly spaced rounds. The following order is a way to state dependencies, not a mandated software architecture.

```text
specify the rules, player utility criteria, controllers, and comparison protocol
initialize world, identities, private types, and each player's permitted information
deliver initial signals and initialize controller state

while the model has not reached its declared stopping condition:
    identify the next event under the current schedule

    if the event asks players to choose:
        identify the acting group and its legal choices
        deliver only information permitted before these choices
        each acting player chooses using its own information and controller state
        commit all choices in a simultaneous group before revealing any of them
        apply the specified execution law to obtain executed actions

    resolve the event under its announced outcome law
        this may include chance, world changes, membership changes,
        institutional changes, or payoffs to players who did not act

    record actual consequences for evaluation
    deliver only the signals due now to their permitted recipients
    update each controller using only information that player has received
    advance the schedule and apply the declared continuation/termination rules

apply any terminal consequences and due information deliveries
summarize each player's utility and the separately chosen evaluation metrics
```

For models that never terminate, interpret this as a process description and define the infinite-horizon criterion mathematically. A finite computational cutoff would be an experiment approximation, not a silently substituted terminal rule.

Separate boxes do not imply independent random draws. Execution, transitions, and reports can be defined by one joint event law when they share a shock. Similarly, a delivery event may arrive between action events rather than only at the end of a round.

## Recover the simple systems

### Level 0 again

Choose two permanent players; give each C/D; install the original square; make one simultaneous event; use identity execution; assign actual payoffs; stop. Disable messages, rematching, arrivals, learning, and institutional choice. The environmental state is constant and there are no private types. No prior history is needed.

### Level 1 again

Keep that square and permanent pair, schedule four simultaneous rounds, reveal each completed joint action and stage payoffs, and sum each player's payoffs. Allow a history-dependent controller such as tit for tat. There is no environmental change or error.

### A richer composed example

Choose a fixed roster of three contributors, known cost parameters, a publicly observed resource stock, independent replenishment chance, simultaneous withdrawals under a fully specified feasible-action rule, and a known finite horizon. Compare fixed decision rules without messages, private types, rematching, learning, or rule voting.

This uses only selected later capabilities. To add private sensors, edit the information rule; do not accidentally edit the true stock transition. To add learning, edit the controller update; do not silently change the payoff function.

## How to inspect any proposed extension

1. Name the constraint being relaxed, or say honestly that the step only exposes an already representable mechanism.
2. Identify the single setting or law that changes. Hold other settings fixed for the comparison.
3. Work through one possible event trace. Distinguish it from a probability-weighted expectation.
4. Check all information channels for unintended revelations.
5. Explain how the earlier model is recovered, and whether the new example actually contains it or merely illustrates the same pattern.
6. Keep behavioral predictions separate from the rules and from the chosen controller examples.

## Where this draft stops

A useful broad description is a partially observed, possibly stochastic multi-agent process with explicit decisions, information, utilities, and controller updates. That is a description of our target, not a proof of a unique maximal model.

General description does not guarantee an equilibrium exists, a best strategy is computable, learning converges, or a model represents a real situation accurately. This draft does not establish a continuous-time model, handle every infinite action/state space, or formalize unawareness and unknown possible rules. Hidden facts inside an announced model are not the same as players being unaware of which possibilities exist.

Coalitions and binding contracts need explicit feasible agreements and enforcement consequences. They are not supplied merely by labeling a message "binding". Endogenous rules still require an outer interpretation. More named configuration slots alone do not solve these problems.

The point of the ladder is to expose assumptions gradually and make them independently selectable, not to assert that every situation is a prisoner's dilemma with extra options.
