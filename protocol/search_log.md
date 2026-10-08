# Search Log — Phase 1 Discovery

**Date:** 2026-10-05
**Sources:** OpenAlex, Semantic Scholar, Crossref
**Primary year window:** 2021–2026 (seeds searched without year filter)
**Contact (polite pool):** [CONTACT_REDACTED]

## Summary

- Query strings executed: 22
- Seed titles resolved: 12/12
- Survey titles resolved: 2/2
- Raw hits collected (pre-dedupe): 2132
- Deduplicated candidates: 995
- Triage likely_include: 363
- Triage survey_candidate: 10
- Triage review: 599
- Triage likely_exclude: 23
- Raw dump directory: `data/raw/phase1_2026-10-05`
- Candidate CSV: `data/processed/candidates_phase1.csv`

## Important

Triage labels are **keyword heuristics only**. They are **not** final inclusion decisions.
Phase 2 verifies metadata; Phase 3 applies full IC/EC on eligible texts.

## Query executions

| Source | Query | Date | Hits returned | Notes |
|--------|-------|------|---------------|-------|
| openalex+s2 | SEED:An Empirical Evaluation of Using Large Language Models for Automated Unit Test Generation | 2026-10-05 | 2 | seed title resolve |
| openalex+s2 | SEED:CODAMOSA: Escaping Coverage Plateaus in Test Generation with Pre-trained Large Language Models | 2026-10-05 | 2 | seed title resolve |
| openalex+s2 | SEED:ChatUniTest: A Framework for LLM-Based Test Generation | 2026-10-05 | 2 | seed title resolve |
| openalex+s2 | SEED:Effective Test Generation Using Pre-trained Large Language Models and Mutation Testing | 2026-10-05 | 2 | seed title resolve |
| openalex+s2 | SEED:Code-Aware Prompting: A Study of Coverage-Guided Test Generation in Regression Setting Using LLM | 2026-10-05 | 2 | seed title resolve |
| openalex+s2 | SEED:Enhancing LLM-based Test Generation for Hard-to-Cover Branches via Program Analysis | 2026-10-05 | 1 | seed title resolve |
| openalex+s2 | SEED:HITS: High-coverage LLM-based Unit Test Generation via Method Slicing | 2026-10-05 | 2 | seed title resolve |
| openalex+s2 | SEED:On the Evaluation of Large Language Models in Unit Test Generation | 2026-10-05 | 2 | seed title resolve |
| openalex+s2 | SEED:CoverUp: Effective High Coverage Test Generation for Python | 2026-10-05 | 2 | seed title resolve |
| openalex+s2 | SEED:A Large-Scale Empirical Study on Fine-Tuning Large Language Models for Unit Testing | 2026-10-05 | 2 | seed title resolve |
| openalex+s2 | SEED:Mutation-Guided Unit Test Generation with a Large Language Model | 2026-10-05 | 2 | seed title resolve |
| openalex+s2 | SEED:TestCTRL: Automated Unit Test Generation via Chain-of-Thought Prompt and Reinforcement Learning from Coverage Feedback | 2026-10-05 | 2 | seed title resolve |
| openalex+s2 | SURVEY:Unit Test Generation Using Large Language Models: A Systematic Literature Review | 2026-10-05 | 2 | survey title resolve |
| openalex+s2 | SURVEY:Large Language Models for Unit Test Generation: Achievements, Challenges, and the Road Ahead | 2026-10-05 | 1 | survey title resolve |
| openalex | large language model unit test generation | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | large language model unit test generation | 2026-10-05 | 40 | year 2021-2026; limit 40 |
| openalex | LLM unit testing | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | LLM unit testing | 2026-10-05 | 40 | year 2021-2026; limit 40 |
| openalex | LLM test generation | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | LLM test generation | 2026-10-05 | 40 | year 2021-2026; limit 40 |
| openalex | ChatGPT unit test generation | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | ChatGPT unit test generation | 2026-10-05 | 40 | year 2021-2026; limit 40 |
| openalex | GPT unit testing | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | GPT unit testing | 2026-10-05 | 40 | year 2021-2026; limit 40 |
| openalex | LLM software testing unit tests | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | LLM software testing unit tests | 2026-10-05 | 40 | year 2021-2026; limit 40 |
| openalex | LLM mutation testing | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | LLM mutation testing | 2026-10-05 | 40 | year 2021-2026; limit 40 |
| openalex | LLM fault detection unit test | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | LLM fault detection unit test | 2026-10-05 | 40 | year 2021-2026; limit 40 |
| openalex | LLM test repair | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | LLM test repair | 2026-10-05 | 40 | year 2021-2026; limit 40 |
| openalex | LLM coverage guided test generation | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | LLM coverage guided test generation | 2026-10-05 | 40 | year 2021-2026; limit 40 |
| openalex | LLM feedback test generation | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | LLM feedback test generation | 2026-10-05 | 40 | year 2021-2026; limit 40 |
| openalex | LLM iterative test generation | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | LLM iterative test generation | 2026-10-05 | 40 | year 2021-2026; limit 40 |
| openalex | repository context LLM testing | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | repository context LLM testing | 2026-10-05 | 40 | year 2021-2026; limit 40 |
| openalex | retrieval augmented unit test generation | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | retrieval augmented unit test generation | 2026-10-05 | 40 | year 2021-2026; limit 40 |
| openalex | program analysis LLM unit tests | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | program analysis LLM unit tests | 2026-10-05 | 40 | year 2021-2026; limit 40 |
| openalex | real world LLM unit testing | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | real world LLM unit testing | 2026-10-05 | 40 | year 2021-2026; limit 40 |
| openalex | Defects4J LLM test generation | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | Defects4J LLM test generation | 2026-10-05 | 40 | year 2021-2026; limit 40 |
| openalex | mutation score LLM generated tests | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | mutation score LLM generated tests | 2026-10-05 | 40 | year 2021-2026; limit 40 |
| openalex | ChatUniTest | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | ChatUniTest | 2026-10-05 | 11 | year 2021-2026; limit 40 |
| openalex | CODAMOSA | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | CODAMOSA | 2026-10-05 | 5 | year 2021-2026; limit 40 |
| openalex | CoverUp unit test | 2026-10-05 | 50 | filter year 2021-2026; top 50 |
| semanticscholar | CoverUp unit test | 2026-10-05 | 40 | year 2021-2026; limit 40 |
| openalex | MuTAP mutation LLM | 2026-10-05 | 40 | filter year 2021-2026; top 50 |
| semanticscholar | MuTAP mutation LLM | 2026-10-05 | 40 | year 2021-2026; limit 40 |
| crossref | large language model unit test generation | 2026-10-05 | 25 | filter 2021-2026; rows 25 |
| crossref | LLM unit testing | 2026-10-05 | 25 | filter 2021-2026; rows 25 |
| crossref | LLM test generation | 2026-10-05 | 25 | filter 2021-2026; rows 25 |
| crossref | ChatGPT unit test generation | 2026-10-05 | 25 | filter 2021-2026; rows 25 |
| crossref | GPT unit testing | 2026-10-05 | 25 | filter 2021-2026; rows 25 |
| crossref | LLM software testing unit tests | 2026-10-05 | 25 | filter 2021-2026; rows 25 |
| crossref | LLM mutation testing | 2026-10-05 | 25 | filter 2021-2026; rows 25 |
| crossref | LLM fault detection unit test | 2026-10-05 | 25 | filter 2021-2026; rows 25 |

