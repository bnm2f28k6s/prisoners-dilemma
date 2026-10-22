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

**Checkpoint:** What extra rule would make a promise binding rather than merely a message?

**Concept added:** deliberate signals as a distinguishable action phase. A silent channel, or a single available empty message, recovers the prior model. This uses Level 7's action spaces and Level 9's schedule; it is a newly exposed modeling choice, not a new mathematical universe.

Sources: [coordination and information](/sources#foundations).
