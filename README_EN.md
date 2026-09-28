README_EN.md
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23011101.svg)](https://doi.org/10.5281/zenodo.23011101)
---

# Ω⁴-UNIFIED

**A topological model of physics: from the Calabi–Yau manifold to particle masses, cosmology and quantum gravity.**

[![Version](https://img.shields.io/badge/version-79.6-blue)]()
[![Checks](https://img.shields.io/badge/checks-171%2F171-brightgreen)]()
[![Constants](https://img.shields.io/badge/constants-629-blue)]()
[![Statistics](https://img.shields.io/badge/statistics-12.74%CF%83-brightgreen)]()
[![CV](https://img.shields.io/badge/CV-97.8%25-brightgreen)]()
[![License](https://img.shields.io/badge/license-CC%20BY--NC--ND%204.0%20%7C%20UAL--v1.0-lightgrey)]()

---

## What this is about

Ω⁴-UNIFIED is an attempt to build a physical model in which **the topology of a Calabi–Yau manifold generates the structure of physics**:
    from the masses of elementary particles to cosmological parameters and quantum gravity.

Everything starts with **Tian–Yau / Z₃** — a specific Calabi–Yau manifold with Hodge numbers:

```
h¹¹ = 6,  h²¹ = 9,  χ_Hodge = −6,  N_gen = 3
```

From these numbers, via the master polynomial `n(k) = (103k⁴ − 370k³ + 101k² + 478k)/12`, one derives:
- **β-functions of SU(26)** — topological invariants, not spectral ones;
- **particle masses** — via ε_FN = 0.317081645… (the Froggatt–Nielsen parameter);
- **cosmological parameters** — n_s, r, H_0, Ω_DM, Λ;
- **quantum gravity** — M_Pl, G, Λ via FRG.

---

## ⚠️ Honest disclaimer

**This is a working hypothesis, not a proven theory.**

- **PROVEN has not been achieved.** The relation N_eff = 7 is an observed regularity, not a rigorous derivation.
- **The model is an EFT, not a string theory.** It has 26D, SU(26) and compactification, but **no** Polyakov action,
vertex operators or closed-string spectrum.
- **SU(26) is a phenomenological input**, not a consequence of first principles.
- **5 open problems**: unification of constants, M_Z, sin²θ_W, α_s(M_Z), SUSY from gravity.

We state this honestly here so as not to create false expectations.
Details are in the "Limitations" section and in the file `LIMITATIONS.md`.

---

## What is inside

### Results

| What | Value |
|---|---|
| Checks | **171/171** ✅ |
| Constants in the auto-genome | **629** |
| Statistical significance | **12.74σ** (Fisher's method, 24 relations, 10000 polynomials) |
| Cross-validation | **97.8%** (LOO + K-Fold + Holdout) |
| Predictions | **30** (18 confirmed, 10 future, 2 in tension) |
| FRG boundary | **N_eff ≤ 7** — UV stability, **N_eff ≥ 8** — breaks |
| Compactification | **26 = 4 + 6 + 16** |
| Ω-hierarchy | **8/8** completed |

### What is derived

| Area | Examples |
|---|---|
| **Particle masses** | 5 quarks + 3 leptons + Higgs + top + W′ to within < 1% |
| **Cosmology** | n_s = 0.9675, r = 0.00316, H_0 = 67.72, Ω_DM = 0.1207, Λ = 1.1055e-52 |
| **Quantum gravity** | M_Pl = 1.2215e19 GeV (0.045%), G = 6.668e-11 (0.094%), Λ (0.009%) |
| **CP-violation** | J = 2.945e-5, δ_CP = 1.2 rad, ε_CP = 6.4986e-8 |
| **GUT** | α_GUT via ε_FN/(4π) |
| **Topology** | B_i = (32.833, −16.833, −21.000) from c₂ = 101 |

### What is NOT derived

- **M_Z** — effective (0.009%)
- **sin²θ_W** — effective (0.046%)
- **α_s(M_Z)** — effective (0.031%)
- **Unification of constants** — open problem (spread α_i⁻¹ = 22.32)

---

## Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│  core.py  (v79.6)                                                │
│  ─────────────────────────────────────────────────────────────  │
│  Constants, MasterPolynomial, REGISTRY (629 constants)           │
└──────────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────────┐
│  atlas.py  (v78.8)                                               │
│  ─────────────────────────────────────────────────────────────  │
│  34 Lie algebras, E₆/E₇/E₈, SU(26), SU(58), Φ⁺                    │
└──────────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────────┐
│  physics.py  (v78.7)                                             │
│  ─────────────────────────────────────────────────────────────  │
│  37 modules: masses, cosmology, GUT, CP, g-2, tetrahedron, loops │
└──────────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────────┐
│  main.py  (v23)                                                  │
│  ─────────────────────────────────────────────────────────────  │
│  Integration, 171/171 checks, omega4_results.json                │
└──────────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────────┐
│  genome_writer.py  (v1.1)                                        │
│  ─────────────────────────────────────────────────────────────  │
│  constants_genome_omega4.py (629 constants)                      │
└──────────────────────────────────────────────────────────────────┘
```

### Supplementary project (9 combined research files)

```
research_topology.py      — topology, threshold, formulas
research_membrane.py      — membrane
research_bulk.py          — SU(58) bulk
research_m_theory.py      — M-theory
research_omega4.py        — Ω⁴: fields, action, equations
research_omega58.py       — Ω⁵⁸: definition, spectrum, compactification
research_hierarchy.py     — Ω-hierarchy
research_predictions.py   — predictions
research_final.py         — final report
```

### Unifiers

```
main_unified.py           — single entry point
main_research.py  (v3.0)  — supplementary-project orchestrator
check_frg_limit.py (v2.0) — FRG diagnostics
```

---

## How to run

### 1. Installing dependencies

```bash
pip install numpy scipy mpmath
```

`mpmath` is mandatory: without it `ε_FN` will not be computed to the required precision.

### 2. Full run

```bash
python main_unified.py
```

This will run **everything**:
1. The base model (171 checks, `omega4_results.json`)
2. The supplementary project (9 files, `research_results.json`)
3. FRG diagnostics (boundary 7/8)
4. The combined JSON (`unified_results.json`)
5. The auto-genome (`constants_genome_omega4.py`, 629 constants)

### 3. Individual parts

```bash
# Base model only
python main.py

# Supplementary project only
python main_research.py

# FRG boundary only
python check_frg_limit.py

# Core only
python core.py

# Atlas scan only
python atlas_scan.py

```

### 4. Arguments of `main_unified.py`

| Argument | What it does |
|---|---|
| `--no-genome` | Do not generate the auto-genome |
| `--no-save` | Do not save `unified_results.json` |
| `--quiet` | Minimum output |

---

## What has been verified

### 171/171 checks

| Block | Checks |
|---|---|
| Core (`core.py`) | 21/21 |
| Atlas (`atlas.py`) | 18/18 |
| Physics (`physics.py`) | 37/37 |
| Vacuum analysis | 17/17 |
| Atlas scan | 5/5 |
| Magic numbers | 5/5 |
| Quark structure | 7/7 |
| Modular forms | 9/9 |
| Statistics | 2/2 |
| Cross-validation | 5/5 |
| Predictions | 4/4 |
| Sensitivity v1 + v2 + comparison | 15/15 |
| Benchmark | 4/4 |
| Elliptic curve | 6/6 |
| Quantum gravity | 6/6 |
| Compactification 26D → 4D | 6/6 |
| Topology vs Spectrum (Q5) | 4/4 |

### Key discoveries

1. **Topological origin of B_i** (TASK-005 closed):
   ```
   CY₃ → β₁₂ = 4 → c₂ = 101 → B_i = (32.833, −16.833, −21.000)
   ```

2. **FRG boundary 7/8**:
   ```
   N_eff ≤ 7  →  UV stability ✅
   N_eff ≥ 8  →  breaks (8 = dim(SU(3)))
   ```

3. **Topology vs Spectrum (Q5)**:
   ```
   Topology governs the RGE DIRECTLY, bypassing the SU(26) spectrum.
   The SU(26) spectrum is NOT the relevant level of description.
   ```

4. **g-2 via Φ⁺(E₆)**:
   ```
   M_g2 = 2·Φ⁺(E₆) − ε_FN·2.5 = 71.2073 GeV  (dev. 0.0102%)
   ```

5. **Magic numbers**:
   ```
   20 = N_gen·dim(SU(3)) − β₁₂
   28 = χ/22 = 7·β₁₂
   50 = n(1) + 6·β₁₂
   82 = n(1) + n(3) − 2
   126 = n(1) + 100
   ```

---

## Comparison with alternatives

`benchmark.py` compares Ω⁴ with well-known models:

| Model | Parameters | Predictions | Checks | σ | CV |
|---|---|---|---|---|---|
| Standard Model | 19 | 0 | 0 | 0 | 0 |
| MSSM | 105 | 10 | 0 | 0 | 0 |
| String theory | ~10⁵⁰⁰ | 0 | 0 | 0 | 0 |
| Loop QG | 2 | 3 | 0 | 0 | 0 |
| Asymptotic safety | 3 | 5 | 0 | 0 | 0 |
| **Ω⁴-UNIFIED** | **2** | **30** | **47** | **10.33** | **100%** |

Efficiency of Ω⁴: **242.755** — (47 × 10.33) / 2.

---

## Limitations

Details are in `LIMITATIONS.md`. Briefly:

1. **The model is an EFT, not a string theory.** No Polyakov action, no vertex operators, no closed-string spectrum.
                                          Status: `STRUCTURAL_ARGUMENT`.
2. **PROVEN has not been achieved.** The relation N_eff = 7 is an observed regularity, not a derivation.
3. **SU(26) is a phenomenological input.** It is justified via n(1) = 26, χ = 26·24 − 8, compactification 26 = 4 + 6 + 16.
                                          But it is not derived from first principles.
4. **5 open problems:**
   - Unification of constants (spread α_i⁻¹ = 22.32)
   - M_Z (dev. 0.009%)
   - sin²θ_W (dev. 0.046%)
   - α_s(M_Z) (dev. 0.031%)
   - SUSY from gravity (hypothesis)
5. **The SU(26) spectrum is rejected** for the RGE — topology works directly.

---

## Repository structure

```
.
├── README.md                      ← this file
├── LICENSE.txt                    ← UAL-v1.0 + CC BY-NC-ND 4.0
├── CITATION.cff                   ← how to cite
├── requirements.txt               ← dependencies
├── LIMITATIONS.md                 ← what does not work
├── ARCHITECTURE.md                ← dependency diagram
├── CHANGELOG.md                   ← version history
│
├── core.py                        ← core, REGISTRY
├── atlas.py                       ← Lie algebras, 34 algebras
├── physics.py                     ← 37 physics modules
├── main.py                        ← integration (171/171)
├── main_research.py               ← supplementary-project orchestrator
├── main_unified.py                ← single entry point
├── check_frg_limit.py             ← FRG diagnostics
├── genome_writer.py               ← auto-genome generator
│
├── vacuum_analysis.py             ← SU(26) vacuum analysis
├── atlas_scan.py                  ← atlas scan + 8 QNM dimensions
├── magic_numbers.py               ← magic numbers
├── quark_structure.py             ← quark structure
├── modular_forms.py               ← modular forms
├── statistical.py                 ← Monte Carlo
├── cross_validation.py            ← cross-validation
├── predictions.py                 ← predictions
├── sensitivity.py                 ← sensitivity v1
├── sensitivity2.py                ← sensitivity v2
├── benchmark.py                   ← comparison with alternatives
├── elliptic_curve.py              ← elliptic curve (BSD)
├── topological_origin.py          ← topological origin
├── extra_constants.py             ← extra constants
├── system_metrics.py              ← system metrics
├── quantum_gravity.py             ← quantum gravity
├── compactification.py            ← compactification 26D → 4D
│
├── research_topology.py           ← supplementary project: topology
├── research_membrane.py           ← supplementary project: membrane
├── research_bulk.py               ← supplementary project: SU(58) bulk
├── research_m_theory.py           ← supplementary project: M-theory
├── research_omega4.py             ← supplementary project: Ω⁴
├── research_omega58.py            ← supplementary project: Ω⁵⁸
├── research_hierarchy.py          ← supplementary project: Ω-hierarchy
├── research_predictions.py        ← supplementary project: predictions
├── research_final.py              ← supplementary project: final report
│
├── constants_genome_omega4.py     ← AUTO-GENOME (629 constants)
├── omega4_results.json            ← base-model results
├── research_results.json          ← supplementary-project results
└── unified_results.json           ← combined JSON
```

---

## Citation

If you use this work, please cite:

```bibtex
@software{matershov_omega4_2026,
  author       = {Matershov, Sergey Viktorovich},
  title        = {Ω⁴-UNIFIED: a topological model of physics},
  year         = {2026},
  version      = {79.6},
  orcid        = {0009-0009-0641-1357},
  license = {CC BY-NC-ND 4.0 International or Universal Academic Licence v1.0},
  url          = {https://github.com/}
}
```

---
## License

The work is distributed under **two licenses**. You may choose **either** of them — whichever suits your case best.

### Option 1: CC BY-NC-ND 4.0 International

**You may:**
- ✅ Share — copy and redistribute the material in any medium or format.

**Under the following conditions:**
- **Attribution (BY)** — give credit to the author.
- **NonCommercial (NC)** — do not use for commercial purposes.
- **NoDerivatives (ND)** — do not modify the material and do not distribute modified versions.

Full text: [creativecommons.org/licenses/by-nc-nd/4.0/](https://creativecommons.org/licenses/by-nc-nd/4.0/)

### Option 2: Universal Academic Licence v1.0 (UAL-v1.0)

**You may:**
- ✅ Read, copy, distribute
- ✅ Cite and reference
- ✅ Use in educational and non-commercial research
- ✅ Translate and adapt with preservation of authorship
- ✅ Create derivative works under Copyleft terms

**Prohibited without written permission:**
- ❌ Commercial use
- ❌ Military use
- ❌ Patent trolling
- ❌ Distortion of meaning
- ❌ Plagiarism

Full text: [`LICENSE.txt`](./LICENSE.txt)

---

### Which to choose?

| Situation | Recommended license |
|---|---|
| You need a **standard**, recognizable license | CC BY-NC-ND 4.0 |
| You need to **create a derivative work** (translation, adaptation) | UAL-v1.0 (CC BY-NC-ND **prohibits** derivatives) |
| You need to **prohibit military use** | UAL-v1.0 |
| You need to **prohibit patent trolling** | UAL-v1.0 |
| You need to **post on arXiv / Zenodo** | CC BY-NC-ND 4.0 (UAL is not in the standard list) |

**Mandatory in both cases:** indicate the author, ORCID and a link to the chosen license.

**Commercial use:** requires a separate written agreement — smatershov@mail.ru
---

## Author

**Sergey Viktorovich Matershov**

ORCID: [0009-0009-0641-1357](https://orcid.org/0009-0009-0641-1357)

---

## Acknowledgements

The project uses:
- **NumPy** — numerical computations
- **SciPy** — optimization and integration
- **mpmath** — exact arithmetic (for ε_FN)

---

*Last update: 2026-09-28*
*Version: 79.6*
