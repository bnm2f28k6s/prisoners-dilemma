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

## Build this version

### Start from the previous version

Keep Level 15's matching validation, identity-keyed totals, partner memory, and pairwise outcome delivery. Add membership events before matching; do not change the completed encounter resolver. For this example only, use the known C/D square and an exogenous departure of B followed by entry of E. Private types, voluntary exit, and reputation inheritance remain optional and inactive.

### Make the change

1. Separate the historical identity registry from `world.active`. Keep departed identities' totals and evaluator records. Choose never-reused identities for this tutorial: E is not a renamed B.
2. Define an atomic membership event between completed encounters, after their due reports and before the next matching. Validate all departures and arrivals first. Reject an inactive departure, an identity already used, or a player listed for both operations.
3. Our boundary choices are zero departure payment, no later earnings for departed players, and no pending delayed messages across this boundary. If delayed delivery is enabled elsewhere, require an explicit recipient/settlement policy rather than discarding messages silently.
4. Initialize E's total to zero, controller memory empty, known payoff parameters, and permitted initial information before eligibility for matching. Deliver the updated public roster so A recognizes E as new. Retain A's historical memory of B but never copy it into A's entry for E.

```text
input: completed-event world, departures, arrivals, registry, totals
require no unresolved encounters or pending deliveries
validate membership batch without changing state
for each p in departures:
    totals[p] += 0
    remove p from world.active
for each fresh p in arrivals:
    add p to registry and world.active
    totals[p] = 0
    memory[p] = empty controller state
    initialize permitted view[p] and announced parameters
record membership change for evaluator
deliver updated recognized roster to active players
pairs = select and validate matching using world.active
result: settled departed identities and initialized eligible arrivals
```

An odd roster is allowed here: the matching rule may leave a player unmatched with zero event payoff. Presence does not guarantee a turn.

### Check your implementation

- Given A cooperated against defecting B, expect totals A=0 and B=5. After B exits and E enters, expect B still 5, E=0, and B ineligible for the next pair.
- When A first meets E, expect fresh-partner C rather than B-specific retaliation. E must receive initial rules before choosing.
- Given another arrival named B, reject identity reuse without removing E or changing totals. Given an unresolved encounter, reject the membership event rather than removing an actor midway through resolution.
- For backward compatibility, configure empty arrival and departure lists. The same schedule must reproduce Level 15's groups, observations, memory, and totals.

**Checkpoint:** Which pieces must be initialized before E can make its first informed choice?

**Concept added:** participant lifecycles and identity persistence. A membership rule with no arrivals or departures recovers Level 15. Population evolution needs further declared selection and reproduction rules; it is not implied merely by a changing roster.

Sources: [variable-agent environments](/sources#information-and-dynamics). The entry/settlement conventions are our design requirements.
