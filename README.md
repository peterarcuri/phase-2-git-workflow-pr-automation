# phase-2-git-workflow-pr-automation
Automated Git branching and pull request validation pipeline integrating automated security scanning and compliance checks for secure code promotion


# Phase 2 — Git Workflow & PR Automation

A secure Git workflow and pull request automation lab built for a DevSecOps engineering portfolio.

This repository demonstrates how modern DevSecOps teams can enforce quality, security, and review guardrails directly inside the GitHub pull request lifecycle using a Python-based sample project.

---

## Project Purpose

The goal of this repository is to move beyond basic Git commits and demonstrate a production-style workflow using:

- GitFlow-style branching
- automated pull request creation
- continuous integration checks
- Python linting and unit testing
- static application security testing
- secret detection
- dependency vulnerability scanning
- branch protection policies
- required status checks before merge

This project is part of my Phase 2 DevSecOps Engineering roadmap focused on DevOps, CI/CD, automation, and secure software delivery.

---

## Key Features

- Automated PR creation from GitFlow branches
- Branch naming validation
- Python linting with Ruff
- Unit testing with Pytest
- Build verification script
- SAST with CodeQL and Bandit
- Secret detection with TruffleHog
- SCA with pip-audit
- Filesystem vulnerability scanning with Trivy
- Branch protection policy documentation

---

## Supported Branch Patterns

```text
feature/add-login-validation
bugfix/fix-ci-test-failure
hotfix/remove-exposed-secret
release/v1.0.0

This project documents two common Git strategies:

1. **GitFlow**
   - Uses `main` and `develop`
   - Feature branches merge into `develop`
   - Release branches prepare production-ready code

2. **Trunk-Based Development**
   - Uses `main` as the primary integration branch
   - Developers work in short-lived branches
   - Pull requests merge quickly after automated checks pass


GitFlow screenshot demo
