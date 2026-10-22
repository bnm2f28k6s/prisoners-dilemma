---
title: "Level 16: entry and exit"
---

# Level 16: entry and exit

[Previous](/levels/15-matching) | [Walkthrough](/) | [Next: adaptation](/levels/17-adaptation)

## Change one constraint

**Remove:** the roster is constant. Let participants enter or leave under an explicit membership rule.

**Keep:** the selected interaction and matching rules. Being present, being matched, and being scheduled to act are distinct conditions.

## Walk through the new possibility

A and B have completed an encounter. B exits, and a new player E enters before the next matching event. E needs legal actions, a type or known parameters, initial information, initial controller memory, and an evaluation record. Decide whether A recognizes E as new.

B's departure does not erase B's past payoff. State whether B's utility ends at departure, includes a terminal payment, or depends on later consequences. If E is a replacement identity for B, that must be explicit; otherwise identity resets can accidentally make reputation costless to escape.

```text
at the declared membership event:
    settle the specified consequences for departures
    remove departures from future eligible groups
    initialize arrivals under the announced entry rules
    then select the next interacting groups
```

This example makes membership exogenous. Allowing a player to choose exit is also possible: give it a legal exit action and specify the resulting consequences.

**Checkpoint:** Which pieces must be initialized before E can make its first informed choice?

**Concept added:** participant lifecycles and identity persistence. A membership rule with no arrivals or departures recovers Level 15. Population evolution needs further declared selection and reproduction rules; it is not implied merely by a changing roster.

Sources: [variable-agent environments](/sources#information-and-dynamics). The entry/settlement conventions are our design requirements.
