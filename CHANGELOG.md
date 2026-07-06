# Changelog

All notable changes to this curated list are documented here.
The list's data (stars, releases) is refreshed daily by CI; this changelog tracks
structural and editorial changes.

## [Unreleased]

### Added
- Coverage sweep (2026-07-06) added **6 verified gateways** the list was missing — led by
  the two glaring high-star gaps **[OmniRoute](https://github.com/diegosouzapw/OmniRoute)**
  (~12k★, coding-agent token-saver) and **[Chat Nio / CoAI](https://github.com/coaidev/coai)**
  (~9.2k★, multi-tenant billing panel) — plus **Traceloop Hub** (Rust/OTel), and the routers
  **workweave/router**, **UncommonRoute** and **OrcaRouter Lite**. Each verified live via the
  GitHub API (stars, license, activity) before listing; all release-tracked.
- Directory grown to **~122 entries** since 1.0.0. A multi-agent accuracy/coverage audit
  added **17 verified gateways** — including the previously-missing high-star projects
  **CLIProxyAPI**, **sub2api**, **9router** and **NVIDIA Dynamo**, plus enterprise/cloud
  vendors **Axway Amplify**, **Red Hat Connectivity Link**, **Sensedia** and
  **Tencent Cloud AI Gateway** — each with honest risk/maintenance caveats.
- **Bilingual high-intent guide cluster** (EN + Simplified Chinese): *LiteLLM vs OpenRouter*,
  *OpenRouter alternatives*, *self-hosted gateways*, and *how to cut LLM API costs* —
  cross-linked with an interactive **cost calculator** and **gateway picker**.
- First inbound community contribution — **nullsink** added by
  [@c99e](https://github.com/c99e) in [#14](https://github.com/cuihuan/awesome-ai-gateway/pull/14). 🙏
- **CoderPlan** (China-market relay) added by [@onepaperbox](https://github.com/onepaperbox) in
  [#21](https://github.com/cuihuan/awesome-ai-gateway/pull/21) — endpoint independently re-verified
  (`api.coderplan.ai/v1` → `new_api_error`, i.e. new-api-based) before listing, with the standard
  new-and-unverified caveat. 🙏
- **KeepRouter** (OpenAI+Anthropic-compatible gateway, native `/v1/messages`) added by
  [@Digidai](https://github.com/Digidai) in [#22](https://github.com/cuihuan/awesome-ai-gateway/pull/22)
  — live endpoint verified before merge; CoderPlan + KeepRouter also added to the relay watch-list. 🙏

### Changed
- Account-less / crypto-only relays (**Loop Gateway**, **nullsink**) now carry an explicit
  "new & unverified" caveat and sit on the community relay watch-list, matching the FlintAPI
  precedent — listed on evidence, with the resale/recourse risk stated plainly.
- Marked **TensorZero** (archived June 2026) and **Pydantic AI Gateway** (merged into
  Pydantic Logfire) as deprecated/renamed — both verified `archived` via the GitHub API.

### Contributors
Thanks to [@c99e](https://github.com/c99e), [@onepaperbox](https://github.com/onepaperbox) and
[@Digidai](https://github.com/Digidai) for community PRs. Spotted a gateway we're missing, or run
one in production? See [CONTRIBUTING](CONTRIBUTING.md) — most additions are a 2-line PR.

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
- Bilingual **English + Simplified Chinese** throughout; interactive companion site on GitHub Pages.

### Infrastructure
- Daily GitHub Actions refresh of star counts and latest releases.
- CI: 69 unit tests, cost-table/CSV drift checks, advisory awesome-lint, and link-health
  checking (lychee) on PRs and weekly.

[1.0.0]: https://github.com/cuihuan/awesome-ai-gateway/releases/tag/v1.0.0
