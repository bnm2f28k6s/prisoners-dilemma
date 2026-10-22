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

**Checkpoint:** Which parameter changes here that does not change in ordinary tit for tat?

**Concept added:** an explicit controller-update rule. Disable parameter updates to recover fixed-policy controllers. Keep learning state separate from world state and from an evaluator's complete history.

Sources: [history, memory, and experimental models](/sources#experiments). The update rule is our example.
