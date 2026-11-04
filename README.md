# Prisoner's dilemma

A small [Doctave](https://github.com/Doctave/doctave) teaching site. Walk from a one-shot prisoner's dilemma through Levels 0-18, relaxing one constraint or exposing one additional mechanism at a time. Each lesson includes a language-neutral build-along: what to keep, what to change, pseudocode, and concrete checks. The endpoint is a configurable interaction model, not an interactive simulator or a production implementation specification.

- [Read the page](https://bnm2f28k6s.github.io/prisoners-dilemma/)
- Start with the [walkthrough and level map](docs/README.md).
- Use the [build-along guide](docs/build-along.md) for shared notation, event order, and repeatable tests in your own implementation.
- Edit individual lessons in [`docs/levels/`](docs/levels/) and the [combined conceptual model](docs/conceptual-model.md).

## Local setup

Prerequisites: Git, Python 3, Nix with flakes enabled, and the macOS command-line developer tools. The native installer has been tested on Apple Silicon macOS. It builds Doctave 0.4.2 from upstream commit `ad1888feb6bb7f4f043b76474b1df38b520c51c3` with its lockfile and a pinned temporary Rust toolchain. Upstream left the root package version at 0.4.0 in that lockfile; the installer changes only that entry to 0.4.2 so `--locked` builds work, leaving every dependency version and checksum unchanged. No generator features are modified. No global Doctave, Cargo, or Rosetta installation is needed.

```sh
sh scripts/install-doctave.sh
./bin/doctave --version
./bin/doctave build --release
```

The executable goes in ignored `bin/`, temporary sources in ignored `.cache/`, and generated HTML in ignored `site/`. Cargo and Nix may retain their normal dependency caches outside this repository. The installer removes its temporary source directory when it exits.

Doctave's built-in live preview is available with:

```sh
./bin/doctave serve --port 4001
```

Visit `http://localhost:4001/prisoners-dilemma/`. **Doctave 0.4.2 binds this development server to all network interfaces and has no host option.** Only use it on a trusted network. It also uses a loopback live-reload socket on port 35729.

For a loopback-only preview using an existing Python 3 installation:

```sh
./bin/doctave build --release
python3 scripts/preview.py --port 4001
```

Visit `http://127.0.0.1:4001/prisoners-dilemma/`. The helper maps the project prefix to `site/` and resolves Doctave's extensionless page URLs to `.html` files, which a plain `python3 -m http.server` does not do. This static preview has no live reload. Stop either server with Ctrl-C. If the hosting base path changes, update `BASE_PATH` in the preview helper too.

## Publish and check

The GitHub Actions workflow builds on pushes to `main` and publishes only `site/` to GitHub Pages. Pull requests run the build without deployment privileges. It uses upstream's Linux 0.4.2 archive, a recorded SHA-256 digest, and commit-pinned GitHub actions. The digest checks archive stability; upstream did not provide a release checksum or signature for independent verification.

`doctave.yaml` sets the project site's `/prisoners-dilemma` base path. Change it if hosting at a different path. Links inside `docs/` use site-root paths without `.md` or the base-path prefix, such as `/levels/00-one-shot`; Doctave adds the prefix. Navigation explicitly orders the levels. The homepage is reached through the site title and each lesson's Walkthrough link, rather than a custom root navigation entry, which triggers an upstream 0.4.2 bug under a non-root base path. Each documentation directory has its own `README.md` to avoid another base-path bug in generated directory listings.

GitHub Pages must have its publishing source set to GitHub Actions. No custom domain, analytics, third-party plugins, application backend, or project secrets are configured.

Before committing or publishing:

```sh
./bin/doctave build --release
sh -n scripts/install-doctave.sh
git diff --check
gitleaks git --staged --redact --no-banner .
gitleaks git --log-opts="--all" --redact --no-banner .
```

Use Gitleaks if installed, and separately inspect the intended files and Git metadata for private information. A clean scan is not a guarantee. Never commit the binary, generated site, credentials, local agent state, or source-build scratch.

## Static payoff diagrams

Lessons 0-8 include static SVGs generated from one shared template. Row stays on the left, Column stays across the top, and tuples list Row before Column. Early extensions keep the same stage payoffs; probability, execution, observation, and round traces are annotations rather than edited cell values. Later diagrams explicitly name changed payoffs, expanded actions, and a fixed-third-player slice. Text tables and descriptions remain alongside the images. There is no diagram JavaScript, external font, or runtime dependency.

To regenerate or check the committed images:

```sh
python3 scripts/render-payoff-diagrams.py
python3 scripts/render-payoff-diagrams.py --check
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

The SVG source files are in `docs/_include/diagrams/` and are copied into `site/diagrams/` by Doctave. Diagram links use `/diagrams/name.svg` without the project prefix; the generator adds it, just as for page links.

## Build-along tutorial checks

Every numbered lesson keeps its conceptual explanation and adds a practical implementation change from the preceding version. Worked examples sometimes select simpler settings to isolate a mechanism; earlier capabilities remain available. The guide distinguishes illustrative pseudocode from existing repository APIs. This repository does not contain the reader's game runner.

The standard-library test suite also checks level coverage and navigation, the structure of each build step, and calculations from the authored examples. Run the same `python3 -m unittest discover -s tests -v` command above. These checks validate the teaching material, not arbitrary implementations built from it. The published steps include their own outcome, information-flow, boundary, and backward-compatibility checks for readers to run.

## Sources and scope

The [source guide](docs/sources.md) links the foundations to MIT, Yale, Bonanno, and the Stanford Encyclopedia of Philosophy, with OpenSpiel and PettingZoo as broader process-design references. The numbered sequence, examples, and combined model are this project's teaching proposals. There are no reported simulator or tournament results, claims of a universal winning strategy, or claims that every level defines a strictly larger mathematical game class.

Earlier source research and proposed teaching additions are retained in [`research/strategic-game-foundations.md`](research/strategic-game-foundations.md). This development note compares one-shot game structures, clarifies the transition to repeated games, and records source locators and limitations. It is not part of the published site; its smallest-revision recommendation predates the expanded walkthrough.

Doctave is an older upstream tool: its latest published release is 0.4.2 from April 2022. This project uses its existing Markdown tables and Mermaid support without modifying the generator. Inequalities use plain text: the bundled KaTeX stylesheet has root-relative font URLs that break under a project-site base path. Review upstream dependencies before expanding the deployment beyond a static teaching page.

A project-wide reuse license has not been selected. Public visibility alone does not grant an open-source or open-content license. Doctave remains separately licensed under its upstream terms; its binary and source are not committed here.
