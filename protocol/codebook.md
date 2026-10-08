# Taxonomy Codebook

This codebook defines the coding scheme applied to the frozen primary corpus
(P001–P064). Context (C), feedback (F), repair (R), and evaluation (E) codes
are **multi-label**. Realism (RL) is **exclusive** (one level per study).

## Context (C0–C5)

| Code | Label | Meaning |
|------|-------|---------|
| C0 | Focal / local method | Focal method body or narrowly local snippet |
| C1 | Local structural | Class/file neighbors, signatures, local AST structure |
| C2 | Program analysis | Paths, slices, CFG/DFG, hard-to-cover structure, static analysis |
| C3 | Repository / project | Cross-file retrieval, project dependencies, RAG/LSP over the repo |
| C4 | Documentation / usage / semantic | Docs, examples, usage mining, semantic/business intent |
| C5 | Build / framework | Build system, test framework, scaffolding, environment |

## Feedback (F0–F7)

| Code | Label | Meaning |
|------|-------|---------|
| F0 | None / one-shot | No execution or tool feedback loop |
| F1 | Compiler / build | Compile or build errors fed back |
| F2 | Runtime / execution | Runtime failures, stack traces, failing asserts |
| F3 | Coverage | Uncovered lines/branches/paths fed back |
| F4 | Mutation | Surviving mutants or mutation score fed back |
| F5 | Static / analysis | Static analyzer or similar signals |
| F6 | Agent / self | Multi-agent or self-reflective critique without external oracles alone |
| F7 | Human | Developer acceptance, review, or human-in-the-loop feedback |

## Repair (R0–R7)

| Code | Label | Meaning |
|------|-------|---------|
| R0 | One-shot / no repair | Generate once |
| R1 | Regenerate | Discard and resample without structured signal use |
| R2 | Compiler repair | Edit/regenerate using compile/build feedback |
| R3 | Runtime repair | Edit/regenerate using runtime feedback |
| R4 | Coverage-guided repair | Iterate toward coverage objectives |
| R5 | Mutation-guided repair | Iterate toward killing mutants |
| R6 | Deterministic / analysis repair | Rule-based or analysis-driven patches (non-LLM or hybrid) |
| R7 | Agentic repair | Multi-step agent orchestration for repair |

## Evaluation (E0–E6)

| Code | Label | Meaning |
|------|-------|---------|
| E0 | Syntax | Syntactic validity only |
| E1 | Compilation / build | Tests compile/build |
| E2 | Execution / pass | Tests execute; pass rates on current/regression behavior |
| E3 | Coverage | Structural coverage (line/branch/method/…) |
| E4 | Mutation | Mutation score / synthetic fault sensitivity |
| E5 | Real faults | Historical, corpus, or production/real-bug detection |
| E6 | Industrial / developer | Acceptance, deployment, or industrial developer evidence |

**Important distinctions**

- E3 ≠ E5: high coverage does not demonstrate real-fault detection.
- E4 ≠ E5: mutation sensitivity is synthetic; not automatically historical-bug effectiveness.
- Flags `Coverage`, `Mutation`, and `Real_Bugs` in the corpus CSV are aligned to E3/E4/E5 presence.

## Realism (RL0–RL4)

| Code | Label | Meaning |
|------|-------|---------|
| RL0 | Synthetic | Toy or synthetic units |
| RL1 | Method/class OSS | Isolated methods/classes or small OSS units |
| RL2 | File-level | File-scoped evaluation |
| RL3 | Repository | Multi-file repository / project-level setting |
| RL4 | Industrial | Proprietary/industrial deployment or production systems |

## Evidence-quality dimensions (Q1–Q10)

Coded in `data/evidence_quality_matrix.csv` to support interpretation (not automatic exclusion):

1. Benchmark/project described  
2. Model/configuration reported  
3. Strong baseline (proxy)  
4. Same-model control (proxy)  
5. Repeated runs  
6. Statistical analysis  
7. Mutation evaluation  
8. Real-bug evaluation  
9. Repository or industrial realism  
10. Public artifact confirmed  

Values are typically `yes` / `no` / `NR` (not reported / not extracted).

## Frozen classification notes (audited)

- **E5 real-fault evidence:** 13/64 (20.3%).  
- **E4 mutation evaluation:** 12/64 (18.8%).  
- **P061 (UAgent):** coded `E3;E4`, `Real_Bugs=no` — evaluates mutation score on HumanEval; not E5.  
- **P037:** canonical bibliographic record is ICST 2026 proceedings (DOI `10.1109/ICST69053.2026.00040`); arXiv:2601.09695 is the preprint.
