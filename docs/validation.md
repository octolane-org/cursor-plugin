# Validation

## Verified locally

On 4 November 2026, version 0.1.0 was loaded as a local plugin in Cursor.
The plugin details displayed the correct version, repository, and logo. Its MCP
connection reported Connected and exposed 73 tools at the time of testing.
The hosted service controls tool availability; this package does not freeze that count.

Authenticated identity and pipeline reads returned structured results. No CRM
write was used for validation. Private account details and CRM results are not
included in this repository.

These checks establish local package discovery and authenticated reads. They do
not establish write-path correctness, OAuth refresh/revocation behavior, role or
tenant isolation, or accuracy against independently seeded fixtures. Marketplace
review and installation are separate from local installation.

## Repeat a bounded check

1. Install the package using the README and confirm its source is the local plugin.
2. Authenticate to a designated test workspace.
3. In an empty chat, request only the current workspace identity. Confirm it is
   the intended test workspace before requesting CRM records.
4. Request a pipeline overview and compare it with known test fixtures.
5. Record the Cursor version, plugin version, date, and pass/fail results without
   recording credentials or private CRM data in the repository.

Cursor's Try in Chat may immediately run a generated example. Use an explicit
prompt in an empty chat when you need a bounded test.

Write, deletion, email scheduling, refresh, and revocation tests require a
separately planned test workspace and explicit authorization for their effects.
Do not infer these outcomes from a successful connection.

## Package references

- [Cursor plugin format](https://cursor.com/docs/reference/plugins)
- [Local plugin installation](https://cursor.com/docs/plugins)
- [Remote MCP and OAuth](https://cursor.com/docs/mcp)

The package uses native Cursor OAuth discovery and the existing hosted endpoint.
It needs no OpenAI-specific extension, local server, build step, or bundled secret.

The description and unmodified logo are reused from
[Octolane's existing plugin](https://github.com/octolane-org/codex-plugin/tree/ac23d01ab095ad25d82c39b60ed16439a6537a6d).
The 1024×1024 logo has SHA-256
`b7e4bd5e5d1019b96f9a9c222f9deeca658c737eb2c3bd8592799f480ebe6017`.
