description.md

for version v79.6

---

# Ω⁴-UNIFIED — PACKAGE DESCRIPTION

**Version:** unified run v1.1  
**Core:** core.py v79.6  
**Date:** 2026-09-26  
**Author:** Sergey Viktorovich Matershov  
**ORCID:** 0009-0009-0641-1357  
**License:** CC BY-NC-ND 4.0 International

---

## 1. What this is

A package for a single run of the Ω⁴ model, combining three independent parts:

| Part | Entry-point file | What it does |
|---|---|---|
| **Base model** | `main.py` v23 | 171 checks, `omega4_results.json` |
| **Supplementary project** | `main_research.py` v3.0 | 9 combined research files, `research_results.json` |
| **FRG diagnostics** | `check_frg_limit.py` v2.0 | UV-stability boundary 7/8, both signs of θ |

The single entry point is **`main_unified.py` v1.0**. It runs all three parts sequentially, collects a combined JSON and generates the auto-genome.

---

## 2. Package structure

### 2.1. Core and base model

```
core.py               — core: constants, MasterPolynomial, REGISTRY (v79.6)
atlas.py              — Lie algebras, atlas of 34 algebras (v78.8)
physics.py            — physics: masses, cosmology, g-2, CP, GUT (v78.7)
vacuum_analysis.py    — SU(26) vacuum analysis (v5)
atlas_scan.py         — atlas scan + classification of 8 dimensions (v78.5.1)
magic_numbers.py      — magic numbers
quark_structure.py    — quark structure (v79.1)
modular_forms.py      — modular forms
statistical.py        — statistical analysis (Monte Carlo)
cross_validation.py   — cross-validation
predictions.py        — predictions
sensitivity.py        — sensitivity v1 (v2.1)
sensitivity2.py       — sensitivity v2 (v1.2)
benchmark.py          — benchmark against alternative models
elliptic_curve.py     — elliptic curve (BSD)
topological_origin.py — topological origin of constants (v1.1)
extra_constants.py    — extra constants (v79.0.10)
system_metrics.py     — system metrics (v79.0)
quantum_gravity.py    — quantum gravity + FRG (v1.1)
compactification.py   — compactification 26D → 4D (v1.0)
genome_writer.py      — auto-genome generator (v1.1)
main.py               — base-model entry point (v23)
```

### 2.2. Supplementary project: 9 combined research files

Instead of 40 small modules — 9 large ones:

| File | Modules inside | Constants in REGISTRY |
|---|---|---|
| `research_topology.py` | 7 | 35 |
| `research_membrane.py` | 2 | 12 |
| `research_bulk.py` | 5 | 29 |
| `research_m_theory.py` | 3 | 22 |
| `research_omega4.py` | 4 | 32 |
| `research_omega58.py` | 9 | 81 |
| `research_hierarchy.py` | 7 | 68 |
| `research_predictions.py` | 2 | 16 |
| `research_final.py` | 1 | 10 |
| **Total** | **40** | **305** |

The orchestrator of the supplementary project is `main_research.py` v3.0.

### 2.3. FRG diagnostics

```
check_frg_limit.py    — v2.0, UV-stability boundary
```

Functions:
- `main()` — prints the table and the 7/8 boundary.
- `compute_frg_boundary()` — structured dict for JSON.

### 2.4. The unifying main

```
main_unified.py       — v1.0, single entry point
```

---

## 3. Running

### 3.1. Full combined run

```bash
python main_unified.py
```

Order:

```
1. Base model           (main.py)               → omega4_results.json
2. Supplementary project (main_research.py v3.0) → research_results.json
3. FRG diagnostics      (check_frg_limit.py)    → print + compute_frg_boundary()
4. Combined JSON        → unified_results.json
5. Auto-genome          → constants_genome_omega4.py
```

### 3.2. Arguments

| Argument | What it does |
|---|---|
| `--no-genome` | Do not generate the auto-genome |
| `--no-save` | Do not save `unified_results.json` |
| `--quiet` | Minimum output |

### 3.3. Individual parts

```bash
python main.py                      # base model only
python main_research.py             # supplementary project only
python check_frg_limit.py           # FRG diagnostics only
python core.py                      # core only (13 checks)
python atlas_scan.py                # atlas scan only (5 + classification)
```

