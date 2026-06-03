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



# Screenshots & Project Demonstration

The screenshots below document the complete implementation of a secure Git workflow with automated CI/CD validation, security scanning, and branch governance controls.

These artifacts demonstrate how quality assurance and security controls can be integrated directly into the pull request lifecycle using GitHub Actions and modern DevSecOps practices.

---

## Repository Architecture

### Project Structure

**Screenshot:** `screenshots/project-file-tree-gitflow.png`

Shows the complete repository structure including:

* GitHub Actions workflows
* Python source code
* Unit tests
* Security documentation
* Configuration files
* Sample outputs

This demonstrates proper project organization and maintainability standards commonly used in DevOps and DevSecOps environments.

---

## Local Validation Pipeline

### Ruff Code Quality Validation

**Screenshot:** `screenshots/ruff-lint-passing.png`

Ruff performs automated static code quality analysis before code enters the CI pipeline.

Validation includes:

* Import organization
* Style consistency
* Code quality enforcement
* Python best practices

This serves as the first quality gate within the software delivery process.

---

### Automated Unit Testing

**Screenshot:** `screenshots/pytest-passing-gitflow.png`

Pytest validates application behavior and pull request logic.

Tests verify:

* Branch validation logic
* Pull request readiness evaluation
* Security guardrail enforcement
* Merge eligibility requirements

This ensures application functionality remains stable as new code is introduced.

---

### Build Verification

**Screenshot:** `screenshots/build-verification-gitflow.png`

Validates repository structure and required project components.

Verification includes:

* Source code validation
* Test file validation
* Required configuration checks
* Repository integrity verification

This prevents incomplete or malformed project structures from entering the pipeline.

---

## Security Validation

### Static Application Security Testing (SAST)

**Screenshot:** `screenshots/bandit-security-scan-gitflow.png`

Bandit performs automated static security analysis against the Python codebase.

Security controls include:

* Detection of insecure coding practices
* Identification of common security weaknesses
* Security-focused code review automation

This demonstrates implementation of Shift-Left Security principles.

---

## Continuous Integration & Pull Request Workflow

### GitHub Actions Workflow Overview

**Screenshot:** `screenshots/github-actions-workflows.png`

Shows the repository's GitHub Actions workflows responsible for:

* Pull request validation
* Security scanning
* Pull request automation

These workflows enforce quality and security requirements before code can be merged.

---

### Pull Request Creation

**Screenshot:** `screenshots/create-pull-request-gitflow.png`

Demonstrates the GitFlow branching strategy implemented within the repository.

Workflow:

```text
feature/*
    ↓
Pull Request
    ↓
develop
    ↓
main
```

This approach provides controlled integration and release management.

---

### Pull Request Validation In Progress

**Screenshot:** `screenshots/pr-checks-running.png`

Shows GitHub Actions executing validation and security checks against an active pull request.

Validation categories include:

* Branch policy enforcement
* Automated testing
* Security scanning
* Dependency auditing

This demonstrates automated governance during the review process.

---

### Pull Request Validation Success

**Screenshot:** `screenshots/validation-success-gitflow.png`

Shows successful completion of the Continuous Integration workflow.

Successful validation includes:

* Branch Naming Policy Validation
* Ruff Linting
* Unit Test Execution
* Build Verification

Only validated code is eligible for merge.

---

## Security Automation Pipeline

### Security Scan Success

**Screenshot:** `screenshots/security-scans-gitflow.png`

Shows successful completion of all automated security controls.

Implemented security tooling includes:

* TruffleHog Secret Detection
* Bandit SAST Analysis
* CodeQL Security Analysis
* pip-audit Software Composition Analysis (SCA)
* Trivy Filesystem Security Scanning

These controls help identify vulnerabilities before code reaches protected branches.

---

## Repository Governance

### Branch Protection Rulesets

**Screenshot:** `screenshots/branch-protection-ruleset.png`

Shows repository governance controls protecting critical branches.

Implemented protections include:

* Pull request requirement
* Approval requirement
* Force push prevention
* Branch deletion protection

These controls reduce risk and ensure proper review procedures are followed.

---

## Merge Readiness

### Pull Request Ready For Merge

**Screenshot:** `screenshots/pr-ready-for-merge.png`

Shows a pull request after all validation and security requirements have successfully completed.

This represents the final state of the DevSecOps workflow:

```text
Feature Branch
      ↓
Pull Request
      ↓
CI Validation
      ↓
Security Scanning
      ↓
Governance Verification
      ↓
Merge Ready
```

Only code that successfully passes all required controls becomes eligible for integration into protected branches.

---

# DevSecOps Capabilities Demonstrated

This project demonstrates practical implementation of:

* GitFlow Branching Strategy
* Pull Request Automation
* GitHub Actions CI/CD Pipelines
* Branch Protection Rules
* Automated Code Quality Validation
* Unit Testing Automation
* Static Application Security Testing (SAST)
* Secret Detection
* Software Composition Analysis (SCA)
* Dependency Vulnerability Scanning
* Shift-Left Security Practices
* Secure Software Delivery Workflows
* Repository Governance Controls

Together, these controls provide a practical example of how modern DevSecOps teams integrate security, quality assurance, and governance directly into the software development lifecycle.


