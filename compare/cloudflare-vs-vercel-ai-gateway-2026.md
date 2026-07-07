# Cloudflare AI Gateway vs Vercel AI Gateway (2026): Which 0%-Markup Hosted Gateway?

*Last updated 2026-07-07 · Part of [Awesome AI Gateway](../README.md) — the only AI-gateway list with a [reproducible cost benchmark](../BENCHMARKS.md) and a [security-honest scorecard](../BENCHMARKS.md#part-4--gateway-scorecard-compliance--price--security--stability--observability). [⭐ Star it](https://github.com/cuihuan/awesome-ai-gateway).*

> 📊 **Key numbers** · Both gateways are **0% markup**, so the deciding cost factor isn't the gateway — it's the model: a 100K-token report runs **$0.03** (DeepSeek V4-Flash) to **$3.01** (GPT-5.5), a **~106× spread** ([computed](../BENCHMARKS.md#part-3--real-world-token-cost-computed), 2026-06). And caching is measurably underused: across 1,000+ orgs' production traffic **only 28% of LLM calls show any cached input**, while system prompts eat 69% of input tokens ([Datadog, 2026-04](https://www.datadoghq.com/state-of-ai-engineering/)) — both gateways ship caching; turning it on is free money.

If you want a **hosted** AI gateway that **doesn't take a cut of your token spend**, the two from major infrastructure vendors are **Cloudflare AI Gateway** and **Vercel AI Gateway**. Both are **0% markup**, both give you one endpoint in front of many providers, both add observability and fallback. They differ on where they sit in your stack and how far the governance goes. Here's the honest, data-backed breakdown.

## TL;DR

| | Cloudflare AI Gateway | Vercel AI Gateway |
|---|---|---|
| **Markup** | 0% | 0% (incl. BYOK) |
| **Sits in** | Cloudflare's global edge — any stack | Vercel platform + AI SDK |
| **Best for** | Provider-agnostic edge: caching, analytics, DLP across any app | Teams already on Vercel / Next.js / the AI SDK |
| **Compliance** | ★4.5 — SOC 2 II / ISO 27001 / **PCI** / GDPR | ★4.0 — SOC 2 II |
| **SLA** | 100% at Business+ | 99.99% (Enterprise) |
| **Security extras** | Free DLP + PII scanning, guardrails, fallback | ZDR option, BYOK |
| **Scorecard (sec/stab)** | ★4.0 / ★4.5 | ★3.5 / ★4.0 |

## Pick by your actual constraint

- **"I'm already on Vercel / building with the AI SDK"** → **Vercel AI Gateway.** It's unified with your deployment: one place for billing, observability and model switching, **true 0% markup including BYOK**, and a fast path from `ai` SDK code to many models. The least friction if Vercel is already your platform.
- **"I want a provider-agnostic gateway on the edge, for any stack"** → **Cloudflare AI Gateway.** It's not tied to a framework — point any app at it for caching, rate limiting, retries/fallback, analytics and logging, with **free DLP + PII scanning** built in. The stronger choice when the gateway must serve apps that don't live on Vercel.
- **"Compliance is the deciding factor"** → **Cloudflare** edges it (★4.5 vs ★4.0): it carries **PCI DSS** alongside SOC 2 Type II / ISO 27001 / GDPR, and publishes a 100% SLA at Business+. Both are solid; Cloudflare's certificate set is broader today.
- **"Caching to cut cost"** → **Cloudflare's** response caching is a first-class feature and a real lever on repeat-prompt workloads.

## Where they're the same

Both take **0% on your token spend** — you pay the provider's price, not a gateway tax — which already puts them ahead of marketplace gateways like OpenRouter (~5.5%) on raw cost. Both give you a single OpenAI-style endpoint, multi-provider fallback, request logging and usage analytics. For many teams the decision is simply **"which platform am I already on?"**

## The cost angle that dwarfs both

Neither gateway marks up your tokens — so the **model you route to** is your entire bill. Same 100K-token report: **$0.03 on DeepSeek vs $3.01 on GPT-5.5** — a **106× spread**. A 0%-markup gateway's biggest win is making it trivial to route cheap-by-default and escalate only when needed. Full computed cost tables are in the [evaluation set](../BENCHMARKS.md).

## What neither is

Both are **hosted** — your requests transit a vendor. If you need **keys on your own infrastructure**, you want a self-hosted gateway instead: see [best self-hosted AI gateway 2026](best-self-hosted-ai-gateway-2026.md) (LiteLLM / Bifrost / Portkey / Kong). If you want a bigger model marketplace and don't mind a fee, see [OpenRouter alternatives](openrouter-alternatives-2026.md).

## Verdict

- **On Vercel / Next.js / the AI SDK → Vercel AI Gateway.**
- **Any other stack, or compliance-led, or caching-heavy → Cloudflare AI Gateway.**
- **Both beat marketplace gateways on raw cost (0% vs ~5.5%)** — the real money is still the model behind them.

Browse all gateways by need, with decision tree and data: **[Awesome AI Gateway →](../README.md)** · [interactive site](https://cuihuan.github.io/awesome-ai-gateway/).

---

*Found this useful? [⭐ Star the list](https://github.com/cuihuan/awesome-ai-gateway) — it's how the next engineer choosing a gateway finds it. CC0, no signup, no tracking, no vendor money.*
