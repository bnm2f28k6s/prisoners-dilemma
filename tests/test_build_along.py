"""Check tutorial coverage and authored examples, not a reader's game runner."""

from fractions import Fraction
from itertools import product
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'


def level(number):
    paths = list((DOCS / 'levels').glob(f'{number:02d}-*.md'))
    if len(paths) != 1:
        raise AssertionError(f'Expected one authored page for Level {number}')
    return paths[0].read_text()


def pair(value):
    return tuple(int(part.strip()) for part in value.split(','))


def matched(pattern, text, flags=0):
    result = re.search(pattern, text, flags)
    if result is None:
        raise AssertionError(f'Authored example no longer matches {pattern!r}')
    return result


def stage_table():
    rows = re.findall(r'^\| ([CD]) \| \(([-\d, ]+)\) \| \(([-\d, ]+)\) \|$',
                      level(0), re.MULTILINE)
    return {(row, col): pair(value) for row, c, d in rows
            for col, value in [('C', c), ('D', d)]}


def contribution(actions, costs=None):
    costs = costs if costs is not None else [3] * len(actions)
    benefit = 2 * sum(actions)
    return tuple(benefit - cost * action for cost, action in zip(costs, actions))


class BuildAlongTest(unittest.TestCase):
    def test_level_inventory_and_navigation_match_authored_route(self):
        home = (DOCS / 'README.md').read_text()
        route = re.findall(r'^\| \[(\d+)\. [^\]]+\]\((/levels/[^)]+)\)', home, re.MULTILINE)
        self.assertTrue(route)
        numbers = [int(number) for number, _ in route]
        self.assertEqual(numbers, list(range(len(route))))
        paths = [url + '.md' for _, url in route]
        actual = sorted('/levels/' + p.name for p in (DOCS / 'levels').glob('[0-9][0-9]-*.md'))
        self.assertEqual(paths, actual)
        config = (ROOT / 'doctave.yaml').read_text()
        configured = re.findall(r'path: docs(/levels/[^\s]+\.md)', config)
        self.assertEqual(configured, paths)
        for index, (_, url) in enumerate(route):
            text = (DOCS / (url.lstrip('/') + '.md')).read_text()
            nav = text.split('\n')[6]
            with self.subTest(url=url):
                self.assertIn('[Walkthrough](/)', nav)
                self.assertIn(route[index + 1][1] if index + 1 < len(route)
                              else '/conceptual-model', nav)
                if index:
                    self.assertIn(route[index - 1][1], nav)

    def test_every_level_has_an_actionable_build_step(self):
        for path in sorted((DOCS / 'levels').glob('[0-9][0-9]-*.md')):
            text = path.read_text()
            with self.subTest(page=path.name):
                self.assertEqual(text.count('## Build this version'), 1)
                build = text.split('## Build this version\n', 1)[1].split('**Checkpoint:**', 1)[0]
                headings = re.findall(r'^### (.+)$', build, re.MULTILINE)
                self.assertEqual(headings, ['Start from the previous version',
                                            'Make the change', 'Check your implementation'])
                change, checks = build.split('### Make the change', 1)[1].split(
                    '### Check your implementation', 1)
                self.assertRegex(change, r'(?m)^1\. ')
                self.assertIn('```text\n', change)
                self.assertGreaterEqual(len(re.findall(r'^- ', checks, re.MULTILINE)), 3)
                self.assertRegex(checks.lower(), r'recover|restore|disable|previous|level [0-9]|baseline')
                self.assertEqual(text.count('```') % 2, 0)

    def test_shared_guide_and_assembly_are_discoverable(self):
        guide = (DOCS / 'build-along.md').read_text()
        for token in ['view[player]', 'memory[player]', 'record', 'totals[player]',
                      'world', 'rules', 'not runnable source', 'fixed seed']:
            self.assertIn(token, guide)
        for name in ['README.md', 'levels/README.md', 'conceptual-model.md']:
            self.assertIn('(/build-along)', (DOCS / name).read_text())
        self.assertIn('path: docs/build-along.md', (ROOT / 'doctave.yaml').read_text())
        self.assertIn('## Assemble your working versions', (DOCS / 'conceptual-model.md').read_text())

    def test_one_shot_expected_results_match_authored_table(self):
        table = stage_table()
        self.assertEqual(len(table), 4)
        checks = re.findall(r'\(([CD]), ([CD])\) -> \(([-\d, ]+)\)', level(0))
        self.assertEqual(len(checks), len(table))
        for row, col, expected in checks:
            self.assertEqual(table[(row, col)], pair(expected))

    def test_repetition_trace_and_totals(self):
        table = stage_table()
        rows = re.findall(r'^\| [1-4] \| \(([CD]), ([CD])\) \| \(([-\d, ]+)\) \|$',
                          level(1), re.MULTILINE)
        self.assertEqual(len(rows), 4)
        for row, col, expected in rows:
            self.assertEqual(table[(row, col)], pair(expected))
        totals = tuple(sum(table[(row, col)][i] for row, col, _ in rows) for i in range(2))
        authored = matched(r'^\| Total \| \| \(([-\d, ]+)\) \|$', level(1), re.MULTILINE)
        self.assertEqual(totals, pair(authored.group(1)))
        self.assertIn(f'totals `{totals}`', level(1))
        self.assertEqual(tuple(4 * value for value in table[('C', 'C')]), (12, 12))

    def test_continuation_fixture_and_expectation(self):
        text = level(2)
        q = Fraction(matched(r'q = (\d+(?:\.\d+)?)', text).group(1))
        draws = matched(r'continuation draws `([\d., ]+)`', text).group(1)
        completed = 0
        for draw in map(Fraction, draws.split(', ')):
            completed += 1
            if draw >= q:
                break
        self.assertEqual(completed, 3)
        actual = tuple(completed * payoff for payoff in stage_table()[('C', 'C')])
        self.assertIn(f'totals `{actual}`', text)
        expected_rounds = 1 / (1 - q)
        self.assertEqual(expected_rounds, 4)
        self.assertEqual(expected_rounds * stage_table()[('C', 'C')][0], 12)
        self.assertFalse(Fraction(0) < 0)
        self.assertFalse(q < q)

    def test_mixed_policy_expected_values_and_boundaries(self):
        text = level(3)
        p = Fraction(matched(r'Row chooses C with probability (\d+(?:\.\d+)?)', text).group(1))
        table = stage_table()
        expected = tuple(p * table[('C', 'C')][i] + (1 - p) * table[('D', 'C')][i]
                         for i in range(2))
        self.assertIn(f'`({float(expected[0])}, {float(expected[1])})`', text)
        self.assertEqual(['C' if draw < p else 'D' for draw in map(Fraction, ['0.20', '0.90', '0.75'])],
                         ['C', 'D', 'D'])
        self.assertEqual(sum(Fraction(1, 4) for _ in product('CD', repeat=2)), 1)

    def test_execution_trace_preserves_intentions(self):
        rows = re.findall(r'^\| [1-4] \| \(([CD]), ([CD])\) \| \(([CD]), ([CD])\) \|$',
                          level(4), re.MULTILINE)
        self.assertEqual(len(rows), 4)
        previous = None
        for index, (ri, ci, re_, ce) in enumerate(rows):
            intended = ('C', 'C') if previous is None else (previous[1], previous[0])
            self.assertEqual((ri, ci), intended)
            self.assertEqual((re_, ce), ('D', 'C') if index == 0 else intended)
            previous = (re_, ce)
        self.assertEqual(stage_table()[('D', 'C')], (5, 0))
        self.assertIn('execution draws to Row 0.05 and Column 0.50', level(4))
        self.assertEqual([draw < Fraction('0.1') for draw in map(Fraction, ['0.05', '0.50', '0.1'])],
                         [True, False, False])

    def test_false_report_does_not_change_actual_payoff(self):
        self.assertEqual(stage_table()[('C', 'C')], (3, 3))
        self.assertIn("Row's opponent report D", level(5))
        self.assertIn("Column's opponent report C", level(5))
        self.assertIn('next intended pair is `(D, C)`', level(5))
        self.assertIn('queue numerical payoff deliveries until the match ends', level(5))

    def test_stage_equilibria_from_authored_payoff_tables(self):
        rows = re.findall(r'^\| (Prisoner\'s dilemma|Stag hunt|Chicken|Harmony) \| (.+)$',
                          level(6), re.MULTILINE)
        self.assertEqual(len(rows), 4)
        actions = list(product('CD', repeat=2))
        for name, values in rows:
            columns = values.split('|')
            payoffs = [pair(matched(r'\(([-\d, ]+)\)', column).group(1)) for column in columns[:4]]
            table = dict(zip(actions, payoffs))
            equilibria = {a for a in actions if all(
                all(table[a][i] >= table[tuple(action if j == i else a[j] for j in range(2))][i]
                    for action in 'CD') for i in range(2))}
            declared = set(re.findall(r'\(([CD]), ([CD])\)', columns[4]))
            with self.subTest(game=name):
                self.assertEqual(equilibria, declared)
        edited = dict(stage_table())
        edited[('C', 'C')] = (6, 3)
        self.assertGreater(edited[('C', 'C')][0], edited[('D', 'C')][0])
        self.assertGreater(edited[('C', 'D')][1], edited[('C', 'C')][1])

    def test_all_authored_contribution_cells(self):
        for number in [7, 8]:
            rows = re.findall(r'^\| ([012]) \| (.+)$', level(number), re.MULTILINE)
            self.assertEqual(len(rows), 3)
            for x, values in rows:
                tuples = re.findall(r'\(([-\d, ]+)\)', values)
                self.assertEqual(len(tuples), 3)
                for y, expected in enumerate(tuples):
                    actions = [int(x), y] + ([0] if number == 8 else [])
                    self.assertEqual(contribution(actions), pair(expected))
        for actions, result in [([2, 1, 0], (0, 3, 6)), ([2, 1, 1], (2, 5, 5)),
                                ([2, 2, 2], (6, 6, 6))]:
            self.assertEqual(contribution(actions), result)
            self.assertIn(str(result), level(8))
        self.assertEqual(len(list(product(range(3), repeat=3))), 27)

    def test_sequential_and_simultaneous_fixture(self):
        table = stage_table()
        copy_visible_or_c = lambda visible: visible if visible is not None else 'C'
        sequential = ('D', copy_visible_or_c('D'))
        simultaneous = ('D', copy_visible_or_c(None))
        self.assertEqual(table[sequential], (1, 1))
        self.assertEqual(table[simultaneous], (5, 0))
        text = level(9)
        self.assertIn('produces D/D and `(1, 1)`', text)
        self.assertIn('produce D/C and `(5, 0)`', text)

    def test_message_does_not_override_material_action(self):
        text = level(10)
        expected = pair(matched(r'expect earned payoffs `\(([-\d, ]+)\)`', text).group(1))
        self.assertEqual(stage_table()[('D', 'C')], expected)
        self.assertLess(text.index('deliver message to rules.recipients'),
                        text.index('before = copy permitted views after delivery'))
        self.assertIn('Messages cost zero and have no enforcement effect', text)

    def test_deterministic_stock_fixtures(self):
        text = level(11)
        stock = int(matched(r'world.stock = (\d+)', text).group(1))
        totals = [0, 0]
        trace = []
        for _ in range(2):
            legal = {0, 1} if stock >= 2 else {0}
            self.assertIn(1, legal)
            stock -= 2
            totals = [value + 1 for value in totals]
            trace.append(stock)
        authored_stocks = tuple(map(int, matched(r'expect stocks (\d+) then (\d+)', text).groups()))
        self.assertEqual(tuple(trace), authored_stocks)
        expected_totals = pair(matched(r'cumulative totals `\(([-\d, ]+)\)`', text).group(1))
        self.assertEqual(tuple(totals), expected_totals)
        self.assertEqual({0, 1} if 1 >= 2 else {0}, {0})

    def test_environmental_branches_cap_and_point_mass(self):
        text = level(12)
        probability = Fraction(matched(r'probability (\d+\.\d+)', text).group(1))
        amount = int(matched(r'add (\d+) units', text).group(1))
        capacity = int(matched(r'Cap the stock at (\d+)', text).group(1))
        def successor(stock, actions, draw, probability=probability):
            replenishment = amount if draw < probability else 0
            return min(capacity, stock - sum(actions) + replenishment)
        fixtures = matched(r'when `u = ([\d.]+)`, expect successor (\d+); when `u = ([\d.]+)`, '
                           r'expect successor (\d+)', text).groups()
        for draw, expected in [fixtures[:2], fixtures[2:]]:
            self.assertEqual(successor(2, [1, 1], Fraction(draw)), int(expected))
        self.assertEqual(successor(4, [0, 0], Fraction(0)), capacity)
        self.assertEqual(probability * 2 + (1 - probability) * 0, 1)
        for stock in range(capacity + 1):
            legal = [0, 1] if stock >= 2 else [0]
            for actions in product(legal, repeat=2):
                self.assertEqual(successor(stock, actions, Fraction(0), probability=Fraction(0)), stock - sum(actions))

    def test_hidden_stock_view_includes_legal_notice(self):
        text = level(13)
        self.assertIn('one common uniform prior over stocks 0 through 4', text)
        self.assertIn('exclude exact stock, replenishment draw, and evaluator `record`', text)
        views = {stock: ('low' if stock <= 2 else 'high',
                         (0, 1) if stock >= 2 else (0,)) for stock in range(5)}
        self.assertEqual(views[0], views[1])
        self.assertNotEqual(views[1], views[2])
        self.assertEqual([s for s, view in views.items() if view == views[2]], [2])
        self.assertEqual(views[3], views[4])
        self.assertIn('this combination identifies 2', text)

    def test_private_cost_fixture_and_own_reward_disclosure(self):
        text = level(14)
        choices = pair(matched(r'Given contributions `\(([-\d, ]+)\)`', text).group(1))
        expected = matched(r'expect payoffs `\(([-\d, ]+)\)` for cost-1 Row and '
                           r'`\(([-\d, ]+)\)` for cost-3 Row', text).groups()
        self.assertEqual(contribution(choices, [1, 3]), pair(expected[0]))
        self.assertEqual(contribution(choices, [3, 3]), pair(expected[1]))
        self.assertEqual(1 if Fraction('0.5') < Fraction('0.5') else 3, 3)
        self.assertIn("never the opponent's payoff or hidden cost", text)

    def test_partner_memory_and_departed_totals_are_distinct(self):
        earned = stage_table()[('C', 'D')]
        memory = {'A': {'B': 'D'}}
        totals = {'A': earned[0], 'B': earned[1]}
        self.assertEqual(memory['A'].get('C', 'C'), 'C')
        self.assertEqual(memory['A'].get('B', 'C'), 'D')
        active = {'A', 'B'}
        active.remove('B')
        active.add('E')
        totals['E'] = 0
        self.assertEqual(totals, {'A': 0, 'B': 5, 'E': 0})
        self.assertNotIn('B', active)
        self.assertEqual(memory['A'].get('E', 'C'), 'C')
        self.assertIn('A=0 and B=5', level(16))
        self.assertIn('B still 5, E=0', level(16))
        self.assertIn('expect A to choose C despite remembering B', level(15))

    def test_adaptive_updates_use_deliveries_once_and_clamp(self):
        text = level(17)
        p = Fraction(matched(r'initial p=(\d+\.\d+)', text).group(1))
        seen = set()
        trajectory = []
        for identifier, report in [(1, 'C'), (2, 'C'), (3, 'D'), (3, 'D')]:
            if identifier not in seen:
                p = min(1, p + Fraction('0.1')) if report == 'C' else max(0, p - Fraction('0.1'))
                seen.add(identifier)
            trajectory.append(p)
        declared = matched(r'expect successive probabilities ([\d., ]+)\.', text).group(1)
        self.assertEqual(trajectory[:3], list(map(Fraction, declared.split(', '))))
        self.assertEqual(trajectory[3], trajectory[2])
        self.assertEqual(min(1, Fraction('0.95') + Fraction('0.1')), 1)
        self.assertEqual(max(0, Fraction('0.05') - Fraction('0.1')), 0)
        self.assertIn('Given actual D but delivered C, expect an increase', text)

    def test_subsidy_payoffs_budget_and_fresh_contribution_views(self):
        text = level(18)
        for actions, subsidy, expected, spending in [((2, 2), 1, (4, 4), 4),
                                                    ((2, 2), 0, (2, 2), 0),
                                                    ((2, 0), 0, (-2, 4), 0),
                                                    ((2, 0), 1, (0, 4), 2)]:
            base = contribution(actions)
            actual = tuple(base[i] + subsidy * actions[i] for i in range(2))
            self.assertEqual(actual, expected)
            self.assertEqual(subsidy * sum(actions), spending)
            self.assertIn(str(expected), text)
            self.assertLessEqual(spending, 4)
        self.assertLess(text.index('deliver adopted setting to both players'),
                        text.index('beforeContribution = copy permitted views after setting delivery'))
        self.assertIn('world.subsidy = 0; world.subsidyPhase = none', text)


if __name__ == '__main__':
    unittest.main()
