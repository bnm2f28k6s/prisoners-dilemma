---
title: "Level 17: adapting the decision rule"
---

# Level 17: adapting the decision rule

[Previous](/levels/16-membership) | [Walkthrough](/) | [Next: choosing rules](/levels/18-rules)

## Change one modeling restriction

**Remove:** the player's explicitly represented policy parameters stay fixed. Let an update procedure change estimates or decision parameters using permitted experience.

**Keep:** the game's outcome rules. Adaptation happens inside a player's controller, not by secretly changing what a payoff cell means.

## Walk through the new possibility

A player starts with cooperation probability p = 0.5. As a deliberately simple teaching rule, after a reported opponent C, increase p by 0.1 up to 1; after a reported D, decrease p by 0.1 down to 0. This is an adaptive heuristic, not a claim of optimal learning.

If its reports are C, C, D, p becomes 0.6, then 0.7, then 0.6. Noisy reports may drive the update even when the actual actions were different. The update can use numerical rewards only if the observation rules deliver them.

```text
controller state = retained observations, estimates, policy parameters
choose using current controller state and current permitted information
update controller state using only delivered experience
```

There is an important boundary: from outside, an entire learning procedure can itself be described as a fixed strategy over histories. This level makes adaptation explicit for explanation and future experiments; it does not enlarge the mathematical strategy space supplied by the history-dependent strategies introduced at Level 1, with randomization added at Level 3.

Bounded memory or limited computation can now be stated as controller constraints. They restrict what a player can implement rather than making the game more general. Evolutionary selection changes population composition and is not the same process as one player updating p.

## Build this version

### Start from the previous version

Keep Level 16's participant initialization, identity-specific memory, matching, and earned-payoff accounting. Replace the example controller, not the game resolver. For this worked trace only, use a fixed two-player C/D encounter, identity execution, and delivered opponent-action reports. Arrivals, private types, and noisy reporting remain selectable options. If arrivals are enabled, initialize each entrant's adaptive state separately.

### Make the change

1. Add `memory[player].p`, initially 0.5, and a record of consumed delivery identifiers. Keep this probability out of `world`: it is a controller parameter, not an environmental stock or payoff coefficient.
2. Choose C when a private controller draw `u` in `[0, 1)` is strictly below the current p, otherwise D. This tutorial's strict comparison makes p=0 always D and p=1 always C. Reject invalid draws and initial probabilities.
3. Freeze the pre-event views and controller parameters for simultaneous choices, then commit actions before resolving and delivering reports. A report from this event cannot affect this event's already chosen action.
4. After delivery, increase p by 0.1 for each newly delivered opponent C and decrease it by 0.1 for D, clamping after each report. Use declared delivery order for batches. No report means no update; replaying the same delivery identifier must not update twice. Read neither actual opponent actions nor evaluator payoffs unless their reports were delivered.

```text
input: memory[p].p, permitted view[p], controller draw u
require 0 <= u < 1 and 0 <= memory[p].p <= 1
joint[p] = C if u < memory[p].p else D
commit all joint actions; resolve unchanged game and update totals
deliver configured reports
for each p, for each new report r in delivery order:
    if r.id already consumed: continue
    if r.opponentAction == C: memory[p].p = min(1, memory[p].p + 0.1)
    if r.opponentAction == D: memory[p].p = max(0, memory[p].p - 0.1)
    mark r.id consumed
result: next decision uses updated p; earned payoffs are unchanged
```

### Check your implementation

- Given initial p=0.5 and distinct delivered reports C, C, D, expect successive probabilities 0.6, 0.7, 0.6. Compare decimal results with appropriate numeric tolerance if needed.
- Given p=0.5 and draw 0.5, expect D. Given p=0.95 and report C, expect 1; given p=0.05 and D, expect 0.
- Given actual D but delivered C, expect an increase. Given no report or a replayed identifier, expect no additional change. Reject draw 1 without committing an action.
- For backward compatibility, disable parameter updates while retaining fixed initial p and the same controller draws. This recovers a fixed randomized controller in Level 16 without altering membership or payoff rules.

**Checkpoint:** Which parameter changes here that does not change in ordinary tit for tat?

**Concept added:** an explicit controller-update rule. Disable parameter updates to recover fixed-policy controllers. Keep learning state separate from world state and from an evaluator's complete history.

Sources: [history, memory, and experimental models](/sources#experiments). The update rule is our example.
