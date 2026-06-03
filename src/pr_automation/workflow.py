"""Core validation logic for a secure PR automation workflow."""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass

BRANCH_PATTERN = re.compile(r"^(feature|bugfix|hotfix|release)/[a-z0-9._-]+$")
ALLOWED_TARGET_BRANCHES = {"develop", "main"}


@dataclass(frozen=True)
class PullRequestChecks:
    """Represents required quality and security checks for merge readiness."""

    branch_policy_passed: bool
    lint_passed: bool
    tests_passed: bool
    build_passed: bool
    sast_passed: bool
    secrets_scan_passed: bool
    dependency_scan_passed: bool

    def all_passed(self) -> bool:
        """Return True only when every required PR guardrail has passed."""
        return all(asdict(self).values())


def validate_branch_name(branch_name: str) -> bool:
    """Validate GitFlow-style branch names."""
    return bool(BRANCH_PATTERN.fullmatch(branch_name.strip()))


def validate_target_branch(target_branch: str) -> bool:
    """Return True when a PR targets an allowed protected branch."""
    return target_branch.strip() in ALLOWED_TARGET_BRANCHES


def get_pull_request_readiness(checks: PullRequestChecks) -> bool:
    """Determine whether a pull request is ready to merge."""
    return checks.all_passed()


def generate_check_summary(
    branch_name: str,
    target_branch: str,
    checks: PullRequestChecks,
) -> dict:
    """Generate a simple PR status summary."""
    return {
        "branch": branch_name,
        "target_branch": target_branch,
        "branch_name_valid": validate_branch_name(branch_name),
        "target_branch_valid": validate_target_branch(target_branch),
        "checks": asdict(checks),
        "merge_ready": validate_branch_name(branch_name)
        and validate_target_branch(target_branch)
        and checks.all_passed(),
    }
