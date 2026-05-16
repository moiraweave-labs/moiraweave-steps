# MoiraWeave Steps

Step catalog repository for the MoiraWeave platform.

## What lives here

- `steps/`: deployable step implementations.
- `tasks/`: shared task schemas used by the step catalog.

## Local validation

```bash
uv sync --frozen --all-packages
uv run pytest steps/<step-name>/tests -q
```

## Adding a step

Follow [docs/adding-a-step.md](https://github.com/moiraweave-labs/moiraweave-docs/blob/main/docs/adding-a-step.md) for the canonical structure and validation flow.
