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

## Build this version

### Start from the previous version

Keep Level 5's choice, execution, accounting, and delivery steps. Replace the hard-coded payoff table with a supplied payoff rule. For the comparisons here, use one round and zero execution error. Keep information permissions unchanged unless you explicitly choose a different observation setting.

### Make the change

1. Let the resolver receive a payoff table or function as part of `rules`. For every legal joint action, it must return one finite payoff for each player. Validate table coverage at setup; validate function results before committing an event.
2. Preserve player identity when mapping returned values. Do not compute Column's payoff by swapping Row's inputs unless the supplied game explicitly has that symmetry.
3. Leave policy and observation rules outside the payoff function. The payoff function reads executed actions and returns consequences; it does not ask the players to choose again.
4. If you add the optional pure-equilibrium checker, enumerate legal joint actions. For each player, try every unilateral deviation while holding everyone else's action fixed. Mark the original joint action as an equilibrium only if no deviation gives that player a strictly higher payoff.

```text
payoffs = rules.payoff(executed)
require exactly one finite payoff for every participant
record actual payoffs and apply existing delivery permissions

for each legal joint action:
    keep it as a pure equilibrium only if, for every player,
        no legal change of that player's action raises its payoff
```

The checker analyzes the one-shot stage game only. It does not solve the repeated game merely because the match runner can repeat this resolver.

### Check your implementation

- Swap in stag hunt. Row's best responses should be C against C and D against D; the pure equilibria should be C/C and D/D. Check the other authored tables too: chicken has C/D and D/C, harmony has C/C, and the original dilemma has D/D.
- Apply only the asymmetric edit `(C, C) -> (6, 3)`. Expect the other three payoff pairs to stay unchanged. Row now prefers C against C; Column still prefers D against C. This catches an accidental mirrored edit.
- Reject a table missing C/D or returning only Row's payoff before totals or deliveries change.
- Reinstall the original table. All Level 5 traces, reports, and actual payoffs must match with the same inputs. No controller or execution change is needed.

**Checkpoint:** In the stag-hunt square, what is Row's best response to C? To D?

**Concept added:** arbitrary player-specific payoff functions. Restore the original square to recover the previous level. Do not add different players' utility numbers into a supposedly objective welfare score without an explicit comparability assumption.

Sources: [foundations and contrasting games](/sources#foundations).
