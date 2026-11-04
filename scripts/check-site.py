#!/usr/bin/env python3
"""Check built HTML links, assets, fragments, and authored-page coverage offline."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.anchors = set()
        self.links = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.anchors.add(attrs['id'])
        if tag == 'a' and attrs.get('name'):
            self.anchors.add(attrs['name'])
        key = {'a': 'href', 'link': 'href', 'img': 'src', 'script': 'src',
               'iframe': 'src', 'source': 'src', 'video': 'src', 'audio': 'src'}.get(tag)
        if key and attrs.get(key):
            self.links.append(attrs[key])


def configured_base_path():
    # This project uses a simple top-level YAML scalar, not a nested YAML document.
    config = (ROOT / 'doctave.yaml').read_text()
    match = re.search(r'''^base_path:\s*(["']?)(/[^\s"']*)\1\s*$''', config, re.MULTILINE)
    if match is None:
        raise ValueError('Cannot read base_path from doctave.yaml; pass --base-path explicitly')
    return match.group(2)


def normalize_base_path(base_path):
    if not base_path.startswith('/') or any(c in base_path for c in ['?', '#', '%', '\\']):
        raise ValueError('base path must be an absolute URL path without query or encoding')
    if any(part in ['.', '..'] for part in base_path.split('/')) or '//' in base_path:
        raise ValueError('base path must not contain dot segments or repeated slashes')
    return base_path.rstrip('/')


def page_url(path, site, base_path):
    relative = path.relative_to(site)
    if path.name == 'index.html':
        suffix = relative.parent.as_posix()
        suffix = '' if suffix == '.' else suffix + '/'
    else:
        suffix = relative.with_suffix('').as_posix()
    return 'https://site.invalid' + base_path + '/' + suffix


def target_path(url_path, site, base_path):
    decoded = unquote(url_path)
    if base_path and decoded != base_path and not decoded.startswith(base_path + '/'):
        raise ValueError('local URL is outside the configured project prefix')
    relative = decoded[len(base_path):].lstrip('/')
    target = (site / relative).resolve()
    if not target.is_relative_to(site):
        raise ValueError('local URL escapes the site directory')
    if target.is_dir():
        return target / 'index.html'
    if target.is_file():
        return target
    return target.with_suffix('.html') if not target.suffix else target


def check_site(site, base_path, docs=None):
    site = Path(site).resolve()
    base_path = normalize_base_path(base_path)
    errors = []
    pages = {path: Page(path.read_text()) for path in sorted(site.rglob('*.html'))}
    if site / 'index.html' not in pages:
        errors.append('missing built homepage: index.html')
    if not (site / '.nojekyll').is_file():
        errors.append('missing Pages marker: .nojekyll')
    if docs is not None:
        sources = sorted(Path(docs).rglob('*.md'))
        if not sources:
            errors.append('no authored Markdown pages found')
        for source in sources:
            relative = source.relative_to(docs)
            output = relative.with_name('index.html') if source.name == 'README.md' else relative.with_suffix('.html')
            if site / output not in pages:
                errors.append(f'missing built page for {relative.as_posix()}')
    checked = 0
    for source, page in pages.items():
        origin = page_url(source, site, base_path)
        for link in page.links:
            raw = urlsplit(link)
            # No outbound requests: external sites, mail links and inline data are out of scope.
            if raw.scheme or raw.netloc:
                continue
            checked += 1
            url = urlsplit(urljoin(origin, link))
            try:
                target = target_path(url.path, site, base_path)
                if not target.is_file():
                    raise ValueError('target does not exist')
                fragment = unquote(url.fragment)
                if fragment and target.suffix == '.html':
                    if fragment not in pages[target].anchors:
                        raise ValueError('HTML fragment does not exist')
                if fragment and target.suffix == '.svg':
                    anchors = {node.get('id') for node in ET.parse(target).iter()}
                    if fragment not in anchors:
                        raise ValueError('SVG fragment does not exist')
            except (ValueError, KeyError, OSError, ET.ParseError) as error:
                errors.append(f'{source.relative_to(site).as_posix()}: {link!r}: {error}')
    return errors, len(pages), checked


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, default=ROOT / 'site')
    parser.add_argument('--docs', type=Path, default=ROOT / 'docs')
    parser.add_argument('--base-path', help='defaults to base_path in doctave.yaml')
    args = parser.parse_args()
    try:
        base_path = args.base_path if args.base_path is not None else configured_base_path()
        errors, pages, links = check_site(args.site, base_path, args.docs)
    except ValueError as error:
        parser.error(str(error))
    for error in errors:
        print(error)
    if errors:
        print(f'Failed: {len(errors)} site check errors.')
        return 1
    print(f'Checked {pages} built HTML pages and {links} local links/assets; fragments and page coverage passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