## Seed resolution

| Seed title | Resolved? | Best match title | DOI | Sources |
|------------|-----------|------------------|-----|---------|
| An Empirical Evaluation of Using Large Language Models for Automated Unit Test Generation | yes | An Empirical Evaluation of Using Large Language Models for Automated Unit Test Generation | 10.1109/tse.2023.3334955 | openalex+semanticscholar |
| CODAMOSA: Escaping Coverage Plateaus in Test Generation with Pre-trained Large Language Models | yes | CodaMosa: Escaping Coverage Plateaus in Test Generation with Pre-trained Large Language Models | 10.1109/icse48619.2023.00085 | openalex+semanticscholar |
| ChatUniTest: A Framework for LLM-Based Test Generation | yes | ChatUniTest: A Framework for LLM-Based Test Generation | 10.1145/3663529.3663801 | openalex+semanticscholar |
| Effective Test Generation Using Pre-trained Large Language Models and Mutation Testing | yes | Effective test generation using pre-trained Large Language Models and mutation testing | 10.1016/j.infsof.2024.107468 | openalex+semanticscholar |
| Code-Aware Prompting: A Study of Coverage-Guided Test Generation in Regression Setting Using LLM | yes | Code-Aware Prompting: A Study of Coverage-Guided Test Generation in Regression Setting using LLM | 10.1145/3643769 | openalex+semanticscholar |
| Enhancing LLM-based Test Generation for Hard-to-Cover Branches via Program Analysis | yes | Enhancing LLM-based Test Generation for Hard-to-Cover Branches via Program Analysis | 10.48550/arxiv.2404.04966 | semanticscholar |
| HITS: High-coverage LLM-based Unit Test Generation via Method Slicing | yes | HITS: High-coverage LLM-based Unit Test Generation via Method Slicing | 10.1145/3691620.3695501 | openalex+semanticscholar |
| On the Evaluation of Large Language Models in Unit Test Generation | yes | On the Evaluation of Large Language Models in Unit Test Generation | 10.1145/3691620.3695529 | openalex+semanticscholar |
| CoverUp: Effective High Coverage Test Generation for Python | yes | CoverUp: Effective High Coverage Test Generation for Python | 10.1145/3729398 | openalex+semanticscholar |
| A Large-Scale Empirical Study on Fine-Tuning Large Language Models for Unit Testing | yes | A Large-Scale Empirical Study on Fine-Tuning Large Language Models for Unit Testing | 10.1145/3728951 | openalex+semanticscholar |
| Mutation-Guided Unit Test Generation with a Large Language Model | yes | Mutation-Guided Unit Test Generation With a Large Language Model | 10.1109/tse.2026.3682975 | openalex+semanticscholar |
| TestCTRL: Automated Unit Test Generation via Chain-of-Thought Prompt and Reinforcement Learning from Coverage Feedback | yes | Automated Unit Test Generation via Chain-of-Thought Prompt and Reinforcement Learning from Coverage Feedback | 10.1145/3745765 | openalex+semanticscholar |

