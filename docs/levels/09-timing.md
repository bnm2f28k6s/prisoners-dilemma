---
title: "Level 9: who acts when"
---

# Level 9: who acts when

[Previous](/levels/08-players) | [Walkthrough](/) | [Next: messages](/levels/10-messages)

## Change one constraint

**Remove:** every decision happens in one simultaneous group. Introduce a schedule of decision events. An event may ask one player or a group to choose.

**Keep:** the roster, action spaces, payoff rules, and explicit information channels. The schedule must say when choices are committed, resolved, and revealed.

## Walk through the new possibility

Use two players and the original square to isolate timing. Row chooses first, Column observes that action, then Column chooses. Payoffs are assigned after both choices.

Column's strategy now needs a response after Row's C and a response after Row's D. In this square, Column prefers D after either choice, so moving sequentially does not remove the incentive problem. Other payoff functions may give different results.

```text
simultaneous event:
    collect choices without revealing any within-group choice
    resolve only after every required choice is committed

sequential events:
    resolve the first choice
    deliver the signals permitted before the next decision
    ask the next player to choose
```

Asking players one at a time in a program does not by itself make a game sequential in the strategic sense. If later players cannot see earlier choices, it may represent simultaneous play. Conversely, revealing a choice too early changes the game.

**Checkpoint:** What must Column know before its choice for "Row moves first" to matter?

**Concept added:** a decision schedule and information at each decision point. Restore a single simultaneous group each round to recover the previous timing model. A strategy is still a contingent plan, not merely the realized action sequence.

Sources: [extensive-form games and simultaneous-event representations](/sources#information-and-dynamics).
