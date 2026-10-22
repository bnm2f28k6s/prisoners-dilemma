---
title: "Level 6: different incentives"
---

# Level 6: different incentives

[Previous](/levels/05-observations) | [Walkthrough](/) | [Next: more actions](/levels/07-actions)

## Change one constraint

**Remove:** the payoff functions must be the particular symmetric prisoner's dilemma square. Allow a separately specified payoff function for each player.

**Keep:** two players and two actions. Rules and payoff functions are still known to both. Unknown preferences are a later step, not a synonym for unequal payoffs.

## Walk through the new possibility

First compare other symmetric squares. Each entry below gives payoffs for one joint action.

| Example | (C, C) | (C, D) | (D, C) | (D, D) | Pure Nash equilibria of the one-shot stage game |
| --- | --- | --- | --- | --- | --- |
| Prisoner's dilemma | (3, 3) | (0, 5) | (5, 0) | (1, 1) | (D, D) |
| Stag hunt | (4, 4) | (0, 3) | (3, 0) | (2, 2) | (C, C), (D, D) |
| Chicken | (3, 3) | (1, 5) | (5, 1) | (0, 0) | (C, D), (D, C) |
| Harmony | (5, 5) | (2, 3) | (3, 2) | (0, 0) | (C, C) |

These are constructed teaching examples, not a complete classification. The equilibrium column analyzes each square played once. Equilibria of a repeated interaction require separate analysis using its horizon, information, and utility rules. When comparing repeated versions, keep those other settings unchanged and swap only the stage-game square.

Here is the stag-hunt square in the same visual layout. Only its payoff numbers have changed; no cell is outlined because no particular play is being traced.

[![Stag hunt in the same Row/Column layout, with payoffs (4, 4), (0, 3), (3, 0), and (2, 2).](/diagrams/matrix-stag-hunt.svg)](/diagrams/matrix-stag-hunt.svg)

Symmetry can also go. Starting from the prisoner's dilemma, change only Row's payoff at `(C, C)` from 3 to 6. Row now prefers C against C, while Column still prefers D against C. A shared pair of action labels no longer implies shared incentives.

[![The original prisoner's dilemma matrix with only Row's payoff at C/C changed from 3 to 6. The outlined edited cell is (6, 3); all other payoffs are unchanged. The outline marks an edit, not an equilibrium.](/diagrams/matrix-asymmetric.svg)](/diagrams/matrix-asymmetric.svg)

For a symmetric prisoner's dilemma, `(C,C)=(R,R)`, `(C,D)=(S,T)`, `(D,C)=(T,S)`, and `(D,D)=(P,P)`, with `T > R > P > S`. The common additional condition `2R > T + S` makes mutual C better for each than equally alternating the exploiter role. The original numbers satisfy it. General payoff functions need satisfy neither condition.

```text
payoff for player i = that player's function of the joint action
```

**Checkpoint:** In the stag-hunt square, what is Row's best response to C? To D?

**Concept added:** arbitrary player-specific payoff functions. Restore the original square to recover the previous level. Do not add different players' utility numbers into a supposedly objective welfare score without an explicit comparability assumption.

Sources: [foundations and contrasting games](/sources#foundations).
