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

## Build this version

### Start from the previous version

Keep Level 8's identity-keyed actions, payoff maps, and validation. Replace the assumption that one round always asks the whole roster to act together. Add an ordered schedule of events. To isolate timing here, select two players, C/D, the original table, and identity execution. The three-player contribution setup remains a separate selectable example.

### Make the change

1. Give each event an acting group, legal actions, due information deliveries, and a resolution rule. Maintain a pending action map for a stage that spans several events. Clear it before starting a new stage.
2. For simultaneous play, collect every group member's choice from pre-event views. Commit all choices, then resolve, then deliver. Later function-call order must not create extra information.
3. For the sequential example, schedule a Row-choice event, a delivery of Row's executed choice to Column, and a Column-choice event. Row's first event stores its executed action but does not yet award a stage payoff.
4. After Column acts, combine both executed actions, apply the table once, and run the existing accounting and observation steps. Validate the schedule so a missing action or duplicate stage resolution cannot silently produce a score.

```text
pending = empty map
Row event: collect and execute Row's choice; store it in pending
delivery event: put Row's executed choice in Column's view
Column event: collect and execute Column's choice; store it in pending
require pending contains exactly Row and Column
resolve the original table once using pending
score, deliver the completed result, and clear pending
```

Column's rule now needs behavior after either Row C or Row D. It can also ignore the information and always defect. Knowing that a first move occurred is not the same as observing its value.

### Check your implementation

- Fix Row to C and use Column's best response D. Expect one final payoff `(0, 5)`, with no payoff awarded after Row's event alone.
- Use a Column test rule that copies a visible Row action and otherwise chooses C. With Row D, the observed sequential schedule produces D/D and `(1, 1)`. A simultaneous schedule must hide Row's current action and produce D/C and `(5, 0)` under that test rule.
- Reject a schedule that tries to resolve before Column acts or resolves the same stage twice. Ensure pending actions are empty at the next stage's start.
- Restore one simultaneous event for the entire roster and Level 8's contribution settings. Expect the same identity-keyed payoffs and pre-event controller inputs as before.

**Checkpoint:** What must Column know before its choice for "Row moves first" to matter?

**Concept added:** a decision schedule and information at each decision point. Restore a single simultaneous group each round to recover the previous timing model. A strategy is still a contingent plan, not merely the realized action sequence.

Sources: [extensive-form games and simultaneous-event representations](/sources#information-and-dynamics).
