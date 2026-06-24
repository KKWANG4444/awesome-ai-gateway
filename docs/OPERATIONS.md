# Operations & Growth Playbook

How this project is maintained and grown. This is a **living, executable** doc — the
maintainer (and the agent helping) work against it. Pragmatic first goal: **grow stars
and make the project active**, by being *the cited neutral authority on "which AI gateway."*

Status legend: ✅ done · ⬜ todo · 👤 maintainer-does (outward/needs a human) · 🤖 agent-can-prep

---

## 1. Theory — why people star/share this, and our levers

A GitHub star is a cheap bookmark + an identity signal. People star a list/benchmark when, in ~5s,
they can (a) classify what it is, (b) believe it saves a real decision or real money, and (c) trust
it won't rot. Leaderboards (Artificial Analysis, LMArena) spread because they become **the scoreboard
people cite in arguments** — the citation *is* the distribution.

**Our 3–4 levers, ranked:**

1. **Be the cited neutral authority.** Our edge over every vendor blog = independence (CC0, no
   affiliate $), a *reproducible* cost benchmark, and a watch-list that names sketchy relays **on
   evidence**. That's quotable. It's what gets us into listicles, Reddit threads, and AI answers.
2. **Distribution as a sequence, not one spike.** Our lead asset is the **"$788 in a day" story** +
   the **>400× price-spread table**. Spend it across HN → 阮一峰周刊/Reddit → V2EX/linux.do →
   newsletters over ~2 weeks. Concentrated velocity (not one-day) is also what trips GitHub Trending.
3. **Backlinks from other awesome-lists + listicles = compounding discovery.** The awesome-list flywheel.
4. **Liveness + responsiveness.** Daily-update CI already signals "alive"; fast, warm issue triage
   converts the unsolicited relay reports we already get into contributors.

> The **$788 story** is the single strongest hook. Lead every launch post and the HN first comment with it.

---

## 2. Issue & community operations

### Label taxonomy ✅ (created 2026-06-24)
`new-gateway` · `entry-fix` · `watch-list` · `needs-evidence` · `benchmark` · `methodology`
(+ GitHub defaults `good first issue` / `help wanted` / `question`). The `report-relay.yml` template
emits `watch-list` + `needs-evidence`, so these must exist (they now do).

### Triage SLA (solo-maintainer-realistic)
- First human response **≤48h on weekdays**: a label + one acknowledging line. Batch triage 2–3×/week; don't go fully reactive.
- `needs-evidence` reports: auto-point at `scripts/canary_check.py`; **close after 14 days** without proof (per CONTRIBUTING).
- Gateway-add PRs: review **≤5 days**; merge or request the one-line fix.

### Saved-reply templates (GitHub → Settings → Saved replies)
- **New-gateway suggestion** → "Thanks! Fits [section]. To add it I need: (1) on the request path (not an SDK/UI), (2) public repo/docs, (3) active <12mo. It's a 2-line PR — format in CONTRIBUTING; happy to label it `good first issue` and guide you."
- **Relay report w/ evidence** → "Verified — canary diff shows [X]. Adding to the watch-list with your evidence linked. Thank you — this is exactly what keeps the list credible."
- **Relay report w/o evidence** → "We only name relays on shareable proof (rumor → liability). Fastest path is a canary diff: `python scripts/canary_check.py …`. Marking `needs-evidence`; reopen anytime with output."
- **Methodology question** → answer once, then **fold it into BENCHMARKS.md / FAQ** so the next person self-serves.

### Convert reporters → contributors
Every "you should add X" → offer the 2-line PR + `good first issue`. Recognize contributors in
`CHANGELOG.md` and a README `## Contributors` block. Keep 3–5 genuinely-10-minute `good first issue`s open.

---

## 3. Launch sequence (spread over ~2 weeks, never same-day)

Lead asset everywhere: **$788/day** + **>400× price spread** + **reproducible benchmark**. Link the **repo** (not the Pages page) on HN.

