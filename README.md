# Documentator

Documentator is an experimental Python tool for defining documentation page
trees in YAML and synchronizing them through pluggable publishers. The current
prototype includes a working YAML loader, an idempotent in-memory publisher,
and a publisher interface for future integrations.

> [!WARNING]
> Documentator is under active development and is not ready for production use.
> The Confluence publisher is currently a placeholder.

## Features

- Define nested page structures as YAML.
- Load YAML into a typed `Page` tree.
- Traverse the tree through a provider-independent publishing engine.
- Test publishing safely with an in-memory mock provider.

## Quick start

Documentator requires Python 3.10 or newer.

```bash
python -m venv .venv
```

Activate the environment on Linux or macOS:

```bash
source .venv/bin/activate
```

Or on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the project and run the demonstration:

```bash
python -m pip install -e .
python main.py
```

The example publishes `data/structure.yaml` twice. The first pass creates each
page; the second finds the same pages, demonstrating idempotent traversal.

## Structure format

```yaml
title: Engineering Handbook
labels:
  - handbook
children:
  - title: Onboarding
    body: Welcome to the team.
  - title: Services
    children:
      - title: Example Service
```

Each node supports `title`, `body`, `labels`, and `children`. Only `title` is
required.

## Configuration and credentials

`config.example.yaml` documents the planned integration settings. Copy it to
the ignored `config.yaml` for local experimentation. Never commit real tokens,
private instance URLs, or operational data.

## Development

```bash
python -m pip install -e ".[dev]"
pytest
ruff check .
ruff format --check .
```

See [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a change. Security
issues should be reported using the process in [SECURITY.md](SECURITY.md).

## Roadmap

- Implement authenticated Confluence publishing.
- Add update and dry-run behavior.
- Validate configuration and structure files.
- Add pull/export support for backup and migration workflows.
- Package a stable command-line interface.

## License

Documentator is available under the [MIT License](LICENSE). Confluence is a
trademark of Atlassian; this project is independent and is not endorsed by or
affiliated with Atlassian.
