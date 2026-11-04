---
title: "Level 5: imperfect reports"
---

# Level 5: imperfect reports

[Previous](/levels/04-execution) | [Walkthrough](/) | [Next: different incentives](/levels/06-payoffs)

## Change one constraint

**Remove:** everybody receives an accurate public report of completed actions. Replace it with a signal rule that can be noisy, private, delayed, or silent.

**Keep:** the actual executed actions still determine payoffs. The observer's report does not rewrite what happened.

## Walk through the new possibility

Both execute C, so the actual payoff pair is `(3, 3)`. Row's report incorrectly says Column played D. Column correctly sees Row's C. Tit for tat would next tell Row to defect while Column cooperates.

To isolate this mechanism, set execution error to zero. Earlier extensions remain available; we need not switch all of them on in every example.

A model must also state what players see about payoffs. If Row immediately sees its exact stage payoff of 3 in this particular square, it can infer Column's C despite the false action report. For this example, neither player receives its numerical payoff until the interaction ends. Intermediate decisions use action reports only. An evaluator may record true payoffs without revealing them to players.

[![Actual actions C/C give actual payoffs (3, 3). Row incorrectly hears Column D; Column correctly hears Row C. Actual payoffs are withheld from players until the interaction ends.](/diagrams/matrix-observations.svg)](/diagrams/matrix-observations.svg)

This is the reader's view of what actually happened, not information automatically available to either player. A false report does not move the actual outcome to another cell.

```text
completed event -> actual payoffs and event record
completed event -> separate permitted signal for each player
player's next decision uses its signal history, not the evaluator's record
```

## Build this version

### Start from the previous version

Keep Level 4's intention, execution, and actual-payoff records. Replace the accurate delivery step, not the resolver. The example below uses zero execution error and two fixed rounds so you can isolate a false report and its effect on the next choice.

### Make the change

1. Define a signal rule per recipient. It takes the completed event and creates only that player's permitted report. For this example, the round-1 report to Row says opponent D while the report to Column says opponent C.
2. Separate `record`, the evaluator's actual event, from `view[player]`, the player's delivered information. Never pass the record, actual totals, or a mutable reference to either into a controller.
3. Keep actual payoffs in `totals[player]`, but queue numerical payoff deliveries until the match ends. Both players know their own actions; intermediate views contain the opponent action report, not a true joint-action object.
4. Update tit for tat from the delivered report. Give queued deliveries an event identifier and a due time so each arrives once. For this example, a missing action report leaves the last retained opponent report unchanged; with none yet, tit for tat opens with C. This is a tutorial convention, not a universal response to silence.

```text
record = resolve executed actions and compute actual payoffs
add actual payoffs to evaluator totals
for player in players:
    report = signal rule(record, recipient = player)
    deliver report without numerical payoff to view[player]
    queue that player's numerical payoff for match end
    update memory[player] using only delivered reports
at match end: deliver queued own payoffs once
```

### Check your implementation

- Resolve C/C. Expect evaluator payoffs `(3, 3)`, Row's opponent report D, and Column's opponent report C. With tit for tat, the next intended pair is `(D, C)`, even though the actual first outcome was C/C.
- Inspect the inputs to both controllers before round 2. Neither may contain numerical payoffs, actual totals, true opponent actions, or the other player's private report. Checking only the displayed sensor label is insufficient.
- Deliver no report and verify the declared memory behavior. At termination, verify each queued own reward arrives exactly once and never before an intermediate decision.
- Restore accurate action reports and immediate own-payoff delivery. With the same intentions and execution inputs, expect Level 4's views, memory updates, and outcomes again.

**Checkpoint:** Can two players leave the same round with different beliefs about it?

**Concept added:** an observation law and delivery times for every information channel, including rewards. Accurate public action reports and the previous payoff visibility recover Level 4. Observing past actions is not advance visibility of a simultaneous current action, nor is it the technical definition of a perfect-information game.

Sources: [information and timing](/sources#information-and-dynamics).