| # | Channel | How | Owner |
|---|---|---|---|
| 1 | **Hacker News — Show HN** (highest ROI) | Title factual, no superlatives, explain the *approach*: `Show HN: Awesome AI Gateway – reproducible cost benchmark + scorecard for 100+ LLM gateways`. Post the $788 story as your **own first comment** within minutes. Live in-thread for hours. **Never solicit upvotes** (ring-detection nukes you). | 👤 (🤖 drafts) |
| 2 | **阮一峰《科技爱好者周刊》** | Open an issue in `ruanyf/weekly` titled `【开源自荐】…`, 200–500字: what/why, screenshot, $788 hook, license. Don't resubmit until a major update. | 👤 (🤖 drafts) |
| 3 | **r/LocalLLaMA** (best Reddit fit) | Post as a *resource* ("I mapped 100+ gateways & benchmarked cost — sharing the data"), lead with the table. Day 2–3. | 👤 (🤖 drafts) |
| 4 | **r/selfhosted** | Angle on the self-hosted/OSS gateway section. Day 4–5 (stagger). | 👤 (🤖 drafts) |
| 5 | **V2EX `/go/create`** + **linux.do** | Pure OSS share (no aff). V2EX Fri AM; linux.do needs no 推广 tag for a pure GitHub share. | 👤 (🤖 drafts) |
| 6 | **Newsletters** | Console.dev → `osh@codesee.io`; TLDR AI / Ben's Bites tip forms. | 👤 |
| 7 | **X/Twitter + dev.to** (ongoing) | Build-in-public: price-spread chart, $788 thread, weekly benchmark deltas; dev.to repurpose of the README. | 👤 (🤖 drafts) |
| — | r/MachineLearning (weekends only), lobste.rs (needs invite, <25% self-promo), Product Hunt (weak fit for a list) | low priority | — |

Subreddit etiquette: read each sub's self-promo rules; r/LLMDevs **bans** self-promo (only answer "which gateway" questions there).

---

## 4. Get listed elsewhere (the compounding flywheel)

| Target | Action | Bar | Owner |
|---|---|---|---|
| **sindresorhus/awesome** | PR adding us under AI | list ≥**30 days old**, `awesome-lint` clean (see `docs/awesome-lint-triage.md`), title-case heading, slug repo name, **review 4 other PRs**, comment `unicorn` | 👤 (🤖 preps PR) |
| **tensorchord/Awesome-LLMOps**, **InftyAI/Awesome-LLMOps** | PR under gateways/routing | fork→PR | 🤖 preps |
| **Hannibal046/Awesome-LLM** | PR under tools/infra | active queue | 🤖 preps |
| **punkpeye/ & appcypher/awesome-mcp-servers** | PR (we have an MCP/agent section) | relevant | 🤖 preps |
| **"best AI gateway" listicles** (TrueFoundry, Braintrust, denshub, …) | offer our independent benchmark as a citable source | — | 👤 |
| **AI answer engines (GEO)** | already shipped llms.txt/sitemap/JSON-LD/feed.xml; keep feed fresh (daily CI) | ✅ | 🤖 |

