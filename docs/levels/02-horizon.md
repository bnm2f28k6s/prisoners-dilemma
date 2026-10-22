---
title: "Level 2: an uncertain ending"
---

# Level 2: an uncertain ending

[Previous](/levels/01-repetition) | [Walkthrough](/) | [Next: randomized choices](/levels/03-randomization)

## Change one constraint

**Remove:** everybody knows the exact final round. Generalize the stopping rule. For this example, after each completed round the interaction continues with probability `q = 0.75`, independently of play.

**Keep:** the stage game, monitoring, and per-player sum of payoffs. Players know q but do not know which round will be last. There is no additional discounting in this example.

[![The same prisoner's dilemma square: (3, 3), (0, 5), (5, 0), and (1, 1), with unchanged Row and Column axes.](/diagrams/matrix-baseline.svg)](/diagrams/matrix-baseline.svg)

Only the rule deciding whether there is another round changes. Neither the location nor the value of a cell changes.

## Walk through the new possibility

If both always cooperate, the expected number of rounds is `1 / (1 - q) = 4`. Each therefore expects a total payoff of `3 / (1 - q) = 12`. This is an expectation across possible match lengths, not a four-round promise.

Consider cooperation backed by grim trigger. Against a cooperating opponent, cooperating forever gives expected payoff `3 / (1 - q)`. Defecting once and then facing mutual D gives `5 + q / (1 - q)`. The former is at least as good when `q >= 0.5`.

This comparison illustrates a future incentive. It assumes perfect monitoring, the specified response after defection, and the same continuation rule after every outcome. It does not establish that cooperation is inevitable or that every forgiving strategy works.

```text
after resolving and observing a round:
    use the announced stopping rule to decide whether play continues
```

A continuation probability and a discount factor are different concepts. A discount factor changes how a player values later payoffs; a stopping probability changes whether later rounds happen. They can yield similar expected-value formulas under particular assumptions, but should remain separate settings.

**Checkpoint:** If q is zero, is there any future response to deter defection?

**Concept added:** a stopping rule rather than only a fixed round count. Recover Level 1 by choosing its fixed four-round rule. For a never-ending model, separately specify a well-defined criterion such as discounted utility; an undiscounted infinite sum may diverge.

Sources: [repeated games and uncertain horizons](/sources#repetition).
