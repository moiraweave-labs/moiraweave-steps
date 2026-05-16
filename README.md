# MoiraWeave Steps

Official step catalog for the MoiraWeave platform.

## Purpose

This repository maintains reusable step implementations and task contracts that are:
- Tested and maintained by the MoiraWeave team.
- Published as versioned container images.
- Consumed by users via the CLI, not by cloning this repository.

## What lives here

- `steps/`: Official deployable step implementations.
- `tasks/`: Shared task schemas used by the step catalog.

## For Users: How to Consume Official Steps

You do **not** need to clone this repository. Instead:

```bash
# Add an official step to your workspace
moira step add --from-catalog text-embed-fastembed@1.0

# Or create your own custom step
moira step new my-task my-impl
```

The CLI resolves official steps from the catalog by reference and version. Your custom steps live in your own workspace repository.

## For Contributors: Local Development

```bash
uv sync --frozen --all-packages
uv run pytest steps/<step-name>/tests -q
```

## Adding Steps to the Official Catalog

To contribute new steps to the catalog:

1. Follow the structure in `steps/` directory.
2. Create a task contract in `tasks/` if new.
3. Implement the step in `steps/<task>-<impl>/`.
4. Test locally and submit a PR.
5. Once merged, the step is automatically published and available via `moira step add --from-catalog`.

For detailed structure, see [CONTRIBUTING.md](./CONTRIBUTING.md) in this repository.

## Companion repositories

- [moiraweave-core](https://github.com/moiraweave-labs/moiraweave-core): Runtime and infrastructure.
- [moiraweave-cli](https://github.com/moiraweave-labs/moiraweave-cli): Developer CLI (your entry point).
- [moiraweave-docs](https://github.com/moiraweave-labs/moiraweave-docs): Documentation.
