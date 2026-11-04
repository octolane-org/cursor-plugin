"""Check this repository's intentionally small Cursor package without network access."""

import json
from pathlib import Path
import re
import struct


ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def load_json(path):
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, f"duplicate JSON key: {key}")
            result[key] = value
        return result

    return json.loads((ROOT / path).read_text(), object_pairs_hook=unique_keys)


def main():
    manifest = load_json(".cursor-plugin/plugin.json")
    require(manifest["name"] == "octolane", "unexpected plugin identifier")
    require(re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]), "expected stable semver")
    require(manifest["description"].strip(), "description is empty")
    require(manifest["author"]["name"] == "Octolane", "unexpected publisher")
    require(manifest["repository"] == "https://github.com/octolane-org/cursor-plugin",
            "unexpected repository")
    require(manifest["license"] == "MIT", "license must match LICENSE")
    allowed = {"name", "version", "description", "author", "homepage", "repository",
               "license", "keywords", "logo"}
    require(set(manifest) <= allowed, "review new manifest fields before expanding this package")
    logo = Path(manifest["logo"])
    require(not logo.is_absolute() and ".." not in logo.parts, "logo must be a relative path")
    require(not (ROOT / logo).is_symlink(), "logo must be a bundled file")
    data = (ROOT / logo).read_bytes()
    require(data[:8] == b"\x89PNG\r\n\x1a\n", "logo must be a PNG")
    require(struct.unpack(">II", data[16:24]) == (1024, 1024), "expected square 1024px logo")
    require(load_json("mcp.json") == {
        "mcpServers": {"octolane": {"url": "https://mcp.octolane.com/mcp"}}
    }, "MCP config must use only the hosted endpoint and native OAuth discovery")
    for name in ("README.md", "LICENSE", "docs/validation.md"):
        require((ROOT / name).read_text().strip(), f"missing or empty {name}")
    print("PASS: manifest, bundled logo, documentation, and hosted MCP configuration")


if __name__ == "__main__":
    main()
