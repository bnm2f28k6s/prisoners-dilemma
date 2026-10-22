---
title: "Level 13: hidden conditions"
---

# Level 13: hidden conditions

[Previous](/levels/12-chance) | [Walkthrough](/) | [Next: private types](/levels/14-private-types)

## Change one constraint

**Remove:** the environmental state is automatically public. Let the observation law reveal only selected information about it.

**Keep:** the world still has a definite state and evolves under the specified transition law. Hiding information does not change that law.

## Walk through the new possibility

Instead of displaying exact stock, a sensor reports "low" for stock 0, 1, or 2, and "high" for stock 3 or 4. Even an accurate "low" report leaves several possible states.

Legal-action notices can leak information too. With Level 11's withdrawal rule, seeing that withdrawal 1 is legal rules out stocks 0 and 1. A "low" signal plus that notice would identify stock 2 exactly. The model must include both channels, rather than pretending the sensor is the player's only clue.

```text
actual state -> transition and outcome rules
permitted signals and legal-action notices -> player's information
retained information -> optional belief about possible states
```

A **belief state** is a player's assessment of hidden possibilities, not the actual state. A Bayesian update needs an initial belief and a likelihood model; the conceptual framework need not require every player to update that way.

**Checkpoint:** Could two different stocks produce the same information before a decision? List every channel, not just the named sensor.

**Concept added:** partial observation of persistent state. This reuses Level 5's observation mechanism for the environmental state introduced later. Reveal that state fully to recover Level 12. A fixed latest observation need not contain everything useful in the player's previous signals.

Sources: [imperfect information and player information states](/sources#information-and-dynamics).
