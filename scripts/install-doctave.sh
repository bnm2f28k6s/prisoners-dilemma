#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
# Reuse a temporary, pinned Nix toolchain. No global Cargo install or Rosetta.
command -v nix >/dev/null
command -v git >/dev/null
mkdir -p .cache bin
src="$(mktemp -d "$PWD/.cache/doctave-source.XXXXXX")"
trap 'rm -rf "$src"' EXIT HUP INT TERM
git clone --depth 1 --branch 0.4.2 https://github.com/Doctave/doctave.git "$src"
test "$(git -C "$src" rev-parse HEAD)" = ad1888feb6bb7f4f043b76474b1df38b520c51c3
# Upstream 0.4.2 forgot to bump its own package version in Cargo.lock.
# Correct only that metadata; keep every dependency and checksum unchanged.
python3 - "$src/Cargo.lock" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1])
text = p.read_text()
old = 'name = "doctave"\nversion = "0.4.0"'
assert text.count(old) == 1, "Unexpected upstream lockfile"
p.write_text(text.replace(old, 'name = "doctave"\nversion = "0.4.2"'))
PY
nix shell github:NixOS/nixpkgs/7a0f122f5090cf4c2ade2a13a0e229d4e19ba71f#cargo github:NixOS/nixpkgs/7a0f122f5090cf4c2ade2a13a0e229d4e19ba71f#rustc --command cargo build --release --locked --manifest-path "$src/Cargo.toml"
"$src/target/release/doctave" --version
cp "$src/target/release/doctave" bin/doctave
./bin/doctave --version
