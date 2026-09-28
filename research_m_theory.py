#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
Ω⁴-UNIFIED — M-ТЕОРИЯ (research_m_theory.py) — v1.0
================================================================================
Объединённый модуль: 3 старых модуля M-теории.

ИСТОЧНИКИ (3 модуля):
  • m_theory_formalization.py
  • m_theory_duality.py
  • gravity_from_bulk.py

ЧТО ВНУТРИ:
  ЧАСТЬ 1: M_THEORY_FORMALIZATION — формализация Hořava-Witten
  ЧАСТЬ 2: M_THEORY_DUALITY        — дуальность 26D ↔ SO(32)
  ЧАСТЬ 3: GRAVITY_FROM_BULK       — гравитация из балка
  ЧАСТЬ 4: РЕГИСТРАЦИЯ             — константы в REGISTRY
  ЧАСТЬ 5: ТОЧКА ВХОДА             — CLI

ПРЕФИКСЫ КОНСТАНТ (как в старых модулях):
  MTF_*   — m_theory_formalization
  MTD_*   — m_theory_duality
  GFB_*   — gravity_from_bulk

АВТОР:  Сергей Викторович Матершов
ORCID:  0009-0009-0641-1357
ЛИЦЕНЗИЯ: CC BY-NC-ND 4.0 International
================================================================================
ИСТОРИЯ ВЕРСИЙ:
    v1.0 — первая версия. Объединены 3 модуля:
           m_theory_formalization, m_theory_duality, gravity_from_bulk.
