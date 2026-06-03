"""Build verfication script for the DevSecOps PR automation lab."""


from __future__ import annotations

import sys
from pathlib import Path

REQUIRED_PATHS = [
    "src/pr_automation/__init__.py",
    "src/pr_automation/workflow.py",
    "src/pr_automation/cli.py",
    "tests/test_workflow.py",
    ".github/workflows/pr-validation.yml",
    ".github/workflows/security-scans.yml",
]


def main() -> int:
    repo_root = Path.cwd()
    missing = [path for path in REQUIRED_PATHS if not (repo_root / path).exists()]


    if missing:
        print("Build verification failed. Missing required files:")
        for path in missing:
            print(f"- {path}")
            return 1
        

    print("Build verifcation passed. Python repository structure is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())