# Phase 2 — Git Workflow & PR Automation

Automated Git branching, pull request validation, and security scanning pipeline built as part of my DevSecOps Engineering portfolio.

This project demonstrates how modern DevSecOps teams integrate security, quality assurance, and governance controls directly into the pull request lifecycle using GitHub Actions, automated testing, and security scanning.


---

# Project Overview

The goal of this repository is to demonstrate secure software delivery practices beyond basic Git usage.

The workflow implements:

* GitFlow branching strategy
* Pull request validation pipelines
* Automated code quality enforcement
* Security scanning automation
* Dependency vulnerability management
* Branch protection and governance controls

This project is part of Phase 2 of my DevSecOps Engineering roadmap focused on CI/CD automation and secure code promotion.


---

# Architecture

```text
Developer
    ↓
Feature Branch
    ↓
Pull Request
    ↓
GitHub Actions
    ├── Ruff Linting
    ├── Pytest
    ├── Build Verification
    ├── TruffleHog
    ├── Bandit
    ├── CodeQL
    ├── pip-audit
    └── Trivy
    ↓
Protected Branch
```

---

# Technologies Used

## Version Control

* Git
* GitHub
* GitFlow Workflow

## CI/CD

* GitHub Actions

## Code Quality

* Ruff
* Pytest

## Security

* Bandit
* CodeQL
* TruffleHog
* pip-audit
* Trivy

## Language

* Python 3

---

# Security Controls Implemented

### Static Application Security Testing (SAST)

* Bandit
* CodeQL

### Secret Detection

* TruffleHog

### Software Composition Analysis (SCA)

* pip-audit

### Filesystem Vulnerability Scanning

* Trivy

### Governance Controls

* Branch Protection Rules
* Pull Request Reviews
* Required Status Checks
* Protected Branches

---

# Branching Strategy

This repository demonstrates GitFlow concepts:

```text
main
 │
 └── develop
        │
        ├── feature/*
        ├── bugfix/*
        ├── hotfix/*
        └── release/*
```

Feature branches are validated through pull requests before promotion into protected branches.

---

# Project Structure

![Project Structure](screenshots/project-file-tree-gitflow.png)

The repository is organized into source code, testing, automation, workflow configuration, documentation, and security validation components.

---

# CI/CD Validation

## Ruff Code Quality Checks

![Ruff Validation](screenshots/ruff-lint-passing.png)

Automated linting ensures code quality and consistency before code promotion.

---

## Pytest Validation

![Pytest Validation](screenshots/pytest-passing-gitflow.png)

Unit tests validate pull request logic, branch policy enforcement, and merge readiness requirements.

---

## Build Verification

![Build Verification](screenshots/build-verification-gitflow.png)

Build validation ensures repository integrity and required project structure.

---

# Security Validation

## Bandit SAST Scan

![Bandit Security Scan](screenshots/bandit-security-scan-gitflow.png)

Static analysis identifies insecure coding patterns and security misconfigurations.

---

## GitHub Actions Security Pipeline

![Security Scans](screenshots/security-scans-gitflow.png)

The security pipeline automatically executes:

* TruffleHog
* Bandit
* CodeQL
* pip-audit
* Trivy

during every pull request.

---

# Pull Request Lifecycle

## Pull Request Creation

![Pull Request Creation](screenshots/create-pull-request-gitflow.png)

Feature branches are promoted through pull requests for automated validation and review.

---

## Pull Request Validation Running

![PR Validation Running](screenshots/pr-checks-running.png)

GitHub Actions automatically executes validation and security checks.

---

## Validation Success

![Validation Success](screenshots/validation-success-gitflow.png)

All quality and security controls must pass before merge approval.

---

## Pull Request Ready for Merge

![Merge Ready](screenshots/pr-ready-for-merge.png)

Successful completion of all required checks results in merge eligibility.

---

# Branch Governance

## GitHub Actions Workflows

![GitHub Actions Workflows](screenshots/github-actions-workflows.png)

Multiple workflows enforce validation, security scanning, and pull request automation.

---

## Branch Protection Rules

![Branch Protection Rules](screenshots/branch-protection-ruleset.png)

Protected branches enforce:

* Pull request reviews
* Approval requirements
* Required status checks
* Force push prevention
* Branch deletion protection

---

# Skills Demonstrated

* GitFlow Branching Strategy
* Pull Request Automation
* GitHub Actions CI/CD
* Branch Protection Rules
* Static Application Security Testing (SAST)
* Secret Detection
* Software Composition Analysis (SCA)
* Vulnerability Management
* Secure Code Promotion
* Shift-Left Security
* DevSecOps Automation

---

# Results

Successfully implemented a secure pull request workflow that:

* Enforces automated code quality validation
* Executes security scans before merge approval
* Prevents insecure code promotion
* Demonstrates modern DevSecOps CI/CD practices
* Implements governance controls through protected branches

This project provides a practical example of integrating security directly into the software development lifecycle using GitHub Actions and automated DevSecOps controls.


# Screenshots

## Project Structure

Shows the overall repository organization, including GitHub Actions workflows, Python source code, tests, documentation, and security configuration.

![Project Structure](screenshots/project-file-tree-gitflow.png)

---

## Ruff Code Quality Validation

All Ruff linting checks passing successfully.

![Ruff Lint Passing](screenshots/ruff-lint-passing.png)

---

## Pytest Test Suite

All automated unit tests passing successfully.

![Pytest Passing](screenshots/pytest-passing-gitflow.png)

---

## Build Verification

Repository structure validation and build verification passing successfully.

![Build Verification](screenshots/build-verification-gitflow.png)

---

## Bandit Security Scan

Static Application Security Testing (SAST) scan completed with no security findings.

![Bandit Security Scan](screenshots/bandit-security-scan-gitflow.png)

---

## GitHub Actions Workflows

Configured GitHub Actions workflows for pull request validation, security scanning, and PR automation.

![GitHub Actions Workflows](screenshots/github-actions-workflows.png)

---

## Pull Request Creation

Creating a GitFlow-style pull request from a feature branch.

![Pull Request Creation](screenshots/create-pull-request-gitflow.png)

---

## Pull Request Checks Running

Automated CI/CD validation and security checks executing against the pull request.

![PR Checks Running](screenshots/pr-checks-running.png)

---

## Pull Request Validation Success

Pull request validation workflow completed successfully.

![Validation Success](screenshots/validation-success-gitflow.png)

---

## Security Scan Success

All security controls completed successfully including:

* TruffleHog
* Bandit
* CodeQL
* pip-audit
* Trivy

![Security Scans Success](screenshots/security-scans-gitflow.png)

---

## Branch Protection Ruleset

Repository governance controls protecting critical branches.

![Branch Protection Ruleset](screenshots/branch-protection-ruleset.png)

---

## Pull Request Ready For Merge

All required checks passed and pull request approved for merge.

![PR Ready For Merge](screenshots/pr-ready-for-merge.png)
