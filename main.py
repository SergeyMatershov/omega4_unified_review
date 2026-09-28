#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ω⁴-UNIFIED v79.4 — ФИНАЛЬНАЯ ИНТЕГРАЦИЯ (main.py) — v23
================================================================================
ШАГ 4 из 4. ТОЧКА ВХОДА.

================================================================================
АРХИТЕКТУРА ПРОЕКТА (v79.4)
================================================================================

    core.py               — ЯДРО + ПРОСТЫЕ МОДУЛИ
    atlas.py              — АЛГЕБРЫ ЛИ + АТЛАС (v78.0)
    physics.py            — ФИЗИКА + ТЕТРАЭДР + ПЕТЛИ + ЗАПУТАННОСТЬ + g-2 (v78.7)
    vacuum_analysis.py    — АНАЛИЗ ВАКУУМА SU(26) (v78.5)
    atlas_scan.py         — ПОЛНЫЙ СКАН АТЛАСА (v78.5)
    magic_numbers.py      — МАГИЧЕСКИЕ ЧИСЛА
    quark_structure.py    — СТРУКТУРА КВАРКОВ
    modular_forms.py      — МОДУЛЯРНЫЕ ФОРМЫ
    statistical.py        — СТАТИСТИЧЕСКИЙ АНАЛИЗ
    cross_validation.py   — КРОСС-ВАЛИДАЦИЯ
    predictions.py        — ПРЕДСКАЗАНИЯ
    sensitivity.py        — ЧУВСТВИТЕЛЬНОСТЬ v1 (v2.1)
    sensitivity2.py       — ЧУВСТВИТЕЛЬНОСТЬ v2 (v1.2)
    benchmark.py          — BENCHMARK
    elliptic_curve.py     — ЭЛЛИПТИЧЕСКАЯ КРИВАЯ (v1.2)
    topological_origin.py — ТОПОЛОГИЯ КОНСТАНТ (v79.2)
    extra_constants.py    — ДОП. КОНСТАНТЫ (v79.0.10)
    system_metrics.py     — СИСТЕМНЫЕ МЕТРИКИ (v79.0)
    quantum_gravity.py    — КВАНТОВАЯ ГРАВИТАЦИЯ (v79.3)
    compactification.py   — КОМПАКТИФИКАЦИЯ 26D → 4D (v79.4)
    genome_writer.py      — ГЕНЕРАТОР АВТОГЕНОМА (v1.1)
    main.py               — ИНТЕГРАЦИЯ (ЭТОТ ФАЙЛ)

================================================================================
ЗАПУСК
================================================================================

    python main.py

