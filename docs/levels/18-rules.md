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

## Build this version

### Start from the previous version

Keep Level 17's controller boundaries, permitted deliveries, and commit-before-resolution ordering. Add a rule-selection event, not controller permission to edit rules. Select two fixed contributors with contributions `{0, 1, 2}`, benefit coefficient 2, known cost 3 each, and identity execution. Disable C/D-specific adaptation; learning remains optional with a contribution-appropriate update.

### Make the change

1. Keep the outer procedure in `rules`. Store `world.subsidy` and its target contribution-phase identifier in world state. Each cycle has a simultaneous vote, public result delivery, then exactly one simultaneous contribution phase.
2. Give each player legal votes `{yes, no}`. Require one valid vote from each identity; missing votes are errors, not implicit consent. Set subsidy to 1 only for unanimous yes, otherwise 0. Voting itself has zero payoff. Messages cannot set this field.
3. Our tutorial reserves 4 external units per phase, the maximum subsidy for two contributions of 2. Validate before voting. Deduct actual spending from that reserve and release unused units afterward; never subtract it from player payoffs or carry it into another phase.
4. Deliver the adopted setting before contribution choices. Resolve committed contributions using the setting tagged for this phase, then expire it immediately, before the next vote. Rejected contribution input must not pay, spend, or expire the subsidy.

```text
input: phase id k, rules, world, totals, permitted views
require external reserve for k >= 4
beforeVote = copy permitted views
votes = choose from beforeVote[p] with legal[p] = {yes, no}
validate identity-keyed votes; commit all votes
world.subsidy = 1 if every votes[p] == yes else 0
world.subsidyPhase = k
deliver adopted setting to both players
beforeContribution = copy permitted views after setting delivery
joint = choose from beforeContribution[p] with legal[p] = {0, 1, 2}
validate and commit joint; require world.subsidyPhase == k
for each p:
    payoff[p] = 2 * sum(joint.values) - 3 * joint[p]
                + world.subsidy * joint[p]
    totals[p] += payoff[p]
spend world.subsidy * sum(joint.values) from reserve k
record votes, contributions, payoffs, spending for evaluator
world.subsidy = 0; world.subsidyPhase = none
release unused reserve; deliver configured results and expiry
result: one subsidized or unsubsidized phase, settled and expired
```

### Check your implementation

- Given unanimous yes and contributions `(2, 2)`, expect payoffs `(4, 4)` and spending 4. After expiry, the same contributions without adoption earn `(2, 2)` and spend zero.
- Given votes `(yes, no)` and contributions `(2, 0)`, expect `(-2, 4)` and zero spending; unanimous yes instead gives `(0, 4)` and spending 2.
- Reject a missing vote, contribution 3, or reserve below 4 without partial settlement. A later phase must not reuse the expired setting.
- For backward compatibility, disable voting and fix subsidy at zero. The selected contribution resolver and fixed controllers then work as in Level 17's configurable setup.

**Checkpoint:** Who can change the subsidy, and when does that change affect contributions?

**Concept added:** endogenous institutional settings under fixed higher-level rules. Disable rule-selection actions, or leave one legal institutional setting, to recover Level 17. A model still needs a defined outer rule for interpreting events; "anything may happen" is not a usable specification.

This is the endpoint of this first walkthrough, not a claim to cover every possible strategic situation. The [combined model](/conceptual-model) gathers the independent choices and shows how earlier levels are recovered.
