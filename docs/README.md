---
title: From one choice to a general interaction
---

# From one choice to a general interaction

Start with two people making one simultaneous choice. Then remove one constraint at a time. Let them meet again, face an uncertain ending, make mistakes, receive different information, and eventually act in a changing world with other participants.

This is an initial conceptual walkthrough, not a simulator or an implementation specification. The aim is to understand which assumptions a general system would need to expose. We do not assume that every situation is a prisoner's dilemma, or that a more complicated strategy is better.

**[Start at Level 0: one simultaneous choice](/levels/00-one-shot).** Each page links to the next.

## How to read the levels

Each step names what changes, what stays fixed, a small example, and the concept we carry forward. It also explains how to recover the earlier model. Some examples temporarily turn earlier extensions off to isolate the new one; the earlier capabilities remain available.

The order is a teaching route through independent choices, not a standard hierarchy. Imperfect information can exist in a one-shot game; many players need not imply noise. Later steps such as messages, hidden state, adaptation, and institutional choice expose uses of machinery already introduced. They are not all strictly larger mathematical classes.

For the first steps we keep the same payoff square so the transition is easy to see. Once we relax its assumptions, other games become possible.

## The route

| Level | Constraint we relax or mechanism we expose | New concept |
| --- | --- | --- |
| [0. One simultaneous choice](/levels/00-one-shot) | Starting point: two players, two actions, one known square | Players, choices, joint outcomes, payoffs |
| [1. Play again](/levels/01-repetition) | Only one play is allowed | Repetition, histories, strategies, aggregation |
| [2. An uncertain ending](/levels/02-horizon) | The final round is known in advance | General stopping rule |
| [3. Randomized choices](/levels/03-randomization) | A decision rule selects an action with certainty | Distributions over intended choices |
| [4. Intended and executed actions](/levels/04-execution) | Choices always execute correctly | Execution law |
| [5. Imperfect reports](/levels/05-observations) | Completed play is accurately reported to everyone | Private or noisy signals and delivery times |
| [6. Different incentives](/levels/06-payoffs) | The payoff square must be our symmetric dilemma | Player-specific payoff functions |
| [7. More than two actions](/levels/07-actions) | Every player has only C/D | General action spaces |
| [8. More than two players](/levels/08-players) | Exactly two players participate | Joint actions and payoff vectors for a group |
| [9. Who acts when](/levels/09-timing) | Everyone always decides simultaneously | Decision events and schedules |
| [10. Messages before choices](/levels/10-messages) | Players cannot deliberately communicate | Message channels and non-binding signals |
| [11. A persistent environment](/levels/11-state) | The same environmental conditions recur | World state and deterministic transitions |
| [12. Environmental chance](/levels/12-chance) | The environmental successor is deterministic | Transition distributions |
| [13. Hidden conditions](/levels/13-hidden-state) | Environmental state is automatically public | Partial state information and beliefs |
| [14. Private types](/levels/14-private-types) | Everyone knows others' incentive parameters | Private types and priors |
| [15. Changing partners](/levels/15-matching) | The same group always interacts | Matching, networks, identity-specific memory |
| [16. Entry and exit](/levels/16-membership) | The roster never changes | Participant lifecycles |
| [17. Adapting the decision rule](/levels/17-adaptation) | Explicit policy parameters stay fixed | Controller updates and learning state |
| [18. Choosing rules within rules](/levels/18-rules) | Institutional settings are only externally selected | Strategic rule selection under outer rules |

## Where this leads

The [combined conceptual model](/conceptual-model) gathers the settings into one description and an event-based pseudocode process. It separates the rules, actual world, player controllers, and evaluation. It also shows how to recover the one-shot and repeated examples, rather than leaving them behind.

There is no claim that this endpoint covers every conceivable situation or supplies a universal winning strategy. Infinite spaces, continuous time, enforceable agreements, and unawareness need further treatment. The goal here is a clear first route from a small game to a broadly configurable interaction model.

See [sources and teaching choices](/sources) for the research behind the foundations and the boundary between established concepts and our proposed sequence.
