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

## Build this version

### Start from the previous version

Keep Level 14's stable identities, permitted-information routing, and separation of payoff truth from beliefs. Add group selection around the existing event resolver. For this example only, select the original C/D square, four permanent identities A through D, known payoff parameters, and no private types or stock. Keep those other game options configurable rather than treating rematching as a demand to use them all.

### Make the change

1. Add a fixed roster and a schedule of disjoint pairs to `rules`: first `(A, B), (C, D)`, then `(A, C), (B, D)`. For each pair, the first identity takes the square's Row role; payoffs are written back by identity, never by roster position.
2. Validate the whole matching before any decisions. This tutorial permits each identity at most once per simultaneous matching; reject self-pairs, absent identities, and overlaps. Unmatched players neither act nor earn a stage payoff.
3. Deliver the recognized partner identity. Store tit-for-tat history under `memory[player].lastReport[partner]`. Missing history means choose C; a report from B must not become the default action against C.
4. Freeze views for all pairs and commit all their actions before resolving any pair. Route completed action reports only within the corresponding pair, then update partner-indexed memory. Totals persist across pairings; do not reset them with encounter memory.

```text
input: roster, scheduled pairs, view, memory, totals
validate pairs are disjoint eligible identities
for each pair (a, b):
    deliver partner identities and legal[p] = {C, D}
before = copy all permitted views
for each acting p:
    q = delivered partner in before[p]
    joint[p] = memory[p].lastReport[q] if present else C
commit all identity-keyed joint actions
for each pair (a, b):
    payoff = originalSquare(joint[a], joint[b])
    add payoff components to totals[a], totals[b]
    record pair, joint, payoff for evaluator
deliver configured pair reports; update lastReport by partner identity
result: accumulated identity totals and relationship-specific memory
```

### Check your implementation

- Given A chooses C and B D, expect A to earn 0 and B 5. When A next meets previously unseen C, expect A to choose C despite remembering B's D.
- Given A later meets B again with no intervening B report, expect A to choose D. A fresh pairing must not erase that memory.
- Given pairings `(A, B), (A, C)`, reject the matching before either pair earns anything. Pair outsiders must not receive one another's private reports.
- For backward compatibility, choose the same two identities at every event and retain the previous material game and information settings. This recovers the fixed-group implementation from Level 14.

**Checkpoint:** Why might a rule that works in a long fixed pairing fail when every partner is new?

**Concept added:** interaction structure, identities, and memory across encounters. A constant group containing the entire roster recovers the previous model. Match scores and tournament rankings are different summaries; neither automatically identifies an equilibrium or universal winner.

Sources: [matches, tournaments, and population experiments](/sources#experiments).
