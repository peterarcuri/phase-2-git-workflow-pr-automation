# Branch Protection Rules

Recommended GitHub branch protection settings for `main` and `develop`.

## Require Pull Requests

Enable:

- Require a pull request before merging
- Require approvals
- Dismiss stale pull request approvals when new commits are pushed
- Require review from code owners if CODEOWNERS is added later

## Require Status Checks

Enable:

- Require status checks to pass before merging
- Require branches to be up to date before merging

Recommended required checks:

```text
Validate Branch Naming Policy
Lint, Test, and Build
Secret Detection - TruffleHog
SAST - CodeQL Analysis
SAST - Bandit Python Security Scan
SCA - Python Dependency Vulnerability Scan
Trivy Filesystem Scan