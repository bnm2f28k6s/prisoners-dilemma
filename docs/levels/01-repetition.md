---
title: "Level 1: play again"
---

# Level 1: play again

[Previous](/levels/00-one-shot) | [Walkthrough](/) | [Next: an uncertain ending](/levels/02-horizon)

## Change one constraint

**Remove:** the interaction must stop after one play. Play the same stage game for four rounds instead.

**Keep:** the same pair, C/D actions, payoff table, simultaneous choices within each round, and error-free execution. To make repetition precise, both players see the completed joint action and their own stage payoff after each round, know the four-round horizon, and add their own stage payoffs.

Those observation and scoring conventions are necessary parts of the repeated model, not extra strategic mechanisms. **The stage game stays constant; the repeated game is a new, larger game.** [MIT's repeated-game lecture](/sources#repetition) makes this distinction explicit.

## Walk through the new possibility

A move is a choice now. A **strategy** is a rule for choosing at every possible decision history, including histories that do not occur in the example.

| Strategy | First choice | Later choices |
| --- | --- | --- |
| Always cooperate | C | C |
| Always defect | D | D |
| Tit for tat | C | Copy the opponent's previous executed action |
| Grim trigger | C | D forever after any observed opponent D; otherwise C |

Row uses tit for tat; Column always defects.

[![The unchanged payoff matrix is followed by four rounds: C/D, then D/D three times. Stage payoffs are (0, 5), then (1, 1) three times; the match totals are (3, 8).](/diagrams/matrix-repeated.svg)](/diagrams/matrix-repeated.svg)

The square has not moved or changed its values. The strip underneath shows which cell is visited each round; it is a trace of the match, not a new payoff matrix.

| Round | Joint action | Stage payoffs |
| --- | --- | --- |
| 1 | (C, D) | (0, 5) |
| 2 | (D, D) | (1, 1) |
| 3 | (D, D) | (1, 1) |
| 4 | (D, D) | (1, 1) |
| Total | | (3, 8) |

These strategies are stipulated, not claimed to be optimal for four rounds. Tit for tat responds to the first defection, but does not beat always defect in this match.

```text
repeat for four rounds:
    each player chooses using only information already available
    resolve both choices together using the unchanged square
    add each player's payoff to that player's running score
    reveal completed actions and update retained information
```

Repetition makes responses to past behavior possible. It does not guarantee cooperation. With a commonly known finite horizon and common knowledge of rational payoff maximization, backward induction gives defection throughout this prisoner's dilemma. Do not generalize that result to every stage game; multiple stage equilibria can change the argument.

## Memory is a representation choice

Tit for tat needs one previous opponent action. Grim trigger needs one flag, not an unlimited transcript. A fixed strategy that reads history is not automatically learning. Limiting memory is an optional restriction on the player, not the next step toward a more general game.

## Build this version

### Start from the previous version

Keep Level 0's simultaneous-choice collection, action validation, and payoff lookup. Wrap that resolver in a match runner instead of copying its table into a new implementation. The match runner owns duration, accumulated payoffs, and information carried between rounds.

### Make the change

1. Add a fixed `round_limit = 4`, `totals[player] = 0`, and initially empty `memory[player]`. Initialize them once per match, not once per round. Keep stage payoffs separate from totals.
2. Change the decision rule to accept `view[player]` and `memory[player]`. For tit for tat, return C when there is no previous opponent action; otherwise return that action. Always defect still returns D for every input.
3. After both actions resolve, add each payoff to its own total. Deliver the completed joint action and each player's own payoff. Only then update each player's memory. Neither decision in round 2 may see the other's round-2 action.
4. Stop after the fourth paid round. A new match resets both totals and controller memory.

```text
initialize totals to zero and memory to empty for each player
for round in 1 through round_limit:
    choices = collect legal choices from current views and memories
    payoffs, record = resolve together using Level 0's payoff table
    for player in players:
        totals[player] = totals[player] + payoffs[player]
        view[player] = completed actions and that player's payoff
    update each memory from that player's delivered view
return totals
```

Do not hand the evaluator's full match log to a decision rule. This level permits the completed actions, but later levels will restrict reports. A separate delivery step lets you change that permission without rewriting strategies.

### Check your implementation

- With Row tit for tat and Column always defect, expect joint actions `(C, D), (D, D), (D, D), (D, D)` and totals `(3, 8)`.
- With two tit-for-tat rules, expect four `(C, C)` outcomes and totals `(12, 12)`. Restart the match after a defection and verify tit for tat opens with C again.
- Set `round_limit = 1`. Every fixed-action pair must return Level 0's payoffs, with exactly one resolution and no second decision call. Reject a non-positive or non-integer limit before play for this finite runner.

**Checkpoint:** If both use tit for tat, what happens in all four rounds? What is each total?

**Concept added:** a horizon, a payoff aggregation rule, observations of completed play, and history-dependent strategies. Recover Level 0 by setting the horizon to one.
