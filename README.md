# Context and Feedback in Repository-Level LLM Unit-Test Generation: Replication Package

This repository is a **research data and reproducibility package** for a systematic review of empirical studies on LLM-based unit-test generation. It focuses on **context construction**, **feedback/repair**, **repository realism**, and an **evaluation hierarchy** from executability through coverage and mutation to real-fault evidence.

It contains the frozen corpus tables, screening protocol, taxonomy codebook, evidence coding, and scripts needed to recompute headline statistics.

**This repository does not host the manuscript.** Publication details (citation to the paper, journal DOI, etc.) can be added after publication.

## Corpus freeze

| Item | Value |
|------|------:|
| Freeze date | 2026-10-05 |
| Primary studies | 64 (P001–P064) |
| Secondary surveys | 10 (S01–S10; not mixed into \(n=64\) denominators) |
| Mutation evaluation (E4) | 12/64 (18.8%) |
| Real-fault evidence (E5) | 13/64 (20.3%) |

Spot checks encoded in the reproduction script:

- **P061** is `E3;E4` with `Real_Bugs=no` (not E5).
- **P037** canonical venue is ICST 2026 (DOI `10.1109/ICST69053.2026.00040`); arXiv is retained as preprint URL only.

## Repository layout

```
public-replication-package/
├── README.md
├── CITATION.cff
├── LICENSE-CODE          # MIT — scripts/
├── LICENSE-DATA          # CC BY 4.0 — data/ + protocol/
├── .gitignore
├── data/                 # frozen CSVs
├── protocol/             # search, IC/EC, chaining, codebook
└── scripts/              # reproduce_statistics.py
```

## Taxonomy overview

Definitions live in `protocol/codebook.md`:

- **Context** C0–C5
- **Feedback** F0–F7
- **Repair** R0–R7
- **Evaluation** E0–E6 (E3 coverage-related; E4 mutation; E5 historical/real faults)
- **Realism** RL0–RL4

## Data files (`data/`)

| File | Role |
|------|------|
| `final_primary_corpus.csv` | Frozen primary corpus + taxonomy codes |
| `final_secondary_studies.csv` | Ten secondary surveys |
| `fulltext_screening_decisions.csv` | Full-text / provisional screening decisions |
| `verified_claims.csv` | Numeric / claim verification log |
| `context_feedback_outcome_matrix.csv` | Per-study context / feedback / outcome codes |
| `coverage_fault_evidence.csv` | Coverage / mutation / real-fault relationship sheet |
| `evidence_quality_matrix.csv` | Q1–Q10 reporting dimensions |
| `prisma_final_counts.csv` | Auditable selection-stage counts |
| `primary_study_reference_map.csv` | P001–P064 bibliographic keys and DOI/venue map |
| `final_corpus_statistics.csv` | Precomputed corpus statistics (cross-check) |
| `cross_factor_evidence_map.csv` | Co-occurrence / evidence-strength map |
| `artifact_summary.csv` | Artifact confirmation coding |

## Protocol (`protocol/`)

- `search_log.md` — recorded API queries and hit counts
- `inclusion_exclusion.md` — IC/EC criteria and operational screening codes
- `citation_chaining_log.md` — citation-chaining round
- `codebook.md` — taxonomy definitions and classification notes

## Reproduce statistics

Requires Python 3 (standard library only):

```bash
cd public-replication-package
python3 scripts/reproduce_statistics.py
```

The script asserts \(n=64\), E4=12, E5=13, P061 not E5, and P037 ICST metadata.

## Data-quality notes

- Screening was performed by a single lead researcher with tool assistance; dual independent screening / IRR is not claimed.
- Artifact status `NR` means **not established in our check**, not confirmed absence.
- Some shortlist-origin taxonomy codes have lower verification confidence (title-provisional).
- Overlapping discovery pools prevent a single unique-study count at every PRISMA intermediate stage; unique identity is the frozen \(n=64\).
- Bibliographic fields identify third-party works; this package does not redistribute publisher PDFs or paywalled full texts.

### Remaining `[VERIFY]` annotations

Some CSV cells retain a `[VERIFY]` marker. These are **transparent data-quality flags** for experimental details (e.g., exact subject counts, model lists) that were not fully re-checked from PDF for every field. They do **not** change corpus membership or the audited E4/E5 rates above.

Bibliography/DOI/venue metadata in `primary_study_reference_map.csv` is treated as resolved for public release (no pending bibliography-verification markers remain).

## Citation

Cite this replication package via `CITATION.cff`. After the review is published, add the article citation and any archive DOI here.

## License

| Path | License |
|------|---------|
| `scripts/` | **MIT** — see `LICENSE-CODE` |
| `data/` and `protocol/` | **CC BY 4.0** — see `LICENSE-DATA` and https://creativecommons.org/licenses/by/4.0/ |

No ownership is claimed over third-party publications beyond factual bibliographic identifiers included in the tables.