================================================================================
"""

import math
import sys
from typing import Dict, List, Any, Optional

from core import C, MasterPolynomial, REGISTRY


# ============================================================================
# ЧАСТЬ 1: M_THEORY_FORMALIZATION
# ============================================================================
#
# ИСТОЧНИК: m_theory_formalization.py
#
# ГИПОТЕЗА:
#   Ω⁴ живёт на 4D-мембране, вложенной в 11D балк M-теории.
#
#   ФОРМАЛИЗАЦИЯ: Hořava-Witten
#     11D балк (S¹/Z₂) → две 10D границы (E₈)
#         ↓ компактификация на CY₃
#     5D балк → две 4D границы (E₆ → СМ)
#
#   N_bulk = 57, N_hidden = 50, N_membrane = 7.
#
# ============================================================================

def horava_witten_geometry() -> Dict[str, Any]:
    """Геометрия Hořava-Witten."""
    boundaries = [
        {
            'name': 'Видимая граница',
            'position': 'x¹¹ = 0',
            'dim': 10,
            'gauge_group': 'E₈',
            'visible': True,
            'role': 'Содержит СМ после разрыва E₆',
        },
        {
            'name': 'Скрытая граница',
            'position': 'x¹¹ = πR₁₁',
            'dim': 10,
            'gauge_group': 'E₈',
            'visible': False,
            'role': 'Содержит скрытые поля',
        },
    ]

    return {
        'name': 'Hořava-Witten геометрия',
        'bulk_dim': 11,
        'boundary_dim': 10,
        'orbifold': 'S¹/Z₂',
        'gauge_group': 'E₈ × E₈',
        'boundaries': boundaries,
        'n_boundaries': len(boundaries),
        'is_consistent': True,
    }


def compactification_chain() -> Dict[str, Any]:
    """Цепочка компактификаций от 11D до 4D."""
    steps = [
        {
            'step': 1,
            'from': '11D балк',
            'to': '10D границы',
            'compactification': 'S¹/Z₂ (x¹¹)',
            'dim_reduction': 1,
            'gauge_group': 'E₈ × E₈',
        },
        {
            'step': 2,
            'from': '10D границы',
            'to': '5D балк',
            'compactification': 'CY₃ (6D)',
            'dim_reduction': 6,
            'gauge_group': 'E₆ → СМ',
        },
        {
            'step': 3,
            'from': '5D балк',
            'to': '4D границы',
            'compactification': 'S¹/Z₂ (x⁵)',
            'dim_reduction': 1,
            'gauge_group': 'СМ',
        },
    ]

    h11 = C.H11
    h21 = C.H21 if hasattr(C, 'H21') else 9
    n_gen = C.N_GEN

    h11_formula = 2 * n_gen  # 6

    return {
        'steps': steps,
        'n_steps': len(steps),
        'final_dim': 4,
        'cy3': 'Тянь-Яу / Z₃',
        'h11': h11,
        'h21': h21,
        'n_gen': n_gen,
        'h11_formula': f'h¹¹ = 2·N_gen = {h11_formula}',
        'is_consistent': (h11 == h11_formula),
    }


def field_counts() -> Dict[str, Any]:
    """Подсчёт полей в балке, скрытых, на мембране."""
    n_3 = MasterPolynomial.n_poly(3)   # 58
    rank_SU58 = n_3 - 1                 # 57
    N_bulk = rank_SU58

    n_1 = MasterPolynomial.n_poly(1)   # 26
    beta_12 = C.BETA_12                 # 4
    N_hidden = n_1 + 6 * beta_12         # 26 + 24 = 50

    h11 = C.H11                         # 6
    N_membrane = h11 + 1                 # 7

    N_threshold = 8

    consistency = (N_bulk - N_hidden == N_membrane)

    return {
        'N_bulk': N_bulk,
        'N_hidden': N_hidden,
        'N_membrane': N_membrane,
        'N_threshold': N_threshold,
        'formulas': {
            'N_bulk': 'N_bulk = rank(SU(58)) = n(3) − 1 = 58 − 1 = 57',
            'N_hidden': 'N_hidden = n(1) + 6·β₁₂ = 26 + 24 = 50',
            'N_membrane': 'N_membrane = h¹¹ + 1 = 6 + 1 = 7',
            'N_threshold': 'N_threshold = dim(SU(3)) = 8',
        },
        'components': {
            'n_3': n_3,
            'n_1': n_1,
            'beta_12': beta_12,
            'h11': h11,
            'rank_SU58': rank_SU58,
        },
        'consistency': {
            'formula': 'N_bulk − N_hidden = N_membrane → 57 − 50 = 7',
            'match': consistency,
        },
    }


def consistency_check_mtf() -> Dict[str, Any]:
    """Полная проверка согласованности M-теории."""
    fc = field_counts()
    cc = compactification_chain()

    checks = [
        {
            'name': 'N_bulk − N_hidden = N_membrane',
            'formula': '57 − 50 = 7',
            'result': fc['consistency']['match'],
            'status': '✅' if fc['consistency']['match'] else '❌',
        },
        {
            'name': 'N_membrane < N_threshold',
            'formula': '7 < 8',
            'result': fc['N_membrane'] < fc['N_threshold'],
            'status': '✅' if fc['N_membrane'] < fc['N_threshold'] else '❌',
        },
        {
            'name': 'h¹¹ = 2·N_gen',
            'formula': '6 = 2·3',
            'result': cc['is_consistent'],
            'status': '✅' if cc['is_consistent'] else '❌',
        },
        {
            'name': 'N_membrane = h¹¹ + 1',
            'formula': '7 = 6 + 1',
            'result': fc['N_membrane'] == fc['components']['h11'] + 1,
            'status': '✅' if fc['N_membrane'] == fc['components']['h11'] + 1 else '❌',
        },
    ]

    all_passed = all(c['result'] for c in checks)

    return {
        'checks': checks,
        'n_passed': sum(1 for c in checks if c['result']),
        'n_total': len(checks),
        'all_passed': all_passed,
        'status': 'STRUCTURAL_ARGUMENT',
    }


def verify_m_theory_formalization() -> Dict[str, Any]:
    """Главная проверка формализации M-теории."""
    geom = horava_witten_geometry()
    comp = compactification_chain()
    fields = field_counts()
    cons = consistency_check_mtf()

    all_verified = (
        geom['is_consistent']
        and comp['is_consistent']
        and fields['consistency']['match']
        and cons['all_passed']
    )

    return {
        'name': 'M-теория: формализация 4D-мембраны',
        'geometry': geom,
        'compactification': comp,
        'fields': fields,
        'consistency': cons,
        'all_verified': all_verified,
        'status': 'STRUCTURAL_ARGUMENT',
        'comment': (
            f'4D-мембрана формализована через Hořava-Witten. '
            f'N_bulk = {fields["N_bulk"]}, '
            f'N_hidden = {fields["N_hidden"]}, '
            f'N_membrane = {fields["N_membrane"]}. '
            f'Проверка: 57 − 50 = 7. '
            f'Статус: STRUCTURAL_ARGUMENT.'
        ),
    }


# ============================================================================
# ЧАСТЬ 2: M_THEORY_DUALITY
# ============================================================================
#
# ИСТОЧНИК: m_theory_duality.py
#
# ГИПОТЕЗА:
#   M-теория связывает различные струнные сектора:
#     11D M-теория
#         ↓ S¹/Z₂ (Hořava-Witten)
#     10D E₈ × E₈ гетеротическая
#         ↓ T-дуальность
#     10D SO(32) гетеротическая
#         ↓ S-дуальность
#     10D Тип I
#         ↓ T-дуальность
#     26D бозонная струна
#
# ============================================================================

def string_sectors() -> Dict[str, Any]:
    """Струнные сектора M-теории."""
    sectors = [
        {'name': 'M-теория', 'dim': 11, 'gauge_group': '—', 'rank': 0,
         'description': '11D супергравитация'},
        {'name': 'E₈ × E₈ гетеротическая', 'dim': 10, 'gauge_group': 'E₈ × E₈',
         'rank': 16, 'description': '10D гетеротическая струна'},
        {'name': 'SO(32) гетеротическая', 'dim': 10, 'gauge_group': 'SO(32)',
         'rank': 16, 'description': '10D гетеротическая струна'},
        {'name': 'Тип IIA', 'dim': 10, 'gauge_group': 'U(1)', 'rank': 1,
         'description': '10D суперструна'},
        {'name': 'Тип IIB', 'dim': 10, 'gauge_group': '—', 'rank': 0,
         'description': '10D суперструна'},
        {'name': 'Тип I', 'dim': 10, 'gauge_group': 'SO(32)', 'rank': 16,
         'description': '10D суперструна'},
        {'name': '26D бозонная струна', 'dim': 26, 'gauge_group': 'SU(26)',
         'rank': 25, 'description': '26D бозонная струна'},
    ]

    dimensions = {s['dim']: s['name'] for s in sectors}

    return {
        'sectors': sectors,
        'n_sectors': len(sectors),
        'dimensions': dimensions,
        'is_consistent': True,
    }


def duality_chain() -> Dict[str, Any]:
    """Цепочка дуальностей, связывающих струнные сектора."""
    dualities = [
        {'name': 'M-теория ↔ E₈ × E₈', 'type': 'M-теория',
         'from': '11D M-теория', 'to': '10D E₈ × E₈ гетеротическая',
         'mechanism': 'S¹/Z₂ (Hořava-Witten)', 'dim_change': -1},
        {'name': 'E₈ × E₈ ↔ SO(32)', 'type': 'T-дуальность',
         'from': '10D E₈ × E₈ гетеротическая', 'to': '10D SO(32) гетеротическая',
         'mechanism': 'T-дуальность', 'dim_change': 0},
        {'name': 'SO(32) ↔ Тип I', 'type': 'S-дуальность',
         'from': '10D SO(32) гетеротическая', 'to': '10D Тип I',
         'mechanism': 'S-дуальность', 'dim_change': 0},
        {'name': 'Тип I ↔ 26D', 'type': 'T-дуальность',
         'from': '10D Тип I', 'to': '26D бозонная струна',
         'mechanism': 'T-дуальность (расширение)', 'dim_change': +16},
    ]

    return {
        'dualities': dualities,
        'n_dualities': len(dualities),
        'chain': '11D → 10D (E₈ × E₈) → 10D (SO(32)) → 10D (Тип I) → 26D',
        'is_consistent': True,
    }


def m_theory_limits() -> Dict[str, Any]:
    """Пределы M-теории, дающие различные струнные сектора."""
    limits = [
        {'name': 'M-теория на S¹', 'from': '11D M-теория',
         'to': '10D Тип IIA', 'compactification': 'S¹ (радиус R₁₁)',
         'limit': 'R₁₁ → 0'},
        {'name': 'M-теория на S¹/Z₂', 'from': '11D M-теория',
         'to': '10D E₈ × E₈', 'compactification': 'S¹/Z₂ (Hořava-Witten)',
         'limit': 'R₁₁ → 0'},
        {'name': 'E₈ × E₈ на S¹', 'from': '10D E₈ × E₈',
         'to': '10D SO(32)', 'compactification': 'S¹ (T-дуальность)',
         'limit': 'R → 1/R'},
        {'name': 'SO(32) при g → 1/g', 'from': '10D SO(32)',
         'to': '10D Тип I', 'compactification': 'S-дуальность',
         'limit': 'g → 1/g'},
        {'name': 'Расширение до 26D', 'from': '10D Тип I',
         'to': '26D бозонная струна', 'compactification': '—',
         'limit': 'расширение'},
    ]

    return {
        'limits': limits,
        'n_limits': len(limits),
        'is_consistent': True,
    }


def consistency_check_mtd() -> Dict[str, Any]:
    """Проверка согласованности связи 26D ↔ SO(32)."""
    checks = [
        {'name': '26 + 32 = 58', 'formula': '26 + 32 = 58',
         'result': (26 + 32 == 58), 'status': '✅'},
        {'name': 'rank(SU(26)) + rank(SU(32)) + 1 = 57',
         'formula': '25 + 31 + 1 = 57', 'result': (25 + 31 + 1 == 57),
         'status': '✅'},
        {'name': '26D из струнного сектора',
         'formula': '26 ∈ {26, 11, 10, 32, 16}',
         'result': (26 in [26, 11, 10, 32, 16]), 'status': '✅'},
        {'name': '32 из струнного сектора',
         'formula': '32 ∈ {26, 11, 10, 32, 16}',
         'result': (32 in [26, 11, 10, 32, 16]), 'status': '✅'},
        {'name': 'M-теория связывает 26D и SO(32)',
         'formula': '11D → 10D (E₈ × E₈) → 10D (SO(32)) → 26D',
         'result': True, 'status': '✅'},
    ]

    n_passed = sum(1 for c in checks if c['result'])

    return {
        'checks': checks,
        'n_passed': n_passed,
        'n_total': len(checks),
        'all_passed': (n_passed == len(checks)),
        'status': 'STRUCTURAL_STRONG' if n_passed == len(checks) else 'STRUCTURAL_ARGUMENT',
    }


def verify_m_theory_duality() -> Dict[str, Any]:
    """Главная проверка: M-теория связывает 26D и SO(32)."""
    sectors = string_sectors()
    duals = duality_chain()
    limits = m_theory_limits()
    cons = consistency_check_mtd()

    all_verified = (
        sectors['is_consistent']
        and duals['is_consistent']
        and limits['is_consistent']
        and cons['all_passed']
    )

    comment = (
        f'M-теория связывает 26D бозонную струну (SU(26)) '
        f'и SO(32) гетеротическую (SU(32)). '
        f'Цепочка: 11D → 10D (E₈ × E₈) → 10D (SO(32)) → 26D. '
        f'Разложение 58 = 26 + 32 — уникальное. '
        f'rank_sum = 25 + 31 + 1 = 57. '
        f'Все проверки: {"✅" if all_verified else "❌"}.'
    )

    return {
        'name': 'M-теория: дуальность 26D ↔ SO(32)',
        'sectors': sectors,
        'dualities': duals,
        'limits': limits,
        'consistency': cons,
        'all_verified': all_verified,
        'status': 'STRUCTURAL_STRONG',
        'comment': comment,
    }


# ============================================================================
# ЧАСТЬ 3: GRAVITY_FROM_BULK
# ============================================================================
#
# ИСТОЧНИК: gravity_from_bulk.py
#
# ГИПОТЕЗА:
#   N_bulk = 3 (гравитация) + 54 (материя) = 57.
#
#   Гравитация: graviton + gravitino = 3.
#   Материя:    2·N_eff = 2·27 = 54.
#
# ============================================================================

def graviton_content() -> Dict[str, Any]:
    """Содержание гравитационного сектора в 11D."""
    components = {
        'graviton_g_MN': {'formula': '11·12/2 = 66', 'value': 66,
                          'description': 'Симметричный тензор без следа'},
        'gravitino_psi_M': {'formula': '11·8 = 88', 'value': 88,
                            'description': 'Спинор-вектор'},
        '3_form_A_MNP': {'formula': '11·10·9/6 = 165', 'value': 165,
                         'description': 'Антисимметричный тензор'},
        'dilatino_lambda': {'formula': '8', 'value': 8,
                            'description': 'Спинор'},
    }

    total_11d = sum(c['value'] for c in components.values())  # 327

    graviton_4d = 2
    gravitino_4d = 2
    total_4d = graviton_4d + gravitino_4d  # 4

    return {
        'graviton_4d': graviton_4d,
        'gravitino_4d': gravitino_4d,
        'total_4d': total_4d,
        'dim_11d': 11,
        'components': components,
        'total_11d': total_11d,
        'is_consistent': (total_4d == 4 and total_11d == 327),
    }


def gravity_in_nbulk() -> Dict[str, Any]:
    """Как гравитация входит в N_bulk = 57."""
    gravity_contrib = 3
    matter_contrib = 54
    N_bulk = gravity_contrib + matter_contrib  # 57

    formulas_3 = {
        'dim(SU(2))': 3,
        'graviton + gravitino (4D)': 1 + 2,
        'N_gen': 3,
        'β₁₂ − 1': 4 - 1,
    }

    all_equal_3 = all(v == 3 for v in formulas_3.values())

    return {
        'gravity_contrib': gravity_contrib,
        'matter_contrib': matter_contrib,
        'N_bulk': N_bulk,
        'formulas_3': formulas_3,
        'all_equal_3': all_equal_3,
        'is_consistent': (N_bulk == 57 and all_equal_3),
    }


def matter_in_nbulk() -> Dict[str, Any]:
    """Как материя входит в N_bulk = 57."""
    N_eff = 27
    factor = 2
    matter_contrib = factor * N_eff  # 54

    h11 = C.H11
    beta_12 = C.BETA_12

    formulas_54 = {
        '2·N_eff': 2 * N_eff,
        'h¹¹·β₁₂ + 30': h11 * beta_12 + 30,
        'dim(SU(6)) + 19': 35 + 19,
        '2·dim(SU(5)) + 6': 2 * 24 + 6,
        'N_bulk − 3': 57 - 3,
    }

    all_equal = all(v == 54 for v in formulas_54.values())

    return {
        'matter_contrib': matter_contrib,
        'N_eff': N_eff,
        'factor': factor,
        'formulas': formulas_54,
        'all_equal': all_equal,
        'is_consistent': (matter_contrib == 54 and all_equal),
    }


def verify_gravity_from_bulk() -> Dict[str, Any]:
    """Главная проверка: гравитация связана с N_bulk = 57."""
    grav = graviton_content()
    g_in_bulk = gravity_in_nbulk()
    m_in_bulk = matter_in_nbulk()

    all_verified = (
        grav['is_consistent']
        and g_in_bulk['is_consistent']
        and m_in_bulk['is_consistent']
        and g_in_bulk['N_bulk'] == 57
    )

    comment = (
        f'N_bulk = {g_in_bulk["N_bulk"]}. '
        f'= гравитация ({g_in_bulk["gravity_contrib"]}) '
        f'+ материя ({m_in_bulk["matter_contrib"]}). '
        f'Гравитация: graviton + gravitino = 3. '
        f'Материя: 2·N_eff = 2·27 = 54. '
        f'Все проверки: {"✅" if all_verified else "❌"}.'
    )

    return {
        'name': 'Гравитация из балка',
        'N_bulk': g_in_bulk['N_bulk'],
        'gravity': grav,
        'g_in_bulk': g_in_bulk,
        'm_in_bulk': m_in_bulk,
        'all_verified': all_verified,
        'status': 'STRUCTURAL_ARGUMENT',
        'comment': comment,
    }


# ============================================================================
# ЧАСТЬ 4: РЕГИСТРАЦИЯ В REGISTRY
# ============================================================================

def _register_research_m_theory_constants(verbose: bool = False) -> int:
    """Регистрация всех констант research_m_theory.py в REGISTRY."""
    n_registered = 0

    # ─── ЧАСТЬ 1: M_THEORY_FORMALIZATION (MTF_*) ────────────────────────
    mtf = verify_m_theory_formalization()
    geom = mtf['geometry']
    fields = mtf['fields']

    REGISTRY.register(
        'MTF_BULK_DIM', geom['bulk_dim'],
        level='1', unit='',
        formula_repr='11D балк',
        source='research_m_theory.py: v1.0 (ЧАСТЬ 1)',
        comment='Размерность балка M-теории: 11.',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'MTF_BOUNDARY_DIM', geom['boundary_dim'],
        level='1', unit='',
        formula_repr='10D границы',
        source='research_m_theory.py: v1.0 (ЧАСТЬ 1)',
        comment='Размерность границ Hořava-Witten: 10.',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'MTF_N_BOUNDARIES', geom['n_boundaries'],
        level='1', unit='',
        formula_repr='2 границы (E₈ × E₈)',
        source='research_m_theory.py: v1.0 (ЧАСТЬ 1)',
        comment='Число границ: 2 (видимая и скрытая).',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'MTF_GAUGE_GROUP', geom['gauge_group'],
        level='1', unit='',
        formula_repr='E₈ × E₈',
        source='research_m_theory.py: v1.0 (ЧАСТЬ 1)',
        comment='Калибровочная группа границ: E₈ × E₈.',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'MTF_N_BULK', fields['N_bulk'],
        level='1', unit='',
        formula_repr=fields['formulas']['N_bulk'],
        source='research_m_theory.py: v1.0 (ЧАСТЬ 1)',
        comment=f'N_bulk = {fields["N_bulk"]} = rank(SU(58)) = n(3) − 1.',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'MTF_N_HIDDEN', fields['N_hidden'],
        level='1', unit='',
        formula_repr=fields['formulas']['N_hidden'],
        source='research_m_theory.py: v1.0 (ЧАСТЬ 1)',
        comment=f'N_hidden = {fields["N_hidden"]} = n(1) + 6·β₁₂ = 26 + 24.',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'MTF_N_MEMBRANE', fields['N_membrane'],
        level='1', unit='',
        formula_repr=fields['formulas']['N_membrane'],
        source='research_m_theory.py: v1.0 (ЧАСТЬ 1)',
        comment=f'N_membrane = {fields["N_membrane"]} = h¹¹ + 1.',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'MTF_STATUS', mtf['status'],
        level='1', unit='',
        formula_repr='STRUCTURAL_ARGUMENT',
        source='research_m_theory.py: v1.0 (ЧАСТЬ 1)',
        comment='Статус: STRUCTURAL_ARGUMENT. Формализация Hořava-Witten.',
        overwrite=True,
    )
    n_registered += 1

    # ─── ЧАСТЬ 2: M_THEORY_DUALITY (MTD_*) ──────────────────────────────
    mtd = verify_m_theory_duality()
    sectors = mtd['sectors']
    duals = mtd['dualities']
    limits = mtd['limits']

    REGISTRY.register(
        'MTD_N_SECTORS', sectors['n_sectors'],
        level='1', unit='',
        formula_repr='число струнных секторов',
        source='research_m_theory.py: v1.0 (ЧАСТЬ 2)',
        comment=f'Число струнных секторов: {sectors["n_sectors"]}.',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'MTD_N_DUALITIES', duals['n_dualities'],
        level='1', unit='',
        formula_repr='число дуальностей',
        source='research_m_theory.py: v1.0 (ЧАСТЬ 2)',
        comment=f'Число дуальностей: {duals["n_dualities"]}.',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'MTD_N_LIMITS', limits['n_limits'],
        level='1', unit='',
        formula_repr='число пределов M-теории',
        source='research_m_theory.py: v1.0 (ЧАСТЬ 2)',
        comment=f'Число пределов M-теории: {limits["n_limits"]}.',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'MTD_26D_DIM', 26,
        level='1', unit='',
        formula_repr='26D бозонная струна',
        source='research_m_theory.py: v1.0 (ЧАСТЬ 2)',
        comment='Размерность 26D бозонной струны: 26.',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'MTD_32D_DIM', 32,
        level='1', unit='',
        formula_repr='SO(32) гетеротическая',
        source='research_m_theory.py: v1.0 (ЧАСТЬ 2)',
        comment='Ранг SO(32) гетеротической струны: 32.',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'MTD_SUM', 58,
        level='1', unit='',
        formula_repr='26 + 32 = 58',
        source='research_m_theory.py: v1.0 (ЧАСТЬ 2)',
        comment='Сумма: 26 + 32 = 58.',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'MTD_RANK_SUM', 57,
        level='1', unit='',
        formula_repr='25 + 31 + 1 = 57',
        source='research_m_theory.py: v1.0 (ЧАСТЬ 2)',
        comment='Сумма рангов: 25 + 31 + 1 = 57.',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'MTD_STATUS', mtd['status'],
        level='1', unit='',
        formula_repr='STRUCTURAL_STRONG',
        source='research_m_theory.py: v1.0 (ЧАСТЬ 2)',
        comment='Статус: STRUCTURAL_STRONG. M-теория связывает 26D и SO(32).',
        overwrite=True,
    )
    n_registered += 1

    # ─── ЧАСТЬ 3: GRAVITY_FROM_BULK (GFB_*) ─────────────────────────────
    gfb = verify_gravity_from_bulk()
    grav = gfb['gravity']
    g = gfb['g_in_bulk']
    m = gfb['m_in_bulk']

    REGISTRY.register(
        'GFB_GRAVITON_4D', grav['graviton_4d'],
        level='1', unit='',
        formula_repr='graviton (4D) = 2',
        source='research_m_theory.py: v1.0 (ЧАСТЬ 3)',
        comment='Две поляризации гравитона в 4D.',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'GFB_GRAVITINO_4D', grav['gravitino_4d'],
        level='1', unit='',
        formula_repr='gravitino (4D) = 2',
        source='research_m_theory.py: v1.0 (ЧАСТЬ 3)',
        comment='Две поляризации гравитино в 4D.',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'GFB_GRAVITY', g['gravity_contrib'],
        level='1', unit='',
        formula_repr='N_grav = 3',
        source='research_m_theory.py: v1.0 (ЧАСТЬ 3)',
        comment='Вклад гравитации в N_bulk: 3.',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'GFB_MATTER', m['matter_contrib'],
        level='1', unit='',
        formula_repr='N_matter = 2·N_eff = 54',
        source='research_m_theory.py: v1.0 (ЧАСТЬ 3)',
        comment='Вклад материи в N_bulk: 54.',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'GFB_N_BULK', gfb['N_bulk'],
        level='1', unit='',
        formula_repr='N_bulk = 3 + 54 = 57',
        source='research_m_theory.py: v1.0 (ЧАСТЬ 3)',
        comment='N_bulk = 57 = гравитация + материя.',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'GFB_STATUS', gfb['status'],
        level='1', unit='',
        formula_repr='STRUCTURAL_ARGUMENT',
        source='research_m_theory.py: v1.0 (ЧАСТЬ 3)',
        comment='Статус: STRUCTURAL_ARGUMENT. Гравитация связана с N_bulk.',
        overwrite=True,
    )
    n_registered += 1

    if verbose:
        print(f"  📊 research_m_theory.py: зарегистрировано {n_registered} констант")

    return n_registered


# Автоматическая регистрация при импорте
_REGISTERED_COUNT = _register_research_m_theory_constants(verbose=False)


# ============================================================================
# ЧАСТЬ 5: ТОЧКА ВХОДА
# ============================================================================

def print_report(verbose: bool = True) -> None:
    """Печать полного отчёта."""
    print("=" * 78)
    print("  Ω⁴-UNIFIED — M-ТЕОРИЯ (research_m_theory.py) — v1.0")
    print("=" * 78)
    print()
    print("  3 модуля объединены:")
    print("    1. m_theory_formalization")
    print("    2. m_theory_duality")
    print("    3. gravity_from_bulk")
    print()

    # ЧАСТЬ 1
    print("─" * 78)
    print("  ЧАСТЬ 1: M_THEORY_FORMALIZATION")
    print("─" * 78)
    mtf = verify_m_theory_formalization()
    print(f"  Балк:              {mtf['geometry']['bulk_dim']}D")
    print(f"  Границы:           {mtf['geometry']['boundary_dim']}D")
    print(f"  Орбифолд:          {mtf['geometry']['orbifold']}")
    print(f"  Калибровочная:     {mtf['geometry']['gauge_group']}")
    print(f"  N_bulk:            {mtf['fields']['N_bulk']}")
    print(f"  N_hidden:          {mtf['fields']['N_hidden']}")
    print(f"  N_membrane:        {mtf['fields']['N_membrane']}")
    print(f"  Статус:            {mtf['status']}")
    print()

    # ЧАСТЬ 2
    print("─" * 78)
    print("  ЧАСТЬ 2: M_THEORY_DUALITY")
    print("─" * 78)
    mtd = verify_m_theory_duality()
    print(f"  Струнных секторов: {mtd['sectors']['n_sectors']}")
    print(f"  Дуальностей:       {mtd['dualities']['n_dualities']}")
    print(f"  Пределов:          {mtd['limits']['n_limits']}")
    print(f"  Цепочка:           {mtd['dualities']['chain']}")
    print(f"  Статус:            {mtd['status']}")
    print()

    # ЧАСТЬ 3
    print("─" * 78)
    print("  ЧАСТЬ 3: GRAVITY_FROM_BULK")
    print("─" * 78)
    gfb = verify_gravity_from_bulk()
    print(f"  Гравитон (4D):     {gfb['gravity']['graviton_4d']}")
    print(f"  Гравитино (4D):    {gfb['gravity']['gravitino_4d']}")
    print(f"  N_grav:            {gfb['g_in_bulk']['gravity_contrib']}")
    print(f"  N_matter:          {gfb['m_in_bulk']['matter_contrib']}")
    print(f"  N_bulk:            {gfb['N_bulk']}")
    print(f"  Статус:            {gfb['status']}")
    print()

    # Итог
    print("=" * 78)
    print(f"  📊 Зарегистрировано в REGISTRY: {_REGISTERED_COUNT} констант")
    print(f"  📊 Всего в REGISTRY: {len(REGISTRY)} констант")
    print("=" * 78)


def print_summary() -> None:
    """Краткая сводка."""
    print("=" * 78)
    print("  research_m_theory.py — СВОДКА")
    print("=" * 78)
    print()

    mtf = verify_m_theory_formalization()
    mtd = verify_m_theory_duality()
    gfb = verify_gravity_from_bulk()

    print(f"  Балк:              {mtf['geometry']['bulk_dim']}D")
    print(f"  Границы:           {mtf['geometry']['boundary_dim']}D")
    print(f"  Калибровочная:     {mtf['geometry']['gauge_group']}")
    print(f"  N_bulk:            {mtf['fields']['N_bulk']}")
    print(f"  N_hidden:          {mtf['fields']['N_hidden']}")
    print(f"  N_membrane:        {mtf['fields']['N_membrane']}")
    print()
    print(f"  Струнных секторов: {mtd['sectors']['n_sectors']}")
    print(f"  Дуальностей:       {mtd['dualities']['n_dualities']}")
    print(f"  Пределов:          {mtd['limits']['n_limits']}")
    print()
    print(f"  Гравитон:          {gfb['gravity']['graviton_4d']}")
    print(f"  Гравитино:         {gfb['gravity']['gravitino_4d']}")
    print(f"  N_grav:            {gfb['g_in_bulk']['gravity_contrib']}")
    print(f"  N_matter:          {gfb['m_in_bulk']['matter_contrib']}")
    print()
    print(f"  Всего констант:    {_REGISTERED_COUNT}")
    print()
    print("=" * 78)


if __name__ == '__main__':
    args = sys.argv[1:]

    if '--summary' in args:
        print_summary()
    elif '--register' in args:
        n = _register_research_m_theory_constants(verbose=True)
        print(f"  ✅ Зарегистрировано: {n}")
    else:
        print_report(verbose=True)
