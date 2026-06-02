# Trunk-Based Development Workflow

This project primarily demonstrates a GitFlow-style workflow, but also documents how the same DevSecOps guardrails can support trunk-based development.

## What Is Trunk-Based Development?

Trunk-based development is a source control strategy where developers integrate small changes frequently into a single primary branch, usually `main`.

Instead of long-lived feature branches, developers use short-lived branches that are merged quickly after automated checks pass.

## Branch Strategy

```text
main
feature/small-change
bugfix/small-fix
hotfix/urgent-patch