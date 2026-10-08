# Inclusion and Exclusion Criteria

**Survey working title:** From Code Coverage to Fault Detection: A Systematic Review of Context and Feedback in LLM-Based Unit Test Generation for Real-World Software

**Search window (primary):** 2021–2026  
**Foundational earlier work:** included when necessary for background (e.g., classical ATG, mutation testing foundations), but not counted as primary LLM–unit-test studies unless they meet IC1–IC5.

**Protocol status:** Updated for Phase 2 screening (2026-10-05). Operational EC codes below align screening decisions in `data/fulltext_screening_decisions.csv`. Any further change will be logged in `search_log.md`.

---

## Inclusion Criteria (primary studies)

A paper is a **candidate primary study** if it satisfies **all** of IC1–IC3 and **at least one** of IC4–IC5.

| ID | Criterion |
|----|-----------|
| **IC1** | The work uses one or more **large language models / foundation models** (including ChatGPT, Codex, CodeLlama, StarCoder, etc.) as a core component of **unit-level test generation** (or generation + repair of unit tests). |
| **IC2** | The work reports an **empirical evaluation** of generated unit tests (quantitative metrics and/or structured qualitative analysis on programs). |
| **IC3** | Evaluation uses **actual code artifacts**: programs, repositories, or established benchmarks (not purely hypothetical examples). |
| **IC4** | The study analyzes or manipulates **context** supplied to the LLM, **prompting/generation strategy**, **feedback**, **iterative repair**, **coverage**, **mutation testing**, and/or **fault/bug detection**. |
| **IC5** | Methodological detail is sufficient to extract at least: model family, evaluation setting, and one adequacy or fault-detection metric. |

**Existing surveys / SLRs** are collected separately (not as primary studies) if they systematically review LLM-based (unit) test generation or closely related SE testing with LLMs.

---

## Exclusion Criteria

Legacy Phase 1 labels (EC1–EC8) are retained for continuity. Phase 2 screening also uses the standardized operational codes below (preferred in decision logs).

### Operational screening codes (Phase 2+)

| ID | Criterion |
|----|-----------|
| **EC1** | Not LLM-based |
| **EC2** | Not unit-test / test-generation research (or only incidental mention) |
| **EC3** | Fuzzing only (no substantive unit-test generation evaluation) |
| **EC4** | Oracle/assertion-only and outside primary UTG scope |
| **EC5** | Test selection/prioritization only |
| **EC6** | General code generation (not UTG) |
| **EC7** | No empirical evaluation |
| **EC8** | Wrong testing level/domain (GUI/system/hardware/RTL/etc.) |
| **EC9** | Duplicate / preprint version of an included study |
| **EC10** | Secondary study (survey/SLR) — track separately |
| **EC11** | Insufficient relevance |
| **EC12** | Inaccessible / unverifiable bibliographic record |
| **EC13** | Other — explain in Notes |

### Legacy Phase 1 mapping (informational)

| Legacy | Maps roughly to |
|--------|-----------------|
| Legacy EC1 GUI/system | Operational EC8 |
| Legacy EC2 no UTG | Operational EC2 |
| Legacy EC3 opinion/no empirics | Operational EC7 |
| Legacy EC4 duplicates | Operational EC9 |
| Legacy EC5 unverifiable | Operational EC12 |
| Legacy EC6 incidental | Operational EC2/EC6 |
| Legacy EC7 non-scholarly | Operational EC12/EC13 |
| Legacy EC8 non-English | Operational EC13 |

---

## Screening stages

1. **Title/abstract screen** → candidate pool (`data/processed/candidates_phase1.csv`)
2. **Full-text eligibility** → included primary studies (`research/literature_matrix.csv`)
3. **Bibliographic verification** → `research/verification_log.md` statuses

---

## Decision notes

- Prefer **peer-reviewed** venue versions over arXiv when both exist.
- Preprints remain eligible if they meet IC1–IC5; status marked `PREPRINT` until verified peer-reviewed version is found.
- Strong relevance to **context + feedback + fault detection** is preferred when ranking for must-read notes, but inclusion itself follows IC/EC above.
