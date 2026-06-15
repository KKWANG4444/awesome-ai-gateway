# Awesome AI Gateway [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![GitHub stars](https://img.shields.io/github/stars/cuihuan/awesome-ai-gateway?style=social)](https://github.com/cuihuan/awesome-ai-gateway/stargazers)
[![Evaluation set](https://img.shields.io/badge/📊-评测集-orange)](BENCHMARKS.zh-CN.md)
[![Data updated daily](https://img.shields.io/badge/数据-每日更新-success?logo=githubactions&logoColor=white)](.github/workflows/daily-update.yml)

> **按你的诉求，约 10 秒选对 AI 网关——而且这个答案可信。** 一棵决策树、一行接入、可复现的成本评测，外加我们排除灰产的独立证据。按真实诉求分类，而非按厂商罗列。

**语言：** [English](README.md) · 简体中文

<p align="center">
<a href="#我该用哪个网关"><kbd> &nbsp; 🧭 选网关 &nbsp; </kbd></a> &nbsp;
<a href="https://cuihuan.github.io/awesome-ai-gateway/"><kbd> &nbsp; 🚀 在线交互页 &nbsp; </kbd></a> &nbsp;
<a href="BENCHMARKS.zh-CN.md"><kbd> &nbsp; 📊 成本与评分卡 &nbsp; </kbd></a> &nbsp;
<a href="#快速上手一行接入"><kbd> &nbsp; ⚡ 一行接入 &nbsp; </kbd></a>
</p>

<details>
<summary>📑 <b>完整目录</b> —— 快速选 · 按需浏览 · 参考</summary>

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: CC0](https://img.shields.io/badge/license-CC0-lightgrey.svg)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/cuihuan/awesome-ai-gateway)](https://github.com/cuihuan/awesome-ai-gateway/commits/main)

**快速选** · [我该用哪个网关？](#我该用哪个网关) · [快速上手（一行接入）](#快速上手一行接入) · [快速对比](#快速对比)

**按需浏览** · [💰 性价比优先](#-性价比优先) · [🔓 自托管开源](#-自托管开源) · [🏢 企业合规](#-企业合规) · [☁️ 原厂直连](#️-原厂直连云厂商模型厂商) · [🇨🇳 国内生态](#-国内生态) · [🤖 MCP 与 Agent 网关](#-mcp-与-agent-网关)

**参考** · [📊 评测集](BENCHMARKS.zh-CN.md) · [如何安全选型](#如何安全选型) · [常见问题 FAQ](#常见问题-faq) · [📚 必读精选](#-必读精选) · [📰 行业动态](#-行业动态) · [术语表](#术语表) · [参与贡献](#参与贡献)

</details>

## 我该用哪个网关？

<p align="center">
  <img src="assets/decision-tree.zh-CN.png" alt="决策树：我该用哪个 AI 网关？托管（OpenRouter、Vercel、Cloudflare、Bedrock、Azure、Vertex、Portkey）vs 自托管开源（LiteLLM、Bifrost、new-api、one-api、GPT-Load、Kong、Higress、APISIX、Envoy AI Gateway、agentgateway），按你的需求来选。" width="840">
</p>

**⚡ 快速答案** —— 每个需求一个稳妥默认项（备选见各分区链接）：

| 我要… | 首选 | 细读 |
|---|---|---|
| 最低成本接入多模型、零运维 | **OpenRouter** | [性价比优先](#-性价比优先) |
| 用自己的 Key、0 加价 | **Vercel** / **Cloudflare** | [性价比优先](#-性价比优先) |
| 自托管、功能最全 | **LiteLLM** | [自托管开源](#-自托管开源) |
| 自托管、开销最低 | **Bifrost**（Go） | [自托管开源](#-自托管开源) |
| 国产模型 + 团队 Key 计费 | **new-api** | [国内生态](#-国内生态) |
| 企业 K8s + 审计 | **Kong** / **Higress** | [企业合规](#-企业合规) |
| 最强合规（HIPAA/FedRAMP） | **Azure** / **Bedrock** | [原厂直连](#️-原厂直连云厂商模型厂商) |
| 治理 Agent / MCP 流量 | **agentgateway** | [MCP 与 Agent](#-mcp-与-agent-网关) |

<details>
<summary>📋 完整决策树 —— 每条分支、可复制</summary>

```text
要不要自己部署？
│
├─ 不部署 — 托管服务，省运维
│   ├─ 最低成本接入多模型 ──────────▶ OpenRouter · Vercel AI Gateway（0 加价）
│   ├─ 用自己的 Key + 免费控制面 ───▶ Cloudflare AI Gateway
│   ├─ 在意欧盟数据合规 ────────────▶ Requesty · Eden AI · nexos.ai
│   └─ 已绑定某朵云 ────────────────▶ AWS Bedrock · Azure APIM · Vertex AI
│
└─ 要部署 — 自托管 / 开源
    ├─ Python 技术栈、功能最全 ─────▶ LiteLLM
    ├─ 追求极致性能（Go/Rust/TS）──▶ Bifrost · Portkey Gateway
    ├─ 自带评测 + 可观测 ───────────▶ Helicone · Portkey Gateway
    ├─ 国产模型、Key 分发/计费 ─────▶ new-api · one-api · GPT-Load
    ├─ 企业 K8s、审计、护栏 ────────▶ Kong · Higress · APISIX · Envoy AI Gateway
    └─ 治理 Agent / MCP 流量 ───────▶ agentgateway · Lunar.dev
```

</details>

### ✅ 为什么可信
- **独立——不收厂商钱、无返利链接、CC0。** 不像那些靠返利的中转"榜单"，这里没人花钱就能上榜。
- **可复现，而非口说。** 每个成本数字都由[带单测的脚本](scripts/cost_calc.py)从[公开定价数据](data/models.json)算出；星数由 CI 每日刷新。
- **对风险诚实。** 我们披露 CVE、标注已归档/停更项目、并[排除灰产中转](#如何安全选型)——且有研究佐证。

---

> **为什么重要：** 同一个任务，取决于网关背后用哪个模型，成本能差 **100 倍**。**AI 网关**位于你的代码与大模型厂商之间——一个端点、一把 Key、打通所有模型——负责路由、故障转移、缓存、限流、成本核算与护栏，你只需改一个 `base_url`，而非为每家厂商重写应用。先在这里选对网关，[评测集](BENCHMARKS.zh-CN.md)再告诉你该路由到哪个模型。

<p align="center">
  <a href="BENCHMARKS.zh-CN.md"><img src="assets/cost-spread.png" alt="写一份 10 万 token 报告的成本：DeepSeek $0.03 vs GPT-5.5 $3.01——106 倍价差，由带单测的脚本计算" width="760"></a>
</p>

⭐ **觉得有用就点个 [Star](https://github.com/cuihuan/awesome-ai-gateway)** —— 下一个在选网关的工程师就是这样找到它的。CC0 授权，无需注册、无追踪、不收厂商一分钱。

## 快速上手（一行接入）

网关的全部承诺就是：**改一个 `base_url`，OpenAI 代码照旧**。同一个请求，立刻拥有路由、兜底、缓存与成本核算。

```python
from openai import OpenAI

# 托管示例 —— OpenRouter（400+ 模型，一把 Key）：
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-...",
)

# 自托管示例 —— 你自己跑的 LiteLLM 代理：
client = OpenAI(
    base_url="http://localhost:4000",
    api_key="sk-litellm-...",
)

resp = client.chat.completions.create(
    model="anthropic/claude-fable-5",        # 向网关点名任意厂商的模型
    messages=[{"role": "user", "content": "你好！"}],
)
```

**OpenAI 兼容 `base_url` 速查表**（2026 年 6 月核实——换上即用，代码照旧）：

| 网关 | `base_url` |
|---|---|
| OpenRouter | `https://openrouter.ai/api/v1` |
| Vercel AI Gateway | `https://ai-gateway.vercel.sh/v1` |
| Cloudflare AI Gateway | `https://gateway.ai.cloudflare.com/v1/{account}/{gateway}/compat` |
| Portkey | `https://api.portkey.ai/v1` |
| Helicone AI Gateway | `https://ai-gateway.helicone.ai/ai` |
| Requesty | `https://router.requesty.ai/v1` |
| LiteLLM（自托管） | `http://localhost:4000` |

## 快速对比

星数每日自动刷新。✅ 内置 · ➕ 插件/付费版 · ❌ 不支持。

| 项目 | 类型 | 星数 | 协议 | 多厂商 | 故障转移/负载均衡 | 缓存 | 护栏 | 成本核算 |
|---|---|---|---|---|---|---|---|---|
| [LiteLLM](https://github.com/BerriAI/litellm) | 开源代理 + SDK | <!--s:BerriAI/litellm-->⭐ 50.4k<!--/s--> | MIT¹ | ✅ 100+ | ✅ | ✅ | ✅ | ✅ |
| [new-api](https://github.com/QuantumNous/new-api) | 开源中转/计费 | <!--s:QuantumNous/new-api-->⭐ 38.8k<!--/s--> | AGPL-3.0 | ✅ | ✅ | ➕ | ➕ | ✅ |
| [one-api](https://github.com/songquanpeng/one-api) | 开源中转/计费 | <!--s:songquanpeng/one-api-->⭐ 34.9k<!--/s--> | MIT | ✅ | ✅ | ❌ | ❌ | ✅ |
| [Kong AI Gateway](https://github.com/Kong/kong) | 开源 API 网关 | <!--s:Kong/kong-->⭐ 43.6k<!--/s--> | Apache-2.0 | ✅ | ✅ | ✅ 语义缓存 | ✅ | ✅ |
| [Apache APISIX](https://github.com/apache/apisix) | 开源 API 网关 | <!--s:apache/apisix-->⭐ 16.7k<!--/s--> | Apache-2.0 | ✅ | ✅ | ➕ | ➕ | ➕ |
| [Portkey Gateway](https://github.com/Portkey-AI/gateway) | 开源网关 + SaaS | <!--s:Portkey-AI/gateway-->⭐ 12.1k<!--/s--> | MIT | ✅ 1600+ | ✅ | ✅ | ✅ 50+ | ➕ SaaS |
| [TensorZero](https://github.com/tensorzero/tensorzero) | 开源 LLMOps · ⚠️ 已归档'26 | <!--s:tensorzero/tensorzero-->⭐ 11.6k<!--/s--> | Apache-2.0 | ✅ | ✅ | ✅ | ➕ | ✅ |
| [Higress](https://github.com/higress-group/higress) | 开源 AI 原生网关 | <!--s:higress-group/higress-->⭐ 8.7k<!--/s--> | Apache-2.0 | ✅ | ✅ | ✅ | ✅ | ✅ |
| [GPT-Load](https://github.com/tbphp/gpt-load) | 开源密钥池代理 | <!--s:tbphp/gpt-load-->⭐ 6.2k<!--/s--> | MIT | ✅ | ✅ 密钥轮询 | ❌ | ❌ | ➕ |
| [Bifrost](https://github.com/maximhq/bifrost) | 开源网关（Go） | <!--s:maximhq/bifrost-->⭐ 5.8k<!--/s--> | Apache-2.0 | ✅ | ✅ 自适应 | ✅ | ✅ | ✅ |
| [Helicone](https://github.com/Helicone/helicone) | 开源可观测 + 网关 | <!--s:Helicone/helicone-->⭐ 5.8k<!--/s--> | Apache-2.0 | ✅ | ✅ | ✅ | ➕ | ✅ |
| [Envoy AI Gateway](https://github.com/envoyproxy/ai-gateway) | 开源 K8s 网关 | <!--s:envoyproxy/ai-gateway-->⭐ 1.7k<!--/s--> | Apache-2.0 | ✅ | ✅ | ➕ | ➕ | ✅ |
| [OpenRouter](https://openrouter.ai) | SaaS 模型市场 | — | 商业 | ✅ 400+ | ✅ | ✅ | ➕ | ✅ |
| [Vercel AI Gateway](https://vercel.com/ai-gateway) | SaaS（0 加价） | — | 商业 | ✅ 数百 | ✅ | ❌ | ❌ | ✅ |
| [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/) | SaaS 控制面 | — | 商业（免费档） | ✅ | ✅ 动态路由 | ✅ | ✅ | ✅ 预算 |

¹ LiteLLM 核心为 MIT，仓库内含单独授权的企业版目录。

> 📂 **浏览原始数据**（机器可读，CC0）：[模型与价格 JSON](data/models.json) · [成本表 CSV](data/cost_table.csv) · [网关评分卡 CSV](data/gateways_scorecard.csv)。每个成本数字都由[带单测的脚本](scripts/cost_calc.py)从这些数据重新生成。

## 💰 性价比优先

*痛点："用最少的钱接入最多的模型，还不想搞运维。"*

- [OpenRouter](https://openrouter.ai) — 最大的模型市场：一个 OpenAI 兼容 API 背后 400+ 模型，按量付费、自动故障转移；充值约收 5.5% 手续费。2026 年 5 月完成 1.13 亿美元 B 轮，约 800 万用户。
- [Vercel AI Gateway](https://vercel.com/ai-gateway) — 数百模型按**厂商原价（0 加价）**计费，每月 $5 免费额度，可选零数据保留；与 AI SDK 天然搭配。
- [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/) — 免费控制面套在你自己的厂商 Key 之上：缓存、动态路由、统一账单、美元计价的预算上限（2026 公测）。
- [Requesty](https://requesty.ai) — 面向欧盟的 OpenRouter 替代：400+ 模型、20ms 内故障转移、约 5% 加价。
- [Eden AI](https://www.edenai.co) — 统一 API 接入 500+ 模型及视觉/OCR/语音；欧盟公司，平台费约 5.5%。
- [Helicone AI Gateway（云版）](https://www.helicone.ai) — **0 加价**直通计费，可观测能力打包赠送。
- [GPT-Load](https://github.com/tbphp/gpt-load) <!--s:tbphp/gpt-load-->⭐ 6.2k<!--/s--> — Go 写的高性能多渠道密钥轮询代理，把每把 Key 的额度榨干。

> 💡 任何网关都能再省一笔：开**语义缓存**（Kong、Bifrost、Zuplo），设**消费上限**（Cloudflare、Zuplo、Pydantic/Logfire），简单请求路由到便宜模型（见[智能路由](#-智能路由与模型选择)）。

## 🔓 自托管开源

*痛点："Key 在我手里、跑在我机器上，不交按量过路费。"*

- [LiteLLM](https://github.com/BerriAI/litellm) <!--s:BerriAI/litellm-->⭐ 50.4k<!--/s--> — 默认之选：Python SDK + 代理服务，以 OpenAI 格式打通 100+ 厂商，带虚拟 Key、预算、负载均衡与护栏。
- [Portkey Gateway](https://github.com/Portkey-AI/gateway) <!--s:Portkey-AI/gateway-->⭐ 12.1k<!--/s--> — 高速 TypeScript 网关（1600+ 模型、50+ 护栏），同时是 Portkey 商业 LLMOps 平台的底座。
- [TensorZero](https://github.com/tensorzero/tensorzero) <!--s:tensorzero/tensorzero-->⭐ 11.6k<!--/s--> — ⚠️ **2026 年 6 月已归档**（公司关停；仓库只读，Apache-2.0 代码与社区分支尚存）。Rust 网关 + 可观测 + 评测 + 实验优化一体。
- [Bifrost](https://github.com/maximhq/bifrost) <!--s:maximhq/bifrost-->⭐ 5.8k<!--/s--> — Maxim AI 出品的 Go 网关，号称比 LiteLLM 快约 50 倍；自适应负载均衡、集群模式、支持 MCP。
- [Helicone](https://github.com/Helicone/helicone) <!--s:Helicone/helicone-->⭐ 5.8k<!--/s--> — 可观测优先的平台（YC W23），配套 Rust [ai-gateway](https://github.com/Helicone/ai-gateway) <!--s:Helicone/ai-gateway-->⭐ 601<!--/s-->。
- [Plano](https://github.com/katanemo/plano) <!--s:katanemo/plano-->⭐ 6.6k<!--/s--> — 面向 Agent 的 AI 原生代理/数据面（原名 Arch Gateway / archgw）。
- [LLM Gateway](https://github.com/theopenco/llmgateway) <!--s:theopenco/llmgateway-->⭐ 1.3k<!--/s--> — 开源版 OpenRouter：跨厂商路由、管理与分析。
- [APIPark](https://github.com/APIParkLab/APIPark) <!--s:APIParkLab/APIPark-->⭐ 1.8k<!--/s--> — 云原生 LLM API 管理与分发平台。
- [Pydantic AI Gateway](https://github.com/pydantic/pydantic-ai-gateway) <!--s:pydantic/pydantic-ai-gateway-->⭐ 189<!--/s--> — BYOK 网关，带成本上限与 OTel，现已并入 Pydantic Logfire。
- [OptiLLM](https://github.com/algorithmicsuperintelligence/optillm) <!--s:algorithmicsuperintelligence/optillm-->⭐ 4.1k<!--/s--> — 优化型推理代理，用测试时计算技术提升准确率。
- [aisuite](https://github.com/andrewyng/aisuite) <!--s:andrewyng/aisuite-->⭐ 14.4k<!--/s--> — 吴恩达的统一多厂商客户端。是库而非代理服务，适合不想加网络一跳的场景。
- ⚠️ 已停滞但有历史意义：[BricksLLM](https://github.com/bricks-cloud/BricksLLM) <!--s:bricks-cloud/BricksLLM-->⭐ 1.2k<!--/s-->（PII 脱敏、按 Key 限额；2025 年初起不再活跃）、[Glide](https://github.com/EinStack/glide) <!--s:EinStack/glide-->⭐ 160<!--/s-->（2024 年起停更）。

## 🏢 企业合规

*痛点："审计日志、PII 脱敏、RBAC、私有化部署，外加 2026 年 8 月生效的欧盟 AI 法案。"*

- [Kong AI Gateway](https://github.com/Kong/kong) <!--s:Kong/kong-->⭐ 43.6k<!--/s--> — 成熟 API 网关 + AI 插件：语义缓存/路由、Prompt 防护、token 限流；Konnect 提供托管控制面。
- [Apache APISIX](https://github.com/apache/apisix) <!--s:apache/apisix-->⭐ 16.7k<!--/s--> — 云原生 API + AI 网关，`ai-proxy` / `ai-proxy-multi` 插件。
- [Envoy AI Gateway](https://github.com/envoyproxy/ai-gateway) <!--s:envoyproxy/ai-gateway-->⭐ 1.7k<!--/s--> — 基于 Envoy Gateway 的 CNCF 系 GenAI 接入层，Tetrate 与彭博背书。
- [kgateway](https://github.com/kgateway-dev/kgateway) <!--s:kgateway-dev/kgateway-->⭐ 5.6k<!--/s--> — CNCF API/AI 网关，Solo.io 商业版 [Gloo AI Gateway](https://www.solo.io) 的底座。
- [TrueFoundry AI Gateway](https://www.truefoundry.com) — 企业网关：路由、护栏、RBAC，可部署进你的 K8s/VPC。
- [nexos.ai](https://nexos.ai) — Nord Security 创始团队的企业 AI 网关/编排（2025 年 10 月 €3000 万 A 轮）。
- [Tyk AI Studio](https://tyk.io) — AI 治理套件：预算、模型目录、护栏。
- [Gravitee Agent Mesh](https://www.gravitee.io) — APIM 内置 LLM Proxy、MCP Proxy 与 A2A。
- [WSO2 AI Gateway](https://wso2.com/api-manager/usecases/ai-gateway/) — LLM 出口流量管理：模型路由、语义缓存、护栏。
- [F5 AI Gateway](https://www.f5.com) — 容器化 AI 流量网关；通过收购 LeakSignal 增加数据泄露检测（2025-11）。
- [IBM API Connect AI Gateway](https://www.ibm.com) — LLM 流量的策略执行、脱敏与审计。
- [MuleSoft AI / Omni Gateway](https://www.mulesoft.com/platform/ai-gateway) — 把 LLM、MCP、Agent 流量与传统 API 一起治理。
- [Lunar.dev](https://github.com/TheLunarCompany/lunar) <!--s:TheLunarCompany/lunar-->⭐ 455<!--/s--> — 出口消费网关，已转向 MCP/Agent 治理。

## ☁️ 原厂直连（云厂商/模型厂商）

*痛点："已经绑定某朵云，要官方原生方案。"*

- [AWS Bedrock](https://aws.amazon.com/bedrock/) — 统一 Converse API 多模型接入、跨区域推理、AgentCore Gateway 管工具/MCP。
- [Azure API Management — GenAI gateway](https://learn.microsoft.com/azure/api-management/genai-gateway-capabilities) — 在 Azure OpenAI / AI Foundry 前做 token 限额、语义缓存与负载均衡。
- [Google Apigee + Vertex AI](https://cloud.google.com/apigee) — Apigee 的 LLM 网关模式 + Vertex Model Garden 托管模型库。
- [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/) — 见[性价比优先](#-性价比优先)；最强的免费原厂选项。
- [Vercel AI Gateway](https://vercel.com/ai-gateway) — 已 GA，0 加价，可选零数据保留；Next.js / AI SDK 团队的默认选择。
- [Databricks Unity AI Gateway](https://www.databricks.com) — Mosaic AI Gateway 并入 Unity Catalog，增加 Agent + MCP 治理。

## 🇨🇳 国内生态

*痛点："国产模型（通义/DeepSeek/GLM/Kimi）、人民币支付、团队 Key 分发与计费。"*

- [new-api](https://github.com/QuantumNous/new-api) <!--s:QuantumNous/new-api-->⭐ 38.8k<!--/s--> — 最活跃的 one-api 分支，已是"统一 AI 模型枢纽"：协议转换、计费、Rerank/Realtime 端点。AGPL-3.0。
- [one-api](https://github.com/songquanpeng/one-api) <!--s:songquanpeng/one-api-->⭐ 34.9k<!--/s--> — 元祖级 LLM API 管理&分发系统（OpenAI/Azure/Claude/Gemini/DeepSeek/豆包…）；开发节奏已放缓。
- [Higress](https://github.com/higress-group/higress) <!--s:higress-group/higress-->⭐ 8.7k<!--/s--> — 阿里开源、基于 Envoy/Istio 的 AI 原生网关，通义/DeepSeek 一等公民；云版 higress.ai。
- [GPT-Load](https://github.com/tbphp/gpt-load) <!--s:tbphp/gpt-load-->⭐ 6.2k<!--/s--> — 智能密钥轮询的多渠道代理（Go）。
- [one-hub](https://github.com/MartialBE/one-hub) <!--s:MartialBE/one-hub-->⭐ 2.8k<!--/s--> — one-api 分支：更好的非 OpenAI 函数调用与统计页面。
- [simple-one-api](https://github.com/fruitbars/simple-one-api) <!--s:fruitbars/simple-one-api-->⭐ 2.3k<!--/s--> — 单二进制，把千帆/星火/混元/MiniMax/DeepSeek 适配为 OpenAI 接口。
- [Veloera](https://github.com/Veloera/Veloera) <!--s:Veloera/Veloera-->⭐ 1.6k<!--/s--> — one-api/new-api 系新晋中转平台。
- [uni-api](https://github.com/yym68686/uni-api) <!--s:yym68686/uni-api-->⭐ 1.2k<!--/s--> — 轻量级单配置文件统一 API 管理，无前端。
- [APIPark](https://github.com/APIParkLab/APIPark) <!--s:APIParkLab/APIPark-->⭐ 1.8k<!--/s--> — 国产云原生 AI & API 网关，带开放开发者门户。

> ⚠️ 本清单刻意**不收录逆向 / 转售的"free-api"类中转**——而且不只是出于原则。2026 年两篇测量研究发现中转群体存在系统性欺诈：[*Real Money, Fake Models*](https://arxiv.org/abs/2603.01919) 测得 **45.8%** 的指纹测试出现模型身份不符、输出偏离最高达 **47%**；[*Your Agent Is Mine*](https://arxiv.org/abs/2604.08407) 抓到中转**注入恶意代码**并**窃取预埋的 API key**。若你不得不甄别某一家，用[如何安全选型](#如何安全选型)里的 canary 对比测试。

## 🤖 MCP 与 Agent 网关

*痛点："Agent 开始调工具了——像治理 API 一样治理 MCP 流量。"* 2025–2026 最新品类。

- [agentgateway](https://github.com/agentgateway/agentgateway) <!--s:agentgateway/agentgateway-->⭐ 3.3k<!--/s--> — CNCF Agent 流量代理：MCP 治理与 Agent 间（A2A）通信。
- [Lunar.dev MCPX](https://github.com/TheLunarCompany/lunar) <!--s:TheLunarCompany/lunar-->⭐ 455<!--/s--> — 管理 MCP server 消费的网关。
- [Tetrate Agent Router Service](https://tetrate.io/products/tetrate-agent-router-service) — 托管 Envoy AI Gateway 集群：LLM + MCP 网关与护栏（约 5% 费率）。
- [Zuplo AI Gateway](https://zuplo.com/ai-gateway) — 可编程策略：美元消费上限、Prompt 注入检测、密钥脱敏、MCP 支持。
- [NetFoundry MCP/LLM Gateways](https://netfoundry.io) — 零信任 AI 网关（2026 年 6 月发布）。
- [AWS AgentCore Gateway](https://aws.amazon.com/bedrock/) — Bedrock AgentCore 内的工具/MCP 网关。

## 🔧 更多按能力分（横切关注点）

*这些横跨上面按需求分的分区——路由智能、可观测、Kubernetes 基础设施，与你选的网关互补。*

### 🧠 智能路由与模型选择

*痛点："每条 prompt 都路由到能胜任的最便宜模型。"*

- [Not Diamond](https://www.notdiamond.ai) — SOTA 模型路由智能，OpenRouter Auto 的幕后引擎。
- [Martian](https://withmartian.com) — 模型路由商业先驱，与埃森哲合作。
- [Inworld Router](https://inworld.ai/router) — 一个 API 打通 200+ 模型，按查询复杂度实时路由，**0 加价**（直通定价）；另提供开源模型的一方实时推理。研究预览中。
- [RouteLLM](https://github.com/lm-sys/RouteLLM) <!--s:lm-sys/RouteLLM-->⭐ 5k<!--/s--> — LMSYS 开源路由框架（研究级；2024 年后停更，但仍是经典论文+代码）。
- [OpenRouter Auto](https://openrouter.ai) — 一个模型 ID（`openrouter/auto`）按 prompt 自动路由。
- [Unify](https://unify.ai) — 早期神经网络 LLM 路由（公司已转向 Agent 方向）。
- [Bifrost 自适应负载均衡](https://github.com/maximhq/bifrost) / [Cloudflare 动态路由](https://developers.cloudflare.com/ai-gateway/) — 网关内置的路由能力。

### 📊 可观测与成本核算

*痛点："谁在哪个模型上花了多少钱？质量为什么降了？"*

- [Helicone](https://github.com/Helicone/helicone) <!--s:Helicone/helicone-->⭐ 5.8k<!--/s--> — 日志、成本、会话、Prompt 实验；一行代码接入。
- [TensorZero](https://github.com/tensorzero/tensorzero) <!--s:tensorzero/tensorzero-->⭐ 11.6k<!--/s--> — ⚠️ **2026 年 6 月已归档**（仓库只读，Apache-2.0 代码与社区分支尚存）。网关+可观测+评测一体（Rust），数据留在你自己的 ClickHouse。
- [Portkey](https://portkey.ai) — 基于其开源网关的完整 LLMOps：链路追踪、预算、Prompt 管理。
- [vLLora（原 LangDB）](https://github.com/vllora/vllora) <!--s:vllora/vllora-->⭐ 804<!--/s--> — LangDB 团队的 Agent 调试与可观测工具。
- [Braintrust Proxy](https://github.com/braintrustdata/braintrust-proxy) <!--s:braintrustdata/braintrust-proxy-->⭐ 398<!--/s--> — 带缓存的代理，与 Braintrust 评测打通。
- [MLflow AI Gateway](https://github.com/mlflow/mlflow) <!--s:mlflow/mlflow-->⭐ 26.5k<!--/s--> — MLflow 平台内的统一端点与治理组件。

### ☸️ Kubernetes 原生与推理基础设施

*痛点："集群内路由到自托管模型（vLLM/Ollama），还要懂 GPU。"*

- [Gateway API Inference Extension](https://github.com/kubernetes-sigs/gateway-api-inference-extension) <!--s:kubernetes-sigs/gateway-api-inference-extension-->⭐ 693<!--/s--> — Kubernetes 推理感知路由标准。
- [AIBrix](https://github.com/vllm-project/aibrix) <!--s:vllm-project/aibrix-->⭐ 4.9k<!--/s--> — vLLM on K8s 的低成本控制面（字节跳动发起）。
- [llm-d](https://github.com/llm-d/llm-d) <!--s:llm-d/llm-d-->⭐ 3.4k<!--/s--> — K8s 原生分布式推理服务（红帽/谷歌/IBM 背书）。
- [Higress](https://github.com/higress-group/higress) <!--s:higress-group/higress-->⭐ 8.7k<!--/s--> / [Kong](https://github.com/Kong/kong) <!--s:Kong/kong-->⭐ 43.6k<!--/s--> / [Envoy AI Gateway](https://github.com/envoyproxy/ai-gateway) <!--s:envoyproxy/ai-gateway-->⭐ 1.7k<!--/s--> — 均已实现 inference-extension 式路由。
- [Traefik Hub AI Gateway](https://traefik.io) — Traefik 商业运行时内的 LLM 路由/安全。
- [Inference Gateway](https://github.com/inference-gateway/inference-gateway) <!--s:inference-gateway/inference-gateway-->⭐ 125<!--/s--> — 统一云端 + 本地（Ollama）模型的小型云原生网关。

## 📰 行业动态

*人工每月更新。最近审阅：2026-06-12。*

- **2026-05** · **Palo Alto Networks 完成对 Portkey 的收购**（4/30 宣布、5/29 完成），将这个 AI 网关作为其 Prisma AIRS 安全平台的控制面——标志着网关正成为核心安全基础设施。（[Palo Alto Networks](https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-completes-acquisition-of-portkey-to-secure-ai-agents)）
- **2026-05** · OpenRouter 完成 CapitalG 领投的 **1.13 亿美元 B 轮**，估值 13 亿美元——约 800 万用户、月均 ~100 万亿 token。（[TechCrunch](https://techcrunch.com/2026/05/26/openrouter-more-than-doubles-valuation-to-1-3b-in-a-year/)）
- **2026-06** · NetFoundry 发布**零信任 MCP 与 LLM 网关**，思科投资部跟投其 A 轮。（[PR Newswire](https://www.prnewswire.com/news-releases/netfoundry-launches-enterprise-class-mcp-and-llm-gateways-bringing-zero-trust-to-ai-deployments-302789053.html)）
- **2026** · Cloudflare AI Gateway 上线**美元计价消费上限**（公测），叠加动态路由与统一账单。（[Cloudflare 博客](https://blog.cloudflare.com/ai-gateway-spend-limits/)）
- **2025-11** · Pydantic AI Gateway 开放公测，随后并入 **Logfire**；F5 通过收购 **LeakSignal** 为其 AI Gateway 增加数据泄露检测。（[Pydantic Logfire](https://pydantic.dev/logfire)、[F5](https://www.f5.com/company/news/press-releases/data-leakage-detection-prevention-secure-ai-workloads)）
- **趋势** · MCP 网关成为独立品类；消费上限成为标配；**欧盟 AI 法案（2026 年 8 月起强制执行）**推高合规需求；**new-api 星数反超 one-api**，成为国内最活跃的中转系统。

## 🚀 最新版本发布（自动更新）

<!-- RELEASES:START -->
- **2026-06-14** · [yym68686/uni-api v1.7.130](https://github.com/yym68686/uni-api/releases/tag/v1.7.130) — Release 1.7.130
- **2026-06-14** · [BerriAI/litellm v1.89.0](https://github.com/BerriAI/litellm/releases/tag/v1.89.0) — v1.89.0
- **2026-06-13** · [QuantumNous/new-api v1.0.0-rc.11](https://github.com/QuantumNous/new-api/releases/tag/v1.0.0-rc.11) — v1.0.0-rc.11
- **2026-06-12** · [kgateway-dev/kgateway v2.3.3](https://github.com/kgateway-dev/kgateway/releases/tag/v2.3.3) — v2.3.3
- **2026-06-12** · [maximhq/bifrost transports/v1.5.13](https://github.com/maximhq/bifrost/releases/tag/transports/v1.5.13) — Bifrost HTTP v1.5.13
- **2026-06-11** · [andrewyng/aisuite app-v0.1.1](https://github.com/andrewyng/aisuite/releases/tag/app-v0.1.1) — OpenCoworker 0.1.1
- **2026-06-09** · [katanemo/plano 0.4.24](https://github.com/katanemo/plano/releases/tag/0.4.24) — 0.4.24
- **2026-06-06** · [envoyproxy/ai-gateway v0.7.0](https://github.com/envoyproxy/ai-gateway/releases/tag/v0.7.0) — v0.7.0
- **2026-06-04** · [tensorzero/tensorzero 2026.6.0](https://github.com/tensorzero/tensorzero/releases/tag/2026.6.0) — 2026.6.0
- **2026-06-04** · [Kong/kong 3.9.2](https://github.com/Kong/kong/releases/tag/3.9.2) — 3.9.2
- **2026-06-01** · [mlflow/mlflow v3.13.0](https://github.com/mlflow/mlflow/releases/tag/v3.13.0) — v3.13.0
- **2026-05-29** · [tbphp/gpt-load v1.4.8](https://github.com/tbphp/gpt-load/releases/tag/v1.4.8) — v1.4.8
<!-- RELEASES:END -->

## 术语表

<details>
<summary>上面表格里用到的关键术语（点击展开）</summary>

- **AI 网关 / LLM 网关** — 应用与大模型厂商之间的代理；一个端点、一把 Key 打通多模型。
- **LLM 路由** — 决定*每个请求走哪个模型*的部分（便宜款 vs 旗舰款，按成本或质量）。
- **故障转移（Fallback）** — 首选模型/厂商失败或超时时，自动改用另一个重试。
- **负载均衡（LB）** — 把流量分散到多个 Key/厂商，规避限流和宕机。
- **语义缓存** — 当*新* prompt 与历史 prompt 语义相近（而非完全相同）时返回缓存答案。
- **Prompt / 缓存输入** — 厂商对复用的 prompt 前缀大幅打折（约 0.1×）；网关若改动前缀会导致缓存失效。
- **护栏（Guardrails）** — 输入/输出检查：Prompt 注入检测、PII 脱敏、内容过滤、结构化校验。
- **虚拟 Key** — 网关在你真实厂商 Key 前面发放的按用户/团队的 Key，各带预算与限额。
- **ZDR（零数据保留）** — 厂商/网关以合约形式承诺不存储你的 prompt 和回复。
- **BYOK** — 自带 Key：网关用*你自己*的厂商账号，而非转售 token。
- **Markup（加价）** — 网关在厂商 token 成本之上收的费（0% 到约 6%）。
- **MCP 网关** — 治理 Agent ↔ 工具流量（Model Context Protocol），是 LLM 网关在智能体侧的对应物。

</details>

## 如何安全选型

1. **看加价。** 模型市场收 0–6% 不等——量大时，自托管或 0 加价网关（Vercel、Helicone 云版）很快回本。
2. **验模型真伪（canary 对比测试）。** 部分中转会偷偷降智或量化。把固定的"canary"prompt——一道已知高难推理题 + 一个 tokenizer/指纹探针——同时走网关*和*官方直连，再**对比（diff）输出**。2026 年研究发现约 46% 的受测中转出现模型身份不符（[arXiv:2603.01919](https://arxiv.org/abs/2603.01919)）。社区监测站 [apiranking.com](https://apiranking.com) 与 [rate.linux.do](https://rate.linux.do)（需浏览器打开）追踪中转的真伪与稳定性——不得不甄别时可作*信号*，但**列在那里不等于背书，本清单一个都不收录。**
3. **盯数据流向。** 所有网关都看得到你的 prompt。敏感数据：自托管，或拿到书面零数据保留（ZDR）承诺。
4. **嵌入前查协议。** new-api 是 AGPL-3.0；LiteLLM 含企业授权目录；"open core" ≠ 全部免费。
5. **看项目健康度。** 星数 ≠ 维护。看最近 release 日期——几个曾经热门的网关（BricksLLM、Glide、RouteLLM）实际已停更，本清单都打了标。
6. **远离灰产中转**（逆向接口、盗刷额度转售）。除封号风险外，2026 年研究还抓到中转投放被投毒的模型、窃取预埋密钥（[*Your Agent Is Mine*](https://arxiv.org/abs/2604.08407)）——而且最显眼的中转"榜单"往往是付费稿或带返利链接。封号和数据泄露的风险在你，不在它。

## 常见问题 FAQ

**什么是 AI 网关（LLM 网关）？**
位于你的代码与大模型厂商之间的代理：用一个 OpenAI 兼容端点和一把 Key 打通多个模型，附带路由、故障转移、缓存、限流、成本核算与护栏。见[开头介绍](#我该用哪个网关)。

**AI 网关和 LLM 路由有什么区别？**
*路由*决定每个请求*走哪个模型*（如便宜款 vs 旗舰款）；*网关*是完整的代理层（鉴权、缓存、可观测、护栏），通常*包含*路由。见[智能路由](#-智能路由与模型选择)。

**最好的开源 AI 网关是哪个？**
[LiteLLM](https://github.com/BerriAI/litellm) 功能最全（Python，100+ 厂商）；追求性能选 [Bifrost](https://github.com/maximhq/bifrost)（Go）；企业 K8s 选 [Kong](https://github.com/Kong/kong) 或 [Higress](https://github.com/higress-group/higress)。完整列表见[自托管开源](#-自托管开源)。

**LiteLLM 和 OpenRouter 怎么选？**
OpenRouter 是托管（零运维、约 5.5% 手续费、400+ 模型）；LiteLLM 是自托管（Key 在你手里、零加价）。先用托管，量大了再自托管。成本对比见[评测集](BENCHMARKS.zh-CN.md#第三部分--真实-token-成本实测脚本计算)。

**接入多个大模型最省钱的方式？**
零运维：[Vercel AI Gateway](https://vercel.com/ai-gateway) 或 [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/)（0 加价）。论 token 成本，把批量任务路由到便宜模型——一份 10 万 token 报告 **DeepSeek 花 $0.03，GPT-5.5 花 $3.01**。见[性价比优先](#-性价比优先)。

**AI 网关安全吗？谁能看到我的 Prompt？**
所有网关都看得到你的 Prompt。敏感数据请自托管或要求书面零数据保留；合规/安全评分和已知 CVE 见[网关评分卡](BENCHMARKS.zh-CN.md#第四部分--网关四维评分合规价格安全稳定)。

## 📚 必读精选

*一张短而经过核验的书单——下列每个链接都在 2026-06-15 做过实时 HTTP 检查。这些是对比表默认你已掌握的概念，定网关前先读。*

**AI 网关到底是什么**
- [LLM Gateway: The One Decision That Removes 100 AI Engineering Decisions](https://www.latent.space/p/gateway) — Latent.Space（swyx），2025-02 — 为什么一个网关选择，就把路由、缓存、可观测与护栏收敛进同一个控制面。
- [AI Gateway — overview](https://developers.cloudflare.com/ai-gateway/) — Cloudflare — 一方文档定义这一范式：在众多供应商前架一个统一端点，叠加缓存、限流、分析与成本核算。
- [AI Gateway documentation](https://developer.konghq.com/index/ai-gateway/) — Kong — 网关的关注点（供应商无关路由、PII 脱敏、token 限流）如何映射到成熟的 API 网关基础设施。

**路由与故障转移**
- [Routing & load balancing](https://docs.litellm.ai/docs/routing-load-balancing) — LiteLLM — 部署最广的开源网关给出的跨供应商路由、加权负载均衡与分级故障转移。
- [Router architecture (fallbacks & retries)](https://docs.litellm.ai/docs/router_architecture) — LiteLLM — 组内重试与跨组故障转移在遇到 429/连接错误时如何逐级升级——评估可靠性的核心机制。
- [Load balancing](https://portkey.ai/docs/product/ai-gateway/load-balancing) — Portkey — 在供应商、模型与 key 间做加权、粘性分发，让任一供应商都不成为瓶颈。
- [FrugalGPT: Using LLMs While Reducing Cost and Improving Performance](https://arxiv.org/abs/2305.05176) — Chen、Zaharia、Zou（斯坦福），2023 — 成本感知路由的奠基论文：模型级联，先试便宜的、必要时才升级。

**语义缓存**
- [GPTCache documentation](https://gptcache.readthedocs.io/) — Zilliz — 事实标准的开源语义缓存：embedding + 向量相似度 vs 精确匹配。
- [GPTCache: An Open-Source Semantic Cache for LLM Applications](https://openreview.net/forum?id=ivwM8NwM4Z) — Fu Bang，EMNLP 2023 — 经同行评审，论证相似度匹配缓存如何提升命中率、降低成本与延迟。

**Prompt 缓存（本质是前缀匹配）**
- [Prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) — Anthropic — 权威规范：缓存键由断点前的精确字节派生、读写定价与 TTL。
- [Prompt caching](https://platform.openai.com/docs/guides/prompt-caching) — OpenAI — 缓存命中需前缀精确匹配；静态指令在前、可变内容在后以最大化复用。

**推理 token 成本**
- [Building with extended thinking](https://platform.claude.com/docs/en/docs/build-with-claude/extended-thinking) — Anthropic — 推理/思考 token 同样计费且占用输出预算——在网关后启用推理模型前要懂的经济学。

**安全与护栏**
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — OWASP，2025 — 业界标准风险分类，prompt injection 为 LLM01，任何网关护栏都要对照。
- [Design patterns for securing LLM agents against prompt injection](https://simonwillison.net/2025/Jun/13/prompt-injection-design-patterns/) — Simon Willison，2025-06 — 六种具体架构防御（Dual LLM、Plan-Then-Execute、Action-Selector…）。
- [LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) — OWASP — 网关护栏层该实现的纵深防御清单。

**MCP 与 Agent 网关**
- [Model Context Protocol — specification](https://modelcontextprotocol.io/specification/2025-03-26) — 任何 MCP 网关都必须理解并治理的开放标准。
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — Anthropic，2024 — 何时用 workflow、何时用 agent，以及可组合的模式（路由、orchestrator-workers）——这正是 Agent 网关要治理的流量。
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) — Lilian Weng，2023 — agent 架构（规划、记忆、工具调用）的经典全景——MCP/Agent 网关所守护的对象。

**可观测性**
- [AI Gateway observability](https://developers.cloudflare.com/ai-gateway/observability/) — Cloudflare — 逐请求日志、token 用量、成本估算与跨供应商的 OpenTelemetry 导出。
- [How to monitor your LLM API costs](https://www.helicone.ai/blog/monitor-and-optimize-llm-costs) — Helicone — 单次查询成本追踪，以及发现缓存/模型降级机会的实操。
- [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) — Hamel Husain，2024 — 为什么系统化的 evals（而非凭感觉）才是从网关记录的请求/响应数据里真正抓出质量回退的办法。

**自托管经济学**
- [Automatic prefix caching](https://docs.vllm.ai/en/stable/design/prefix_caching/) — vLLM — KV-block 前缀缓存（及逐请求缓存隔离），自托管时省钱的底层机制。

## 指南与对比

针对大家真实搜索的问题,做了数据支撑的深度对比:

- [**one-api vs new-api vs LiteLLM**](compare/one-api-vs-new-api-vs-litellm.zh-CN.md) — 国内大模型 API 中转/网关怎么选(2026)
- [**LiteLLM vs OpenRouter vs Portkey (2026)**](compare/litellm-vs-openrouter-vs-portkey-2026.md) — 该用哪个 AI 网关?(英文)
- [**Best self-hosted AI gateway 2026**](compare/best-self-hosted-ai-gateway-2026.md) — 自托管网关对比(英文)

*更多对比陆续更新。想看哪个对比?提个 [issue](https://github.com/cuihuan/awesome-ai-gateway/issues)。*

## 参与贡献

欢迎贡献！请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。收录标准简述：必须是真正的 LLM/Agent 流量网关、代理或路由（不是 SDK 封装或聊天 UI），公开可用，且最近 12 个月内活跃——或明确标注停滞状态。

## Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=cuihuan/awesome-ai-gateway&type=Date)](https://star-history.com/#cuihuan/awesome-ai-gateway&Date)

## 许可

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，贡献者已放弃本作品的所有版权及相关权利。
