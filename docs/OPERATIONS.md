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

## 3. Launch sequence (one concentrated 48–72h burst — distinct post per channel)

> **Corrected 2026-06-25 (was "spread over ~2 weeks").** GitHub Trending ranks star *velocity vs. this repo's own ~1–2 star/day baseline*, so 15–25 stars in one day is already a large multiple — spreading the same posts over two weeks *dilutes* that multiple. HN delivers ~92% of its star impact within 48h. So: fire the high-velocity channels inside **one 48–72h window** (ideally Mon–Tue ~13–16 UTC), each with a **channel-distinct** post (copy-paste across subreddits triggers shadowbans), and stay present to answer. "Never same-day" still applies *per channel* (don't repost the same HN/subreddit), not across channels.

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
| **tensorchord/Awesome-LLMOps** | PR under gateways/routing | fork→PR | ✅ submitted #572 |
| **Hannibal046/Awesome-LLM** | PR under tools/infra | active queue | ✅ submitted #682 |
| ~~InftyAI/Awesome-LLMOps~~ · ~~punkpeye/awesome-mcp-servers~~ | — | verified bad fit (don't PR) | ❌ skip — but punkpeye is now **reciprocally linked** in our Related-lists footer |
| **Next-wave awesome targets** (see §9): kyrolabs/awesome-langchain, eudk/awesome-ai-tools, awesomelistsio/awesome-llmops | PR under each list's meta/LLMOps section | verified actively-merging 2026 | 🤖 preps — hold ~1/mo |
| **"best AI gateway" listicles** (TechSY, TrueFoundry, Braintrust, denshub, …) + **OpenAlternative.co** directory | offer our independent benchmark as a citable source / submit via their form | — | 👤 |
| **AI answer engines (GEO)** | llms.txt/sitemap/JSON-LD/feed shipped; **+ machine-readable `dateModified` + IndexNow→Bing shipped 2026-06-25**; Bing WMT account still 👤 (see §9) | partial — see §9 | 🤖 + 👤 |

**Submitted backlink PRs (check here before opening new ones — don't duplicate):**
- ✅ [kelvins/awesome-mlops #216](https://github.com/kelvins/awesome-mlops/pull/216) — OPEN (Other Lists)
- ✅ [tensorchord/Awesome-LLMOps #572](https://github.com/tensorchord/Awesome-LLMOps/pull/572) — OPEN (Awesome Lists)
- ✅ [Hannibal046/Awesome-LLM #682](https://github.com/Hannibal046/Awesome-LLM/pull/682) — OPEN (Miscellaneous)
- ✅ [steven2358/awesome-generative-ai #902](https://github.com/steven2358/awesome-generative-ai/pull/902) — OPEN (More lists)
- ✅ [mahseema/awesome-ai-tools #1631](https://github.com/mahseema/awesome-ai-tools/pull/1631) — OPEN (Related Awesome Lists)
- ✅ [underlines/awesome-ml #65](https://github.com/underlines/awesome-ml/pull/65) — OPEN (llm-tools.md / Libraries & Wrappers)
- ❌ skip (verified bad fit): InftyAI/Awesome-LLMOps & EthicalML/awesome-production-machine-learning (tools-only, no meta-list section + star gate) · punkpeye/awesome-mcp-servers (MCP-only) · DefTruth/Awesome-LLM-Inference (deprecated/papers-only) · formulahendry/awesome-gpt (PR-averse, unmerged since 2023)
- ⏳ sindresorhus/awesome — **eligible ~2026-07-11** (repo created 2026-06-11; the ≥30-day gate is the only blocker — topics/branch already pass). Then: lint-clean + maintainer personally reviews 4 PRs + `unicorn`; 👤. Do NOT submit before then (auto-closed).
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

---

## 9. Deep-research update (2026-06-25) — evidence-backed method v2

A 6-agent research pass (how comparable awesome-lists + LLM-gateway projects actually grow & maintain, + GEO citation mechanics, + verified new backlink targets) sharpened the method. The headline: **the moat is credibility + freshness, and the unfixed bottleneck is the retrieval layer (Bing) + the human-led launch — not more on-page artifacts.**

### 9a. What the research changed (corrections to conventional wisdom — all evidence-backed)
- **llms.txt is near-dead for AI *citations*** (~0.1% of AI-bot traffic touches it; Google's Illyes confirmed Google won't support it). Keep it (≈0 cost) but **reclassify it as a B2A / IDE-agent convenience** (Cursor/Claude Code/Copilot *do* fetch it); optionally add `/llms-full.txt`. It is *not* the GEO win §4 used to imply.
- **The real GEO precondition is being in Bing's index** — ~87% of ChatGPT Search citations match Bing top results. → shipped **IndexNow** (push protocol, no account needed) + machine-readable **`dateModified`**; Bing Webmaster Tools account is still 👤 (9d).
- **Buying stars backfires** (controlled study: zero effect on real downloads; detection tooling flags the inorganic spike — the *opposite* of the velocity pattern Trending rewards). The maintainer's no-fraud stance is *empirically* correct, not just ethical.
- **"Show HN" tag isn't magic** — engagement *score* predicts stars (r≈0.29), comment count barely does (r≈0.10). Optimize for a clear factual title + fast author replies, not a lively comment thread.
- **Badge walls + posting-time obsession are cargo-cult** — current 5–6 functional badges are at the right ceiling; best-vs-worst HN slot is only ~4×. Don't let timing anxiety delay a ready launch.
- **"Asking for stars" is nuanced, not banned** — a soft README CTA + *personalized 1:1 thank-you-and-ask* to people who already engaged converts; generic "please star" pleas + mass-DMs are spam. Crossing **~100 real stars** is the human-credibility gate that lets organic traffic convert against a visible number.
- **The 2014 category land-grab is not replicable in 2026** — `awesome-ai-gateway` enters a crowded namespace, so chasing first-mover timing is wasted; win on the moats incumbents won't build (independence/CC0, the reproducible $788 benchmark, the evidence-based relay watch-list).

### 9b. Shipped 2026-06-25 (agent-doable, done)
- ✅ **IndexNow** key + `scripts/ping_indexnow.py` (+6 unit tests) + daily-CI ping step → Bing/Yandex discovery.
- ✅ **Machine-readable freshness** — `dateModified`/`datePublished` + `article:modified_time` on compare pages, auto-stamped from the byline (never fabricated).
- ✅ **Reciprocal "Related lists" footer** (EN+zh) — the backlink-graph play's missing half.
- ✅ **Release-tracking** for the 13 audit-added repos; **CHANGELOG** brought current + first contributor (@c99e) credited.

### 9c. Agent-doable queue (next iterations — do NOT do all at once; one focused change per loop)
1. **Add `dateModified` to the 8 static guide pages + index.html** (currently only compare/* have it). Honest date = file's last-commit date.
2. **Extend schema**: `FAQPage` on compare pages (only top-level pages have it), `ItemList` for the ranked list on README/index, `SoftwareApplication` (sameAs→repo) for the top 4 gateways. *Each FAQ Q&A is a citation candidate (highest-leverage GEO schema).*
3. **"Key numbers" block** — surface the proprietary stats ($0.03-vs-$3.01 = 106×, $788, >400×) as standalone **dated + sourced one-sentence claims** atop each comparison page. The only peer-reviewed GEO study (Princeton/KDD-2024) shows Statistics + Quotations + Cite-Sources each yield +30–40% AI visibility.
4. ✅ **DONE 2026-06-25** — **"won't-rot" stale-gateway CI** (`scripts/check_stale_gateways.py` + monthly `stale-check.yml` + published removal rule in CONTRIBUTING). Flags any release-tracked repo that's archived/no-push-in-12mo AND not already ⚠️-labeled (cross-references the README), so the "active within 12mo or labeled stale" promise is mechanical. Advisory (own workflow, doesn't touch the main CI badge); red only on an actionable unlabeled-stale or a 0-coverage fetch failure. Code-reviewer-vetted (caught + fixed a substring-match blocker). Link-check workflow already existed; keep the contribution *gate* narrow (3-criteria + 5-day SLA) — the opposite of punkpeye's 1,700-open-PR firehose.
5. **Above-the-fold visual** — a GIF/screenshot of gateway-picker.html / the decision tree (the one missing <7s-conversion element; ≈2× conversion). *May need 👤 for a clean browser capture.*

### 9d. New verified backlink/listing targets (the NEXT WAVE — hold to ~1/month; 6 already open is enough for the launch window)
| Target | Section we fit | Recent-merge evidence | Priority |
|---|---|---|---|
| [kyrolabs/awesome-langchain](https://github.com/kyrolabs/awesome-langchain) (9.4k★) | `## Complement to this list` (+ optional fix: flag the now-archived TensorZero under `## Other LLM Frameworks` as reviewer value-add) | merged ext. PRs #327/#322 (2026-04-26), #215/#210 (03-14); **0 open PRs** | **TOP** |
| [eudk/awesome-ai-tools](https://github.com/eudk/awesome-ai-tools) (522★) | `## LLM Ops` | 10 recent merges 2026-06-05→07 from distinct authors | secondary (≠ the already-submitted mahseema/awesome-ai-tools #1631) |
| [awesomelistsio/awesome-llmops](https://github.com/awesomelistsio/awesome-llmops) | `## Related Awesome Lists` | ext. PRs #16 (06-22), #28 (06-23); 0 open | lowest-friction (small but compounding network cross-links) |
| [OpenAlternative.co](https://github.com/piotrkulpinski/openalternative) (6.4k★) | AI-gateways category, via /submit form | repo pushed 2026-06-24; public /submit | best **non-awesome** directory — 👤 (lists tools, not catalogs; submit individual angle) |
| [TechSY "8 Gateways Ranked 2026"](https://techsy.io/en/blog/best-llm-gateway-tools) | listicle citation (no PR path) | updated 2026-06-13; admits it uses only internal testing + star counts, **no independent benchmark** | 👤 outreach — offer our benchmark as the missing independent cross-check |

### 9e. 👤 Maintainer-only — the moves that actually move stars now (agent has maxed the prep)
1. **Create a Bing Webmaster Tools account** (bing.com/webmasters) → *Import from Google Search Console* (1-click) → submit `sitemap.xml` → record the June-2026 **Citation Share** baseline (it can't be backfilled, so every week of delay loses trend history). This unlocks the IndexNow pings already firing.
2. **Submit to sindresorhus/awesome** — ⏳ **NOT YET ELIGIBLE.** The repo was created **2026-06-11**, and sindresorhus auto-closes lists **< 30 days old** — so the earliest valid submission is **~2026-07-11**. Topics (`awesome`+`awesome-list`) ✅ and branch `main` ✅ already pass; only the age blocks it. *(Correcting an earlier note that claimed we clear the age gate — we don't until mid-July.)* When eligible: agent preps (`npx awesome-lint` to zero via `docs/awesome-lint-triage.md`, PR body); you open the PR, **review 4 other open PRs**, post `unicorn` in one sitting. No star minimum exists. This is the single biggest evergreen backlink — worth doing the day it's eligible.
3. **Run the 48–72h launch burst** (§3) — HN (factual title, $788 first comment) + r/LocalLLaMA + r/selfhosted + one newsletter, channel-distinct posts, present to answer. Drafts in `docs/launch-posts.md` (agent keeps them channel-distinct).
4. **Warm 1:1 outreach** to people who already engaged (issue reporters, the #14 contributor, anyone who forked) — the proven path to the first ~100 real stars.
