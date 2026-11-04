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

## Build this version

### Start from the previous version

Keep Level 1's round resolver, payoff sum, deliveries, and memory updates. Replace only the fixed loop's stopping decision. Preserve the fixed-four-round option so existing tests still run without randomness.

### Make the change

1. Put duration behind a rule with two options: stop after N completed rounds, or continue with probability q after each completed round. The first round always happens in the random-continuation example.
2. Validate `0 <= q < 1` for this terminating, undiscounted runner. A never-ending model requires a different utility criterion; do not accept q = 1 and silently impose a round cap.
3. Supply a random-number source that your tests can replace with a fixed sequence. Draw a value `u` in `[0, 1)` only after resolution, payoff accounting, delivery, and memory update. Continue exactly when `u < q`. Keep this source separate from future policy or error draws.

```text
completed = 0
repeat:
    play, score, deliver, and update one round as in Level 1
    completed = completed + 1
    if duration is fixed:
        if completed == round_limit: stop
    otherwise:
        u = next continuation draw in [0, 1)
        if u >= q: stop
```

Each run returns its actual round count and actual totals. Compute expectations separately. An optional operational safety limit should report an incomplete run rather than claim that the game's stopping event occurred.

### Check your implementation

- Set q to 0.75 and feed continuation draws `0.20, 0.60, 0.90`. Expect three paid rounds. Two always-cooperate rules receive totals `(9, 9)`, not the expected totals `(12, 12)`.
- Set q to zero. Expect one paid round even when the first draw is zero. At q = 0.75, a draw of exactly 0.75 stops; it does not continue.
- Check the expectation separately: `1 / (1 - 0.75) = 4` rounds and `3 * 4 = 12` per always-cooperating player. A particular run need not have those values.
- Select fixed duration 4. Expect exactly Level 1's traces and totals, with no continuation draws consumed. Reject q below zero or q = 1 in this runner.

**Checkpoint:** If q is zero, is there any future response to deter defection?

**Concept added:** a stopping rule rather than only a fixed round count. Recover Level 1 by choosing its fixed four-round rule. For a never-ending model, separately specify a well-defined criterion such as discounted utility; an undiscounted infinite sum may diverge.

Sources: [repeated games and uncertain horizons](/sources#repetition).
