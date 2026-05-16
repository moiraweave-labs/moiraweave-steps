#!/usr/bin/env python
"""Generate catalog.yaml and catalog.json from step definitions."""

from __future__ import annotations

import json
import pathlib
import sys
from typing import Any

import yaml


def generate_catalog(repo_root: pathlib.Path) -> dict[str, Any]:
    """Generate catalog metadata from step and task definitions.

    :param repo_root: Repository root containing steps/ and tasks/.
    :returns: Catalog dictionary ready for serialization.
    """
    steps_dir = repo_root / "steps"
    tasks_dir = repo_root / "tasks"

    if not steps_dir.exists():
        print(f"Error: steps/ directory not found at {steps_dir}")
        return {"version": 1, "steps": []}

    catalog: dict[str, Any] = {
        "version": 1,
        "generated_from": "moiraweave-steps repository",
        "steps": [],
    }

    # Process each step directory
    for step_dir in sorted(steps_dir.iterdir()):
        if not step_dir.is_dir():
            continue

        step_yaml_path = step_dir / "step.yaml"
        schema_path = step_dir / "schema.json"
        version_path = step_dir / "VERSION"

        if not step_yaml_path.exists():
            print(f"Warning: step.yaml not found in {step_dir}")
            continue

        # Load step metadata
        try:
            step_yaml = yaml.safe_load(step_yaml_path.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"Warning: failed to parse {step_yaml_path}: {e}")
            continue

        step_name = step_yaml.get("name", step_dir.name)
        task_name = step_yaml.get("task", "unknown")
        description = step_yaml.get("description", "")

        # Read version
        if version_path.exists():
            version = version_path.read_text(encoding="utf-8").strip()
        else:
            version = "0.1.0"

        # Load task schema if available
        task_schema = None
        if tasks_dir.exists():
            task_schema_path = tasks_dir / task_name / "schema.json"
            if task_schema_path.exists():
                try:
                    task_schema = json.loads(
                        task_schema_path.read_text(encoding="utf-8")
                    )
                except Exception as e:
                    print(f"Warning: failed to parse {task_schema_path}: {e}")

        step_entry: dict[str, Any] = {
            "name": step_name,
            "version": version,
            "task": task_name,
            "description": description,
            "path": str(step_dir.relative_to(repo_root)),
            "min_runtime_version": "0.1.0",
            "image_uri": f"ghcr.io/moiraweave-labs/moiraweave-step-{step_name}:v{version}",
        }

        # Add task schema if available
        if task_schema:
            step_entry["task_contract"] = {
                "inputs": task_schema.get("inputs", []),
                "outputs": task_schema.get("outputs", []),
            }

        catalog["steps"].append(step_entry)

    return catalog


def main() -> int:
    """Main entrypoint."""
    repo_root = pathlib.Path.cwd()

    # Generate catalog
    catalog = generate_catalog(repo_root)

    # Write catalog.yaml
    catalog_yaml_path = repo_root / "catalog.yaml"
    catalog_yaml_path.write_text(yaml.safe_dump(catalog, sort_keys=False), encoding="utf-8")
    print(f"Generated {catalog_yaml_path}")

    # Write catalog.json
    catalog_json_path = repo_root / "catalog.json"
    catalog_json_path.write_text(
        json.dumps(catalog, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Generated {catalog_json_path}")

    print(f"Catalog contains {len(catalog['steps'])} steps")
    for step in catalog["steps"]:
        print(f"  - {step['name']}@{step['version']} ({step['task']})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