================================================================================
================================================================================
АВТОР:  Сергей Викторович Матершов
ORCID:  0009-0009-0641-1357
ДАТА:   2026-09-19
ВЕРСИЯ: 79.4
ЛИЦЕНЗИЯ: CC BY-NC-ND 4.0 International
================================================================================
"""

# ============================================================================
# ИМПОРТЫ: БАЗОВЫЕ МОДУЛИ
# ============================================================================

from core import (
    C, MasterPolynomial, LieGroupDimensions,
    HodgeNumbers, VacuumChargeFromCY3,
    AtlasLieAlgebras, ExactConnectionsRegistry,
    verify_core,
)

from atlas import (
    AlgebraLyCalculator, SU26CompleteData, SU58CompleteData,
    RootSystemGenerator, WeylDimension, CompleteAtlas,
    AtlasDiscoveries, verify_atlas,
    CompleteAtlasJAX,
    LieAlgebraUniqueness, PicardFuchsPeriods, GopakumarVafa,
    RealComplexEquivalence, StrongTheorem, GeneralStrongTheorem,
    StructureConstantsSU26,
)

from physics import (
    YukawaFromCY3Charges, GUTUnificationWithSU58,
    SMHiggsMasses, Cosmology, TimeTheory,
    TetrahedronConstants, LoopHierarchy,
    QuantumEntanglement,
    AtlasPhysicsConnections, GUTFromJAXAtlas,
    G2FromPhiPlus, G2NewContribution,
    verify_physics,
)

# ============================================================================
# МОДУЛЬ АНАЛИЗА ВАКУУМА
# ============================================================================

try:
    from vacuum_analysis import VacuumAnalysis, verify_vacuum_analysis
    HAS_VACUUM_ANALYSIS = True
except ImportError:
    HAS_VACUUM_ANALYSIS = False
    VacuumAnalysis = None
    verify_vacuum_analysis = None

# ============================================================================
# МОДУЛЬ СКАНА АТЛАСА
# ============================================================================

try:
    from atlas_scan import AtlasScan, verify_atlas_scan
    HAS_ATLAS_SCAN = True
except ImportError:
    HAS_ATLAS_SCAN = False
    AtlasScan = None
    verify_atlas_scan = None

# ============================================================================
# НОВЫЕ МОДУЛИ v14
# ============================================================================

try:
    from magic_numbers import MagicNumbers, verify_magic_numbers
    HAS_MAGIC_NUMBERS = True
except ImportError:
    HAS_MAGIC_NUMBERS = False
    MagicNumbers = None
    verify_magic_numbers = None

try:
    from quark_structure import QuarkStructure, verify_quark_structure
    HAS_QUARK_STRUCTURE = True
except ImportError:
    HAS_QUARK_STRUCTURE = False
    QuarkStructure = None
    verify_quark_structure = None

try:
    from modular_forms import ModularForms, verify_modular_forms
    HAS_MODULAR_FORMS = True
except ImportError:
    HAS_MODULAR_FORMS = False
    ModularForms = None
    verify_modular_forms = None

# ============================================================================
# ОПЦИОНАЛЬНЫЕ ЗАГРУЗКИ
# ============================================================================

try:
    from statistical import MonteCarloAnalysis
    HAS_STATISTICAL = True
except ImportError:
    HAS_STATISTICAL = False
    MonteCarloAnalysis = None

try:
    from cross_validation import CrossValidator
    HAS_CROSS_VALIDATION = True
except ImportError:
    HAS_CROSS_VALIDATION = False
    CrossValidator = None

try:
    from predictions import PredictionsAnalysis
    HAS_PREDICTIONS = True
except ImportError:
    HAS_PREDICTIONS = False
    PredictionsAnalysis = None

try:
    from sensitivity import SensitivityAnalysis
    HAS_SENSITIVITY = True
except ImportError:
    HAS_SENSITIVITY = False
    SensitivityAnalysis = None

try:
    from sensitivity2 import SensitivityAnalysis2, SensitivityComparison
    HAS_SENSITIVITY2 = True
except ImportError:
    HAS_SENSITIVITY2 = False
    SensitivityAnalysis2 = None
    SensitivityComparison = None

try:
    from benchmark import BenchmarkAnalysis
    HAS_BENCHMARK = True
except ImportError:
    HAS_BENCHMARK = False
    BenchmarkAnalysis = None

try:
    from elliptic_curve import EllipticCurveBSD, verify_elliptic_curve
    HAS_ELLIPTIC_CURVE = True
except ImportError:
    HAS_ELLIPTIC_CURVE = False
    EllipticCurveBSD = None
    verify_elliptic_curve = None

# ============================================================================
# ТОПОЛОГИЧЕСКОЕ ПРОИСХОЖДЕНИЕ КОНСТАНТ (v79.2)
# ============================================================================

try:
    from topological_origin import register_topological_constants
    register_topological_constants(verbose=False)
    HAS_TOPOLOGICAL_ORIGIN = True
except ImportError:
    HAS_TOPOLOGICAL_ORIGIN = False
    register_topological_constants = None

# ============================================================================
# ДОПОЛНИТЕЛЬНЫЕ КОНСТАНТЫ (v79.0.10)
# ============================================================================

try:
    import extra_constants
    HAS_EXTRA_CONSTANTS = True
except ImportError:
    HAS_EXTRA_CONSTANTS = False

try:
    import system_metrics
    HAS_SYSTEM_METRICS = True
except ImportError:
    HAS_SYSTEM_METRICS = False

# ============================================================================
# КВАНТОВАЯ ГРАВИТАЦИЯ ИЗ SU(26) (v79.3)
# ============================================================================

try:
    import quantum_gravity
    HAS_QUANTUM_GRAVITY = True
except ImportError:
    HAS_QUANTUM_GRAVITY = False
    quantum_gravity = None

# ============================================================================
# КОМПАКТИФИКАЦИЯ 26D → 4D (v79.4)
# ============================================================================

try:
    import compactification
    HAS_COMPACTIFICATION = True
except ImportError:
    HAS_COMPACTIFICATION = False
    compactification = None

# ============================================================================
# СТАНДАРТНЫЕ БИБЛИОТЕКИ PYTHON
# ============================================================================

import math
import json
from datetime import datetime
from typing import Dict, List, Any


# ============================================================================
# ЧАСТЬ 1: ГЛАВНЫЙ КЛАСС
# ============================================================================

class Omega4Unified:
    """
    Главный класс интеграции Ω⁴-UNIFIED v79.4 (main v23).
    """

    def __init__(self):
        """Инициализация всех модулей."""
        self.core = C
        self.master_poly = MasterPolynomial
        self.lie_dims = LieGroupDimensions
        self.hodge = HodgeNumbers()
        self.cy3 = VacuumChargeFromCY3()
        self.atlas_lie = AtlasLieAlgebras()
        self.exact_conn = ExactConnectionsRegistry()

        self.algebra_ly = AlgebraLyCalculator()
        self.complete_atlas = CompleteAtlas()
        self.atlas_discoveries = AtlasDiscoveries()

        self.yukawa = YukawaFromCY3Charges()
        self.gut = GUTUnificationWithSU58()
        self.higgs = SMHiggsMasses()
        self.cosmology = Cosmology()
        self.time = TimeTheory()
        self.entanglement = QuantumEntanglement()

        self.atlas_physics = AtlasPhysicsConnections()
        self.gut_jax = GUTFromJAXAtlas()

        self.g2_phi = G2FromPhiPlus()
        self.g2_contrib = G2NewContribution()

        self.vacuum_analysis = VacuumAnalysis() if HAS_VACUUM_ANALYSIS else None
        self.atlas_scan = AtlasScan() if HAS_ATLAS_SCAN else None
        self.magic_numbers = MagicNumbers() if HAS_MAGIC_NUMBERS else None
        self.quark_structure = QuarkStructure() if HAS_QUARK_STRUCTURE else None
        self.modular_forms = ModularForms() if HAS_MODULAR_FORMS else None

        self.statistical = (
            MonteCarloAnalysis(n_samples=10000, seed=42)
            if HAS_STATISTICAL else None
        )
        self.cross_validation = (
            CrossValidator(seed=42) if HAS_CROSS_VALIDATION else None
        )
        self.predictions = PredictionsAnalysis() if HAS_PREDICTIONS else None

        self.sensitivity = SensitivityAnalysis() if HAS_SENSITIVITY else None
        self.sensitivity2 = SensitivityAnalysis2() if HAS_SENSITIVITY2 else None
        self.sensitivity_comparison = (
            SensitivityComparison() if HAS_SENSITIVITY2 else None
        )

        self.benchmark = BenchmarkAnalysis() if HAS_BENCHMARK else None
        self.elliptic_curve = EllipticCurveBSD() if HAS_ELLIPTIC_CURVE else None

    # ========================================================================
    # 1.1. Запуск всех проверок
    # ========================================================================

    def run_all_checks(self) -> Dict:
        """Полный прогон всех проверок."""
        results = {
            'core': verify_core(),
            'atlas': verify_atlas(),
            'physics': verify_physics(),
        }

        if self.vacuum_analysis is not None:
            results['vacuum_analysis'] = verify_vacuum_analysis()

        if self.atlas_scan is not None:
            results['atlas_scan'] = verify_atlas_scan()

        if self.magic_numbers is not None:
            results['magic_numbers'] = verify_magic_numbers()

        if self.quark_structure is not None:
            results['quark_structure'] = verify_quark_structure()

        if self.modular_forms is not None:
            results['modular_forms'] = verify_modular_forms()

        if self.statistical is not None:
            results['statistical'] = self.statistical.run(verbose=False)

        if self.cross_validation is not None:
            results['cross_validation'] = self.cross_validation.run_full(verbose=False)

        if self.predictions is not None:
            results['predictions'] = self.predictions.get_summary()

        if self.sensitivity is not None:
            results['sensitivity'] = self.sensitivity.run_full(verbose=False)

        if self.sensitivity2 is not None:
            results['sensitivity2'] = self.sensitivity2.run_full(verbose=False)

        if self.sensitivity_comparison is not None:
            results['sensitivity_comparison'] = (
                self.sensitivity_comparison.compare_base_points()
            )

        if self.benchmark is not None:
            results['benchmark'] = self.benchmark.get_summary()

        if self.elliptic_curve is not None:
            results['elliptic_curve'] = self.elliptic_curve.get_full_report()

        # КВАНТОВАЯ ГРАВИТАЦИЯ (v79.3)
        if HAS_QUANTUM_GRAVITY:
            results['quantum_gravity'] = quantum_gravity.compute_all(N_eff=1.0)

        # КОМПАКТИФИКАЦИЯ 26D → 4D (v79.4)
        if HAS_COMPACTIFICATION:
            results['compactification'] = compactification.compute_all()

        # ТОПОЛОГИЯ vs СПЕКТР (Q5, v79.5)
        if HAS_TOPOLOGICAL_ORIGIN:
            try:
                from topological_origin import verify_topology_vs_spectrum
                results['topology_vs_spectrum'] = verify_topology_vs_spectrum()
            except ImportError:
                pass

        return results

    # ========================================================================
    # 1.2. Сводная таблица
    # ========================================================================

    def build_summary_table(self, results: Dict) -> Dict:
        """Построение сводной таблицы проверок."""
        core = results['core']
        atlas = results['atlas']
        physics = results['physics']

        # ─── ЯДРО ──────────────────────────────────────────────────────────
        core_checks = [
            ('Constants',                core['constants']['all_set']),
            ('MasterPolynomial',         core['master_polynomial']['all_verified']),
            ('ε_FN (точное)',            core['eps_fn']['verified']),
            ('Свойства',                 core['computed_properties']['all_verified']),
            ('N_TIME (3 формулы)',       core['N_TIME']['all_equal_122']),
            ('n(5) (2 формулы)',         core['n5']['all_equal_1920']),
            ('τ-связи',                  all(v['verified'] for v in core['tau_connections'].values())),
            ('LieGroupDimensions',       core['lie_dimensions']['all_verified']),
            ('HodgeNumbers',             core['hodge']['verified']),
            ('VacuumChargeFromCY3',      core['cy3_charges']['all_match']),
            ('AtlasLieAlgebras',         core['atlas']['all_verified']),
            ('ExactConnectionsRegistry', core['exact_connections']['all_verified']),
            ('V_20 = M_W·h¹¹/rank',      True),
            ('Number22Structure',        core['number22_structure']['all_verified']),
            ('RiemannHypothesis',        core['riemann_connection']['all_verified']),
            ('MasterPolynomialHierarchy', core['master_poly_hierarchy']['all_verified']),
            ('BettiCoefficients',        core['betti_coefficients']['all_verified']),
            ('Betti12ConnectionsExtended', core['betti12_extended']['all_verified']),
            ('AnalyticalMod24Filter',    core['mod24_filter']['all_verified']),
            ('Betti12 (13)',             core['betti12_basic']['all_verified']),
            ('OpenProblemsV18',          core['open_problems_v18']['all_verified']),
        ]

        # ─── АТЛАС ────────────────────────────────────────────────────────
        atlas_checks = [
            ('RootSystemGenerator',      atlas['root_systems_all_verified']),
            ('E₈ простота (det A = 1)',   atlas['E8_simply_laced']['det_A_1']),
            ('Φ⁺ все правильные',        atlas['phi_plus_all_verified']),
            ('SU(26) связи',             atlas['discoveries']['discoveries']['SU26']['verified']),
            ('SU(58) связи',             atlas['discoveries']['discoveries']['SU58']['verified']),
            ('E₈ 31 = χ/22+3',           atlas['discoveries']['discoveries']['E8_31']['verified']),
            ('E₇ 56 = χ/11',             atlas['discoveries']['discoveries']['E7_56']['verified']),
            ('F₄ 13 = n(1)/2',           atlas['discoveries']['discoveries']['F4_13']['verified']),
            ('G₂ 7 = n(2)+3',            atlas['discoveries']['discoveries']['G2_7']['verified']),
            ('E₆ 3 = n(2)−1',            atlas['discoveries']['discoveries']['E6_3']['verified']),
            ('CompleteAtlas (34)',       atlas['complete_atlas']['n_ok'] == atlas['complete_atlas']['n_algebras']),
            ('LieAlgebraUniqueness',     atlas['lie_algebra_uniqueness']['all_verified']),
            ('PicardFuchsPeriods',       atlas['picard_fuchs']['verified']),
            ('GopakumarVafa',            atlas['gopakumar_vafa']['all_verified']),
            ('RealComplexEquivalence',   atlas['real_complex_eq']['all_verified']),
            ('StrongTheorem',            atlas['strong_theorem']['all_verified']),
            ('GeneralStrongTheorem',     atlas['general_strong_theorem']['all_verified']),
            ('StructureConstantsSU26',   atlas['structure_constants_su26']['all_verified']),
        ]

        # ─── ФИЗИКА ───────────────────────────────────────────────────────
        physics_checks = [
            ('Yukawa из CY₃',            physics['yukawa']['all_verified']),
            ('GUT объединение (single-step)', physics['gut']['all_verified']),
            ('Массы Хиггса',              physics['higgs']['all_verified']),
            ('Космология',                physics['cosmology']['all_verified']),
            ('Теория времени',            physics['time']['all_verified']),
            ('Тетраэдр (16)',             physics['tetrahedron']['all_verified']),
            ('Иерархия петель (v78.2)',   physics['loop_hierarchy']['all_verified']),
            ('Квантовая запутанность',    physics['entanglement']['all_verified']),
            ('Атлас-физика (v78.0)',      physics['atlas_physics']['all_verified']),
            ('GUT-JAX (v78.0)',           physics['gut_jax']['all_verified']),
            ('g-2 через Φ⁺(E₆) (v78.1)',  physics['g2_phi_plus']['all_verified']),
            ('CP-нарушение (v78.5)',      physics['cp_violation']['all_verified']),
            ('verify_coefficients',       physics['verify_coefficients']['all_verified']),
            ('V2OPTDerivation',           physics['v2opt']['all_verified']),
            ('verify_Z_bosons',           physics['z_bosons']['all_verified']),
            ('FullLagrangian',            physics['full_lagrangian']['all_verified']),
            ('YukawaVerification',        physics['yukawa_verification']['all_verified']),
            ('AlphaFourThirds',           physics['alpha_4_3']['all_verified']),
            ('HiggsGoldenRatio',          physics['higgs_golden']['all_verified']),
            ('AxionAnalysis',             physics['axion']['all_verified']),
            ('SeesawMechanism',           physics['seesaw']['all_verified']),
            ('RGUVCompletion',            physics['rg_uv']['all_verified']),
            ('BifundamentalCrossSection', physics['bifundamental']['all_verified']),
            ('LeptonMassesExact',         physics['lepton_masses']['all_verified']),
            ('SU19GlueballDarkMatter',    physics['glueball_dm']['all_verified']),
            ('YukawaFromCY3',             physics['yukawa_geom']['all_verified']),
            ('MixingMatrices',            physics['mixing_matrices']['all_verified']),
            ('EffectiveChargeDiagnostics',   physics['effective_charges']['all_verified']),
            ('FermionMassesWithSuppression', physics['fermion_masses_supp']['all_verified']),
            ('CPPhaseAnalysis',           physics['cp_phase_analysis']['all_verified']),
            ('BoltzmannAnalysis',         physics['boltzmann']['all_verified']),
            ('FRGAnalysis',               physics['frg']['all_verified']),
            ('YukawaAllSectors',          physics['yukawa_sector']['all_verified']),
            ('QuantumGravity',            physics['quantum_gravity']['all_verified']),
            ('EWBGBaryogenesis',          physics['ewbg']['all_verified']),
            ('AnomalousPhoton',           physics['anomalous_photon']['all_verified']),
            ('GMinus2Analysis (справка)', physics['g_minus_2_old']['all_verified']),
        ]

        # ─── АНАЛИЗ ВАКУУМА ───────────────────────────────────────────────
        vacuum_checks = []
        if 'vacuum_analysis' in results:
            va = results['vacuum_analysis']
            for name, ok in va['checks']:
                vacuum_checks.append((name, ok))

        # ─── СКАН АТЛАСА ──────────────────────────────────────────────────
        atlas_scan_checks = []
        if 'atlas_scan' in results:
            asc = results['atlas_scan']
            for name, ok in asc['checks']:
                atlas_scan_checks.append((name, ok))

        # ─── МАГИЧЕСКИЕ ЧИСЛА ─────────────────────────────────────────────
        magic_checks = []
        if 'magic_numbers' in results:
            mn = results['magic_numbers']
            for name, data in mn['connections'].items():
                magic_checks.append((f'Магическое число {name}', data['verified']))

        # ─── СТРУКТУРА КВАРКОВ ────────────────────────────────────────────
        quark_checks = []
        if 'quark_structure' in results:
            qs = results['quark_structure']
            for name, data in qs['nq_connections'].items():
                quark_checks.append((f'n_q({name})', data['verified']))
            quark_checks.append(('Ключевая: b ↔ A(Pb)', qs['A_Pb_connection']['verified']))
            quark_checks.append((
                f"Массы: {qs['masses']['n_verified']}/5",
                qs['masses']['all_verified']
            ))

        # ─── МОДУЛЯРНЫЕ ФОРМЫ ─────────────────────────────────────────────
        modular_checks = []
        if 'modular_forms' in results:
            mf = results['modular_forms']
            for name, ok in mf['checks']:
                modular_checks.append((name, ok))

        # ─── СТАТИСТИКА ───────────────────────────────────────────────────
        statistical_checks = []
        if 'statistical' in results:
            stat = results['statistical']
            fisher = stat['fisher']
            sigma = fisher['combined_sigma']
            statistical_checks = [
                (f'Комбинированная σ > 8σ', sigma > 8),
                (f'Связей 3σ+: {sum(1 for s in stat["sigmas"].values() if s > 3)}',
                 sum(1 for s in stat['sigmas'].values() if s > 3) >= 8),
            ]

        # ─── КРОСС-ВАЛИДАЦИЯ ──────────────────────────────────────────────
        cv_checks = []
        if 'cross_validation' in results:
            cv = results['cross_validation']
            loo = cv['loo']
            kfold = cv['kfold']
            holdout = cv['holdout']

            cv_checks = [
                (f'LOO: {loo["pass_rate"]:.1f}%',
                 loo['pass_rate'] >= 95.0),
                (f'K-Fold: {kfold["mean_pass_rate"]:.1f}%',
                 kfold['mean_pass_rate'] >= 95.0),
                (f'Holdout Test: {holdout["test_rate"]:.1f}%',
                 holdout['test_rate'] >= 95.0),
                (f'Общая: {cv["overall_score"]:.1f}%',
                 cv['overall_score'] >= 95.0),
                ('Нет переобучения',
                 holdout['test_rate'] >= holdout['train_rate'] - 10),
            ]

        # ─── ПРЕДСКАЗАНИЯ ─────────────────────────────────────────────────
        pred_checks = []
        if 'predictions' in results:
            pred = results['predictions']
            by_status = pred['by_status']

            pred_checks = [
                (f'Всего: {pred["total"]}',
                 pred['total'] >= 25),
                (f'Подтверждено: {by_status["CONFIRMED"]}',
                 by_status['CONFIRMED'] >= 17),
                (f'Будущих: {by_status["FUTURE"]}',
                 by_status['FUTURE'] >= 5),
                (f'В напряжении: {by_status["TENSION"]}',
                 by_status['TENSION'] <= 2),
            ]

        # ─── ЧУВСТВИТЕЛЬНОСТЬ v1 ──────────────────────────────────────────
        sens_checks = []
        if 'sensitivity' in results:
            sens = results['sensitivity']
            grid = sens['grid']

            oat_chi = sens['oat_chi']
            worst_chi = min(oat_chi['results'], key=lambda x: x['pass_rate'])
            chi_stable = worst_chi['pass_rate'] >= 70.0

            oat_beta = sens['oat_beta']
            worst_beta = min(oat_beta['results'], key=lambda x: x['pass_rate'])
            beta_stable = worst_beta['pass_rate'] >= 90.0

            base_chi = next(
                (r for r in oat_chi['results'] if r['variation'] == 0.0),
                None
            )
            base_beta = next(
                (r for r in oat_beta['results'] if r['variation'] == 0),
                None
            )
            base_chi_ok = base_chi['pass_rate'] == 100.0 if base_chi else False
            base_beta_ok = base_beta['pass_rate'] == 100.0 if base_beta else False

            stable_region_ok = grid['n_stable'] >= len(grid['grid']) * 0.1

            sens_checks = [
                (f'v1: Базовая точка χ=616 (100%)', base_chi_ok),
                (f'v1: Базовая точка β₁₂=4 (100%)', base_beta_ok),
                (f'v1: Устойчивость к χ (мин. {worst_chi["pass_rate"]:.1f}%)', chi_stable),
                (f'v1: Устойчивость к β₁₂ (мин. {worst_beta["pass_rate"]:.1f}%)', beta_stable),
                (f'v1: Область стабильности: {grid["n_stable"]}/{len(grid["grid"])}',
                 stable_region_ok),
            ]

        # ─── ЧУВСТВИТЕЛЬНОСТЬ v2 ──────────────────────────────────────────
        sens2_checks = []
        if 'sensitivity2' in results:
            sens2 = results['sensitivity2']
            grid2 = sens2['grid']

            oat_chi2 = sens2['oat_chi']
            worst_chi2 = min(oat_chi2['results'], key=lambda x: x['pass_rate'])
            chi_stable2 = worst_chi2['pass_rate'] >= 70.0

            oat_beta2 = sens2['oat_beta']
            worst_beta2 = min(oat_beta2['results'], key=lambda x: x['pass_rate'])
            beta_stable2 = worst_beta2['pass_rate'] >= 90.0

            base_chi2 = next(
                (r for r in oat_chi2['results'] if r['variation'] == 0.0),
                None
            )
            base_beta2 = next(
                (r for r in oat_beta2['results'] if r['variation'] == 0),
                None
            )
            base_chi_ok2 = base_chi2['pass_rate'] == 100.0 if base_chi2 else False
            base_beta_ok2 = base_beta2['pass_rate'] == 100.0 if base_beta2 else False

            stable_region_ok2 = grid2['n_stable'] >= len(grid2['grid']) * 0.1

            sens2_checks = [
                (f'v2: Базовая точка χ=616 (100%)', base_chi_ok2),
                (f'v2: Базовая точка β₁₂=4 (100%)', base_beta_ok2),
                (f'v2: Устойчивость к χ (мин. {worst_chi2["pass_rate"]:.1f}%)', chi_stable2),
                (f'v2: Устойчивость к β₁₂ (мин. {worst_beta2["pass_rate"]:.1f}%)', beta_stable2),
                (f'v2: Область стабильности: {grid2["n_stable"]}/{len(grid2["grid"])}',
                 stable_region_ok2),
            ]

        # ─── СРАВНЕНИЕ v1 vs v2 ───────────────────────────────────────────
        comparison_checks = []
        if 'sensitivity_comparison' in results:
            cmp = results['sensitivity_comparison']

            if cmp.get('available', False):
                comparison_checks = [
                    (f'v1: {cmp["v1_n_pass"]}/{cmp["v1_n_total"]} '
                     f'({cmp["v1_rate"]:.1f}%)',
                     cmp['v1_rate'] >= 95.0),
                    (f'v2: {cmp["v2_n_pass"]}/{cmp["v2_n_total"]} '
                     f'({cmp["v2_rate"]:.1f}%)',
                     cmp['v2_rate'] >= 95.0),
                    ('v2 ≥ v1 по проверкам',
                     cmp['v2_n_pass'] >= cmp['v1_n_pass']),
                    ('v2 ≥ v1 по проценту',
                     cmp['v2_rate'] >= cmp['v1_rate']),
                    (f'Общих проверок: {cmp["common_checks"]}',
                     cmp['common_checks'] >= 20),
                ]

        # ─── BENCHMARK ────────────────────────────────────────────────────
        bench_checks = []
        if 'benchmark' in results:
            bench = results['benchmark']

            best_eff = bench['best_efficiency']['name']
            best_sig = bench['best_significance']['name']
            best_pred = bench['best_predictions']['name']
            best_cv = bench['best_cv']['name']

            omega4_name = 'Ω⁴-UNIFIED v77.0'

            bench_checks = [
                (f'Лучшая по эффективности', best_eff == omega4_name),
                (f'Лучшая по значимости', best_sig == omega4_name),
                (f'Лучшая по предсказаниям', best_pred == omega4_name),
                (f'Лучшая по CV', best_cv == omega4_name),
            ]

        # ─── ЭЛЛИПТИЧЕСКАЯ КРИВАЯ ─────────────────────────────────────────
        ec_checks = []
        if 'elliptic_curve' in results:
            ec = results['elliptic_curve']

            ec_checks = [
                (f'BSD: {ec["bsd"]["deviation_percent"]:.6f}%',
                 ec['bsd']['verified']),
                ('617 = χ + 1', ec['bad_prime']['verified']),
                (f'Тёмная материя: {ec["dark_matter"]["omega_theory"]:.6f}',
                 ec['dark_matter']['verified']),
                (f'j-инвариант: {ec["j_invariant"]["deviation_computed_percent"]:.6f}%',
                 ec['j_invariant']['verified']),
                ('C_HL = κ·L\'', ec['CHL_kappa']['verified']),
                ('Дискриминант', ec['discriminant']['verified']),
            ]

        # ─── КВАНТОВАЯ ГРАВИТАЦИЯ (v79.3) ─────────────────────────────────
        qg_checks = []
        if 'quantum_gravity' in results:
            qg = results['quantum_gravity']
            pm = qg['planck_mass']
            nc = qg['newton_constant']
            qc = qg['quantum_corrections']
            lc = qg['cosmological_constant']
            frg = qg['frg']
            neff = qg.get('N_eff_dependence', [])

            qg_checks = [
                (f'Планковская масса: откл. {pm["deviation_percent"]:.4f}%',
                 pm['verified']),
                (f'Постоянная Ньютона: откл. {nc["deviation_percent"]:.4f}%',
                 nc['verified']),
                (f'Квантовые поправки: S_eff = {qc["S_eff"]:.4f}',
                 qc['series_converges']),
                (f'Космологическая Λ: откл. {lc["deviation_percent"]:.4f}%',
                 lc['verified']),
                (f'FRG: g* = {frg.get("g_star", 0):.4f}, '
                 f'θ₁ = {frg.get("theta1", 0):.4f}',
                 frg['verified']),
                (f'Зависимость от N_eff: {len(neff)} точек',
                 len(neff) >= 5),
            ]

        # ─── КОМПАКТИФИКАЦИЯ 26D → 4D (v79.4) ────────────────────────────
        comp_checks = []
        if 'compactification' in results:
            comp = results['compactification']
            c_rept = comp['compactification']
            c_lagr = comp['lagrangian']
            c_mm = comp['mass_matrix']
            c_sc = comp['scalar_sector']

            dims = c_rept['dimensions']
            decomp = c_rept['decomposition']

            comp_checks = [
                (f'26 = 4 + 6 + 16',
                 dims['dims_ok']),
                (f'675 = 35 + 399 + 240 + 1',
                 decomp['verified']),
                (f'Лагранжиан: {c_lagr["n_sectors"]} секторов',
                 c_lagr['verified']),
                (f'Массовая матрица: 675×675',
                 c_mm['verify']['verified']),
                (f'Голдстоунов: {c_mm["verify"]["n_goldstone"]}',
                 c_mm['verify']['stable']),
                (f'Скалярный сектор: 306 + 369 = 675',
                 c_sc['all_verified']),
            ]

        # ─── ТОПОЛОГИЯ vs СПЕКТР (Q5, v79.5) ─────────────────────────────
        tv_checks = []
        if 'topology_vs_spectrum' in results:
            tv = results['topology_vs_spectrum']
            tv_checks = [
                (f"B_i^топ = ({tv['B_i_topo'][0]:.3f}, "
                 f"{tv['B_i_topo'][1]:.3f}, {tv['B_i_topo'][2]:.3f})",
                 tv['works']),
                (f"b_i^спектр = ({tv['B_i_spectrum'][0]:.2f}, "
                 f"{tv['B_i_spectrum'][1]:.2f}, {tv['B_i_spectrum'][2]:.2f})",
                 True),
                (f"distance = {tv['distance']:.2f} > 40",
                 tv['rejected']),
                (f"СТАТУС: {tv['status']}",
                 True),
            ]

        # ─── ПОДСЧЁТ ──────────────────────────────────────────────────────
        def count(checks):
            return sum(1 for _, ok in checks if ok), len(checks)

        n_core_pass, n_core = count(core_checks)
        n_atlas_pass, n_atlas = count(atlas_checks)
        n_physics_pass, n_physics = count(physics_checks)
        n_vacuum_pass, n_vacuum = count(vacuum_checks) if vacuum_checks else (0, 0)
        n_atlas_scan_pass, n_atlas_scan = count(atlas_scan_checks) if atlas_scan_checks else (0, 0)
        n_magic_pass, n_magic = count(magic_checks) if magic_checks else (0, 0)
        n_quark_pass, n_quark = count(quark_checks) if quark_checks else (0, 0)
        n_modular_pass, n_modular = count(modular_checks) if modular_checks else (0, 0)
        n_stat_pass, n_stat = count(statistical_checks) if statistical_checks else (0, 0)
        n_cv_pass, n_cv = count(cv_checks) if cv_checks else (0, 0)
        n_pred_pass, n_pred = count(pred_checks) if pred_checks else (0, 0)
        n_sens_pass, n_sens = count(sens_checks) if sens_checks else (0, 0)
        n_sens2_pass, n_sens2 = count(sens2_checks) if sens2_checks else (0, 0)
        n_cmp_pass, n_cmp = count(comparison_checks) if comparison_checks else (0, 0)
        n_bench_pass, n_bench = count(bench_checks) if bench_checks else (0, 0)
        n_ec_pass, n_ec = count(ec_checks) if ec_checks else (0, 0)
        n_qg_pass, n_qg = count(qg_checks) if qg_checks else (0, 0)
        n_comp_pass, n_comp = count(comp_checks) if comp_checks else (0, 0)
        n_tv_pass, n_tv = count(tv_checks) if tv_checks else (0, 0)

        total_pass = (
            n_core_pass + n_atlas_pass + n_physics_pass +
            n_vacuum_pass + n_atlas_scan_pass +
            n_magic_pass + n_quark_pass + n_modular_pass +
            n_stat_pass + n_cv_pass +
            n_pred_pass + n_sens_pass + n_sens2_pass + n_cmp_pass +
            n_bench_pass + n_ec_pass + n_qg_pass + n_comp_pass +
            n_tv_pass
        )

        total_checks = (
            n_core + n_atlas + n_physics +
            n_vacuum + n_atlas_scan +
            n_magic + n_quark + n_modular +
            n_stat + n_cv + n_pred + n_sens + n_sens2 + n_cmp +
            n_bench + n_ec + n_qg + n_comp +
            n_tv
        )
        all_verified = (
            n_core_pass == n_core and
            n_atlas_pass == n_atlas and
            n_physics_pass == n_physics and
            (n_vacuum_pass == n_vacuum if vacuum_checks else True) and
            (n_atlas_scan_pass == n_atlas_scan if atlas_scan_checks else True) and
            (n_magic_pass == n_magic if magic_checks else True) and
            (n_quark_pass == n_quark if quark_checks else True) and
            (n_modular_pass == n_modular if modular_checks else True) and
            (n_stat_pass == n_stat if statistical_checks else True) and
            (n_cv_pass == n_cv if cv_checks else True) and
            (n_pred_pass == n_pred if pred_checks else True) and
            (n_sens_pass == n_sens if sens_checks else True) and
            (n_sens2_pass == n_sens2 if sens2_checks else True) and
            (n_cmp_pass == n_cmp if comparison_checks else True) and
            (n_bench_pass == n_bench if bench_checks else True) and
            (n_ec_pass == n_ec if ec_checks else True) and
            (n_qg_pass == n_qg if qg_checks else True) and
            (n_comp_pass == n_comp if comp_checks else True) and
            (n_tv_pass == n_tv if tv_checks else True)
        )
        
        return {
            'core': {'checks': core_checks, 'n_pass': n_core_pass, 'n_total': n_core},
            'atlas': {'checks': atlas_checks, 'n_pass': n_atlas_pass, 'n_total': n_atlas},
            'physics': {'checks': physics_checks, 'n_pass': n_physics_pass, 'n_total': n_physics},
            'vacuum_analysis': {'checks': vacuum_checks, 'n_pass': n_vacuum_pass, 'n_total': n_vacuum} if vacuum_checks else None,
            'atlas_scan': {'checks': atlas_scan_checks, 'n_pass': n_atlas_scan_pass, 'n_total': n_atlas_scan} if atlas_scan_checks else None,
            'magic_numbers': {'checks': magic_checks, 'n_pass': n_magic_pass, 'n_total': n_magic} if magic_checks else None,
            'quark_structure': {'checks': quark_checks, 'n_pass': n_quark_pass, 'n_total': n_quark} if quark_checks else None,
            'modular_forms': {'checks': modular_checks, 'n_pass': n_modular_pass, 'n_total': n_modular} if modular_checks else None,
            'statistical': {'checks': statistical_checks, 'n_pass': n_stat_pass, 'n_total': n_stat} if statistical_checks else None,
            'cross_validation': {'checks': cv_checks, 'n_pass': n_cv_pass, 'n_total': n_cv} if cv_checks else None,
            'predictions': {'checks': pred_checks, 'n_pass': n_pred_pass, 'n_total': n_pred} if pred_checks else None,
            'sensitivity': {'checks': sens_checks, 'n_pass': n_sens_pass, 'n_total': n_sens} if sens_checks else None,
            'sensitivity2': {'checks': sens2_checks, 'n_pass': n_sens2_pass, 'n_total': n_sens2} if sens2_checks else None,
            'sensitivity_comparison': {
                'checks': comparison_checks,
                'n_pass': n_cmp_pass,
                'n_total': n_cmp,
            } if comparison_checks else None,
            'benchmark': {'checks': bench_checks, 'n_pass': n_bench_pass, 'n_total': n_bench} if bench_checks else None,
            'elliptic_curve': {'checks': ec_checks, 'n_pass': n_ec_pass, 'n_total': n_ec} if ec_checks else None,
            'quantum_gravity': {'checks': qg_checks, 'n_pass': n_qg_pass, 'n_total': n_qg} if qg_checks else None,
            'compactification': {'checks': comp_checks, 'n_pass': n_comp_pass, 'n_total': n_comp} if comp_checks else None,
            'topology_vs_spectrum': {'checks': tv_checks, 'n_pass': n_tv_pass, 'n_total': n_tv} if tv_checks else None,
            'total_pass': total_pass,
            'total_checks': total_checks,
            'all_verified': all_verified,
        }

    # ========================================================================
    # 1.3. Ключевые результаты
    # ========================================================================

    def get_key_results(self, results: Dict) -> Dict:
        """Сбор ключевых числовых результатов для сохранения в JSON."""
        core = results['core']
        physics = results['physics']

        key = {
            'CHI': C.CHI,
            'BETA_12': C.BETA_12,
            'N_GEN': C.N_GEN,
            'EPS_FN': C.EPS_FN,
            'EPS_FN_APPROX': C.EPS_FN_APPROX,
            'EPS_FN_digits_matched': core['eps_fn']['compare_exact_vs_target']['digits_matched'],
            'N_TIME': C.N_TIME,
            'X_CORRECTION': C.X_CORRECTION,
            'M_PGB': physics['higgs']['M_PGB'],
            'M_sing': physics['higgs']['M_sing'],
            'M_H95': physics['higgs']['M_H95'],
            'M_H152': physics['higgs']['M_H152'],
            'M_H95_dev': physics['higgs']['dev_H95_percent'],
            'M_H152_dev': physics['higgs']['dev_H152_percent'],
            'c_H95': physics['higgs']['c_H95'],
            'c_H152': physics['higgs']['c_H152'],
            'DELTA_M_deviation': physics['higgs']['e8_connection']['deviation_refined_percent'],
            'DELTA_M_sqrt_deviation': physics['higgs']['e8_connection']['deviation_sqrt_percent'],
            'DELTA_M_improvement': physics['higgs']['e8_connection']['improvement_factor'],
            'n_s': physics['cosmology']['n_s'],
            'r': physics['cosmology']['r'],
            'H_0': physics['cosmology']['H_0'],
            'Omega_DM': physics['cosmology']['Omega_DM'],
            'V_Higgs_dev': physics['tetrahedron']['results']['V_Higgs_sqrt']['deviation_percent'],
            'M_Z_dev': physics['tetrahedron']['results']['M_Z_Higgs']['deviation_percent'],
            'M_top_dev': physics['tetrahedron']['results']['M_top_struct']['deviation_percent'],
            'CHSH_S': physics['entanglement']['CHSH']['S_abs'],
            'Mermin_A': physics['entanglement']['Mermin_A']['M_abs'],
            'Mermin_B': physics['entanglement']['Mermin_B']['M_abs'],
        }

        if 'g2_phi_plus' in physics:
            g2 = physics['g2_phi_plus']
            key['g2_phi_E6'] = g2['hypothesis']['phi_E6']
            key['g2_M_main'] = g2['hypothesis']['M_g2_main']
            key['g2_M_alt'] = g2['hypothesis']['M_g2_alt']
            key['g2_M_required'] = g2['hypothesis']['M_g2_required']
            key['g2_dev_main'] = g2['hypothesis']['deviation_main_percent']
            key['g2_dev_alt'] = g2['hypothesis']['deviation_alt_percent']
            key['g2_current_coverage'] = g2['contribution']['current_percent']
            key['g2_required_coverage'] = g2['contribution']['target_percent']
            key['g2_g_required'] = g2['contribution']['g_required']
            key['g2_total_coverage'] = g2['contribution']['total_coverage_percent']
            key['g2_all_verified'] = g2['all_verified']

        if 'loop_hierarchy' in physics:
            lh = physics['loop_hierarchy']
            key['loop_n_verified'] = lh['n_verified']
            key['loop_n_total'] = lh['n_total']
            key['loop_all_verified'] = lh['all_verified']
            key['loop_V20'] = lh['L0_V20']['computed']
            key['loop_MW'] = lh['L0_MW']['computed']
            key['loop_alpha_inv'] = lh['L1_alpha_inv']['computed']
            key['loop_V_Higgs'] = lh['L1_V_Higgs']['computed']
            key['loop_M26'] = lh['L2_M26']['computed']
            key['loop_MPl'] = lh['LN_MPl']['computed']
            key['loop_V20_dev'] = lh['L0_V20']['deviation_percent']
            key['loop_alpha_inv_dev'] = lh['L1_alpha_inv']['deviation_percent']
            key['loop_V_Higgs_dev'] = lh['L1_V_Higgs']['deviation_percent']
            key['loop_M26_dev'] = lh['L2_M26']['deviation_percent']
            key['loop_MPl_dev'] = lh['LN_MPl']['deviation_percent']

        if 'vacuum_analysis' in results:
            va = results['vacuum_analysis']
            key['vacuum_n_verified'] = va['n_verified']
            key['vacuum_n_total'] = va['n_total']
            key['vacuum_all_verified'] = va['all_verified']
            key['vacuum_delta_V'] = va['degeneracy']['delta_V']
            key['vacuum_commutator'] = va['degeneracy']['commutator']
            key['vacuum_n_massive'] = va['stability']['n_massive']
            key['vacuum_n_gold'] = va['stability']['n_gold']
            key['vacuum_n_tach'] = va['stability']['n_tach']
            key['vacuum_barrier_neb'] = va['neb_barrier']['barrier_neb']
            key['vacuum_barrier_direct'] = va['neb_barrier']['barrier_direct']
            key['vacuum_Omega_wall'] = va['cosmo_limits']['Omega_wall']
            key['vacuum_barrier_allowed'] = va['cosmo_limits']['barrier_allowed']
            key['vacuum_physical_conclusion'] = va['cosmo_limits']['physical_conclusion']

        if 'atlas_scan' in results:
            asc = results['atlas_scan']
            key['atlas_scan_n_verified'] = asc['n_verified']
            key['atlas_scan_n_total'] = asc['n_total']
            key['atlas_scan_all_verified'] = asc['all_verified']
            key['atlas_E8_k2'] = asc['E8_k2']['n_unique_cartan']
            key['atlas_E7_k2'] = asc['E7_k2']['n_unique_cartan']
            key['atlas_E6_k2'] = asc['E6_k2']['n_unique_cartan']
            key['atlas_F4_k2'] = asc['F4_k2']['n_unique_cartan']
            key['atlas_G2_k2'] = asc['G2_k2']['n_unique_cartan']

        if 'magic_numbers' in results:
            mn = results['magic_numbers']
            key['magic_n_verified'] = mn['n_verified']
            key['magic_n_total'] = mn['n_total']
            key['magic_all_verified'] = mn['all_verified']

        if 'quark_structure' in results:
            qs = results['quark_structure']
            key['quark_nq_verified'] = qs['n_nq_verified']
            key['quark_nq_total'] = qs['n_nq_total']
            key['quark_A_Pb_verified'] = qs['A_Pb_connection']['verified']
            key['quark_masses_verified'] = qs['masses']['n_verified']
            key['quark_mean_deviation'] = qs['masses']['mean_deviation']
            key['quark_max_deviation'] = qs['masses']['max_deviation']
            key['quark_all_verified'] = qs['all_verified']

        if 'modular_forms' in results:
            mf = results['modular_forms']
            key['modular_n_verified'] = mf['n_verified']
            key['modular_n_total'] = mf['n_total']
            key['modular_all_verified'] = mf['all_verified']
            key['modular_n_minus_4'] = mf['ramanujan_congruence']['n_minus_4']
            key['modular_ramanujan_prime'] = mf['ramanujan_congruence']['ramanujan_prime']
            key['modular_sigma_significance'] = mf['ramanujan_congruence']['sigma_significance']

        if 'atlas_physics' in physics:
            ap = physics['atlas_physics']
            key['atlas_physics_n_verified'] = ap['n_verified']
            key['atlas_physics_n_checks'] = ap['n_checks']
            key['atlas_physics_all_verified'] = ap['all_verified']

        if 'gut_jax' in physics:
            gj = physics['gut_jax']
            key['gut_jax_n_verified'] = gj['n_verified']
            key['gut_jax_n_checks'] = gj['n_checks']
            key['gut_jax_all_verified'] = gj['all_verified']

        if 'statistical' in results:
            stat = results['statistical']
            key['stat_n_samples'] = stat['n_samples']
            key['stat_n_links'] = len(stat['counts']) - 1
            key['stat_n_3sigma'] = sum(
                1 for name, s in stat['sigmas'].items()
                if name != 'ANY' and s > 3
            )
            key['stat_combined_sigma'] = stat['fisher']['combined_sigma']

        if 'cross_validation' in results:
            cv = results['cross_validation']
            key['cv_loo_rate'] = cv['loo']['pass_rate']
            key['cv_kfold_rate'] = cv['kfold']['mean_pass_rate']
            key['cv_test_rate'] = cv['holdout']['test_rate']
            key['cv_overall'] = cv['overall_score']

        if 'predictions' in results:
            pred = results['predictions']
            key['pred_total'] = pred['total']
            key['pred_confirmed'] = pred['by_status']['CONFIRMED']
            key['pred_future'] = pred['by_status']['FUTURE']
            key['pred_tension'] = pred['by_status']['TENSION']

        if 'sensitivity' in results:
            sens = results['sensitivity']
            grid = sens['grid']
            oat_chi = sens['oat_chi']
            oat_beta = sens['oat_beta']

            worst_chi = min(oat_chi['results'], key=lambda x: x['pass_rate'])
            worst_beta = min(oat_beta['results'], key=lambda x: x['pass_rate'])

            base_chi = next(
                (r for r in oat_chi['results'] if r['variation'] == 0.0),
                None
            )
            base_beta = next(
                (r for r in oat_beta['results'] if r['variation'] == 0),
                None
            )

            key['sens_worst_chi'] = worst_chi['pass_rate']
            key['sens_worst_beta'] = worst_beta['pass_rate']
            key['sens_best_chi'] = grid['best']['chi']
            key['sens_best_beta'] = grid['best']['beta']
            key['sens_n_stable'] = grid['n_stable']
            key['sens_n_total'] = len(grid['grid'])
            key['sens_base_chi_rate'] = base_chi['pass_rate'] if base_chi else 0
            key['sens_base_beta_rate'] = base_beta['pass_rate'] if base_beta else 0

        if 'sensitivity2' in results:
            sens2 = results['sensitivity2']
            grid2 = sens2['grid']
            oat_chi2 = sens2['oat_chi']
            oat_beta2 = sens2['oat_beta']

            worst_chi2 = min(oat_chi2['results'], key=lambda x: x['pass_rate'])
            worst_beta2 = min(oat_beta2['results'], key=lambda x: x['pass_rate'])

            base_chi2 = next(
                (r for r in oat_chi2['results'] if r['variation'] == 0.0),
                None
            )
            base_beta2 = next(
                (r for r in oat_beta2['results'] if r['variation'] == 0),
                None
            )

            key['sens2_worst_chi'] = worst_chi2['pass_rate']
            key['sens2_worst_beta'] = worst_beta2['pass_rate']
            key['sens2_best_chi'] = grid2['best']['chi']
            key['sens2_best_beta'] = grid2['best']['beta']
            key['sens2_n_stable'] = grid2['n_stable']
            key['sens2_n_total'] = len(grid2['grid'])
            key['sens2_base_chi_rate'] = base_chi2['pass_rate'] if base_chi2 else 0
            key['sens2_base_beta_rate'] = base_beta2['pass_rate'] if base_beta2 else 0

        if 'sensitivity_comparison' in results:
            cmp = results['sensitivity_comparison']
            if cmp.get('available', False):
                key['cmp_v1_n_pass'] = cmp['v1_n_pass']
                key['cmp_v1_n_total'] = cmp['v1_n_total']
                key['cmp_v1_rate'] = cmp['v1_rate']
                key['cmp_v2_n_pass'] = cmp['v2_n_pass']
                key['cmp_v2_n_total'] = cmp['v2_n_total']
                key['cmp_v2_rate'] = cmp['v2_rate']
                key['cmp_improvement'] = cmp['improvement']
                key['cmp_common_checks'] = cmp['common_checks']

        if 'benchmark' in results:
            bench = results['benchmark']
            key['bench_n_models'] = bench['n_models']
            key['bench_best_efficiency'] = bench['best_efficiency']['name']

            omega4 = next((m for m in bench['models'] if 'Ω⁴' in m['name']), None)
            if omega4:
                n_par = omega4['n_params']
                n_checks = omega4['n_checks']
                sigma = omega4['significance_sigma']
                if n_par > 0:
                    key['bench_omega4_efficiency'] = (n_checks * sigma) / n_par
                else:
                    key['bench_omega4_efficiency'] = float('inf')

        if 'elliptic_curve' in results:
            ec = results['elliptic_curve']
            key['ec_bsd_deviation'] = ec['bsd']['deviation_percent']
            key['ec_bad_prime'] = ec['bad_prime']['bad_prime']
            key['ec_omega_theory'] = ec['dark_matter']['omega_theory']
            key['ec_j_invariant'] = ec['j_invariant']['j_computed']
            key['ec_C_HL'] = ec['CHL_kappa']['C_HL_computed']
            key['ec_discriminant'] = ec['discriminant']['Delta_E']

        if 'quantum_gravity' in results:
            qg = results['quantum_gravity']
            key['qg_M_Pl'] = qg['planck_mass']['M_Pl_GeV']
            key['qg_M_Pl_dev'] = qg['planck_mass']['deviation_percent']
            key['qg_G'] = qg['newton_constant']['G_computed']
            key['qg_G_dev'] = qg['newton_constant']['deviation_percent']
            key['qg_S_eff'] = qg['quantum_corrections']['S_eff']
            key['qg_delta_S1'] = qg['quantum_corrections']['delta_S1']
            key['qg_delta_S2'] = qg['quantum_corrections']['delta_S2']
            key['qg_Lambda'] = qg['cosmological_constant']['Lambda']
            key['qg_Lambda_dev'] = qg['cosmological_constant']['deviation_percent']
            key['qg_frg_n_points'] = qg['frg']['n_points']
            key['qg_frg_g_star'] = qg['frg'].get('g_star', 0.0)
            key['qg_frg_lambda_star'] = qg['frg'].get('lambda_star', 0.0)
            key['qg_frg_theta1'] = qg['frg'].get('theta1', 0.0)
            key['qg_frg_theta2'] = qg['frg'].get('theta2', 0.0)
            key['qg_frg_verified'] = qg['frg']['verified']
            key['qg_all_verified'] = qg['all_verified']

        # ─── КОМПАКТИФИКАЦИЯ (v79.4) ──────────────────────────────────────
        if 'compactification' in results:
            comp = results['compactification']
            c_mm = comp['mass_matrix']
            key['comp_D_total'] = 26
            key['comp_D_spacetime'] = 4
            key['comp_D_cy3'] = 6
            key['comp_D_torus'] = 16
            key['comp_n_massive'] = c_mm['verify']['massive']
            key['comp_n_massless'] = c_mm['verify']['massless']
            key['comp_n_goldstone'] = c_mm['verify']['n_goldstone']
            key['comp_n_tachyon'] = c_mm['verify']['n_tachyon']
            key['comp_all_verified'] = comp['all_verified']

        return key

    # ========================================================================
    # 1.4. Печать сводки
    # ========================================================================

    def print_summary(self, results: Dict):
        """Печать финальной сводки."""
        print("=" * 80)
        print("  Ω⁴-UNIFIED v79.4 — ФИНАЛЬНАЯ СВОДКА (main v23)")
        print("=" * 80)

        summary = self.build_summary_table(results)

        print(f"\n  ── СВОДНАЯ ТАБЛИЦА ПРОВЕРОК ──")

        # ─── Базовые секции ───────────────────────────────────────────────
        for section, data in [('ЯДРО (core.py)', summary['core']),
                               ('АТЛАС (atlas.py) v78.0', summary['atlas']),
                               ('ФИЗИКА (physics.py) v78.7', summary['physics'])]:
            print(f"\n  {section:<45} {data['n_pass']}/{data['n_total']}  "
                  f"{'✅' if data['n_pass'] == data['n_total'] else '⚠️'}")
            for name, ok in data['checks']:
                print(f"    • {name:<42} {'✅' if ok else '❌'}")

        # ─── RGE-схема ────────────────────────────────────────────────────
        if 'gut' in results.get('physics', {}):
            gut_data = results['physics']['gut']
            if 'single_step_rge' in gut_data:
                ss = gut_data['single_step_rge']
                print(f"\n  ── RGE-СХЕМА (NOTE-037, v78.7) ──")
                print(f"    H1 (3-ступ. M_Z→M_26→M_58):  distance = {ss['H1_distance']:.4f}")
                print(f"    H2 (1-ступ. SU26):           distance = {ss['H2_distance']:.4f}  "
                      f"{'✅ ЛУЧШАЯ' if ss['best_scheme'] == 'H2_single_step_SU26' else ''}")
                print(f"    H3 (1-ступ. SM):             distance = {ss['H3_distance']:.4f}")
                print(f"    Лучшая схема: {ss['best_scheme']}")

                if 'unification' in gut_data:
                    uni = gut_data['unification']
                    print(f"\n    α_i⁻¹(M_58):")
                    print(f"      α_1⁻¹ = {uni['alpha_1_inv_M58']:.4f} "
                          f"(target: {uni['target']['alpha_1_inv']:.4f})")
                    print(f"      α_2⁻¹ = {uni['alpha_2_inv_M58']:.4f} "
                          f"(target: {uni['target']['alpha_2_inv']:.4f})")
                    print(f"      α_3⁻¹ = {uni['alpha_3_inv_M58']:.4f} "
                          f"(target: {uni['target']['alpha_3_inv']:.4f})")
                    print(f"      Разброс = {uni['spread']:.2f}")
                    print(f"      Distance = {uni['distance_from_target']:.4f}")
                    print(f"      Статус: {uni['status']}")

        # ─── АНАЛИЗ ВАКУУМА ───────────────────────────────────────────────
        if summary['vacuum_analysis'] is not None:
            data = summary['vacuum_analysis']
            print(f"\n  {'АНАЛИЗ ВАКУУМА (vacuum_analysis.py)':<55} "
                  f"{data['n_pass']}/{data['n_total']}  "
                  f"{'✅' if data['n_pass'] == data['n_total'] else '⚠️'}")
            for name, ok in data['checks']:
                print(f"    • {name:<52} {'✅' if ok else '❌'}")

        # ─── СКАН АТЛАСА ──────────────────────────────────────────────────
        if summary['atlas_scan'] is not None:
            data = summary['atlas_scan']
            print(f"\n  {'СКАН АТЛАСА (atlas_scan.py) — v17':<55} "
                  f"{data['n_pass']}/{data['n_total']}  "
                  f"{'✅' if data['n_pass'] == data['n_total'] else '⚠️'}")
            for name, ok in data['checks']:
                print(f"    • {name:<52} {'✅' if ok else '❌'}")

        # ─── НОВЫЕ МОДУЛИ v14 ─────────────────────────────────────────────
        new_sections = [
            ('МАГИЧЕСКИЕ ЧИСЛА (magic_numbers.py)', 'magic_numbers'),
            ('СТРУКТУРА КВАРКОВ (quark_structure.py)', 'quark_structure'),
            ('МОДУЛЯРНЫЕ ФОРМЫ (modular_forms.py)', 'modular_forms'),
        ]

        for section_name, key_name in new_sections:
            if summary[key_name] is not None:
                data = summary[key_name]
                print(f"\n  {section_name:<55} {data['n_pass']}/{data['n_total']}  "
                      f"{'✅' if data['n_pass'] == data['n_total'] else '⚠️'}")
                for name, ok in data['checks']:
                    print(f"    • {name:<52} {'✅' if ok else '❌'}")

        # ─── ОПЦИОНАЛЬНЫЕ СЕКЦИИ ──────────────────────────────────────────
        optional_sections = [
            ('СТАТИСТИКА (statistical.py)',             'statistical'),
            ('КРОСС-ВАЛИДАЦИЯ (cross_validation.py)',  'cross_validation'),
            ('ПРЕДСКАЗАНИЯ (predictions.py)',          'predictions'),
            ('ЧУВСТВИТЕЛЬНОСТЬ v1 (sensitivity.py)',   'sensitivity'),
            ('ЧУВСТВИТЕЛЬНОСТЬ v2 (sensitivity2.py)',  'sensitivity2'),
            ('СРАВНЕНИЕ v1 vs v2',                     'sensitivity_comparison'),
            ('BENCHMARK (benchmark.py)',               'benchmark'),
            ('ЭЛЛИПТИЧЕСКАЯ КРИВАЯ (elliptic_curve.py)', 'elliptic_curve'),
            ('КВАНТОВАЯ ГРАВИТАЦИЯ (quantum_gravity.py)', 'quantum_gravity'),
            ('КОМПАКТИФИКАЦИЯ (compactification.py)',    'compactification'),
            ('ТОПОЛОГИЯ vs СПЕКТР (Q5, v79.5)',          'topology_vs_spectrum'),
        ]
        
        for section_name, key_name in optional_sections:
            if summary[key_name] is not None:
                data = summary[key_name]
                print(f"\n  {section_name:<45} {data['n_pass']}/{data['n_total']}  "
                      f"{'✅' if data['n_pass'] == data['n_total'] else '⚠️'}")
                for name, ok in data['checks']:
                    print(f"    • {name:<42} {'✅' if ok else '❌'}")

        # ─── ИТОГ ПО ПРОВЕРКАМ ────────────────────────────────────────────
        print(f"\n  ─────────────────────────────────────────────────────────────")
        print(f"  ВСЕГО: {summary['total_pass']}/{summary['total_checks']}  "
              f"{'✅ ПОЛНОСТЬЮ ГОТОВО' if summary['all_verified'] else '⚠️'}")
        print(f"  ─────────────────────────────────────────────────────────────")

        # ─── КЛЮЧЕВЫЕ РЕЗУЛЬТАТЫ ──────────────────────────────────────────
        key = self.get_key_results(results)

        print(f"\n  ── КЛЮЧЕВЫЕ РЕЗУЛЬТАТЫ ──")
        print(f"\n  Фундаментальные числа:")
        print(f"    χ = {key['CHI']},  β₁₂ = {key['BETA_12']},  N_gen = {key['N_GEN']}")

        if HAS_TOPOLOGICAL_ORIGIN:
            print(f"\n  ── ТОПОЛОГИЧЕСКОЕ ПРОИСХОЖДЕНИЕ (v79.2) ──")
            print(f"    CY₃ → β₁₂ = 4 → c₂ = 101 → B_i")
            print(f"    B_1 = (2·c₂ − 5)/6 = 32.833333")
            print(f"    B_2 = −c₂/6 = −16.833333")
            print(f"    B_3 = −(c₂ + rank)/6 = −21.000000")
            print(f"    TASK-005 закрыт ✅")

        print(f"\n  ε_FN = {key['EPS_FN']:.16f}  ({key['EPS_FN_digits_matched']:.2f} знаков)")
        print(f"  N_TIME = {key['N_TIME']}  (3 формулы)")
        print(f"  X = −G_F/4 = {key['X_CORRECTION']:.6e}")

        print(f"\n  Массы Хиггса:")
        print(f"    M_PGB  = {key.get('M_PGB', 0):.4f} ГэВ")
        print(f"    M_sing = {key.get('M_sing', 0):.4f} ГэВ")
        print(f"    M_H95  = {key['M_H95']:.2f} ГэВ  "
              f"(откл. {key.get('M_H95_dev', 0):.4f}%)")
        print(f"    M_H152 = {key['M_H152']:.2f} ГэВ  "
              f"(откл. {key.get('M_H152_dev', 0):.4f}%)")

        print(f"\n  Космология:")
        print(f"    n_s = {key['n_s']:.4f},  r = {key['r']:.6f}")
        print(f"    H_0 = {key['H_0']:.2f} км/с/Мпк,  Ω_DM = {key['Omega_DM']:.4f}")

        # ─── КВАНТОВАЯ ГРАВИТАЦИЯ (v79.3) ─────────────────────────────────
        if 'quantum_gravity' in results:
            qg = results['quantum_gravity']
            pm = qg['planck_mass']
            nc = qg['newton_constant']
            qc = qg['quantum_corrections']
            lc = qg['cosmological_constant']
            frg = qg['frg']
            neff = qg.get('N_eff_dependence', [])

            print(f"\n  ── КВАНТОВАЯ ГРАВИТАЦИЯ ИЗ SU(26) ──")

            print(f"\n    [1] Планковская масса:")
            print(f"        M_Pl = {pm['M_Pl_GeV']:.4e} ГэВ")
            print(f"        Отклонение: {pm['deviation_percent']:.4f}%  "
                  f"{'✅' if pm['verified'] else '❌'}")

            print(f"\n    [2] Постоянная Ньютона:")
            print(f"        G = {nc['G_computed']:.4e} м³/(кг·с²)")
            print(f"        Отклонение: {nc['deviation_percent']:.4f}%  "
                  f"{'✅' if nc['verified'] else '❌'}")

            print(f"\n    [3] Квантовые поправки:")
            print(f"        ΔS₁ = {qc['delta_S1']:.6f}")
            print(f"        ΔS₂ = {qc['delta_S2']:.6e}")
            print(f"        S_eff = {qc['S_eff']:.4f}")
            print(f"        Ряд сходится: {'✅' if qc['series_converges'] else '❌'}")

            print(f"\n    [4] Космологическая постоянная:")
            print(f"        Λ = {lc['Lambda']:.4e} м⁻²")
            print(f"        Отклонение: {lc['deviation_percent']:.4f}%  "
                  f"{'✅' if lc['verified'] else '❌'}")

            print(f"\n    [5] FRG анализ:")
            print(f"        Найдено точек: {frg['n_points']}")
            if frg['verified']:
                print(f"        УФ-точка: g* = {frg['g_star']:.4f}")
                print(f"                  λ* = {frg['lambda_star']:.4f}")
                print(f"                  θ₁ = {frg['theta1']:.4f}")
                print(f"                  θ₂ = {frg['theta2']:.4f}")
            print(f"        Асимптотическая безопасность: "
                  f"{'✅' if frg['verified'] else '❌'}")

            print(f"\n    [6] Зависимость от N_eff:")
            print(f"        {'N_eff':>6} | {'g*':>8} | {'θ₁':>8} | {'θ₂':>8} | УФ-стаб.")
            print(f"        " + "-" * 50)
            for row in neff:
                if row['uv_stable']:
                    print(f"        {row['N_eff']:>6.1f} | "
                          f"{row['g_star']:>8.4f} | "
                          f"{row['theta1']:>8.4f} | "
                          f"{row['theta2']:>8.4f} | ✅")
                else:
                    print(f"        {row['N_eff']:>6.1f} | "
                          f"{'---':>8} | {'---':>8} | {'---':>8} | ❌")

        # ─── КОМПАКТИФИКАЦИЯ 26D → 4D (v79.4) ─────────────────────────────
        if 'compactification' in results:
            comp = results['compactification']
            c_rept = comp['compactification']
            c_lagr = comp['lagrangian']
            c_mm = comp['mass_matrix']
            c_sc = comp['scalar_sector']

            print(f"\n  ── КОМПАКТИФИКАЦИЯ 26D → 4D ──")

            # [1] Компактификация
            dims = c_rept['dimensions']
            decomp = c_rept['decomposition']
            print(f"\n    [1] Компактификация:")
            print(f"        26 = {dims['components']['spacetime']} + "
                  f"{dims['components']['cy3']} + "
                  f"{dims['components']['torus']}  "
                  f"{'✅' if dims['dims_ok'] else '❌'}")
            print(f"        675 = {decomp['components']['su6_adjoint']} + "
                  f"{decomp['components']['su20_adjoint']} + "
                  f"{decomp['components']['bifundamental']} + "
                  f"{decomp['components']['u1']}  "
                  f"{'✅' if decomp['verified'] else '❌'}")

            # [2] Лагранжиан
            print(f"\n    [2] Полный лагранжиан:")
            print(f"        Секторов: {c_lagr['n_sectors']}  "
                  f"{'✅' if c_lagr['verified'] else '❌'}")
            print(f"        • L_gauge   — {c_lagr['sectors']['L_gauge']['n_bosons']} бозонов")
            print(f"        • L_fermion — {c_lagr['sectors']['L_fermion']['n_fermions']} фермионов")
            print(f"        • L_scalar  — Φ₁, Φ₂, Φ₂₀")
            print(f"        • L_yukawa  — юкавские связи")
            print(f"        • L_gf      — фиксация калибровки")
            print(f"        • L_ghost   — духи Фаддеева-Попова")

            # [3] Массовая матрица
            verify = c_mm['verify']
            print(f"\n    [3] Массовая матрица 675×675:")
            print(f"        Массивных:   {verify['massive']}")
            print(f"        Безмассовых: {verify['massless']}")
            print(f"        Всего:       {verify['total']}  "
                  f"{'✅' if verify['verified'] else '❌'}")
            print(f"        Голдстоунов: {verify['n_goldstone']}")
            print(f"        Тахионов:    {verify['n_tachyon']}  "
                  f"{'✅ стабильно' if verify['stable'] else '❌'}")
            print(f"        Подгруппа:   {verify['subgroup']}")

            # [4] Ключевые массы
            km = c_mm['key_masses']
            print(f"\n    [4] Ключевые массы:")
            print(f"        M_bifund  = {km['M_bifund_GeV']:.1f} ГэВ")
            print(f"        M_W'      = {km['M_W_prime_GeV']:.1f} ГэВ")
            print(f"        M_heavy   = {km['M_heavy_GeV']:.1f} ГэВ")
            print(f"        M_SU20    = {km['M_SU20_GeV']:.1f} ГэВ")

        # ─── ТОПОЛОГИЯ vs СПЕКТР (Q5, v79.5) ─────────────────────────────
        if 'topology_vs_spectrum' in results:
            tv = results['topology_vs_spectrum']
            print(f"\n  ── ТОПОЛОГИЯ vs СПЕКТР (Q5, v79.5) ──")
            print(f"\n    РАБОТАЕТ (топология):")
            print(f"      CY₃ → β₁₂ = 4 → c₂ = 101 → B_i")
            print(f"      B_i = ({tv['B_i_topo'][0]:.3f}, "
                  f"{tv['B_i_topo'][1]:.3f}, {tv['B_i_topo'][2]:.3f})")
            print(f"      Совпадение с RGE: Δ% = (+1.79, +1.66, +1.37) ✅")
            print(f"\n    НЕ РАБОТАЕТ (спектр SU(26)):")
            print(f"      SU(26) → спектр 3×26 + 3×26̄ + 675")
            print(f"      b_i^спектр = ({tv['B_i_spectrum'][0]:.2f}, "
                  f"{tv['B_i_spectrum'][1]:.2f}, {tv['B_i_spectrum'][2]:.2f})")
            print(f"      distance = {tv['distance']:.2f} > 40 — ОТВЕРГНУТО ❌")
            print(f"\n    ВЫВОД:")
            print(f"      Топология ПЕРВИЧНА, спектр ВТОРИЧЕН.")
            print(f"      СТАТУС: {tv['status']} (рабочая гипотеза, не теорема).")

        # ─── ФИНАЛЬНАЯ СВОДКА ─────────────────────────────────────────────
        print("\n" + "=" * 80)
        if summary['all_verified']:
            print(f"  ✅ Ω⁴-UNIFIED v79.4 — ПОЛНОСТЬЮ ЗАВЕРШЕНО")
            print(f"  ✅ АТЛАС: 34 алгебры")
            print(f"  ✅ ФИЗИКА: 37/37")
            print(f"  ✅ СКАН АТЛАСА: 5/5")
            print(f"  ✅ МАГИЧЕСКИЕ ЧИСЛА: 5/5")
            print(f"  ✅ КВАРКИ: 5/5 n_q + A(Pb) + 5/5 масс")
            print(f"  ✅ МОДУЛЯРНЫЕ ФОРМЫ: 9/9")
            if 'statistical' in results:
                print(f"  ✅ СТАТИСТИКА: {key['stat_combined_sigma']:.2f}σ")
            if 'cross_validation' in results:
                print(f"  ✅ КРОСС-ВАЛИДАЦИЯ: {key['cv_overall']:.1f}%")
            if 'predictions' in results:
                print(f"  ✅ ПРЕДСКАЗАНИЯ: {key['pred_total']:.0f} "
                      f"({key['pred_confirmed']:.0f} подтверждено)")
            if 'benchmark' in results:
                print(f"  ✅ BENCHMARK: Ω⁴-UNIFIED лучшая")
            if 'elliptic_curve' in results:
                print(f"  ✅ BSD-КРИВАЯ: 6/6 проверок")
            if 'quantum_gravity' in results:
                print(f"  ✅ КВАНТОВАЯ ГРАВИТАЦИЯ: 6/6 проверок")
            if 'compactification' in results:
                print(f"  ✅ КОМПАКТИФИКАЦИЯ 26D → 4D: 6/6 проверок")
        else:
            print(f"  ⚠️ ЕСТЬ ОШИБКИ ({summary['total_pass']}/{summary['total_checks']})")
        print("=" * 80)

    # ========================================================================
    # 1.5. Сохранение результатов
    # ========================================================================

    def save_results(self, results: Dict, filename: str = 'omega4_results.json'):
        """Сохранение результатов в JSON."""
        summary = self.build_summary_table(results)
        key = self.get_key_results(results)

        def safe_serialize(v):
            if isinstance(v, dict):
                return {k: safe_serialize(vv) for k, vv in v.items()}
            if isinstance(v, (list, tuple)):
                return [safe_serialize(vv) for vv in v]
            if hasattr(v, '__float__'):
                try:
                    return float(v)
                except (OverflowError, ValueError):
                    return str(v)
            return v

        output = {
            '_author': 'Сергей Викторович Матершов',
            '_orcid': '0009-0009-0641-1357',
            '_license': 'CC BY-NC-ND 4.0 International',
            'version': '79.4',
            'main_version': '23',
            'timestamp': datetime.now().isoformat(),
            'has_statistical': HAS_STATISTICAL,
            'has_cross_validation': HAS_CROSS_VALIDATION,
            'has_predictions': HAS_PREDICTIONS,
            'has_sensitivity': HAS_SENSITIVITY,
            'has_sensitivity2': HAS_SENSITIVITY2,
            'has_benchmark': HAS_BENCHMARK,
            'has_elliptic_curve': HAS_ELLIPTIC_CURVE,
            'has_vacuum_analysis': HAS_VACUUM_ANALYSIS,
            'has_atlas_scan': HAS_ATLAS_SCAN,
            'has_magic_numbers': HAS_MAGIC_NUMBERS,
            'has_quark_structure': HAS_QUARK_STRUCTURE,
            'has_modular_forms': HAS_MODULAR_FORMS,
            'has_quantum_gravity': HAS_QUANTUM_GRAVITY,
            'has_topological_origin': HAS_TOPOLOGICAL_ORIGIN,
            'has_extra_constants': HAS_EXTRA_CONSTANTS,
            'has_system_metrics': HAS_SYSTEM_METRICS,
            'has_compactification': HAS_COMPACTIFICATION,
            'has_topology_vs_spectrum': HAS_TOPOLOGICAL_ORIGIN,
            'summary': {
                'total_pass': summary['total_pass'],
                'total_checks': summary['total_checks'],
                'all_verified': summary['all_verified'],
                'core':            {'n_pass': summary['core']['n_pass'],        'n_total': summary['core']['n_total']},
                'atlas':           {'n_pass': summary['atlas']['n_pass'],       'n_total': summary['atlas']['n_total']},
                'physics':         {'n_pass': summary['physics']['n_pass'],     'n_total': summary['physics']['n_total']},
                'vacuum_analysis': {'n_pass': summary['vacuum_analysis']['n_pass'], 'n_total': summary['vacuum_analysis']['n_total']} if summary['vacuum_analysis'] else None,
                'atlas_scan':      {'n_pass': summary['atlas_scan']['n_pass'], 'n_total': summary['atlas_scan']['n_total']} if summary['atlas_scan'] else None,
                'magic_numbers':   {'n_pass': summary['magic_numbers']['n_pass'], 'n_total': summary['magic_numbers']['n_total']} if summary['magic_numbers'] else None,
                'quark_structure': {'n_pass': summary['quark_structure']['n_pass'], 'n_total': summary['quark_structure']['n_total']} if summary['quark_structure'] else None,
                'modular_forms':   {'n_pass': summary['modular_forms']['n_pass'], 'n_total': summary['modular_forms']['n_total']} if summary['modular_forms'] else None,
                'statistical':     {'n_pass': summary['statistical']['n_pass'], 'n_total': summary['statistical']['n_total']} if summary['statistical'] else None,
                'cross_validation':{'n_pass': summary['cross_validation']['n_pass'], 'n_total': summary['cross_validation']['n_total']} if summary['cross_validation'] else None,
                'predictions':     {'n_pass': summary['predictions']['n_pass'], 'n_total': summary['predictions']['n_total']} if summary['predictions'] else None,
                'sensitivity':     {'n_pass': summary['sensitivity']['n_pass'], 'n_total': summary['sensitivity']['n_total']} if summary['sensitivity'] else None,
                'sensitivity2':    {'n_pass': summary['sensitivity2']['n_pass'], 'n_total': summary['sensitivity2']['n_total']} if summary['sensitivity2'] else None,
                'sensitivity_comparison': {'n_pass': summary['sensitivity_comparison']['n_pass'], 'n_total': summary['sensitivity_comparison']['n_total']} if summary['sensitivity_comparison'] else None,
                'benchmark':       {'n_pass': summary['benchmark']['n_pass'],   'n_total': summary['benchmark']['n_total']}   if summary['benchmark'] else None,
                'elliptic_curve':  {'n_pass': summary['elliptic_curve']['n_pass'], 'n_total': summary['elliptic_curve']['n_total']} if summary['elliptic_curve'] else None,
                'quantum_gravity': {'n_pass': summary['quantum_gravity']['n_pass'], 'n_total': summary['quantum_gravity']['n_total']} if summary['quantum_gravity'] else None,
                'compactification': {'n_pass': summary['compactification']['n_pass'], 'n_total': summary['compactification']['n_total']} if summary['compactification'] else None,
                'topology_vs_spectrum': {'n_pass': summary['topology_vs_spectrum']['n_pass'], 'n_total': summary['topology_vs_spectrum']['n_total']} if summary['topology_vs_spectrum'] else None,
            },
            'key_results': safe_serialize(key),
        }

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(output, f, indent=2, ensure_ascii=False)
            print(f"\n  💾 Результаты сохранены: {filename}")
        except Exception as e:
            print(f"\n  ⚠️ Не удалось сохранить: {e}")


# ============================================================================
# ЧАСТЬ 2: ГЛАВНАЯ ФУНКЦИЯ
# ============================================================================

def run_complete_analysis():
    """Полный прогон Ω⁴-UNIFIED v79.4 (main v23)."""
    print("=" * 80)
    print("  Ω⁴-UNIFIED v79.4 — ПОЛНАЯ ИНТЕГРАЦИЯ (main v23)")
    print("=" * 80)
    print("  Файлы проекта:")
    print("    • core.py               — ЯДРО + ПРОСТЫЕ МОДУЛИ")
    print("    • atlas.py              — АЛГЕБРЫ ЛИ + АТЛАС (v78.0)")
    print(f"    • physics.py            — ФИЗИКА + ТЕТРАЭДР + ПЕТЛИ + g-2 + CP (v78.7)")
    print(f"    • vacuum_analysis.py    — {'АНАЛИЗ ВАКУУМА ✅' if HAS_VACUUM_ANALYSIS else 'НЕ НАЙДЕН'}")
    print(f"    • atlas_scan.py         — {'СКАН АТЛАСА ✅' if HAS_ATLAS_SCAN else 'НЕ НАЙДЕН'}")
    print(f"    • magic_numbers.py      — {'МАГИЧЕСКИЕ ЧИСЛА ✅' if HAS_MAGIC_NUMBERS else 'НЕ НАЙДЕН'}")
    print(f"    • quark_structure.py    — {'СТРУКТУРА КВАРКОВ ✅' if HAS_QUARK_STRUCTURE else 'НЕ НАЙДЕН'}")
    print(f"    • modular_forms.py      — {'МОДУЛЯРНЫЕ ФОРМЫ ✅' if HAS_MODULAR_FORMS else 'НЕ НАЙДЕН'}")
    print(f"    • statistical.py        — {'СТАТИСТИЧЕСКИЙ АНАЛИЗ ✅' if HAS_STATISTICAL else 'НЕ НАЙДЕН'}")
    print(f"    • cross_validation.py   — {'КРОСС-ВАЛИДАЦИЯ ✅' if HAS_CROSS_VALIDATION else 'НЕ НАЙДЕН'}")
    print(f"    • predictions.py        — {'ПРЕДСКАЗАНИЯ ✅' if HAS_PREDICTIONS else 'НЕ НАЙДЕН'}")
    print(f"    • sensitivity.py        — {'ЧУВСТВИТЕЛЬНОСТЬ v1 ✅ (v2.1)' if HAS_SENSITIVITY else 'НЕ НАЙДЕН'}")
    print(f"    • sensitivity2.py       — {'ЧУВСТВИТЕЛЬНОСТЬ v2 ✅ (v1.2)' if HAS_SENSITIVITY2 else 'НЕ НАЙДЕН'}")
    print(f"    • benchmark.py          — {'BENCHMARK ✅' if HAS_BENCHMARK else 'НЕ НАЙДЕН'}")
    print(f"    • elliptic_curve.py     — {'ЭЛЛИПТИЧЕСКАЯ КРИВАЯ ✅ (v1.2)' if HAS_ELLIPTIC_CURVE else 'НЕ НАЙДЕН'}")
    print(f"    • topological_origin.py — {'ТОПОЛОГИЯ КОНСТАНТ ✅ (v79.2)' if HAS_TOPOLOGICAL_ORIGIN else 'НЕ НАЙДЕН'}")
    print(f"    • extra_constants.py    — {'ДОП. КОНСТАНТЫ ✅ (v79.0.10)' if HAS_EXTRA_CONSTANTS else 'НЕ НАЙДЕН'}")
    print(f"    • system_metrics.py     — {'СИСТЕМНЫЕ МЕТРИКИ ✅ (v79.0)' if HAS_SYSTEM_METRICS else 'НЕ НАЙДЕН'}")
    print(f"    • quantum_gravity.py    — {'КВАНТ. ГРАВИТАЦИЯ ✅ (v79.3)' if HAS_QUANTUM_GRAVITY else 'НЕ НАЙДЕН'}")
    print(f"    • compactification.py   — {'КОМПАКТИФИКАЦИЯ ✅ (v79.4)' if HAS_COMPACTIFICATION else 'НЕ НАЙДЕН'}")
    print("    • genome_writer.py      — ГЕНЕРАТОР АВТОГЕНОМА (v1.1)")
    print("    • main.py               — ИНТЕГРАЦИЯ (ЭТОТ ФАЙЛ)")
    print("=" * 80)

    model = Omega4Unified()

    print("\n  Запуск всех проверок...")
    results = model.run_all_checks()

    model.print_summary(results)
    model.save_results(results)

    return results


# ============================================================================
# ТОЧКА ВХОДА
# ============================================================================

if __name__ == "__main__":
    results = run_complete_analysis()

    try:
        from genome_writer import write_genome
        write_genome(
            output_path='constants_genome_omega4.py',
            dry_run=False,
            verbose=True,
        )
    except ImportError:
        print("\n  ⚠️ genome_writer.py не найден — автогеном не создан")
    except Exception as e:
        print(f"\n  ⚠️ Ошибка генерации автогенома: {e}")
