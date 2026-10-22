---
title: "Level 15: changing partners"
---

# Level 15: changing partners

[Previous](/levels/14-private-types) | [Walkthrough](/) | [Next: entry and exit](/levels/16-membership)

## Change one constraint

**Remove:** the same group always interacts together. Add a rule selecting partners or groups from a fixed roster.

**Keep:** every selected interaction has explicit action, payoff, timing, and observation rules. Nobody enters or leaves the roster yet.

## Walk through the new possibility

A, B, C, and D are registered. One schedule pairs A with B and C with D, then A with C and B with D. Use the original C/D square separately in each pair.

Suppose B defects against A in the first pairing. When A meets C, does tit for tat start with C, copy B's last action, or retrieve a previous memory specific to C? Those are different strategies. Here the rule is to keep separate memory by partner and start new pairings with C.

```text
matching rule selects interacting groups
resolve each group under its specified game
route observations to their permitted recipients
update memory using the declared identity and reset rules
```

A network can restrict which partners are reachable. If one player is in multiple simultaneous interactions, state whether it makes a separate choice per relationship or one shared choice, and how resource conflicts are resolved. A round-robin tournament also needs an explicit schedule, reset policy, and comparison metric.

**Checkpoint:** Why might a rule that works in a long fixed pairing fail when every partner is new?

**Concept added:** interaction structure, identities, and memory across encounters. A constant group containing the entire roster recovers the previous model. Match scores and tournament rankings are different summaries; neither automatically identifies an equilibrium or universal winner.

Sources: [matches, tournaments, and population experiments](/sources#experiments).
