# CHANGELOG — 2026-10-13 synchronization

## Summary

Synchronized public package data with the repaired research corpus after a codebook-aligned E5 cleanup and P001 identity correction. Screening ledgers, search log, and citation-chaining log were **not** rewritten.

## What changed

| Area | Change |
|------|--------|
| Primary corpus | P001 metadata → AthenaTest arXiv `2009.05617` (2020); E5/`Real_Bugs` removed for P001, P003, P010, P024 |
| Statistics | E5 **9/64 (14.1%)**; `reports_real_bugs_flag` 9/64; year histogram includes 2020 |
| Cross-factor map | C3→E5 **ABSENT (N=0)**; C3→E4 remains STRONG (N=4); F4→E5 remains MODERATE (N=1, P011) |
| Derived matrices | CFO, coverage-fault, evidence-quality, reference map, artifact summary synced from research |
| Codebook frozen notes | Reported E5 count updated to 9/64; **E5 definition unchanged** |
| Reproduction script | Asserts updated to E5=9 / Real_Bugs=9; P001 identity spot-checks added |
| Protocol | Added `protocol/INTERPRETATION_ADDENDUM_2026-10-13.md` (post-hoc BART/IC1 + foundational-primary) |

## Why E5 changed from 13 to 9

Under the codebook, **E5** requires reported historical / real-fault / production-bug detection — not coverage, correctness, or mutation alone, and not merely using Defects4J as a fixed-code benchmark.

Unsupported E5 codes withdrawn:

| ID | Study | Reason (brief) |
|----|-------|----------------|
| P001 | AthenaTest | Fixed-version coverage/correctness; authors defer fault-detection analysis |
| P003 | A3Test | Correct tests + method coverage; fault detection listed as future work |
| P010 | Domain adaptation / CodeT5 | Line coverage + mutation score; no real-bug detection experiment |
| P024 | CasModaTest | Accuracy + focal-method coverage only |

Retained E5 IDs (9): P007, P011, P017, P021, P030, P033, P036, P041, P045.

## How P001 identity was corrected

Frozen P001 mixed AthenaTest’s title/authors with the Methods2Test MSR 2022 DOI (`10.1145/3524842.3528009`) and arXiv `2203.12776`. The corrected record is AthenaTest (arXiv `2009.05617`, 2020). Screening CSV rows that still show the Methods2Test DOI are retained as **historical** evidence of the splice.

## Foundational-study clause and BART/IC1

Documented in `protocol/INTERPRETATION_ADDENDUM_2026-10-13.md`. Both readings are author-approved **2026-10-13** post-hoc decisions — not preregistered and not contemporaneous with the 2026-10-05 freeze.

## Historical artifacts left unchanged

- `data/fulltext_screening_decisions.csv`
- `protocol/search_log.md`
- `protocol/citation_chaining_log.md`
- Pre-sync backups under the parent survey repo `audit_pre_resubmission/stvr_repair_plan_v1/backups_*`
