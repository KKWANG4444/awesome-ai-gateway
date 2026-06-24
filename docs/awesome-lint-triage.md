# awesome-lint triage (path to the sindresorhus/awesome submission)

`awesome-lint` runs in CI as **advisory** (`.github/workflows/ci.yml`). The success
metric in [SPEC.md](SPEC.md) is being listed in
[sindresorhus/awesome](https://github.com/sindresorhus/awesome), which requires
`awesome-lint` to pass. As of the last run it reports **622 errors + 8 warnings**,
but they collapse into a few categories — most are *design tensions* (the
pain-point layout, compact wide tables, a TOC), not defects. This file triages
them so the conformance pass is a deliberate decision, not a surprise.

Run it yourself: `npx --yes awesome-lint`.

| Rule | Count | What it wants | Disposition |
|---|---|---|---|
| `table-pipe-alignment` + `table-cell-padding` | ~300 | Every table cell space-padded so pipes align (e.g. "add 356 spaces"). | **Maintainer call.** A formatter (`prettier`/`remark`) auto-fixes it, but it bloats the source of the wide comparison tables and makes hand-edits painful. Either accept the bloat (run prettier once + add a CI check) or seek an exception. Biggest single blocker. |
| `awesome-list-item` | ~178 | Entries as `- [Name](link) - Description.` (hyphen separator, capitalized, trailing period). | **Partly fixable.** Our entries use ` — ` (em-dash) and some are table cells, not list items. A mechanical reformat is possible but changes the house style; decide hyphen-vs-em-dash first. |
| `double-link` | ~103 | A URL must not be linked twice in the README. | **Intentional.** The collapsible TOC links each section, then the body links them again — standard navigation. Fixing means dropping the in-README TOC (UX loss). Seek an exception or move the TOC out. |
| `emphasis-marker` | 36 | `*italic*` should be `_italic_`. | **Easy, do it.** Purely cosmetic, no UX impact; `prettier` fixes it in one pass. |
| `no-emphasis-as-heading` | 2 | An italic lead-in line reads as a section intro. | **Easy.** Reword the two intro lines or make them real text. |
| `no-heading-punctuation` | 1 | A heading ends with punctuation. | **Easy.** Drop the trailing punctuation. |
| `awesome-license` | 1 | License link/format expectation. | **Easy.** Check the License badge/link matches the expected form. |
| `awesome-spell-check` | 8 (⚠) | "K8s"→"Kubernetes", "WASM"→"WebAssembly". | **Optional.** Warnings only; the abbreviations are fine in image alt-text. |

## Recommended sequence (when you decide to submit)

1. **Quick wins first** (no UX cost): `emphasis-marker`, `no-emphasis-as-heading`,
   `no-heading-punctuation`, `awesome-license` — ~40 errors gone, zero design impact.
2. **Decide the two big trade-offs**: (a) table alignment — accept prettier's
   padding or request an exception; (b) the TOC double-links — keep the TOC and
   seek an exception, or relocate it. These are ~400 errors and the real decision.
3. **`awesome-list-item`**: settle hyphen-vs-em-dash, then reformat entries (or
   request an exception for the deliberate ` — ` style).
4. Re-run `npx awesome-lint`; once green (or with documented exceptions), flip the
   CI step from advisory to blocking and open the sindresorhus/awesome PR.

> Until then the CI step stays **advisory** on purpose: the list is more useful to
> readers in its current shape than it would be flattened to satisfy every rule.
> This is a curation-quality vs. lint-conformance call, made explicitly.
