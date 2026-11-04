# Contributing

This repository packages Octolane's existing hosted MCP service for Cursor.
Keep changes focused on configuration, documentation, and assets. Backend behavior
and credentials do not belong in this package.

Run the dependency-free check with Python 3:

```sh
python3 scripts/validate.py
git diff --check
```

The validator checks this package's intended configuration; it is not a complete
implementation of Cursor's manifest schema. GitHub Actions runs it on pushes and
pull requests with read-only repository permissions.

For runtime changes, repeat the bounded checks in [validation](docs/validation.md)
and describe what actually passed in the pull request. Use a designated test
workspace. Never include tokens, private CRM results, screenshots with personal
data, or local environment files in commits or issue reports.

Use a semantic version for package changes. Review any added executable code or
dependencies carefully: this plugin currently needs neither to connect to Octolane.
Keep the README and validation notes aligned with the behavior being released.

Report security concerns privately through [Octolane support](https://octolane.com/docs/support/contact).
Do not post credentials or exploit details in a public issue.