---

## 4. Output artifacts

| File | Content |
|---|---|
| `omega4_results.json` | Base-model result, 171/171 |
| `research_results.json` | Supplementary-project result, v3.0 |
| `unified_results.json` | Combined JSON, three blocks + `combined_summary` |
| `constants_genome_omega4.py` | Auto-genome, **629 constants** |

### 4.1. Structure of `unified_results.json`

```json
{
  "version": "1.0",
  "timestamp": "...",
  "base_model": {
    "results": {...},     // full result of run_all_checks()
    "summary": {...}      // {total_pass, total_checks, all_verified}
  },
  "research_project": {
    "summary": {...},     // N_eff_max, N_bulk, N_hidden, N_membrane, status_overall
    "details": {...},     // details on each topic
    "files": [...],       // list of 9 research files
    "formulas_for_7": {...}
  },
  "frg_boundary": {
    "available": true,
    "N_eff_max_stable": 7.0,
    "N_eff_min_unstable": 8.0,
    "boundary": "between 7.0 and 8.0",
    "table": [...],
    "table_with_theta_old": [...],
    "string_sector": {...}
  },
  "combined_summary": {
    "base_model_all_verified": true,
    "base_model_total_pass": 171,
    "base_model_total_checks": 171,
    "research_status_overall": "STRUCTURAL_STRONG",
    "research_N_eff_max": 7,
    "research_N_bulk": 57,
    "research_N_hidden": 50,
    "research_N_membrane": 7,
    "frg_boundary_available": true,
    "frg_N_eff_max_stable": 7.0,
    "frg_N_eff_min_unstable": 8.0,
    "frg_boundary_text": "between 7.0 and 8.0"
  }
}
```

---

## 5. Key numbers

### 5.1. CY₃ topology

| Parameter | Value |
|---|---|
| h¹¹ | 6 |
| h²¹ | 9 |
| χ_Hodge | −6 |
| N_gen | 3 |
| Manifold | Tian–Yau / Z₃ |

### 5.2. Fundamental numbers of Ω⁴

| Parameter | Value |
|---|---|
| χ | 616 = 2³·7·11 |
| β₁₂ | 4 |
| ε_FN | 0.3170816450303804 (15.52 digits) |
| N_TIME | 122 |

### 5.3. Structural relations (v79.6)

| Relation | Formula | Value |
|---|---|---|
| χ = D·24 − 8 | 26·24 − 8 | 616 |
| k = 8π/(D−N_eff) | 8π/19 | ≈ 1.322768 |

where D = 26 (critical dimension of the bosonic string),
N_eff = 7 (FRG boundary).

### 5.4. The relation N_eff = 7

Six independent formulas:

```
F1: N_s_SU26 − rank       = 32 − 25          = 7
F2: N_bulk − N_hidden      = 100 − 93         = 7
F3: h¹¹ + 1                = 6 + 1            = 7
F4: β₁₂ + N_gen            = 4 + 3            = 7
F5: N_bulk − N_hidden      = 57 − 50          = 7
F6: (N_grav + N_matter) − N_hidden = (3+54) − 50 = 7
```

### 5.5. The SU(58) bulk

| Parameter | Value |
|---|---|
| Group | SU(58) |
| Decomposition | 58 = 26 + 32 |
| N_bulk | 57 = rank(SU(58)) |
| N_hidden | 50 |
| N_membrane | 7 |
| N_grav | 3 |
| N_matter | 54 |

### 5.6. Ω-hierarchy (8/8)

| Theory | Dim. | Group | Key number |
|---|---|---|---|
| Ω⁴ | 4D | — | N_membrane = 7 |
| Ω⁵ | 5D | — | N_grav = 3 |
| Ω⁶ | 6D | — | h¹¹ = 6, h²¹ = 9 |
| Ω¹⁰ | 10D | E₈ × E₈ | rank = 16 |
| Ω¹¹ | 11D | — | 327 components |
| Ω²⁶ | 26D | SU(26) | N_26 = 25 |
| Ω³² | 10D | SU(32) | N_32 = 31 |
| Ω⁵⁸ | 11D | SU(58) | N_bulk = 57 |

### 5.7. Classification of the 8 QNM dimensions (v79.6)

