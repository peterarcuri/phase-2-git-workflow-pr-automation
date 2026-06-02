
from pr_automation import (
    PullRequestChecks,
    generate_check_summary,
    get_pull_request_readiness,
    validate_branch_name,
    validate_target_branch,
)


def passing_checks() -> PullRequestChecks:
    return PullRequestChecks(
        branch_policy_passed=True,
        lint_passed=True,
        tests_passed=True,
        build_passed=True,
        sast_passed=True,
        secrets_scan_passed=True,
        dependency_scan_passed=True,
    )


def test_accepts_valid_gitflow_branch_names():
    assert validate_branch_name("feature/add-security-workflow") is True
    assert validate_branch_name("bugfix/fix-ci-lint") is True
    assert validate_branch_name("hotfix/patch-secret-scan") is True
    assert validate_branch_name("release/v1.0.0") is True


def test_rejects_invalid_or_unsafe_branch_names():
    assert validate_branch_name("main") is False
    assert validate_branch_name("dev") is False
    assert validate_branch_name("feature/Add Security Workflow") is False
    assert validate_branch_name("security-update") is False
    assert validate_branch_name("feature/add security workflow") is False


def test_validates_allowed_target_branches():
    assert validate_target_branch("develop") is True
    assert validate_target_branch("main") is True
    assert validate_target_branch("production") is True


def test_pr_requires_all_guardrails_to_pass():
    assert get_pull_request_readiness(passing_checks()) is True

    failing_checks = PullRequestChecks(
        branch_policy_passed=True,
        lint_passed=True,
        tests_passed=True,
        build_passed=True,
        sast_passed=True,
        secrets_scan_passed=True,
        dependency_scan_passed=True,
    )

    assert get_pull_request_readiness(failing_checks) is False


def test_generates_merge_summary():
    summary = generate_check_summary("feature/add-pr-automation", "develop", passing_checks())

    assert summary["branch_name_valid"] is True
    assert summary["target_branch_valid"] is True
    assert summary["merge_ready"] is True
    assert summary["checks"]["sast_passed"] is True

