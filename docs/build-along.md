---
title: "Build along in your own language"
---

# Build along in your own language

[Walkthrough and level map](/) | [Start building at Level 0](/levels/00-one-shot)

Use the lessons to build a small game runner in the language you already know. Start with one paid outcome, then change one part at a time. You do not need a web interface, a game engine, or a learning library. A function that accepts fixed choices and returns their payoffs is enough for Level 0.

Each lesson has a **Build this version** section. It tells you what to keep from the previous implementation, which data and logic to change, and what results to check before moving on. The conceptual explanation and diagram tell you why the change matters. Read both.

The pseudocode is a recipe, not runnable source or an API you must copy. Choose your own function names, modules, types, and test framework. The tutorial supplies implementation choices for its finite examples; it does not specify a production simulator or solve every game it can describe.

## Work through one level

1. Run the checks for the version you already built. Save that working version using whatever version-control workflow you prefer.
2. Read **Start from the previous version**. Keep the existing capabilities, but select the settings named for this example. Some lessons switch back to two players or turn noise off to make one change visible.
3. Follow **Make the change**. Add only the data and behavior needed at this step. Do not build every later option in advance.
4. Turn **Check your implementation** into assertions or repeatable manual checks. Compare returned values and controller inputs, not just printed messages.
5. Select the earlier settings again and rerun the earlier checks. A new feature should not silently change the old game.

You are extending what your runner can express, not accumulating every example's settings into one increasingly noisy match. The contribution game, for example, needs contribution controllers and compatible execution rules. A C/D flip is not automatically meaningful for contribution 2.

## Shared notation

A **map** associates a key with a value, like a dictionary, record, or associative array. Use stable player identities as keys. Display order is a separate choice: when we print a payoff tuple, Row comes before Column.

- `rules` holds legal actions, payoff rules, timing, and information permissions. The runner reads the full rules; controllers receive the announced parts.
- `world` holds authoritative conditions, such as stock and active membership. Resolution logic reads it; players receive only permitted signals.
- `view[player]` holds information delivered to that player by this decision point. Only that player's controller reads this view.
- `memory[player]` holds that controller's retained reports, estimates, or policy parameters.
- `intended[player]` is the action sampled from that player's decision rule. Execution logic reads it; reveal it only as permitted.
- `executed[player]` is what actually happened after execution. Outcome logic reads it; report it only as permitted.
- `totals[player]` holds accumulated actual payoffs. Accounting reads it; reveal it only on the declared schedule.
- `record` is an evaluator's factual account of a resolved event. Tests and evaluation can read it, but players cannot automatically do so.

An evaluator can see that a sensor was wrong. A controller cannot use that fact unless the information rules deliver it. Use copies or read-only snapshots at this boundary so a player cannot discover hidden facts through a shared mutable object. This is an implementation discipline, not a security sandbox for untrusted controller code.

In the pseudocode, `require` means validate and report an error if the condition fails. Validate configuration before starting; validate submitted choices and computed consequences before changing authoritative state, adding payoffs, or delivering reports. Invalid input must not leave a half-paid or half-updated event. A player's committed choice and the runner's committed consequences are different steps.

## Preserve the event order

The first version has one event. Repetition adds a loop; Level 9 makes the schedule explicit. Throughout, preserve these dependencies:

```text
prepare permitted pre-decision views
collect and validate choices from those views
commit all choices in each simultaneous group
apply execution rules
compute and validate actual consequences
commit world changes and earned payoffs; record the event
route only the reports due to each player
update each controller from delivered information
advance the schedule or stop
```

A program can call Row before Column while still modeling simultaneous play. Column simply must not receive Row's current choice. Later sequential events deliberately change that delivery order.

## Make random examples repeatable

For checks, supply a short list of draws instead of relying on a lucky run. The examples use draws in `[0, 1)` and strict comparisons such as `draw < probability`. Test the boundary as well as values on either side.

Keep separate draw sources or separately addressed draws for policy sampling, execution errors, reporting errors, continuation, and environmental chance. Turning execution noise off should not shift every later policy choice. A fixed seed alone does not preserve a trace if adding a feature changes how many draws a shared source consumes.

The examples state when draws are independent. Shared shocks need an explicit joint rule, not accidental reuse of a random number. Report realized outcomes separately from expected values. A computed expected stock of 1 does not mean the transition actually visited stock 1.

## What to keep at the end

Keep a small set of selectable examples and their checks, including the original one-shot and four-round games. Do not delete those examples when later lessons use withdrawals, private costs, or changing partners.

After [Level 18](/levels/18-rules), use the [combined model](/conceptual-model#assemble-your-working-versions) to connect the pieces and audit information flow. The repository's own tests check the authored examples and tutorial coverage. They do not execute your implementation or prove its correctness; run the checks in your own project too.