| Dimension | Role | Class |
|---|---|---|
| 5 | Ω⁵ (5D Randall–Sundrum bulk) | strong |
| 6 | Ω⁶ (CY₃ Tian–Yau / Z₃) | argument |
| 7 | N_eff = 7 (FRG boundary) | numerology |
| 8 | dim(SU(3)) = 8 | numerology |
| 10 | Ω¹⁰ (E₈ × E₈ heterotic) | strong |
| 11 | Ω¹¹ (M-theory) | strong |
| 12 | β₁₂ = 4 (Betti number, index 12) | numerology |
| 26 | Ω²⁶ (26D bosonic string) | strong |

**Total:** strong 4/8, argument 1/8, numerology 3/8.
**QNM instability:** dimension 6 (Batic–Dutykh 2026).

---

## 6. The FRG boundary (key result)

### 6.1. Result

```
N_eff = 0 ... 7   → UV stability ✅
N_eff = 8 ... 100 → UV stability ❌
Boundary: between 7 and 8.
```

### 6.2. Threshold 8 = dim(SU(3))

At N_eff = 8 a **color field** SU(3) is added, which does not fit on the 4D membrane in full.
This breaks UV stability.

### 6.3. Membrane explanation

| Level | N_eff | What |
|---|---|---|
| Bulk | ~100 | Full SM |
| Membrane | 7 | Only effective fields |
| Threshold | 8 | dim(SU(3)) |

**Relation:** N_bulk − N_hidden = N_membrane → 57 − 50 = 7.

### 6.4. Sign convention for θ

In the FRG literature the convention is:

```
θ_i = eig_i(J)
Re θ_i > 0 for all i  →  UV stability
Re θ_i < 0 for all i  →  IR stability
```

In older versions of `quantum_gravity.py` (v1.0) the opposite convention `θ = −eig(J)` was used.
Both give **the same** 7/8 boundary.
In v1.1 it is brought to the standard. `check_frg_limit.py` shows **both signs** for clarity.

---

## 7. Statuses

### 7.1. What has been verified

- Base model: **171/171** ✅
- Supplementary project: **9/9** files ✅
- FRG boundary: **7/8** confirmed ✅
- Auto-genome: **629 constants** ✅

### 7.2. Open problems (`OpenProblemsV18`)

| # | Name | Status |
|---|---|---|
| 1 | Fundamental meaning of 0.198 | CLOSED (v18.2) |
| 2 | Topology for τ | FOUND (A(Pb)) |
| 3 | g-2: full coverage | SOLVED (Φ_g2 = 71.2 GeV) |
| 4 | Unification of constants | OPEN |
| 5 | Quarks: exact formula | CLOSED (v79.1, mean 0.50%) |
| 6 | M_Z — not derived | EFFECTIVE |
| 7 | sin²θ_W — not derived | EFFECTIVE |
| 8 | α_s(M_Z) — not derived | EFFECTIVE |
| **9** | **SUSY from gravity (Darboux factorization)** | **HYPOTHESIS (v79.6)** |

**Total:** 9 problems, 2 closed, 7 open/effective.

### 7.3. Honest assessment

- **PROVEN has not been achieved.** The relation N_eff = 7 is an observed regularity, not a rigorous derivation.
- **The model is an EFT with SU(26)**, not a string theory in the strict sense (no Polyakov action, no vertex operators, no closed-string spectrum).
Status: `STRUCTURAL_ARGUMENT`.
- **The membrane hypothesis** is a working one, but not a theorem.
- **SUSY from gravity** is a hypothesis (problem 9), not a proof.

---

## 8. Dependencies

```
Python      3.11+
numpy       for computations
scipy       for root()
mpmath      for ε_FN with high precision
```

Installation:

```bash
pip install numpy scipy mpmath
```

---

## 9. Registration of constants

All modules register constants in `core.REGISTRY` on import.
At the end of `main_unified.py`, `genome_writer.write_genome()` is called, which saves **all** constants to `constants_genome_omega4.py`:

- **629 constants** (was 627 in v1.0; +2 in v79.6: `CHI_FROM_D`, `K_LAMBDA`)
- Levels: 0 — 126, 1 — 413, 2 — 1, 3 — 18, CP — 4, LOST — 32, OBS — 33
- File size: ~240 KB
- CLI for viewing:
  ```bash
  python constants_genome_omega4.py --summary
  python constants_genome_omega4.py --verify
  python constants_genome_omega4.py --search magic
  python constants_genome_omega4.py --level 0
  python constants_genome_omega4.py --source core
  ```

