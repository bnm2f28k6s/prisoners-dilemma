---
title: "Level 0: one simultaneous choice"
---

# Level 0: one simultaneous choice

[Walkthrough](/) | [Next: repeat the game](/levels/01-repetition)

## The starting system

Row and Column each choose **cooperate (C)** or **defect (D)** once. They choose without seeing the other's current choice. Then the interaction ends. Both know the rules and payoff table.

Each cell contains `(Row's payoff, Column's payoff)`. Higher is better for that player.

[![Payoff matrix with Row on the left and Column across the top. The outlined Row C, Column D cell pays Row 0 and Column 5.](/diagrams/matrix-one-shot.svg)](/diagrams/matrix-one-shot.svg)

The visual key stays the same throughout the lessons: **Row is on the left and its payoff comes first; Column is across the top and its payoff comes second.** Row's labels and numbers are blue; Column's are purple. Position and labels carry the meaning even without color. C comes before D on both axes. The outline draws attention to the example named inside the cell, not necessarily a good or optimal choice. Select any diagram to open it full size.

The same values are available as a text table:

| Row's choice | Column chooses C | Column chooses D |
| --- | --- | --- |
| C | (3, 3) | (0, 5) |
| D | (5, 0) | (1, 1) |

A **joint action** is everybody's choice together, such as `(C, D)`. A **payoff function** reads the joint action and returns one player's payoff. The square is a small lookup table for these functions.

```text
players = Row, Column
actions for each = C or D
both choose without seeing the other's choice
look up the joint action in the table
assign each player's payoff
stop
```

## Walk through one outcome

Suppose Row chooses C and Column chooses D. The table gives Row 0 and Column 5. There is no second chance to retaliate, forgive, or build a reputation within this interaction.

Why is this a prisoner's dilemma? If Column chooses C, Row gets 5 by choosing D instead of 3 by choosing C. If Column chooses D, Row gets 1 by choosing D instead of 0 by choosing C. Column has the same incentives. D **strictly dominates** C for each player.

Three different questions now have different answers:

- A **best response** gives the player the highest payoff against the other player's specified choice. Here D is always a best response.
- A **Nash equilibrium** permits no player to improve by changing only their own choice. Here `(D, D)` is the unique equilibrium.
- A **Pareto improvement** makes someone better off without making anyone worse off. Moving from `(D, D)` to `(C, C)` improves both players, but requires both to change.

An equilibrium need not be fair or best for everyone. These are comparisons inside the specified model, not predictions that people must act this way.

## What is fixed?

Two players, two actions each, these known payoffs, simultaneous choices, deterministic execution and resolution, and one interaction. There are no messages or changing environmental conditions.

For this first example we inspect deterministic choices. Randomized decision rules arrive at Level 3. The rules describe what can happen; a decision rule describes what a player chooses to do.

**Checkpoint:** Explain why Row would not improve by switching from D to C when Column chooses D. Then explain why both might still prefer `(C, C)`.

**Concept carried forward:** players, legal actions, joint actions, and player-specific payoffs. A deterministic one-shot game can be summarized as `G = (players, action sets, payoff functions)`.

Sources: [foundations and payoff interpretation](/sources#foundations).
