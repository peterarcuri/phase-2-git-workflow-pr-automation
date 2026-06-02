# Security Controls

This repository demonstrates security guardrails inside the pull request lifecycle.

## SAST

CodeQL and Bandit are used to detect insecure coding patterns before code is merged.

## Secret Detection

TruffleHog scans for accidental credential exposure.

Examples of secrets that should never be committed:

- API keys
- passwords
- private tokens
- cloud access keys
- database credentials

## SCA

Dependency scanning is performed with `pip-audit`, with optional Snyk support.

## Trivy

Trivy performs filesystem scanning for vulnerabilities and misconfigurations.

## Branch Protection

Branch protection helps enforce:

- pull request reviews
- required status checks
- restricted direct pushes
- consistent review workflows

## Secure SDLC Value

These controls demonstrate shift-left security by identifying quality and security issues before merge.
