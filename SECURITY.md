# Security Policy

## Reporting a vulnerability

Please report security issues **privately** via GitHub's
[private vulnerability reporting](https://github.com/cuihuan/awesome-ai-gateway/security/advisories/new)
rather than opening a public issue. We aim to acknowledge reports within a few days.

## Scope

This repository is a curated list plus a small data pipeline:

- **Scripts** (`scripts/*.py`) run in GitHub Actions and process first-party,
  public data (open pricing/benchmark JSON) and the public GitHub API. They are
  unit-tested and take no untrusted runtime input.
- **The site** (`index.html`, `compare/*.html`) is static and loads only
  first-party, CC0 data files from this repo.

This project does **not** handle user secrets, API keys, or production traffic.

## Out of scope

Vulnerabilities in the third-party AI gateways *listed* here belong to those
upstream projects — please report them to the respective maintainers. If a
listed relay is serving a swapped/poisoned model or harvesting data, that is a
**content** report: open a
[watch-list report](https://github.com/cuihuan/awesome-ai-gateway/issues/new?template=report-relay.yml)
with evidence (e.g. `scripts/canary_check.py` output).
