# Octolane for Cursor

<img src="assets/logo.png" alt="Octolane" width="80" height="80">

Revenue superintelligence built for modern sales and go-to-market teams.
Connect your Octolane workspace to Cursor to work with deals, contacts,
companies, tasks, notes, meetings, and pipeline information through Octolane's
hosted MCP service.

This repository contains the Cursor plugin package. The service runs at
`https://mcp.octolane.com/mcp`; there is no local server or dependency installation.
An existing Octolane account and workspace access are required. Available tools
and actions depend on workspace permissions and connected services.

## Local installation

1. Copy this repository's `.cursor-plugin/`, `mcp.json`, and `assets/` into
   `~/.cursor/plugins/local/octolane/`. Copy actual files: Cursor skips symlinks
   whose targets are outside its local plugin directory.
2. Restart Cursor or run **Developer: Reload Window**.
3. Open **Customize**, confirm Octolane appears, and enable its MCP server.
4. Complete the Octolane browser OAuth sign-in and select the intended workspace.
   Cursor discovers OAuth from the service; no API key, client secret, or
   OpenAI extension is needed in this package.

Enterprise administrators may need to enable **Allow Local Plugin Imports**.
A marketplace installation with the same name takes precedence over a local copy.
An existing manually configured Octolane MCP connection is separate from this
plugin; verify the server shown is `plugin-octolane-octolane` when testing it.

Try “Show my Octolane pipeline overview” or “Find stale deals in Octolane.”
For writes, specify the exact records and desired changes. Review tool requests
before approving them, especially deletion and email scheduling.

## Package and testing

`.cursor-plugin/plugin.json` supplies metadata and the bundled logo. Cursor
discovers the remote server from root `mcp.json`. This is a single-plugin repo,
so it needs no marketplace manifest, hooks, skills, build step, or extra backend.

The package has been loaded in Cursor and tested with an authenticated identity
lookup and pipeline read. It has not been submitted to the Cursor Marketplace.
See [validation](docs/validation.md) for the scope and limitations of these checks.

## Troubleshooting

- **Plugin missing:** check the manifest is at
  `~/.cursor/plugins/local/octolane/.cursor-plugin/plugin.json`, reload Cursor,
  and check your organization allows local plugins.
- **Needs authentication:** sign in from the plugin's MCP entry in Customize.
  A separate manually configured connection does not verify this plugin.
- **Unexpected workspace or permission error:** verify the connected workspace
  and your role before retrying. The plugin does not grant additional access.
- **An uncertain write result:** inspect the target record before retrying to avoid
  duplicate tasks, records, or scheduled emails.

## Links

- [Octolane](https://www.octolane.com/)
- [Support](https://octolane.com/docs/support/contact)
- [Privacy policy](https://www.octolane.com/privacy-policy)
- [Terms](https://www.octolane.com/terms)
- [Cursor plugin reference](https://cursor.com/docs/reference/plugins)
- [Cursor local installation](https://cursor.com/docs/plugins)
- [Cursor MCP and OAuth](https://cursor.com/docs/mcp)

MIT licensed; see [LICENSE](LICENSE).
