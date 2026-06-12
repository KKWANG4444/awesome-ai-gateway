# Awesome AI Gateway [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![GitHub stars](https://img.shields.io/github/stars/cuihuan/awesome-ai-gateway?style=social)](https://github.com/cuihuan/awesome-ai-gateway/stargazers)
[![Gateways](https://img.shields.io/badge/gateways-50%2B-blue)](#quick-comparison)
[![Data updated daily](https://img.shields.io/badge/data-updated%20daily-success?logo=githubactions&logoColor=white)](.github/workflows/daily-update.yml)
[![Evaluation set](https://img.shields.io/badge/📊-evaluation%20set-orange)](BENCHMARKS.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: CC0](https://img.shields.io/badge/license-CC0-lightgrey.svg)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/cuihuan/awesome-ai-gateway)](https://github.com/cuihuan/awesome-ai-gateway/commits/main)

> **The only AI-gateway list that _scores_ 50+ gateways and ships a reproducible cost benchmark — not just links.** Organized by what you actually need, not by vendor.

**50+ gateways scored** · **reproducible 106× cost benchmark** (unit-tested) · **4-axis scorecard** — compliance · price · security · stability · **bilingual EN/中文** · **auto-updated daily**

**Languages:** English · [简体中文](README.zh-CN.md)

<p align="center">
<a href="#which-gateway-should-i-use"><kbd> &nbsp; 🧭 Pick a gateway &nbsp; </kbd></a> &nbsp;
<a href="BENCHMARKS.md"><kbd> &nbsp; 📊 Cost & scorecard &nbsp; </kbd></a> &nbsp;
<a href="#quick-start-drop-in"><kbd> &nbsp; ⚡ Drop-in snippet &nbsp; </kbd></a>
</p>

<p align="center">
  <a href="BENCHMARKS.md"><img src="assets/cost-spread.png" alt="Cost to write one 100K-token report: $0.03 on DeepSeek vs $3.01 on GPT-5.5 — a 106x spread, computed by a unit-tested script" width="780"></a>
</p>

> The same task can cost **100× more** depending on the model behind your gateway. An **AI gateway** sits between your code and LLM providers — one endpoint, one key, many models — handling routing, failover, caching, rate limits, cost tracking and guardrails so you change a `base_url` instead of rewriting your app. This list helps you pick the right one, then the [evaluation set](BENCHMARKS.md) shows you which model to route to.

## Contents

- [📊 Evaluation set: model benchmarks · token cost · gateway scorecard](BENCHMARKS.md)
- [Which gateway should I use? (decision tree)](#which-gateway-should-i-use)
- [Quick start (drop-in)](#quick-start-drop-in)
- [Quick comparison](#quick-comparison)
- [💰 Cost-first: cheapest multi-model access](#-cost-first-cheapest-multi-model-access)
- [🔓 Self-hosted open source](#-self-hosted-open-source)
- [🏢 Enterprise & compliance](#-enterprise--compliance)
- [☁️ First-party gateways (cloud & model vendors)](#️-first-party-gateways-cloud--model-vendors)
- [🇨🇳 China ecosystem](#-china-ecosystem)
- [🧠 Smart routing & model selection](#-smart-routing--model-selection)
- [📊 Observability & cost tracking](#-observability--cost-tracking)
- [🤖 MCP & agent gateways](#-mcp--agent-gateways)
- [☸️ Kubernetes-native & inference infra](#️-kubernetes-native--inference-infra)
- [📰 What's new](#-whats-new)
- [🚀 Recent releases (auto-updated)](#-recent-releases-auto-updated)
- [Glossary](#glossary)
- [How to choose safely](#how-to-choose-safely)
- [FAQ](#faq)
- [Contributing](#contributing)

## Which gateway should I use?

```text
Do you want to self-host?
│
├─ NO — hosted, minimal ops
│   ├─ Cheapest access to many models ──────────▶ OpenRouter · Vercel AI Gateway (0% markup)
│   ├─ Free control plane over your own keys ───▶ Cloudflare AI Gateway
│   ├─ EU data residency matters ───────────────▶ Requesty · Eden AI · nexos.ai
│   └─ Already on one cloud ────────────────────▶ AWS Bedrock · Azure APIM · Vertex AI
│
└─ YES — self-hosted / open source
    ├─ Python stack, broadest features ─────────▶ LiteLLM
    ├─ Raw performance (Go/Rust/TS) ────────────▶ Bifrost · TensorZero · Portkey Gateway
    ├─ Built-in evals + observability ──────────▶ TensorZero · Helicone
    ├─ Key distribution / billing / CN models ──▶ new-api · one-api · GPT-Load
    ├─ Enterprise K8s, audit, guardrails ───────▶ Kong · Higress · APISIX · Envoy AI Gateway
    └─ Governing AI agents & MCP traffic ───────▶ agentgateway · Lunar.dev
```

## Quick start (drop-in)

The whole promise of a gateway: **change `base_url`, keep your OpenAI code.** Same request, now with routing, fallback, caching and cost tracking.

```python
from openai import OpenAI

# Hosted example — OpenRouter (400+ models, one key):
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-...",
)

# Self-hosted example — a LiteLLM proxy you run:
client = OpenAI(
    base_url="http://localhost:4000",
    api_key="sk-litellm-...",
)

resp = client.chat.completions.create(
    model="anthropic/claude-fable-5",        # ask the gateway for any provider's model
    messages=[{"role": "user", "content": "Hello!"}],
)
```

**OpenAI-compatible `base_url` cheat sheet** (verified June 2026 — swap in, keep your code):

| Gateway | `base_url` |
|---|---|
| OpenRouter | `https://openrouter.ai/api/v1` |
| Vercel AI Gateway | `https://ai-gateway.vercel.sh/v1` |
| Cloudflare AI Gateway | `https://gateway.ai.cloudflare.com/v1/{account}/{gateway}/compat` |
| Portkey | `https://api.portkey.ai/v1` |
| Helicone AI Gateway | `https://ai-gateway.helicone.ai/ai` |
| Requesty | `https://router.requesty.ai/v1` |
| LiteLLM (self-hosted) | `http://localhost:4000` |

## Quick comparison

Stars auto-refresh daily. ✅ built-in · ➕ via plugin/paid tier · ❌ not available.

| Project | Type | Stars | License | Multi-provider | Fallback / LB | Caching | Guardrails | Cost tracking |
|---|---|---|---|---|---|---|---|---|
| [LiteLLM](https://github.com/BerriAI/litellm) | OSS proxy + SDK | <!--s:BerriAI/litellm-->⭐ 50.1k<!--/s--> | MIT¹ | ✅ 100+ | ✅ | ✅ | ✅ | ✅ |
| [new-api](https://github.com/QuantumNous/new-api) | OSS relay/billing | <!--s:QuantumNous/new-api-->⭐ 38.4k<!--/s--> | AGPL-3.0 | ✅ | ✅ | ➕ | ➕ | ✅ |
| [one-api](https://github.com/songquanpeng/one-api) | OSS relay/billing | <!--s:songquanpeng/one-api-->⭐ 34.9k<!--/s--> | MIT | ✅ | ✅ | ❌ | ❌ | ✅ |
| [Kong AI Gateway](https://github.com/Kong/kong) | OSS API gateway | <!--s:Kong/kong-->⭐ 43.6k<!--/s--> | Apache-2.0 | ✅ | ✅ | ✅ semantic | ✅ | ✅ |
| [Apache APISIX](https://github.com/apache/apisix) | OSS API gateway | <!--s:apache/apisix-->⭐ 16.7k<!--/s--> | Apache-2.0 | ✅ | ✅ | ➕ | ➕ | ➕ |
| [Portkey Gateway](https://github.com/Portkey-AI/gateway) | OSS gateway + SaaS | <!--s:Portkey-AI/gateway-->⭐ 12k<!--/s--> | MIT | ✅ 1600+ | ✅ | ✅ | ✅ 50+ | ➕ SaaS |
| [TensorZero](https://github.com/tensorzero/tensorzero) | OSS LLMOps stack | <!--s:tensorzero/tensorzero-->⭐ 11.5k<!--/s--> | Apache-2.0 | ✅ | ✅ | ✅ | ➕ | ✅ |
| [Higress](https://github.com/higress-group/higress) | OSS AI-native gateway | <!--s:higress-group/higress-->⭐ 8.6k<!--/s--> | Apache-2.0 | ✅ | ✅ | ✅ | ✅ | ✅ |
| [GPT-Load](https://github.com/tbphp/gpt-load) | OSS key-pool proxy | <!--s:tbphp/gpt-load-->⭐ 6.2k<!--/s--> | MIT | ✅ | ✅ key rotation | ❌ | ❌ | ➕ |
| [Bifrost](https://github.com/maximhq/bifrost) | OSS gateway (Go) | <!--s:maximhq/bifrost-->⭐ 5.7k<!--/s--> | Apache-2.0 | ✅ | ✅ adaptive | ✅ | ✅ | ✅ |
| [Helicone](https://github.com/Helicone/helicone) | OSS observability + gateway | <!--s:Helicone/helicone-->⭐ 5.8k<!--/s--> | Apache-2.0 | ✅ | ✅ | ✅ | ➕ | ✅ |
| [Envoy AI Gateway](https://github.com/envoyproxy/ai-gateway) | OSS K8s gateway | <!--s:envoyproxy/ai-gateway-->⭐ 1.7k<!--/s--> | Apache-2.0 | ✅ | ✅ | ➕ | ➕ | ✅ |
| [OpenRouter](https://openrouter.ai) | SaaS marketplace | — | Commercial | ✅ 400+ | ✅ | ✅ | ➕ | ✅ |
| [Vercel AI Gateway](https://vercel.com/ai-gateway) | SaaS (0% markup) | — | Commercial | ✅ 100s | ✅ | ❌ | ❌ | ✅ |
| [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/) | SaaS control plane | — | Commercial (free tier) | ✅ | ✅ dynamic | ✅ | ✅ | ✅ budgets |

¹ LiteLLM core is MIT; the repo contains a separately licensed enterprise directory.

> 📂 **Browse the raw data** (machine-readable, CC0): [models & pricing JSON](data/models.json) · [cost table CSV](data/cost_table.csv) · [gateway scorecard CSV](data/gateways_scorecard.csv). Every cost cell is regenerated from this data by a [unit-tested script](scripts/cost_calc.py).

## 💰 Cost-first: cheapest multi-model access

*Pain point: "I want many models for the least money and zero ops."*

- [OpenRouter](https://openrouter.ai) — The dominant model marketplace: 400+ models behind one OpenAI-compatible API, pay-as-you-go with automatic failover; ~5.5% fee when buying credits. $113M Series B (May 2026), ~8M users.
- [Vercel AI Gateway](https://vercel.com/ai-gateway) — Hundreds of models at **provider list price (0% markup)**, $5/month free credits, zero-data-retention option; pairs naturally with the AI SDK.
- [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/) — Free control plane in front of your own provider keys: caching, dynamic routing, unified billing, and dollar-denominated spend limits (2026 beta).
- [Requesty](https://requesty.ai) — EU-friendly OpenRouter alternative: 400+ models, sub-20ms failover, ~5% markup.
- [Eden AI](https://www.edenai.co) — Unified API for 500+ models plus vision/OCR/speech; EU-based, ~5.5% platform fee.
- [Helicone AI Gateway (cloud)](https://www.helicone.ai) — Passthrough billing at **0% markup** with observability bundled.
- [GPT-Load](https://github.com/tbphp/gpt-load) <!--s:tbphp/gpt-load-->⭐ 6.2k<!--/s--> — High-performance Go proxy that rotates pools of API keys across channels to maximize quota usage.

> 💡 Squeeze more from any gateway: enable **semantic caching** (Kong, Bifrost, Zuplo), set **spend limits** (Cloudflare, Zuplo, Pydantic/Logfire), and route easy prompts to cheap models (see [Smart routing](#-smart-routing--model-selection)).

## 🔓 Self-hosted open source

*Pain point: "My keys, my infra, no per-token middleman fee."*

- [LiteLLM](https://github.com/BerriAI/litellm) <!--s:BerriAI/litellm-->⭐ 50.1k<!--/s--> — The default choice: Python SDK + proxy server speaking OpenAI format to 100+ providers, with virtual keys, budgets, load balancing and guardrails.
- [Portkey Gateway](https://github.com/Portkey-AI/gateway) <!--s:Portkey-AI/gateway-->⭐ 12k<!--/s--> — Fast TypeScript gateway (1,600+ models, 50+ guardrails) that also powers Portkey's commercial LLMOps platform.
- [TensorZero](https://github.com/tensorzero/tensorzero) <!--s:tensorzero/tensorzero-->⭐ 11.5k<!--/s--> — Rust gateway unified with observability, evals, experimentation and optimization — built around a data/feedback flywheel.
- [Bifrost](https://github.com/maximhq/bifrost) <!--s:maximhq/bifrost-->⭐ 5.7k<!--/s--> — Go gateway from Maxim AI claiming ~50x LiteLLM throughput; adaptive load balancing, cluster mode, MCP support.
- [Helicone](https://github.com/Helicone/helicone) <!--s:Helicone/helicone-->⭐ 5.8k<!--/s--> — Observability-first platform (YC W23) with a Rust [ai-gateway](https://github.com/Helicone/ai-gateway) <!--s:Helicone/ai-gateway-->⭐ 600<!--/s-->.
- [Plano](https://github.com/katanemo/plano) <!--s:katanemo/plano-->⭐ 6.6k<!--/s--> — AI-native proxy and data plane for agents (formerly Arch Gateway / archgw).
- [LLM Gateway](https://github.com/theopenco/llmgateway) <!--s:theopenco/llmgateway-->⭐ 1.3k<!--/s--> — Open-source OpenRouter alternative: route, manage and analyze requests across providers.
- [APIPark](https://github.com/APIParkLab/APIPark) <!--s:APIParkLab/APIPark-->⭐ 1.8k<!--/s--> — Cloud-native LLM API management and distribution platform.
- [Pydantic AI Gateway](https://github.com/pydantic/pydantic-ai-gateway) <!--s:pydantic/pydantic-ai-gateway-->⭐ 189<!--/s--> — BYOK gateway with cost caps and OTel, now folded into Pydantic Logfire.
- [OptiLLM](https://github.com/algorithmicsuperintelligence/optillm) <!--s:algorithmicsuperintelligence/optillm-->⭐ 4.1k<!--/s--> — Optimizing inference proxy that boosts accuracy via test-time compute techniques.
- [aisuite](https://github.com/andrewyng/aisuite) <!--s:andrewyng/aisuite-->⭐ 13.8k<!--/s--> — Andrew Ng's unified multi-provider client. A library rather than a deployable proxy — fits when you don't want network hops.
- ⚠️ Stale but historically notable: [BricksLLM](https://github.com/bricks-cloud/BricksLLM) <!--s:bricks-cloud/BricksLLM-->⭐ 1.2k<!--/s--> (PII masking, per-key limits; inactive since early 2025), [Glide](https://github.com/EinStack/glide) <!--s:EinStack/glide-->⭐ 160<!--/s--> (inactive since 2024).

## 🏢 Enterprise & compliance

*Pain point: "Audit logs, PII redaction, RBAC, on-prem, and the EU AI Act (enforceable Aug 2026)."*

- [Kong AI Gateway](https://github.com/Kong/kong) <!--s:Kong/kong-->⭐ 43.6k<!--/s--> — Mature API gateway with AI plugins: semantic caching/routing, prompt guard, token rate-limiting; Konnect for managed control plane.
- [Apache APISIX](https://github.com/apache/apisix) <!--s:apache/apisix-->⭐ 16.7k<!--/s--> — Cloud-native API + AI gateway with `ai-proxy` / `ai-proxy-multi` plugins.
- [Envoy AI Gateway](https://github.com/envoyproxy/ai-gateway) <!--s:envoyproxy/ai-gateway-->⭐ 1.7k<!--/s--> — CNCF-aligned GenAI access on Envoy Gateway, backed by Tetrate and Bloomberg.
- [kgateway](https://github.com/kgateway-dev/kgateway) <!--s:kgateway-dev/kgateway-->⭐ 5.6k<!--/s--> — CNCF API/AI gateway, the base of Solo.io's commercial [Gloo AI Gateway](https://www.solo.io).
- [TrueFoundry AI Gateway](https://www.truefoundry.com) — Enterprise gateway with routing, guardrails and RBAC, deployable into your K8s/VPC.
- [nexos.ai](https://nexos.ai) — Enterprise AI gateway/orchestration from the Nord Security founders (€30M Series A, Oct 2025).
- [Tyk AI Studio](https://tyk.io) — AI governance suite: budgets, model catalogs, guardrails on Tyk's gateway.
- [Gravitee Agent Mesh](https://www.gravitee.io) — LLM Proxy, MCP Proxy and A2A support inside Gravitee APIM.
- [WSO2 AI Gateway](https://wso2.com/api-manager/usecases/ai-gateway/) — Egress management for LLM traffic: model routing, semantic caching, guardrails.
- [F5 AI Gateway](https://www.f5.com) — Containerized AI traffic gateway; data-leakage detection via the LeakSignal acquisition (Nov 2025).
- [IBM API Connect AI Gateway](https://www.ibm.com) — Policy enforcement, masking and audit for LLM traffic.
- [MuleSoft AI / Omni Gateway](https://www.mulesoft.com/platform/ai-gateway) — Governs LLM, MCP and agent traffic alongside classic APIs.
- [Lunar.dev](https://github.com/TheLunarCompany/lunar) <!--s:TheLunarCompany/lunar-->⭐ 454<!--/s--> — Egress consumption gateway repositioned around MCP/agent governance.

## ☁️ First-party gateways (cloud & model vendors)

*Pain point: "We're already committed to one cloud — give us the native path."*

- [AWS Bedrock](https://aws.amazon.com/bedrock/) — Multi-model access via the unified Converse API, cross-region inference, and AgentCore Gateway for tools/MCP.
- [Azure API Management — GenAI gateway](https://learn.microsoft.com/azure/api-management/genai-gateway-capabilities) — Token limits, semantic caching and load balancing in front of Azure OpenAI / AI Foundry.
- [Google Apigee + Vertex AI](https://cloud.google.com/apigee) — LLM gateway patterns on Apigee with Vertex Model Garden as the managed hub.
- [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/) — See [Cost-first](#-cost-first-cheapest-multi-model-access); the strongest free first-party option.
- [Vercel AI Gateway](https://vercel.com/ai-gateway) — GA, 0% markup, ZDR option; the default for Next.js/AI SDK shops.
- [Databricks Unity AI Gateway](https://www.databricks.com) — Mosaic AI Gateway folded into Unity Catalog, adding agent + MCP governance.

## 🇨🇳 China ecosystem

*Pain point: "Domestic models (Qwen/DeepSeek/GLM/Kimi), CNY payment, key distribution & billing for teams."*

- [new-api](https://github.com/QuantumNous/new-api) <!--s:QuantumNous/new-api-->⭐ 38.4k<!--/s--> — The most active one-api fork, now a "unified AI model hub": protocol conversion, billing, Rerank/Realtime endpoints. AGPL-3.0.
- [one-api](https://github.com/songquanpeng/one-api) <!--s:songquanpeng/one-api-->⭐ 34.9k<!--/s--> — The original LLM API 管理&分发系统 (OpenAI/Azure/Claude/Gemini/DeepSeek/豆包…); development has slowed.
- [Higress](https://github.com/higress-group/higress) <!--s:higress-group/higress-->⭐ 8.6k<!--/s--> — Alibaba's AI-native gateway on Envoy/Istio, first-class 通义/DeepSeek support; hosted version at higress.ai.
- [GPT-Load](https://github.com/tbphp/gpt-load) <!--s:tbphp/gpt-load-->⭐ 6.2k<!--/s--> — 智能密钥轮询 multi-channel proxy in Go.
- [one-hub](https://github.com/MartialBE/one-hub) <!--s:MartialBE/one-hub-->⭐ 2.8k<!--/s--> — one-api fork with better non-OpenAI function calling and stats.
- [simple-one-api](https://github.com/fruitbars/simple-one-api) <!--s:fruitbars/simple-one-api-->⭐ 2.3k<!--/s--> — Single binary adapting 千帆/星火/混元/MiniMax/DeepSeek to the OpenAI interface.
- [Veloera](https://github.com/Veloera/Veloera) <!--s:Veloera/Veloera-->⭐ 1.6k<!--/s--> — Newer relay platform in the one-api/new-api lineage.
- [uni-api](https://github.com/yym68686/uni-api) <!--s:yym68686/uni-api-->⭐ 1.2k<!--/s--> — Lightweight single-config unified API manager, no frontend.
- [APIPark](https://github.com/APIParkLab/APIPark) <!--s:APIParkLab/APIPark-->⭐ 1.8k<!--/s--> — China-origin, cloud-native AI & API gateway with an open developer portal.

> ⚠️ This list deliberately **excludes reverse-engineered "free-api" relays** (ToS violations, account risk). For commercial 中转站 price comparisons, see [awesome-ai-api-proxy](https://github.com/howardpen9/awesome-ai-api-proxy).

## 🧠 Smart routing & model selection

*Pain point: "Send each prompt to the cheapest model that can handle it."*

- [Not Diamond](https://www.notdiamond.ai) — SOTA model-routing intelligence; powers OpenRouter's Auto router.
- [Martian](https://withmartian.com) — Pioneer commercial model router; Accenture partnership.
- [Inworld Router](https://inworld.ai/router) — One API for 200+ models with real-time complexity-based routing and **0% markup** (pass-through pricing); adds first-party realtime inference for open models. Research preview.
- [RouteLLM](https://github.com/lm-sys/RouteLLM) <!--s:lm-sys/RouteLLM-->⭐ 5k<!--/s--> — LMSYS's open router framework (research-grade; inactive since 2024 but still the canonical paper/code).
- [OpenRouter Auto](https://openrouter.ai) — One model id (`openrouter/auto`) that routes per-prompt.
- [Unify](https://unify.ai) — Early neural LLM router (company since pivoted to agents).
- [Bifrost adaptive load balancing](https://github.com/maximhq/bifrost) / [Cloudflare dynamic routing](https://developers.cloudflare.com/ai-gateway/) — routing built into gateways themselves.

## 📊 Observability & cost tracking

*Pain point: "Who spent what, on which model, and why did quality drop?"*

- [Helicone](https://github.com/Helicone/helicone) <!--s:Helicone/helicone-->⭐ 5.8k<!--/s--> — Logs, costs, sessions, prompt experiments; one-line proxy integration.
- [TensorZero](https://github.com/tensorzero/tensorzero) <!--s:tensorzero/tensorzero-->⭐ 11.5k<!--/s--> — Gateway + observability + evals in one Rust binary, data stays in your ClickHouse.
- [Portkey](https://portkey.ai) — Full LLMOps suite over its OSS gateway: traces, budgets, prompt management.
- [vLLora (ex-LangDB)](https://github.com/vllora/vllora) <!--s:vllora/vllora-->⭐ 802<!--/s--> — Agent debugging and observability from the LangDB team.
- [Braintrust Proxy](https://github.com/braintrustdata/braintrust-proxy) <!--s:braintrustdata/braintrust-proxy-->⭐ 398<!--/s--> — Caching proxy wired into Braintrust evals.
- [MLflow AI Gateway](https://github.com/mlflow/mlflow) <!--s:mlflow/mlflow-->⭐ 26.4k<!--/s--> — Unified endpoints + governance inside the MLflow platform.

## 🤖 MCP & agent gateways

*Pain point: "Agents call tools now — govern MCP traffic like you govern APIs."* The newest category (2025–2026).

- [agentgateway](https://github.com/agentgateway/agentgateway) <!--s:agentgateway/agentgateway-->⭐ 3.2k<!--/s--> — CNCF proxy for agentic traffic: MCP governance and agent-to-agent (A2A) communication.
- [Lunar.dev MCPX](https://github.com/TheLunarCompany/lunar) <!--s:TheLunarCompany/lunar-->⭐ 454<!--/s--> — Gateway for managing MCP server consumption.
- [Tetrate Agent Router Service](https://tetrate.io/products/tetrate-agent-router-service) — Managed Envoy AI Gateway fleet: LLM + MCP gateway with guardrails (~5% fee).
- [Zuplo AI Gateway](https://zuplo.com/ai-gateway) — Programmable policies: USD spend limits, prompt-injection detection, secret masking, MCP support.
- [NetFoundry MCP/LLM Gateways](https://netfoundry.io) — Zero-trust gateways for AI deployments (launched June 2026).
- [AWS AgentCore Gateway](https://aws.amazon.com/bedrock/) — Tool/MCP gateway inside Bedrock AgentCore.

## ☸️ Kubernetes-native & inference infra

*Pain point: "Routing to self-hosted models (vLLM/Ollama) inside the cluster, GPU-aware."*

- [Gateway API Inference Extension](https://github.com/kubernetes-sigs/gateway-api-inference-extension) <!--s:kubernetes-sigs/gateway-api-inference-extension-->⭐ 690<!--/s--> — The Kubernetes standard for inference-aware routing.
- [AIBrix](https://github.com/vllm-project/aibrix) <!--s:vllm-project/aibrix-->⭐ 4.9k<!--/s--> — Cost-efficient control plane for vLLM on K8s (ByteDance-origin).
- [llm-d](https://github.com/llm-d/llm-d) <!--s:llm-d/llm-d-->⭐ 3.3k<!--/s--> — K8s-native distributed inference serving (Red Hat/Google/IBM-backed).
- [Higress](https://github.com/higress-group/higress) <!--s:higress-group/higress-->⭐ 8.6k<!--/s--> / [Kong](https://github.com/Kong/kong) <!--s:Kong/kong-->⭐ 43.6k<!--/s--> / [Envoy AI Gateway](https://github.com/envoyproxy/ai-gateway) <!--s:envoyproxy/ai-gateway-->⭐ 1.7k<!--/s--> — all implement inference-extension-style routing.
- [Traefik Hub AI Gateway](https://traefik.io) — LLM routing/security in Traefik's commercial runtime.
- [Inference Gateway](https://github.com/inference-gateway/inference-gateway) <!--s:inference-gateway/inference-gateway-->⭐ 124<!--/s--> — Small cloud-native gateway unifying cloud + local (Ollama) providers.

## 📰 What's new

*Curated monthly. Last review: 2026-06-12.*

- **2026-05** · **Palo Alto Networks completed its acquisition of Portkey** (announced Apr 30, closed May 29), making the AI gateway the control plane for its Prisma AIRS security platform — a sign gateways are becoming core security infrastructure. ([Palo Alto Networks](https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-completes-acquisition-of-portkey-to-secure-ai-agents))
- **2026-05** · OpenRouter raised a **$113M Series B** led by CapitalG at a $1.3B valuation — ~8M users, ~100T tokens/month. ([TechCrunch](https://techcrunch.com/2026/05/26/openrouter-more-than-doubles-valuation-to-1-3b-in-a-year/))
- **2026-06** · NetFoundry launched **zero-trust MCP and LLM gateways**; Cisco Investments joined its Series A. ([PR Newswire](https://www.prnewswire.com/news-releases/netfoundry-launches-enterprise-class-mcp-and-llm-gateways-bringing-zero-trust-to-ai-deployments-302789053.html))
- **2026** · Cloudflare AI Gateway shipped **dollar-denominated spend limits** (public beta) on top of dynamic routing and unified billing. ([Cloudflare blog](https://blog.cloudflare.com/ai-gateway-spend-limits/))
- **2025-11** · Pydantic AI Gateway went open beta and has since merged into **Logfire**; F5 added data-leakage detection to its AI Gateway via the **LeakSignal** acquisition. ([Pydantic Logfire](https://pydantic.dev/logfire), [F5](https://www.f5.com/company/news/press-releases/data-leakage-detection-prevention-secure-ai-workloads))
- **Trend** · MCP gateways emerged as a distinct category; spend-limit enforcement became table stakes; the **EU AI Act (enforceable Aug 2026)** is driving the compliance bucket; **new-api overtook one-api** as the most active China-ecosystem relay.

## 🚀 Recent releases (auto-updated)

<!-- RELEASES:START -->
- **2026-06-11** · [andrewyng/aisuite app-v0.1.1](https://github.com/andrewyng/aisuite/releases/tag/app-v0.1.1) — OpenCoworker 0.1.1
- **2026-06-11** · [yym68686/uni-api v1.7.115](https://github.com/yym68686/uni-api/releases/tag/v1.7.115) — Release 1.7.115
- **2026-06-09** · [katanemo/plano 0.4.24](https://github.com/katanemo/plano/releases/tag/0.4.24) — 0.4.24
- **2026-06-09** · [BerriAI/litellm v1.88.1](https://github.com/BerriAI/litellm/releases/tag/v1.88.1) — v1.88.1
- **2026-06-08** · [maximhq/bifrost ent-v1.4.8-base](https://github.com/maximhq/bifrost/releases/tag/ent-v1.4.8-base) — Enterprise v1.4.8 base
- **2026-06-06** · [envoyproxy/ai-gateway v0.7.0](https://github.com/envoyproxy/ai-gateway/releases/tag/v0.7.0) — v0.7.0
- **2026-06-04** · [kgateway-dev/kgateway v2.3.2](https://github.com/kgateway-dev/kgateway/releases/tag/v2.3.2) — v2.3.2
- **2026-06-04** · [tensorzero/tensorzero 2026.6.0](https://github.com/tensorzero/tensorzero/releases/tag/2026.6.0) — 2026.6.0
- **2026-06-04** · [Kong/kong 3.9.2](https://github.com/Kong/kong/releases/tag/3.9.2) — 3.9.2
- **2026-06-01** · [mlflow/mlflow v3.13.0](https://github.com/mlflow/mlflow/releases/tag/v3.13.0) — v3.13.0
- **2026-05-29** · [tbphp/gpt-load v1.4.8](https://github.com/tbphp/gpt-load/releases/tag/v1.4.8) — v1.4.8
- **2026-05-26** · [QuantumNous/new-api v1.0.0-rc.10](https://github.com/QuantumNous/new-api/releases/tag/v1.0.0-rc.10) — v1.0.0-rc.10
<!-- RELEASES:END -->

## Glossary

<details>
<summary>Key terms used in the tables above (click to expand)</summary>

- **AI gateway / LLM gateway** — a proxy between your app and LLM providers; one endpoint and key for many models.
- **LLM router** — the part that decides *which model* serves each request (cheap vs flagship, by cost or quality).
- **Fallback** — automatically retry on another model/provider when the first fails or times out.
- **Load balancing (LB)** — spread traffic across keys/providers to dodge rate limits and outages.
- **Semantic caching** — return a cached answer when a *new* prompt is semantically similar to a past one (not just identical).
- **Prompt / cached input** — providers bill reused prompt prefixes at a steep discount (≈0.1×); the gateway must not mangle the prefix or the cache misses.
- **Guardrails** — input/output checks: prompt-injection detection, PII redaction, content filtering, schema enforcement.
- **Virtual keys** — per-user/team keys the gateway issues in front of your real provider keys, with their own budgets and limits.
- **ZDR (zero data retention)** — provider/gateway contractually does not store your prompts or completions.
- **BYOK** — bring your own key: the gateway uses *your* provider accounts rather than reselling tokens.
- **Markup** — the gateway's fee on top of provider token cost (0% to ~6%).
- **MCP gateway** — governs agent ↔ tool traffic (Model Context Protocol), the agentic counterpart to an LLM gateway.

</details>

## How to choose safely

1. **Check the markup.** Marketplaces charge 0–6% — for high volume, self-hosting or 0%-markup gateways (Vercel, Helicone cloud) pay for themselves fast.
2. **Verify model fidelity.** Some relays silently downgrade models. Send a canary prompt (e.g. a known hard reasoning question) through the gateway and direct to the provider, then diff.
3. **Mind data flow.** Every gateway sees your prompts. For sensitive data: self-host, or require ZDR (zero data retention) in writing.
4. **License check before embedding.** new-api is AGPL-3.0; LiteLLM has an enterprise-licensed directory; "open core" ≠ everything free.
5. **Project health.** Star count ≠ maintenance. Check last release date — several once-popular gateways (BricksLLM, Glide, RouteLLM) are effectively unmaintained; this list labels them.
6. **Avoid gray-market relays** reselling reverse-engineered or stolen-quota access — account bans and data leaks are your risk, not theirs.

## FAQ

**What is an AI gateway (LLM gateway)?**
A proxy between your code and LLM providers: one OpenAI-compatible endpoint and key for many models, adding routing, failover, caching, rate limits, cost tracking and guardrails. See the [intro](#which-gateway-should-i-use).

**AI gateway vs LLM router — what's the difference?**
A *router* decides *which model* gets each request (e.g. cheap vs flagship); a *gateway* is the full proxy layer (auth, caching, observability, guardrails) that usually *includes* routing. See [smart routing](#-smart-routing--model-selection).

**What's the best open-source AI gateway?**
[LiteLLM](https://github.com/BerriAI/litellm) is the default for breadth (Python, 100+ providers). For raw performance pick [Bifrost](https://github.com/maximhq/bifrost) (Go) or [TensorZero](https://github.com/tensorzero/tensorzero) (Rust); for enterprise K8s pick [Kong](https://github.com/Kong/kong) or [Higress](https://github.com/higress-group/higress). Full list under [self-hosted](#-self-hosted-open-source).

**LiteLLM vs OpenRouter — which should I use?**
OpenRouter is hosted (zero ops, ~5.5% fee, 400+ models); LiteLLM is self-hosted (your keys, your infra, $0 markup). Hosted to start, self-host when volume justifies it. Cost math in the [evaluation set](BENCHMARKS.md#part-3--real-world-token-cost-computed).

**What's the cheapest way to call many LLMs?**
For zero ops: [Vercel AI Gateway](https://vercel.com/ai-gateway) or [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/) (0% markup). For lowest token cost, route bulk work to cheap models — a 100K-token report runs **$0.03 on DeepSeek vs $3.01 on GPT-5.5**. See [cost-first](#-cost-first-cheapest-multi-model-access).

**Are AI gateways safe? Who sees my prompts?**
Every gateway sees your prompts. For sensitive data self-host or require zero-data-retention in writing; check the [gateway scorecard](BENCHMARKS.md#part-4--gateway-scorecard-compliance--price--security--stability) for compliance/security ratings and known CVEs.

## Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first. Inclusion criteria, in short: the project must be an actual gateway/proxy/router for LLM or agent traffic (not an SDK wrapper or chat UI), publicly available, and active within the last 12 months — or clearly labeled as stale.

## Star history

[![Star History Chart](https://api.star-history.com/svg?repos=cuihuan/awesome-ai-gateway&type=Date)](https://star-history.com/#cuihuan/awesome-ai-gateway&Date)

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this work.
