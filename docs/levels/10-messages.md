---
title: "Level 10: messages before choices"
---

# Level 10: messages before choices

[Previous](/levels/09-timing) | [Walkthrough](/) | [Next: a persistent environment](/levels/11-state)

## Change one constraint

**Remove:** players cannot deliberately communicate. Add a message channel, using the decision schedule to deliver messages before specified action choices.

**Keep:** the existing material actions and payoff rules. In this example messages are public, costless, and non-binding. They cannot directly force another player's action or change the payoff table.

## Walk through the new possibility

Row announces "I will cooperate". Column receives the message. Both then choose simultaneously in the original one-shot square.

If Column chooses C, Row still receives 5 by choosing D instead of 3 by choosing C. The message alone has not removed the temptation. It can influence beliefs or decision rules, but it is not an enforceable contract.

In a coordination game such as the stag-hunt example, messages may help players select compatible actions. Communication does not have the same strategic role in every payoff structure.

```text
message decision -> delivery rule -> recipients' information
material-action decision -> ordinary execution and payoff rules
```

Specify who can send, what they can send, recipients, delivery times, costs, and whether reports can be false. A public random recommendation could be another signal mechanism, but would need an explicitly specified source and distribution.

## Build this version

### Start from the previous version

Keep Level 9's event schedule, identity-keyed legal-action maps, committed choices, execution, and payoff resolver. Insert a communication event rather than attaching promises to the payoff calculation. For this example only, select the original two-player C/D square, identity execution, and simultaneous material choices. Retain other scheduling options without enabling them here. The following names are tutorial pseudocode, not an existing simulator interface.

### Make the change

1. Add explicit `rules` for sender Row, recipients Row and Column, and the finite message choices `silence` and `promise C`. Messages cost zero and have no enforcement effect.
2. Schedule one message decision and delivery before the material decision. Choose silence as a real delivered value, not a missing event. Reject unrecognized messages before changing state.
3. Put the delivered message in each recipient's `view[player]`. Keep any retained interpretation in `memory[player]`. Never let the material resolver read the promise as an instruction to replace an action.
4. Freeze both material views after delivery. Commit both material actions before execution or outcome delivery. If you later add simultaneous senders, likewise commit all messages before delivering any.

```text
input: rules, view, memory, totals
message = choose(Row, view[Row], memory[Row], messageLegal[Row])
require message in messageLegal[Row]
commit message
deliver message to rules.recipients
before = copy permitted views after delivery
joint = {p: choose(p, before[p], memory[p], legal[p]) for p in players}
validate and commit joint
result = resolve original square using joint
totals[p] += result.payoff[p] for each p
record actual message, joint, result for evaluator
deliver only configured outcome reports; update memory from deliveries
result: totals and permitted information updated; payoff rule unchanged
```

### Check your implementation

- Given Row's delivered `promise C`, when Row chooses D and Column C, expect earned payoffs `(5, 0)`, not cooperation or a penalty.
- Given a recipient outside the declared set, expect no message in that player's view. Given an unknown message token, expect rejection without a payoff or partial delivery.
- Given a controller that ignores messages, changing `promise C` to `silence` must not change its material choice. A controller may instead respond to the delivered message, but not to an uncommitted choice.
- For backward compatibility, allow only `silence` and omit its display. The same scripted material decisions must recover Level 9's outcomes and timing.

**Checkpoint:** What extra rule would make a promise binding rather than merely a message?

**Concept added:** deliberate signals as a distinguishable action phase. A silent channel, or a single available empty message, recovers the prior model. This uses Level 7's action spaces and Level 9's schedule; it is a newly exposed modeling choice, not a new mathematical universe.

Sources: [coordination and information](/sources#foundations).
