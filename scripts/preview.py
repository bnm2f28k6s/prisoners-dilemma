#!/usr/bin/env python3
"""Preview the built project site on loopback with clean HTML URLs."""

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

SITE = Path(__file__).resolve().parents[1] / 'site'
BASE_PATH = '/prisoners-dilemma'


class PreviewHandler(SimpleHTTPRequestHandler):
    def send_head(self):
        url = urlsplit(self.path)
        if url.path == BASE_PATH:
            location = BASE_PATH + '/'
            if url.query:
                location += '?' + url.query
            self.send_response(301)
            self.send_header('Location', location)
            self.send_header('Content-Length', '0')
            self.end_headers()
            return None
        if not url.path.startswith(BASE_PATH + '/'):
            self.send_error(404)
            return None
        return super().send_head()

    def translate_path(self, path):
        relative = urlsplit(path).path[len(BASE_PATH):]
        translated = Path(super().translate_path(relative))
        html = translated.with_suffix('.html')
        if not translated.suffix and html.is_file():
            return str(html)
        return str(translated)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=4001)
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error('--port must be between 1 and 65535')
    if not (SITE / 'index.html').is_file():
        parser.error('build the site first with ./bin/doctave build --release')
    handler = partial(PreviewHandler, directory=str(SITE))
    with ThreadingHTTPServer(('127.0.0.1', args.port), handler) as server:
        print(f'Preview: http://127.0.0.1:{args.port}{BASE_PATH}/', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    main()
