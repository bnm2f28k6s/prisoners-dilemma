# Prisoner's dilemma

A small [Doctave](https://github.com/Doctave/doctave) teaching site. Start with a two-by-two payoff square, then add repeated rounds, observations, memory, and strategies. The current site is one introductory page, not an interactive simulator.

- [Read the page](https://bnm2f28k6s.github.io/prisoners-dilemma/)
- Edit the lesson in [`docs/README.md`](docs/README.md).

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
mkdir -p .cache/preview
ln -sfn ../../site .cache/preview/prisoners-dilemma
python3 -m http.server 4001 --bind 127.0.0.1 --directory .cache/preview
```

Visit `http://127.0.0.1:4001/prisoners-dilemma/`. The ignored symlink maps the build to its configured GitHub Pages path. This static preview has no live reload. Stop either server with Ctrl-C.

## Publish and check

The GitHub Actions workflow builds on pushes to `main` and publishes only `site/` to GitHub Pages. Pull requests run the build without deployment privileges. It uses upstream's Linux 0.4.2 archive, a recorded SHA-256 digest, and commit-pinned GitHub actions. The digest checks archive stability; upstream did not provide a release checksum or signature for independent verification.

`doctave.yaml` sets the project site's `/prisoners-dilemma` base path. Change it if hosting at a different path. GitHub Pages must have its publishing source set to GitHub Actions. No custom domain, analytics, third-party plugins, application backend, or project secrets are configured.

Before committing or publishing:

```sh
./bin/doctave build --release
sh -n scripts/install-doctave.sh
git diff --check
gitleaks git --staged --redact --no-banner .
gitleaks git --log-opts="--all" --redact --no-banner .
```

Use Gitleaks if installed, and separately inspect the intended files and Git metadata for private information. A clean scan is not a guarantee. Never commit the binary, generated site, credentials, local agent state, or source-build scratch.

## Sources and scope

The initial lesson links to Steven Kuhn's [Prisoner's Dilemma](https://plato.stanford.edu/entries/prisoner-dilemma/) in the Stanford Encyclopedia of Philosophy. The model decomposition and future lesson sequence are this project's teaching proposals. There are no tournament results or claims that a particular strategy is universally best.

Doctave is an older upstream tool: its latest published release is 0.4.2 from April 2022. This project uses its existing Markdown tables and Mermaid support without modifying the generator. Inequalities use plain text: the bundled KaTeX stylesheet has root-relative font URLs that break under a project-site base path. Review upstream dependencies before expanding the deployment beyond a static teaching page.

A project-wide reuse license has not been selected. Public visibility alone does not grant an open-source or open-content license. Doctave remains separately licensed under its upstream terms; its binary and source are not committed here.
