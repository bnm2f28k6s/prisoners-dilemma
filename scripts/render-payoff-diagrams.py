#!/usr/bin/env python3
"""Render the static lesson SVGs from one shared, dependency-free template."""

import argparse
from html import escape
from pathlib import Path

OUTPUT = Path(__file__).resolve().parents[1] / 'docs' / '_include' / 'diagrams'
ROW_COLOR = '#1d4ed8'
COLUMN_COLOR = '#7c3aed'
THIRD_COLOR = '#475569'
PD = ((3, 3), (0, 5), (5, 0), (1, 1))
GRID = (168, 160, 560, 240)

DIAGRAMS = {
    'matrix-baseline': {
        'subtitle': 'Same square. Each cell lists (Row, Column).',
        'description': 'Row chooses C or D down the left; Column chooses C or D across the top. '
                       'Cells in row-major order are (3, 3), (0, 5), (5, 0), and (1, 1).',
        'footer': ('The stopping rule can change without changing this square.',),
    },
    'matrix-one-shot': {
        'subtitle': 'Example: Row chooses C; Column chooses D.',
        'description': 'The usual prisoners dilemma matrix, with the top-right C/D cell outlined. '
                       'Row receives 0 and Column receives 5. Only this one outcome occurs.',
        'focus': {(0, 1): 'example outcome'},
        'footer': ('Read down from Column D and across from Row C.',
                   'Their intersection gives (0, 5). Then the game ends.'),
    },
    'matrix-repeated': {
        'subtitle': 'Same square. Now visit one cell each round.',
        'description': 'The payoff square is unchanged. Tit for tat versus always defect visits '
                       'C/D in round 1, then D/D in rounds 2, 3, and 4. '
                       'Stage payoffs are (0, 5), (1, 1), (1, 1), (1, 1). Totals are (3, 8).',
        'focus': {(0, 1): 'round 1', (1, 1): 'rounds 2-4'},
        'rounds': (('C', 'D'), ('D', 'D'), ('D', 'D'), ('D', 'D')),
    },
    'matrix-randomized': {
        'subtitle': 'Same square. Random choice changes which cell is reached.',
        'description': 'Column always chooses C. Row chooses C with probability 75 percent and D '
                       'with probability 25 percent. Only the left-column cells are possible. '
                       'Their payoffs remain (3, 3) and (5, 0); expected payoffs are (3.5, 2.25).',
        'focus': {(0, 0): '75% chance', (1, 0): '25% chance'},
        'footer': ('Outlined cells are alternatives, not two outcomes in one round.',
                   'Expected payoffs: (3.5, 2.25). The cell values do not change.'),
    },
    'matrix-execution': {
        'subtitle': 'Same square. Resolve the executed actions, not the intentions.',
        'description': 'Both intend C, but an execution error changes Row to D. '
                       'The executed D/C outcome is the bottom-left cell, with payoffs (5, 0).',
        'focus': {(1, 0): 'executed outcome'},
        'footer': ('Intended (C, C)  →  execution error  →  executed (D, C).',
                   'The executed cell gives (5, 0), even though both intended C.'),
    },
    'matrix-observations': {
        'subtitle': 'Same square. A mistaken report does not change the outcome.',
        'description': 'The actual joint action is C/C, with actual payoffs (3, 3). '
                       'Row incorrectly hears that Column played D; Column hears that Row played C. '
                       'These payoffs are evaluator information, withheld from players until the end.',
        'focus': {(0, 0): 'actual outcome'},
        'footer': ('Row hears: Column D.  |  Column hears: Row C.',
                   'Actual payoffs (3, 3) are withheld from players until the end.'),
    },
    'matrix-stag-hunt': {
        'subtitle': 'Stag hunt: same axes and payoff order; different numbers.',
        'description': 'Stag hunt with cells (4, 4), (0, 3), (3, 0), and (2, 2). '
                       'Row prefers C against C and D against D.',
        'values': ((4, 4), (0, 3), (3, 0), (2, 2)),
        'footer': ('Against Column C, Row prefers C. Against Column D, Row prefers D.',),
    },
    'matrix-asymmetric': {
        'subtitle': 'Asymmetry: only Row\'s payoff at (C, C) changes, from 3 to 6.',
        'description': 'The starting matrix with only Row payoff at C/C changed from 3 to 6. '
                       'Cells are (6, 3), (0, 5), (5, 0), and (1, 1). '
                       'The outlined cell marks the edited entry, not a chosen action or equilibrium.',
        'values': ((6, 3), (0, 5), (5, 0), (1, 1)),
        'focus': {(0, 0): 'edited cell'},
        'footer': ('The outline marks the edit, not a chosen outcome or an equilibrium.',
                   'Row now prefers C against C; Column still prefers D against C.'),
    },
    'matrix-contributions': {
        'subtitle': 'More actions: expand the square, keeping Row first and Column second.',
        'description': 'Three by three contribution matrix. Row chooses x and Column chooses y '
                       'from 0, 1, 2. Payoffs are (2(x+y)-3x, 2(x+y)-3y). '
                       'The outlined example x=2, y=1 gives (0, 3).',
        'contributions': True,
        'focus': {(2, 1): 'example outcome'},
        'footer': ('New actions and payoffs: x and y are contributions, not C/D labels.',
                   'Example: Row x = 2, Column y = 1  →  payoffs (0, 3).'),
    },
    'matrix-three-player-slice': {
        'subtitle': 'Three players: show a slice with the third contribution fixed at 0.',
        'description': 'A three by three slice of a three-player contribution game, with the third '
                       'contribution fixed at zero. Rows vary x and columns vary y. '
                       'Each cell lists Row, Column, and third-player payoffs. '
                       'The outlined x=2, y=1 cell gives (0, 3, 6). Other third-player actions need other slices.',
        'contributions': True,
        'third': True,
        'focus': {(2, 1): 'example outcome'},
        'footer': ('Payoffs now list (Row, Column, third player). Third action = 0.',
                   'This is one slice, not the full three-player game.'),
    },
}