**Submitted backlink PRs (check here before opening new ones — don't duplicate):**
- ✅ [kelvins/awesome-mlops #216](https://github.com/kelvins/awesome-mlops/pull/216) — OPEN (Other Lists)
- ✅ [tensorchord/Awesome-LLMOps #572](https://github.com/tensorchord/Awesome-LLMOps/pull/572) — OPEN (Awesome Lists)
- ✅ [Hannibal046/Awesome-LLM #682](https://github.com/Hannibal046/Awesome-LLM/pull/682) — OPEN (Miscellaneous)
- ✅ [steven2358/awesome-generative-ai #902](https://github.com/steven2358/awesome-generative-ai/pull/902) — OPEN (More lists)
- ✅ [mahseema/awesome-ai-tools #1631](https://github.com/mahseema/awesome-ai-tools/pull/1631) — OPEN (Related Awesome Lists)
- ✅ [underlines/awesome-ml #65](https://github.com/underlines/awesome-ml/pull/65) — OPEN (llm-tools.md / Libraries & Wrappers)
- ❌ skip (verified bad fit): InftyAI/Awesome-LLMOps & EthicalML/awesome-production-machine-learning (tools-only, no meta-list section + star gate) · punkpeye/awesome-mcp-servers (MCP-only) · DefTruth/Awesome-LLM-Inference (deprecated/papers-only) · formulahendry/awesome-gpt (PR-averse, unmerged since 2023)
- ⬜ sindresorhus/awesome — gated (≥30d old + lint-clean + maintainer personally reviews 4 PRs + `unicorn`); 👤
- **6 backlink PRs is plenty for launch period — hold further submissions (more same-week = spam-perception).**

---

## 5. GitHub discovery
- **Topics** ✅ (20, incl. `benchmark`, `cost-optimization`, `llm-gateway`, `llmops`, `mcp`, `openrouter`, `litellm`).
- **Description** ✅ ("100+ …", keyword-rich).
- **Website field** ✅ (Pages site).
- **Social-preview image** ⬜👤 — upload a 1280×640 card (decision-tree or price-spread chart) at Settings → Social preview. Drives click-through on every share.
- **Profile README + pinned repos** ⬜👤 — pin all three repos; cross-link them (READMEs already cross-link ✅).
- **Trending** = star *velocity vs. own baseline* + issues/PRs/forks. Concentrate launch pushes to create velocity; keep activity flowing after.

---

## 6. Weekly cadence
| When | Do | Time |
|---|---|---|
| Daily | glance new issues/PRs, label only | 5m |
| 2–3×/wk | triage batch: respond w/ templates, merge trivial PRs | 20m |
| Weekly | post a "benchmark delta / what's new" (X + the README `📊 Latest evaluations` table); engage 1 Reddit thread genuinely | 45m |
| Weekly | refresh 1 `good first issue`; thank contributors in CHANGELOG | 15m |
| Monthly | 1 backlink PR to another awesome-list; 1 dev.to/掘金 article | 2h |

## 7. Metrics (only these)
Total stars + **weekly velocity** (star-history.com) · **GitHub Insights → Traffic → Referrers**
(which channel actually converts — double down) · issue first-response time · PR merge time. Ignore the rest.

---

## 8. Foundation status (2026-06-24)
✅ Label taxonomy created · ✅ #8 classified (`watch-list`+`needs-evidence`) · ✅ description→"100+" · ✅ topics tuned ·
✅ artifacts complete (llms.txt/sitemap/feed/JSON-LD/CITATION/SECURITY) ·
✅ launch-post drafts (`docs/launch-posts.md`) · ✅ +8 verified gateways (coverage audit) · ✅ batch pushed live (Pages verified) ·
✅ 3 awesome-list backlink PRs open (kelvins#216, tensorchord#572, Hannibal046#682) ·
⬜👤 social-preview image · ⬜👤 pin+profile README · ⬜👤 execute forum launch (drafts ready).

### Maintenance / growth log
- **2026-06-24 · accuracy audit** — all 66 GitHub-backed entries verified via `gh api`: 61 active, 5 stale/archived (TensorZero, pydantic-ai-gateway, BricksLLM, Glide, RouteLLM) — **all 5 already correctly labeled** in the list. 0 uncorrected issues; the "active within 12 months or labeled stale" promise holds. Re-run quarterly (or after big additions).
- **2026-06-24 · growth actions executed (agent-doable):** +8 verified gateways · cost-calculator.html live · 3 `good first issue`s (#11–13) · 3 awesome-list backlink PRs (kelvins#216, tensorchord#572, Hannibal046#682) · 阮一峰周刊 self-rec ([ruanyf/weekly#10435](https://github.com/ruanyf/weekly/issues/10435)).
- **Still 👤 (needs you — live presence / your account):** the real-time forum launch (HN Show HN, r/LocalLLaMA, r/selfhosted, V2EX, linux.do — drafts in `launch-posts.md`), social-preview image upload, pin repos, sindresorhus/awesome PR. These move stars most but backfire if fired without you present.

_Sources & full research: condensed from a 2026 competitive-research pass (HN/Reddit/周刊/awesome-list mechanics, GitHub Trending, issue-ops). The bottleneck is distribution + issue-ops + backlinks — not more artifacts._