---

## 10. Recommended run order

```bash
# 1. Full run with generation of everything
python main_unified.py

# 2. Check combined_summary
python -c "import json; d=json.load(open('unified_results.json',encoding='utf-8')); [print(f'{k:<35} = {v}') for k,v in d['combined_summary'].items()]"

# 3. Check structural relations (v79.6)
python -c "from core import C, OpenProblemsV18; print(f'CHI_FROM_D = {C.CHI_FROM_D}'); print(f'K_LAMBDA = {C.K_LAMBDA:.6f}'); p = OpenProblemsV18.get_full_report(); print(f'Problems: {p[\"n_total\"]}, open: {p[\"n_open\"]}')"

# 4. View the auto-genome
python constants_genome_omega4.py --summary
```

Expected output of `combined_summary`:

```
base_model_all_verified             = True
base_model_total_pass               = 171
base_model_total_checks             = 171
research_status_overall             = STRUCTURAL_STRONG
research_N_eff_max                  = 7
research_N_bulk                     = 57
research_N_hidden                   = 50
research_N_membrane                 = 7
frg_boundary_available              = True
frg_N_eff_max_stable                = 7.0
frg_N_eff_min_unstable              = 8.0
frg_boundary_text                   = between 7.0 and 8.0
```

Expected output of step 3:

```
CHI_FROM_D = 616
K_LAMBDA = 1.322776
Problems: 9, open: 7
```

---

## 11. Version history

| Version | Changes |
|---|---|
| v1.0 | Combination of `main.py` + `main_research.py` + `check_frg_limit.py` + `genome_writer.py`. 627 constants. |
| **v1.1** | **Core: v79.5 → v79.6. Added structural relations `CHI_FROM_D` (χ = D·24 − 8) and `K_LAMBDA` (k = 8π/19).
Added problem 9 (SUSY from gravity). `atlas_scan.py`: added classification of 8 QNM dimensions (v78.5.1).
Auto-genome: 629 constants.** |

---

## 12. Contacts

**Author:** Sergey Viktorovich Matershov  
**ORCID:** [0009-0009-0641-1357](https://orcid.org/0009-0009-0641-1357)  
**License:** CC BY-NC-ND 4.0 International
```

---

## 📋 What changed relative to the old `description.md`

| # | What | Was (v1.0) | Now (v1.1) |
|---|-----|-------------|--------------|
| 1 | **Version in the header** | "unified run v1.0" | "unified run v1.1, core v79.6" |
| 2 | **Package structure** | `core.py` without version | `core.py` v79.6 |
| 3 | **`atlas_scan.py`** | without version | v78.5.1 + "classification of 8 dimensions" |
| 4 | **`quantum_gravity.py`** | v1.1 | v1.1 (unchanged) |
| 5 | **Running individual parts** | 3 commands | + `python core.py`, + `python atlas_scan.py` |
| 6 | **Auto-genome** | 627 constants | **629 constants** |
| 7 | **New section 5.3** | — | **Structural relations (v79.6)**: χ = D·24 − 8, k = 8π/19 |
| 8 | **New section 5.7** | — | **Classification of 8 QNM dimensions** |
| 9 | **OpenProblemsV18** | not mentioned | **Table of 9 problems** (including the new problem 9 — SUSY) |
| 10 | **New section 11** | — | **Version history** (v1.0 → v1.1) |
| 11 | **Honest assessment** | 3 points | **4 points** (+ SUSY as a hypothesis) |
| 12 | **Run order** | 3 steps | **4 steps** (+ checking structural relations) |

---

## 🎯 What is now in `description.md`

**Current as of v79.6:**
- 171/171 checks of the base model.
- 9 research files, 305 constants.
- FRG boundary 7/8.
- **629 constants** in the auto-genome.
- **9 problems** (2 closed, 7 open/effective).
- **Classification of 8 dimensions** QNM.
- **2 new structural relations**: χ = D·24 − 8, k = 8π/19.
- **Version history** v1.0 → v1.1.