## Survey resolution

| Survey title | Resolved? | Best match title | DOI | Sources |
|--------------|-----------|------------------|-----|---------|
| Unit Test Generation Using Large Language Models: A Systematic Literature Review | yes | Unit Test Generation Using Large Language Models: A Systematic Literature Review | 10.15388/lmitt.2024.20 | openalex+semanticscholar |
| Large Language Models for Unit Test Generation: Achievements, Challenges, and the Road Ahead | yes | Large Language Models for Unit Test Generation: Achievements, Challenges, and the Road Ahead | — | semanticscholar |

## Next steps

1. Manually review `likely_include` + `review` rows in the candidate CSV.
2. Resolve missing DOIs / venue conflicts across OpenAlex vs Semantic Scholar vs Crossref.
3. Begin citation chaining (backward/forward) on high-relevance seeds.
4. Proceed to Phase 2 verification for shortlisted papers.

---

## Phase 2 — Reconciliation & screening (2026-10-05)

**Sources used:** OpenAlex, Semantic Scholar, Crossref (bibliographic APIs); arXiv Atom API; ACM/publisher pages via WebFetch for selected surveys and key preprints; Deep Research reports treated as discovery only.

### Reconciliation

| Check | Result |
|-------|--------|
| DR46 matched in Phase1 | 39/46 |
| DR46 matched in shortlist | 36/46 |
| DR-only | 7 |
| Bibliographic status after API+manual | 38 PARTIALLY VERIFIED, 8 PREPRINT (0 UNVERIFIED remaining) |
| Named surveys resolved | 10/10 |

Outputs: `research/corpus_reconciliation.csv`, `research/existing_surveys.csv`, `data/processed/phase2_bib_lookup.json`.

### Shortlist IC/EC screen (title/abstract)

| Decision | Count |
|----------|------:|
| INCLUDE (incl. 46 DR) | 146 |
| EXCLUDE | 235 |
| SECONDARY | 2 |
| UNCERTAIN | 37 |

Outputs: `data/processed/phase2_screening_decisions.csv`, `research/literature_matrix.csv`, `research/coverage_fault_evidence.csv`, `research/phase2_report.md`.

### Citation chaining

**Status:** not yet run as a formal round.  
**Plan:** forward/backward chaining from must-read set (`research/must_read_papers.md`) via Semantic Scholar / OpenAlex; log new eligible hits here before matrix insertion.

### Important corrections logged

- TypeTest (arXiv:2503.14000v1) → Test4Py / retitled v2
- MocklessTester → IntTestGen (arXiv:2605.26851v2)
- Chu et al. corpus 115 → **178** (v3 through 2026-07-31)
- Do not claim prior surveys omit context/feedback


## Phase 2 Freeze — 2026-10-05

- Full-text/provisional screen of 100 shortlist includes → `fulltext_screening_decisions.csv`
- Citation chaining Round 1 (+conditional Round 2) → `citation_chaining_log.md`
- Must-read claim verification → `verified_claims.csv`
- Frozen primary corpus n=64 → `final_primary_corpus.csv`
