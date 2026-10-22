---
title: "Level 18: choosing rules within rules"
---

# Level 18: choosing rules within rules

[Previous](/levels/17-adaptation) | [Walkthrough](/) | [Next: the combined conceptual model](/conceptual-model)

## Change one modeling restriction

**Remove:** institutional settings can change only through external configuration. Let a specified decision process change selected settings during play.

**Keep:** explicit rules determining which changes are legal, who decides, when they take effect, and how their effects are observed. Players do not acquire unrestricted power to rewrite the model.

## Walk through the new possibility

Before a contribution phase, two players vote on whether to impose a contribution subsidy of 1 per unit. The subsidy applies only if both vote yes, lasts for the next contribution phase, and is funded by a declared external budget large enough for that phase. Contributions still use the existing action and timing rules.

The payoff rule reads the active subsidy setting. Messages alone cannot enact it. The vote is a material action with a specified consequence, and the budget must be accounted for if it is not intentionally external.

```text
legal rule-selection action
    -> announced decision procedure
    -> updated institutional state
    -> subsequent action, payoff, or matching rules read that state
```

Like adaptation, this can already be represented inside earlier machinery: treat the institution as world state and votes as actions. The new step is exposing a formerly external setting to strategic choice. It is not a theorem that another, unrestricted kind of game has been reached.

**Checkpoint:** Who can change the subsidy, and when does that change affect contributions?

**Concept added:** endogenous institutional settings under fixed higher-level rules. Disable rule-selection actions, or leave one legal institutional setting, to recover Level 17. A model still needs a defined outer rule for interpreting events; "anything may happen" is not a usable specification.

This is the endpoint of this first walkthrough, not a claim to cover every possible strategic situation. The [combined model](/conceptual-model) gathers the independent choices and shows how earlier levels are recovered.