def values_for(spec):
    if spec.get('contributions'):
        return tuple((2 * (x + y) - 3 * x, 2 * (x + y) - 3 * y)
                     + ((2 * (x + y),) if spec.get('third') else ())
                     for x in range(3) for y in range(3))
    return spec.get('values', PD)


def render(name, spec):
    height = 620 if 'rounds' in spec else 520
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 {height}" '
             'width="760" role="img" aria-labelledby="title description">',
             f'<title id="title">{escape(spec["subtitle"])}</title>',
             f'<desc id="description">{escape(spec["description"])}</desc>',
             '<rect width="760" height="100%" rx="18" fill="#fff"/>',
             '<g font-family="system-ui, -apple-system, sans-serif" fill="#172033">']

    def text(x, y, value, size=18, color='#172033', anchor='start', weight=400):
        parts.append(f'<text x="{x:g}" y="{y:g}" font-size="{size}" fill="{color}" '
                     f'text-anchor="{anchor}" font-weight="{weight}">{escape(str(value))}</text>')

    def payoff(x, y, values, size=34):
        parts.append(f'<text x="{x:g}" y="{y:g}" text-anchor="middle" font-size="{size}" '
                     'font-weight="650">')
        parts.append('<tspan fill="#475569">(</tspan>')
        for i, value in enumerate(values):
            if i:
                parts.append('<tspan fill="#475569">, </tspan>')
            color = (ROW_COLOR, COLUMN_COLOR, THIRD_COLOR)[i]
            parts.append(f'<tspan fill="{color}" data-player="{i}">{value}</tspan>')
        parts.append('<tspan fill="#475569">)</tspan></text>')

    text(28, 34, 'THE PAYOFF MATRIX', 20, weight=700)
    text(28, 64, spec['subtitle'], 17)
    text(448, 100, 'COLUMN →', 18, COLUMN_COLOR, 'middle', 700)
    text(28, 144, 'ROW ↓', 18, ROW_COLOR, weight=700)
    n = 3 if spec.get('contributions') else 2
    x0, y0, width, grid_height = GRID
    cell_width, cell_height = width / n, grid_height / n
    for i in range(n):
        label = f'y = {i}' if n == 3 else ('C · cooperate', 'D · defect')[i]
        text(x0 + (i + 0.5) * cell_width, 138, label, 20, COLUMN_COLOR, 'middle', 600)
        label = f'x = {i}' if n == 3 else ('C', 'D')[i]
        cy = y0 + (i + 0.5) * cell_height
        text(88, cy + 6, label, 24, ROW_COLOR, 'middle', 700)
        if n == 2:
            text(88, cy + 31, ('cooperate', 'defect')[i], 16, ROW_COLOR, 'middle')
    values = values_for(spec)
    for row in range(n):
        for column in range(n):
            x, y = x0 + column * cell_width, y0 + row * cell_height
            focus = spec.get('focus', {}).get((row, column))
            parts.append(f'<g data-cell="{row},{column}">')
            parts.append(f'<rect x="{x:g}" y="{y:g}" width="{cell_width:g}" '
                         f'height="{cell_height:g}" fill="{"#eef8f7" if focus else "#f8fafc"}" '
                         f'stroke="{"#0f766e" if focus else "#cbd5e1"}" stroke-width="{3 if focus else 1}"/>')
            if focus:
                text(x + cell_width / 2, y + 22, focus, 14, '#115e59', 'middle', 600)
            payoff(x + cell_width / 2, y + cell_height / 2 + 14,
                   values[row * n + column], 28 if spec.get('third') else 34)
            parts.append('</g>')
    text(28, 434, 'Payoff order:', 17)
    text(150, 434, 'Row first', 17, ROW_COLOR, weight=600)
    text(255, 434, 'Column second', 17, COLUMN_COLOR, weight=600)
    if spec.get('third'):
        text(425, 434, 'third player last', 17, THIRD_COLOR, weight=600)
    if 'rounds' in spec:
        for i, joint_action in enumerate(spec['rounds']):
            x = 28 + 180 * i
            parts.append(f'<rect x="{x}" y="454" width="164" height="104" rx="10" '
                         'fill="#f8fafc" stroke="#cbd5e1"/>')
            text(x + 82, 478, f'Round {i + 1}', 17, anchor='middle')
            text(x + 82, 506, ', '.join(joint_action), 21, anchor='middle', weight=600)
            r, c = (('C', 'D').index(a) for a in joint_action)
            payoff(x + 82, 541, PD[2 * r + c], 25)
        text(28, 592, 'Add stage payoffs separately. Match totals: Row 3, Column 8.', 19, weight=600)
    else:
        for i, line in enumerate(spec['footer']):
            text(28, 470 + 28 * i, line, 17)
    parts.extend(('</g>', '</svg>', ''))
    return '\n'.join(parts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='check committed SVGs without writing')
    args = parser.parse_args()
    if not args.check:
        OUTPUT.mkdir(parents=True, exist_ok=True)
    stale = []
    for name, spec in DIAGRAMS.items():
        target = OUTPUT / (name + '.svg')
        expected = render(name, spec)
        if args.check:
            if not target.is_file() or target.read_text() != expected:
                stale.append(target.name)
        else:
            target.write_text(expected)
    if stale:
        parser.exit(1, 'Missing or outdated diagrams: ' + ', '.join(stale) + '\n')
    print(f'{"Checked" if args.check else "Rendered"} {len(DIAGRAMS)} static payoff diagrams.')


if __name__ == '__main__':
    main()
