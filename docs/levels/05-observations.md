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

**Checkpoint:** Can two players leave the same round with different beliefs about it?

**Concept added:** an observation law and delivery times for every information channel, including rewards. Accurate public action reports and the previous payoff visibility recover Level 4. Observing past actions is not advance visibility of a simultaneous current action, nor is it the technical definition of a perfect-information game.

Sources: [information and timing](/sources#information-and-dynamics).
