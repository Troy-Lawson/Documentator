# Contributing

Documentator is an early-stage project. Bug reports, focused fixes, tests, and
small design proposals are welcome.

## Development setup

1. Fork and clone the repository.
2. Create and activate a Python 3.10+ virtual environment.
3. Run `python -m pip install -e ".[dev]"`.
4. Create a topic branch for the change.

Before opening a pull request, run:

```bash
pytest
ruff check .
ruff format --check .
```

Keep pull requests focused and explain both the behavior change and its tests.
Use fake, organization-neutral data in fixtures, examples, logs, and screenshots.
Never submit credentials, private URLs, customer data, or internal operational
details.

For vulnerabilities, follow [SECURITY.md](SECURITY.md) instead of opening a
public issue.
