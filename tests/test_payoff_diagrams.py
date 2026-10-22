"""Keep static lesson diagrams numerically correct and visually consistent."""

import importlib.util
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('diagrams', ROOT / 'scripts/render-payoff-diagrams.py')
assert SPEC is not None and SPEC.loader is not None
diagrams = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(diagrams)
NS = {'s': 'http://www.w3.org/2000/svg'}


def tree(name):
    return ET.fromstring(diagrams.render(name, diagrams.DIAGRAMS[name]))


def cells(svg):
    return {tuple(map(int, node.attrib['data-cell'].split(','))): node
            for node in svg.findall('.//s:g[@data-cell]', NS)}


def cell_payoffs(svg):
    return {position: tuple(int(node.text) for node in cell.findall('.//s:tspan[@data-player]', NS))
            for position, cell in cells(svg).items()}


def cell_rectangles(svg):
    return {position: tuple(float(cell.find('s:rect', NS).attrib[key])
                            for key in ('x', 'y', 'width', 'height'))
            for position, cell in cells(svg).items()}


def plain(svg):
    return ' '.join(svg.itertext())


class PayoffDiagramsTest(unittest.TestCase):
    def test_generated_assets_are_current(self):
        expected = {name + '.svg' for name in diagrams.DIAGRAMS}
        self.assertEqual({p.name for p in diagrams.OUTPUT.glob('*.svg')}, expected)
        for name, spec in diagrams.DIAGRAMS.items():
            with self.subTest(name=name):
                self.assertEqual((diagrams.OUTPUT / (name + '.svg')).read_text(), diagrams.render(name, spec))

    def test_early_extensions_keep_identical_matrix(self):
        baseline = tree('matrix-baseline')
        expected = {(0, 0): (3, 3), (0, 1): (0, 5), (1, 0): (5, 0), (1, 1): (1, 1)}
        for name in ('matrix-baseline', 'matrix-one-shot', 'matrix-repeated', 'matrix-randomized',
                     'matrix-execution', 'matrix-observations'):
            with self.subTest(name=name):
                svg = tree(name)
                self.assertEqual(cell_payoffs(svg), expected)
                self.assertEqual(cell_rectangles(svg), cell_rectangles(baseline))

    def test_role_order_colors_and_axes_stay_fixed(self):
        for name in diagrams.DIAGRAMS:
            with self.subTest(name=name):
                svg = tree(name)
                texts = {node.text: node for node in svg.findall('.//s:text', NS)}
                for label, color, x, y in (('ROW ↓', diagrams.ROW_COLOR, '28', '144'),
                                           ('COLUMN →', diagrams.COLUMN_COLOR, '448', '100')):
                    self.assertEqual(texts[label].attrib['fill'], color)
                    self.assertEqual((texts[label].attrib['x'], texts[label].attrib['y']), (x, y))
                for cell in cells(svg).values():
                    values = cell.findall('.//s:tspan[@data-player]', NS)
                    self.assertEqual([node.attrib['data-player'] for node in values],
                                     [str(i) for i in range(len(values))])
                    self.assertEqual([node.attrib['fill'] for node in values],
                                     [diagrams.ROW_COLOR, diagrams.COLUMN_COLOR, diagrams.THIRD_COLOR][:len(values)])
                self.assertIn('Row first', texts)
                self.assertIn('Column second', texts)

    def test_payoff_changes_are_exactly_the_declared_changes(self):
        self.assertEqual(cell_payoffs(tree('matrix-stag-hunt')),
                         {(0, 0): (4, 4), (0, 1): (0, 3), (1, 0): (3, 0), (1, 1): (2, 2)})
        asymmetric = cell_payoffs(tree('matrix-asymmetric'))
        baseline = cell_payoffs(tree('matrix-baseline'))
        changes = {cell: value for cell, value in asymmetric.items() if value != baseline[cell]}
        self.assertEqual(changes, {(0, 0): (6, 3)})
        self.assertIn('not a chosen outcome or an equilibrium', plain(tree('matrix-asymmetric')))

    def test_expanded_actions_and_three_player_slice(self):
        two = cell_payoffs(tree('matrix-contributions'))
        three = cell_payoffs(tree('matrix-three-player-slice'))
        self.assertEqual(len(two), 9)
        self.assertEqual(len(three), 9)
        for (x, y), payoff in two.items():
            self.assertEqual(payoff, (2 * (x + y) - 3 * x, 2 * (x + y) - 3 * y))
            self.assertEqual(three[(x, y)], payoff + (2 * (x + y),))
        self.assertEqual(two[(2, 1)], (0, 3))
        self.assertEqual(three[(2, 1)], (0, 3, 6))
        self.assertIn('not the full three-player game', plain(tree('matrix-three-player-slice')))
        # Expanded matrices retain the same outer drawing area as the 2x2 matrix.
        for name in ('matrix-baseline', 'matrix-contributions', 'matrix-three-player-slice'):
            rects = cell_rectangles(tree(name)).values()
            self.assertAlmostEqual(min(r[0] for r in rects), 168)
            self.assertAlmostEqual(min(r[1] for r in rects), 160)
            self.assertAlmostEqual(max(r[0] + r[2] for r in rects), 728, places=2)
            self.assertAlmostEqual(max(r[1] + r[3] for r in rects), 400, places=2)

    def test_contribution_text_tables_match_diagrams(self):
        for level, name in (('07-actions.md', 'matrix-contributions'),
                            ('08-players.md', 'matrix-three-player-slice')):
            text = (ROOT / 'docs/levels' / level).read_text()
            rows = [line for line in text.splitlines() if re.match(r'^\| [012] \|', line)]
            self.assertEqual(len(rows), 3)
            actual = cell_payoffs(tree(name))
            for row_index, line in enumerate(rows):
                tuples = re.findall(r'\(([-\d, ]+)\)', line)
                self.assertEqual(len(tuples), 3)
                for column_index, value in enumerate(tuples):
                    self.assertEqual(tuple(map(int, value.split(','))), actual[(row_index, column_index)])

    def test_round_trace_and_focused_outcomes(self):
        rounds = diagrams.DIAGRAMS['matrix-repeated']['rounds']
        expected = (('C', 'D'), ('D', 'D'), ('D', 'D'), ('D', 'D'))
        self.assertEqual(rounds, expected)
        stage = {('C', 'C'): (3, 3), ('C', 'D'): (0, 5), ('D', 'C'): (5, 0), ('D', 'D'): (1, 1)}
        self.assertEqual(tuple(sum(stage[a][i] for a in rounds) for i in (0, 1)), (3, 8))
        self.assertIn('Match totals: Row 3, Column 8', plain(tree('matrix-repeated')))
        self.assertEqual(diagrams.DIAGRAMS['matrix-execution']['focus'], {(1, 0): 'executed outcome'})
        self.assertEqual(diagrams.DIAGRAMS['matrix-observations']['focus'], {(0, 0): 'actual outcome'})
        self.assertIn('withheld from players until the end', plain(tree('matrix-observations')))
        self.assertEqual(diagrams.DIAGRAMS['matrix-randomized']['focus'],
                         {(0, 0): '75% chance', (1, 0): '25% chance'})

    def test_svg_accessibility_and_no_external_or_active_content(self):
        for name in diagrams.DIAGRAMS:
            with self.subTest(name=name):
                svg = tree(name)
                self.assertEqual(svg.attrib['role'], 'img')
                self.assertEqual(svg.attrib['aria-labelledby'], 'title description')
                self.assertTrue(svg.findtext('s:title', namespaces=NS))
                self.assertTrue(svg.findtext('s:desc', namespaces=NS))
                for element in svg.iter():
                    self.assertIn(element.tag.split('}')[-1], ('svg', 'title', 'desc', 'g', 'rect', 'text', 'tspan'))
                    self.assertFalse(any('href' in key or key.startswith('on') for key in element.attrib))

    def test_every_diagram_is_embedded_with_alt_text_and_full_size_link(self):
        embedded = set()
        for path in (ROOT / 'docs/levels').glob('*.md'):
            for alt, name, target in re.findall(r'\[!\[([^\]]+)\]\(/diagrams/([^/]+)\.svg\)\]\(([^)]+)\)', path.read_text()):
                self.assertTrue(alt.strip())
                self.assertIn(name, diagrams.DIAGRAMS)
                self.assertEqual(target, '/diagrams/' + name + '.svg')
                embedded.add(name)
        self.assertEqual(embedded, set(diagrams.DIAGRAMS))


if __name__ == '__main__':
    unittest.main()
