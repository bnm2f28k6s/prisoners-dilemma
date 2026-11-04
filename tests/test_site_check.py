"""Exercise site-checker failures with isolated synthetic sites."""

import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('site_check', ROOT / 'scripts/check-site.py')
assert SPEC is not None and SPEC.loader is not None
site_check = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(site_check)


class SiteCheckTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=os.environ.get('TMPDIR'))
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.site = self.root / 'site'
        self.docs = self.root / 'docs'
        self.site.mkdir()
        self.docs.mkdir()
        self.write(self.site, '.nojekyll', '')
        self.write(self.site, 'index.html', '<h1 id="home">Home</h1>')
        self.write(self.docs, 'README.md', '# Home')

    def write(self, root, name, text):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return path

    def errors(self, base='/project'):
        return site_check.check_site(self.site, base, self.docs)[0]

    def test_clean_urls_relative_links_queries_and_encoded_anchors(self):
        self.write(self.site, 'index.html', '<h1 id="home">Home</h1><a href="/project/guide?mode=1#hello%20world">Guide</a>')
        self.write(self.site, 'guide.html', '<h1 id="hello world">Guide</h1><a href="./#home">Home</a>')
        self.assertEqual(self.errors(), [])

    def test_directory_indexes_and_same_page_anchors(self):
        self.write(self.site, 'index.html', '<a href="/project/levels/">Levels</a>')
        self.write(self.site, 'levels/index.html', '<h1 id="levels">Levels</h1><a href="#levels">Again</a>')
        self.write(self.docs, 'levels/README.md', '# Levels')
        self.assertEqual(self.errors(), [])

    def test_direct_assets_and_svg_fragments(self):
        self.write(self.site, 'index.html', '<img src="/project/chart.svg#cell"><script src="/project/app.js"></script>'
                   '<link href="/project/style.css" rel="stylesheet">')
        self.write(self.site, 'chart.svg', '<svg xmlns="http://www.w3.org/2000/svg"><g id="cell"/></svg>')
        self.write(self.site, 'app.js', '')
        self.write(self.site, 'style.css', '')
        self.assertEqual(self.errors(), [])
        self.write(self.site, 'chart.svg', '<svg xmlns="http://www.w3.org/2000/svg"/>')
        self.assertIn('SVG fragment does not exist', self.errors()[0])

    def test_missing_page_and_asset_fail(self):
        self.write(self.site, 'index.html', '<a href="/project/missing">Missing</a><img src="/project/missing.svg">')
        errors = self.errors()
        self.assertEqual(len(errors), 2)
        self.assertTrue(all('target does not exist' in error for error in errors))

    def test_missing_fragment_fails_even_when_page_exists(self):
        self.write(self.site, 'index.html', '<a href="/project/#missing">Broken anchor</a>')
        self.assertIn('HTML fragment does not exist', self.errors()[0])

    def test_missing_project_prefix_and_double_prefix_fail(self):
        self.write(self.site, 'index.html', '<a href="/guide">Wrong root</a><a href="/project/project/guide">Double</a>')
        self.write(self.site, 'guide.html', '<h1>Guide</h1>')
        errors = self.errors()
        self.assertEqual(len(errors), 2)
        self.assertIn('outside the configured project prefix', errors[0])
        self.assertIn('target does not exist', errors[1])

    def test_encoded_path_escape_fails(self):
        self.write(self.root, 'outside.html', '<h1>Not part of site</h1>')
        self.write(self.site, 'index.html', '<a href="/project/%2e%2e/outside.html">Escape</a>')
        self.assertIn('escapes the site directory', self.errors()[0])

    def test_external_links_are_not_checked(self):
        self.write(self.site, 'index.html', '<a href="https://unreachable.invalid/no-page">External</a>'
                   '<a href="//unreachable.invalid/">External</a><a href="mailto:test@example.invalid">Mail</a>')
        self.assertEqual(self.errors(), [])

    def test_unlinked_authored_page_must_be_built(self):
        self.write(self.docs, 'unlinked.md', '# Unlinked')
        self.assertIn('missing built page for unlinked.md', self.errors())

    def test_empty_build_and_missing_pages_marker_fail(self):
        (self.site / 'index.html').unlink()
        (self.site / '.nojekyll').unlink()
        errors = self.errors()
        self.assertIn('missing built homepage: index.html', errors)
        self.assertIn('missing Pages marker: .nojekyll', errors)

    def test_empty_docs_do_not_pass_vacuously(self):
        (self.docs / 'README.md').unlink()
        self.assertIn('no authored Markdown pages found', self.errors())

    def test_root_hosting_and_legacy_named_anchor(self):
        self.write(self.site, 'index.html', '<a name="old"></a><a href="/#old">Root</a>')
        self.assertEqual(self.errors('/'), [])

    def test_project_homepage_without_trailing_slash(self):
        self.write(self.site, 'index.html', '<a href="/project">Home</a>')
        self.assertEqual(self.errors(), [])

    def test_base_path_validation_and_current_config(self):
        self.assertEqual(site_check.configured_base_path(), '/prisoners-dilemma')
        for base in ['project', '/project/../elsewhere', '/project?query', '//project', '/project%2fother']:
            with self.subTest(base=base), self.assertRaises(ValueError):
                self.errors(base)

    def test_command_returns_nonzero_on_a_broken_build(self):
        self.write(self.site, 'index.html', '<a href="/project/missing">Broken</a>')
        command = [sys.executable, str(ROOT / 'scripts/check-site.py'), '--site', str(self.site),
                   '--docs', str(self.docs), '--base-path', '/project']
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('target does not exist', result.stdout)
        self.assertIn('Failed: 1 site check errors', result.stdout)
        self.write(self.site, 'missing.html', '<h1>Now present</h1>')
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
