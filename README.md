# MoiraWeave Steps

[![Step CI](https://github.com/moiraweave-labs/moiraweave-steps/actions/workflows/step-ci.yml/badge.svg?branch=main)](https://github.com/moiraweave-labs/moiraweave-steps/actions/workflows/step-ci.yml)
[![Publish Catalog and Steps](https://github.com/moiraweave-labs/moiraweave-steps/actions/workflows/publish-catalog.yml/badge.svg?branch=main)](https://github.com/moiraweave-labs/moiraweave-steps/actions/workflows/publish-catalog.yml)
[![Release Please](https://github.com/moiraweave-labs/moiraweave-steps/actions/workflows/release.yml/badge.svg?branch=main)](https://github.com/moiraweave-labs/moiraweave-steps/actions/workflows/release.yml)
[![Python](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/)
[![Docs](https://img.shields.io/badge/docs-live-blue)](https://moiraweave-labs.github.io/moiraweave-docs/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Legacy reusable step catalog for historical MoiraWeave pipeline examples.
The current product path is workload templates plus `moira up`; the active
MoiraWeave platform does not depend on this repository.

## Scope

This repository contains reusable step implementations and task contracts that were:

- tested and maintained by the MoiraWeave team
- versioned and published through CI/CD
- consumed by the legacy step catalog workflow

## Repository structure

- `steps/`: official deployable step implementations
- `tasks/`: official task schemas
- `scripts/generate_catalog.py`: catalog generation logic

## Current status

You do not need this repository to deploy agents, model services, or workload
templates with MoiraWeave. New examples should live in workload manifests or in
the documentation. This repository can be archived once the historical examples
are no longer useful as reference material.

## For contributors

```bash
uv sync --frozen --all-packages
uv run pytest steps/<step-name>/tests -q
```

Contribution flow:

1. Add or update a step under `steps/<task>-<impl>/`
2. Add/update the task schema under `tasks/` when needed
3. Validate with tests and linting
4. Open a pull request

## CI/CD summary

- `step-ci.yml`: validates changed steps and contracts
- `publish-catalog.yml`: builds catalog and publishes step images
- `release.yml`: release automation and version flow

## Related repositories

- [moiraweave-cli](https://github.com/moiraweave-labs/moiraweave-cli)
- [moiraweave](https://github.com/moiraweave-labs/moiraweave)
- [moiraweave-docs](https://github.com/moiraweave-labs/moiraweave-docs)
