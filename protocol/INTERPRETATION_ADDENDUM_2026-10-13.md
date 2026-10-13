# Protocol Interpretation Addendum — 2026-10-13

**Status:** Author-approved post-hoc interpretation.
**Not preregistered.** Not contemporaneous with the 2026-10-05 screening freeze.
**Does not rewrite** the IC1–IC5 body text or the 2021–2026 search-window sentence in `inclusion_exclusion.md`.
**Companion change log:** `../CHANGELOG_2026-10-13.md`.

---

## Purpose

Document how existing protocol wording was applied when correcting P001 identity and when counting AthenaTest (BART, 2020) as a primary study.

---

## IC1 — pretrained foundation language models (including BART)

**Protocol IC1 (unchanged):** the work uses one or more large language models / foundation models (including ChatGPT, Codex, CodeLlama, StarCoder, etc.) as a core component of unit-level test generation.

**Author-approved reading (2026-10-13):** The parenthetical list is illustrative, not exhaustive. A **pretrained foundation language model** used as the core generator of unit tests satisfies IC1 even when it is an encoder–decoder architecture. **BART**, as used in AthenaTest (arXiv `2009.05617`) for focal-context unit-test generation, is in scope for IC1. EC1 (“Not LLM-based”) does not apply to BART-based unit-test generation under this reading.

---

## Foundational-primary year clause (protocol lines 5–6)

**Protocol text (unchanged):**

> **Search window (primary):** 2021–2026
> **Foundational earlier work:** included when necessary for background … but not counted as primary LLM–unit-test studies unless they meet IC1–IC5.

**Author-approved invocation for P001 (2026-10-13):** AthenaTest (2020) is outside the default 2021–2026 window. It is counted as primary P001 because:

1. Screening/seed intent (DR46) targeted this work (AthenaTest title / aka), not the later Methods2Test dataset paper alone.
2. IC1–IC5 are met under the BART IC1 reading above.
3. The study is foundational for transformer + focal-context unit-test generation in this literature line.
4. Admission uses only the documented “unless they meet IC1–IC5” path.

**Identity:** P001 bibliographic fields refer to AthenaTest (`2009.05617`, 2020). The Methods2Test ACM DOI `10.1145/3524842.3528009` is not the P001 primary identity.

---

## Historical screening ledgers

`data/fulltext_screening_decisions.csv` and related screening logs are **preserved as historical**. They may still show the pre-correction Methods2Test DOI splice for the AthenaTest title row. Those rows were **not** rewritten to appear contemporaneous with this addendum.
