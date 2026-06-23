# Changelog

All notable changes to this curated list are documented here.
The list's data (stars, releases) is refreshed daily by CI; this changelog tracks
structural and editorial changes.

## [1.0.0] - 2026-06-18

First tagged release. The list is stable, bilingual, and CI-verified.

### Added
- Pain-point-organized directory of **100+ AI gateways / LLM proxies** across 9 categories
  (cost-first, self-hosted, enterprise & compliance, first-party clouds, China ecosystem,
  MCP & agent gateways, and cross-cutting routing/observability).
- **Decision tree** ("which gateway should I use?") plus a 10-second fast-answer table.
- **Reproducible cost benchmark** — a unit-tested Python script computes per-task token costs
  from open pricing JSON (the 106× spread is recomputed, not hand-typed).
- **Gateway scorecard** — compliance / price / security / stability scored ★1–5 against a
  published rubric, with honest CVE disclosure.
- **Evidence-based gray-relay exclusion** citing measurement papers, plus `canary_check.py`,
  a runnable model-fidelity checker, and a community relay watch-list process.
- **6 deep-dive comparison pages** (LiteLLM/OpenRouter/Portkey, LiteLLM alternatives,
  OpenRouter alternatives, Cloudflare vs Vercel, best self-hosted, one-api vs new-api).
- Bilingual **English + 简体中文** throughout; interactive companion site on GitHub Pages.

### Infrastructure
- Daily GitHub Actions refresh of star counts and latest releases.
- CI: 69 unit tests, cost-table/CSV drift checks, advisory awesome-lint, and link-health
  checking (lychee) on PRs and weekly.

[1.0.0]: https://github.com/cuihuan/awesome-ai-gateway/releases/tag/v1.0.0
