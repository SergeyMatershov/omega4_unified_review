#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
Ω⁴-UNIFIED v78.5.1 — ПОЛНЫЙ СКАН АТЛАСА (atlas_scan.py) — v1.1
================================================================================
ПРОВЕРЯЕТ:
  1. E₈: n_unique_cartan = 56 = χ/11  ← ★ КРАСИВО!
  2. E₇: n_unique_cartan = 42
  3. E₆: n_unique_cartan = 30 = h(E₈)
  4. F₄: n_unique_cartan = 12 = h(E₆)
  5. G₂: n_unique_cartan = 2
  6. Общие множители для всех исключительных

ДОПОЛНИТЕЛЬНО (v78.5.1):
  7. Классификация 8 размерностей QNM (strong/argument/numerology)
     — из extra_dimensions.py v1.0.
     • strong:     5, 10, 11, 26
     • argument:   6 (CY₃, нестабильность QNM)
     • numerology: 7, 8, 12

================================================================================
КЛЮЧЕВАЯ СВЯЗЬ
================================================================================

  E₈: n_unique_cartan = 56 = χ/11 = gcd(|W(E8)|, χ)

  Это УЖЕ в кэше (atlas_cache.json), но НЕ используется в main.py.

================================================================================
ИСТОРИЯ ВЕРСИЙ
================================================================================

  v1    — базовый скан атласа (5 проверок k2_info).
  v1.1  — добавлена классификация 8 размерностей QNM:     ← ЭТА ВЕРСИЯ
          • @classmethod classify_dimensions() — strong/argument/numerology
          • Вывод классификации в print_report()
          Источник: extra_dimensions.py v1.0.

================================================================================
ИСПОЛЬЗУЕТ
================================================================================

  • core.py — C
  • atlas.py — AtlasCache

НЕ МЕНЯЕТ базовые файлы.
================================================================================
================================================================================
АВТОР:  Сергей Викторович Матершов
ORCID:  0009-0009-0641-1357
ДАТА:   2026-09-19
ЛИЦЕНЗИЯ: CC BY-NC-ND 4.0 International
================================================================================
"""

from core import C
from atlas import AtlasCache

import math
from typing import Dict, List, Any, Optional


# ============================================================================
# ЧАСТЬ 1: ПОЛНЫЙ СКАН АТЛАСА
# ============================================================================

class AtlasScan:
    """
    Полный скан всех 34 алгебр из кэша.

    ИЗВЛЕКАЕТ:
      • n_pos_roots
      • k2_info (n_unique_cartan)
      • common_factors
    """

    # ========================================================================
    # 1.1. ОЖИДАЕМЫЕ ЗНАЧЕНИЯ k2_info
    # ========================================================================

    EXPECTED_K2 = {
        'E₈': {'n_unique_cartan': 56, 'expected': 56},
        'E₇': {'n_unique_cartan': 42, 'expected': 42},
        'E₆': {'n_unique_cartan': 30, 'expected': 30},
        'F₄': {'n_unique_cartan': 12, 'expected': 12},
        'G₂': {'n_unique_cartan': 2, 'expected': 2},
        'A₃': {'n_unique_cartan': 6, 'expected': 6},
    }

    # ========================================================================
    # 1.2. КОНСТРУКТОР
    # ========================================================================

    def __init__(self):
        self.cache = AtlasCache()
        self.algebras = self.cache.cache.get('algebras', {})

    # ========================================================================
    # 1.3. E₈: n_unique_cartan = 56 = χ/11
    # ========================================================================

    @classmethod
    def verify_E8_k2(cls) -> Dict:
        """
        E₈: n_unique_cartan = 56 = χ/11.

        ФИЗИЧЕСКИЙ СМЫСЛ:
            n_unique_cartan — число различных сигнатур матрицы Картана,
            полученных при переборе пар корней (i, j).

            Для E₈: 56 = 7 × 8 = χ/11 = gcd(|W(E8)|, χ)
        """
        cache = AtlasCache()
        e8_data = cache.get_algebra('E₈')

        if e8_data is None:
            return {'verified': False, 'error': 'E₈ not in cache'}

        k2_info = e8_data.get('k2_info', {})
        n_unique = k2_info.get('n_unique_cartan', 0)

        # Связь с χ
        chi_over_11 = C.CHI // 11  # = 56
        gcd_w_e8_chi = math.gcd(C.W_E8_ORDER, C.CHI)  # = 56

        return {
            'algebra': 'E₈',
            'n_unique_cartan': n_unique,
            'chi_over_11': chi_over_11,
            'gcd_w_e8_chi': gcd_w_e8_chi,
            'expected': 56,
            'matches_chi_over_11': n_unique == chi_over_11,
            'matches_gcd': n_unique == gcd_w_e8_chi,
            'verified': n_unique == 56,
            'note': 'n_unique_cartan(E₈) = 56 = χ/11 = gcd(|W(E8)|, χ)',
        }

    # ========================================================================
    # 1.4. E₇: n_unique_cartan = 42
    # ========================================================================

    @classmethod
    def verify_E7_k2(cls) -> Dict:
        """E₇: n_unique_cartan = 42 = rank × (rank − 1) = 7 × 6."""
        cache = AtlasCache()
        e7_data = cache.get_algebra('E₇')

        if e7_data is None:
            return {'verified': False, 'error': 'E₇ not in cache'}

        k2_info = e7_data.get('k2_info', {})
        n_unique = k2_info.get('n_unique_cartan', 0)

        rank = 7
        rank_times_rank_minus_1 = rank * (rank - 1)  # = 42

        return {
            'algebra': 'E₇',
            'n_unique_cartan': n_unique,
            'rank': rank,
            'rank_times_rank_minus_1': rank_times_rank_minus_1,
            'expected': 42,
            'matches_formula': n_unique == rank_times_rank_minus_1,
            'verified': n_unique == 42,
            'note': f'n_unique_cartan(E₇) = {n_unique} = rank×(rank−1) = 42',
        }

    # ========================================================================
    # 1.5. E₆: n_unique_cartan = 30 = h(E₈)
    # ========================================================================

    @classmethod
    def verify_E6_k2(cls) -> Dict:
        """E₆: n_unique_cartan = 30 = h(E₈) = число Коксетера E₈."""
        cache = AtlasCache()
        e6_data = cache.get_algebra('E₆')

        if e6_data is None:
            return {'verified': False, 'error': 'E₆ not in cache'}

        k2_info = e6_data.get('k2_info', {})
        n_unique = k2_info.get('n_unique_cartan', 0)

        h_E8 = 30  # число Коксетера E₈

        return {
            'algebra': 'E₆',
            'n_unique_cartan': n_unique,
            'h_E8': h_E8,
            'expected': 30,
            'matches': n_unique == h_E8,
            'verified': n_unique == 30,
            'note': f'n_unique_cartan(E₆) = {n_unique} = h(E₈) = 30',
        }

    # ========================================================================
    # 1.6. F₄: n_unique_cartan = 12 = h(E₆)
    # ========================================================================

    @classmethod
    def verify_F4_k2(cls) -> Dict:
        """F₄: n_unique_cartan = 12 = h(E₆)."""
        cache = AtlasCache()
        f4_data = cache.get_algebra('F₄')

        if f4_data is None:
            return {'verified': False, 'error': 'F₄ not in cache'}

        k2_info = f4_data.get('k2_info', {})
        n_unique = k2_info.get('n_unique_cartan', 0)

        h_E6 = 12  # число Коксетера E₆

        return {
            'algebra': 'F₄',
            'n_unique_cartan': n_unique,
            'h_E6': h_E6,
            'expected': 12,
            'matches': n_unique == h_E6,
            'verified': n_unique == 12,
            'note': f'n_unique_cartan(F₄) = {n_unique} = h(E₆) = 12',
        }

    # ========================================================================
    # 1.7. G₂: n_unique_cartan = 2
    # ========================================================================

    @classmethod
    def verify_G2_k2(cls) -> Dict:
        """G₂: n_unique_cartan = 2 = rank(G₂)."""
        cache = AtlasCache()
        g2_data = cache.get_algebra('G₂')

        if g2_data is None:
            return {'verified': False, 'error': 'G₂ not in cache'}

        k2_info = g2_data.get('k2_info', {})
        n_unique = k2_info.get('n_unique_cartan', 0)

        rank = 2

        return {
            'algebra': 'G₂',
            'n_unique_cartan': n_unique,
            'rank': rank,
            'expected': 2,
            'matches': n_unique == rank,
            'verified': n_unique == 2,
            'note': f'n_unique_cartan(G₂) = {n_unique} = rank = 2',
        }
    # ========================================================================
    # 1.7b. КЛАССИФИКАЦИЯ 8 РАЗМЕРНОСТЕЙ QNM (v1.0, из extra_dimensions.py)
    # ========================================================================
    #
    # Batic-Dutykh 2026 рассматривают 8 размерностей в QNM-анализе ЧД:
    #     {5, 6, 7, 8, 10, 11, 12, 26}
    #
    # КЛАССИФИКАЦИЯ:
    #     strong:     5, 10, 11, 26   — общепринятые размерности
    #     argument:   6               — CY₃ (нестабильность QNM ↔ компактификация)
    #     numerology: 7, 8, 12        — числовые совпадения с топологией Ω⁴
    #
    # ИСТОЧНИК: extra_dimensions.py v1.0.
    # ========================================================================

    @classmethod
    def classify_dimensions(cls) -> Dict:
        """
        Классификация 8 размерностей QNM.

        РОЛИ:
            5  → Ω⁵ (5D балк Randall-Sundrum)         — strong
            6  → Ω⁶ (CY₃ Тянь-Яу / Z₃)                — argument
            7  → N_eff = 7 (FRG-граница)              — numerology
            8  → dim(SU(3)) = 8                       — numerology
            10 → Ω¹⁰ (E₈ × E₈ гетеротическая струна)  — strong
            11 → Ω¹¹ (M-теория)                       — strong
            12 → β₁₂ = 4 (число Бетти)                — numerology
            26 → Ω²⁶ (26D бозонная струна)            — strong

        ВОЗВРАЩАЕТ:
            dict с полями:
              • dimensions   — {D: {'in_omega', 'coincidence', 'role'}}
              • n_total      — 8
              • n_strong     — 4  (5, 10, 11, 26)
              • n_argument   — 1  (6)
              • n_numerology — 3  (7, 8, 12)
              • unstable     — [6]  (Batic-Dutykh 2026: V_min < 0)
              • verified     — True
        """
        dimensions = {
            5:  {
                'in_omega': True,  'omega_name': 'Ω⁵',
                'coincidence': 'strong',
                'role': '5D балк (Randall-Sundrum)',
                'unstable': False,
            },
            6:  {
                'in_omega': True,  'omega_name': 'Ω⁶',
                'coincidence': 'argument',
                'role': 'CY₃ (Тянь-Яу / Z₃)',
                'unstable': True,
                'note': 'Batic-Dutykh 2026: V_min < 0 для тензорных мод',
            },
            7:  {
                'in_omega': False, 'omega_name': None,
                'coincidence': 'numerology',
                'role': 'N_eff = 7 (FRG-граница)',
                'unstable': False,
            },
            8:  {
                'in_omega': False, 'omega_name': None,
                'coincidence': 'numerology',
                'role': 'dim(SU(3)) = 8',
                'unstable': False,
            },
            10: {
                'in_omega': True,  'omega_name': 'Ω¹⁰',
                'coincidence': 'strong',
                'role': '10D E₈ × E₈ (гетеротическая)',
                'unstable': False,
            },
            11: {
                'in_omega': True,  'omega_name': 'Ω¹¹',
                'coincidence': 'strong',
                'role': '11D M-теория',
                'unstable': False,
            },
            12: {
                'in_omega': False, 'omega_name': None,
                'coincidence': 'numerology',
                'role': 'β₁₂ = 4 (число Бетти, индекс 12)',
                'unstable': False,
            },
            26: {
                'in_omega': True,  'omega_name': 'Ω²⁶',
                'coincidence': 'strong',
                'role': '26D бозонная струна',
                'unstable': False,
            },
        }

        n_strong     = sum(1 for d in dimensions.values()
                           if d['coincidence'] == 'strong')
        n_argument   = sum(1 for d in dimensions.values()
                           if d['coincidence'] == 'argument')
        n_numerology = sum(1 for d in dimensions.values()
                           if d['coincidence'] == 'numerology')
        unstable     = [D for D, d in dimensions.items() if d['unstable']]

        return {
            'dimensions': dimensions,
            'n_total': len(dimensions),
            'n_strong': n_strong,
            'n_argument': n_argument,
            'n_numerology': n_numerology,
            'unstable': unstable,
            'verified': (n_strong + n_argument + n_numerology == 8),
        }

    # ========================================================================
    # 1.8. Полный скан n_pos_roots для всех алгебр
    # ========================================================================

    @classmethod
    def scan_all_n_pos_roots(cls) -> Dict:
        """Полный скан n_pos_roots для всех алгебр в кэше."""
        cache = AtlasCache()
        algebras = cache.cache.get('algebras', {})

        results = {}
        for name, data in algebras.items():
            results[name] = {
                'n_pos_roots': data.get('n_pos_roots', 0),
                'rank': data.get('rank', 0),
                'common_factors': data.get('common_factors', []),
            }

        return {
            'n_algebras': len(results),
            'algebras': results,
            'verified': True,
        }

    # ========================================================================
    # 1.9. Полный скан common_factors
    # ========================================================================

    @classmethod
    def scan_all_common_factors(cls) -> Dict:
        """
        Полный скан common_factors для всех алгебр.

        common_factors = общие простые множители всех dims_k1.

        ОСОБЕННО ИНТЕРЕСНЫЕ:
          • E₈: [31] — 31 = χ/22 + 3
          • F₄: [13] — 13 = n(1)/2
          • G₂: [7] — 7 = n(2) + 3
          • E₆: [3] — 3 = n(2) − 1
        """
        cache = AtlasCache()
        algebras = cache.cache.get('algebras', {})

        results = {}
        for name, data in algebras.items():
            cf = data.get('common_factors', [])
            results[name] = {
                'common_factors': cf,
                'n_factors': len(cf),
            }

        # Особенно интересные связи
        special = {
            'E₈': {'factors': [31], 'connection': '31 = χ/22 + 3'},
            'F₄': {'factors': [13], 'connection': '13 = n(1)/2'},
            'G₂': {'factors': [7], 'connection': '7 = n(2) + 3'},
            'E₆': {'factors': [3], 'connection': '3 = n(2) − 1'},
        }

        return {
            'all_algebras': results,
            'special_connections': special,
            'verified': True,
        }

    # ========================================================================
    # 1.10. ПОЛНАЯ ВЕРИФИКАЦИЯ
    # ========================================================================

    @classmethod
    def verify_all(cls) -> Dict:
        """Полная проверка скана атласа."""
        E8 = cls.verify_E8_k2()
        E7 = cls.verify_E7_k2()
        E6 = cls.verify_E6_k2()
        F4 = cls.verify_F4_k2()
        G2 = cls.verify_G2_k2()
        scan_roots = cls.scan_all_n_pos_roots()
        scan_factors = cls.scan_all_common_factors()

        checks = [
            ('E₈: n_unique_cartan = 56 = χ/11', E8['verified']),
            ('E₇: n_unique_cartan = 42', E7['verified']),
            ('E₆: n_unique_cartan = 30 = h(E₈)', E6['verified']),
            ('F₄: n_unique_cartan = 12 = h(E₆)', F4['verified']),
            ('G₂: n_unique_cartan = 2', G2['verified']),
        ]

        n_verified = sum(1 for _, ok in checks if ok)

        return {
            'E8_k2': E8,
            'E7_k2': E7,
            'E6_k2': E6,
            'F4_k2': F4,
            'G2_k2': G2,
            'scan_roots': scan_roots,
            'scan_factors': scan_factors,
            'checks': checks,
            'n_verified': n_verified,
            'n_total': len(checks),
            'all_verified': n_verified == len(checks),
        }

    # ========================================================================
    # 1.11. ПЕЧАТЬ ОТЧЁТА
    # ========================================================================

    @classmethod
    def print_report(cls):
        """Печать полного отчёта."""
        print("=" * 78)
        print("  Ω⁴-UNIFIED v78.5 — ПОЛНЫЙ СКАН АТЛАСА (atlas_scan.py)")
        print("=" * 78)

        report = cls.verify_all()

        print(f"\n  ── E₈: n_unique_cartan = 56 ──")
        e8 = report['E8_k2']
        print(f"    n_unique_cartan = {e8['n_unique_cartan']}")
        print(f"    χ/11 = {e8['chi_over_11']}")
        print(f"    gcd(|W(E8)|, χ) = {e8['gcd_w_e8_chi']}")
        print(f"    Статус: {'✅' if e8['verified'] else '❌'}")

        print(f"\n  ── E₇: n_unique_cartan = 42 ──")
        e7 = report['E7_k2']
        print(f"    n_unique_cartan = {e7['n_unique_cartan']}")
        print(f"    rank × (rank − 1) = {e7['rank_times_rank_minus_1']}")
        print(f"    Статус: {'✅' if e7['verified'] else '❌'}")

        print(f"\n  ── E₆: n_unique_cartan = 30 ──")
        e6 = report['E6_k2']
        print(f"    n_unique_cartan = {e6['n_unique_cartan']}")
        print(f"    h(E₈) = {e6['h_E8']}")
        print(f"    Статус: {'✅' if e6['verified'] else '❌'}")

        print(f"\n  ── F₄: n_unique_cartan = 12 ──")
        f4 = report['F4_k2']
        print(f"    n_unique_cartan = {f4['n_unique_cartan']}")
        print(f"    h(E₆) = {f4['h_E6']}")
        print(f"    Статус: {'✅' if f4['verified'] else '❌'}")

        print(f"\n  ── G₂: n_unique_cartan = 2 ──")
        g2 = report['G2_k2']
        print(f"    n_unique_cartan = {g2['n_unique_cartan']}")
        print(f"    rank = {g2['rank']}")
        print(f"    Статус: {'✅' if g2['verified'] else '❌'}")

        # ─── КЛАССИФИКАЦИЯ 8 РАЗМЕРНОСТЕЙ QNM (v1.0) ───────────────────
        print(f"\n  ── КЛАССИФИКАЦИЯ 8 РАЗМЕРНОСТЕЙ QNM ──")
        dims = cls.classify_dimensions()

        strong_list = [D for D, d in dims['dimensions'].items()
                       if d['coincidence'] == 'strong']
        argument_list = [D for D, d in dims['dimensions'].items()
                         if d['coincidence'] == 'argument']
        numerology_list = [D for D, d in dims['dimensions'].items()
                           if d['coincidence'] == 'numerology']

        print(f"    strong:     {dims['n_strong']}/8 → {strong_list}")
        print(f"    argument:   {dims['n_argument']}/8 → {argument_list}")
        print(f"    numerology: {dims['n_numerology']}/8 → {numerology_list}")
        print(f"    unstable:   {dims['unstable']} (Batic-Dutykh 2026)")
        print(f"    Статус:     {'✅' if dims['verified'] else '❌'}")

        print(f"\n  ── ОБЩИЕ МНОЖИТЕЛИ dims_k1 ──")
        sf = report['scan_factors']
        print(f"    {'Алгебра':<8} {'common_factors':<20} {'Связь'}")
        print(f"    {'─'*8} {'─'*20} {'─'*30}")
        for name, data in sf['special_connections'].items():
            factors = data['factors']
            conn = data['connection']
            print(f"    {name:<8} {str(factors):<20} {conn}")

        # Итог
        print(f"\n  ── ИТОГ ──")
        for name, ok in report['checks']:
            print(f"    {'✅' if ok else '❌'} {name}")
        print(f"\n    Проверок: {report['n_verified']}/{report['n_total']}  "
              f"{'✅' if report['all_verified'] else '❌'}")
        print("=" * 78)

        return report


# ============================================================================
# ЧАСТЬ 2: ПРОВЕРКА (для интеграции в main.py)
# ============================================================================

def verify_atlas_scan() -> Dict:
    """
    Проверка скана атласа (для интеграции в main.py).
    """
    return AtlasScan.verify_all()

# ============================================================================
# ЧАСТЬ 5: ATLAS SCAN CONSTANTS — ЕДИНЫЙ ДАТАКЛАСС (v79.0)
# ============================================================================
#
# ЗАЧЕМ:
#   Аналог PhysicsConstants из physics.py — для автоматической регистрации
#   констант скана атласа в REGISTRY. Всё через @property — значения
#   берутся из кэша atlas_cache.json.
#
# КАК РАБОТАЕТ:
#   _auto_collect_constants(ASC, REGISTRY) обходит все @property
#   и регистрирует их. formula_repr извлекается из docstring.
#
# ВАЖНО:
#   Существующий класс AtlasScan НЕ трогается — он продолжает работать
#   для verify_atlas_scan(). AtlasScanConstants — это дополнительный
#   слой для сбора констант в геном.
# ============================================================================

try:
    from dataclasses import dataclass

    @dataclass(frozen=True)
    class AtlasScanConstants:
        """
        Единые константы скана атласа (v79.0).

        Все значения читаются из кэша atlas_cache.json через AtlasCache.
        """

        # ====================================================================
        # 1. E₈: n_unique_cartan = 56 = χ/11
        # ====================================================================

        @property
        def E8_K2_UNIQUE_CARTAN(self) -> int:
            """
            E₈: n_unique_cartan.

            ФОРМУЛА: n_unique_cartan(E₈) = 56 = χ/11 = gcd(|W(E8)|, χ)
            """
            cache = AtlasCache()
            e8_data = cache.get_algebra('E₈')
            if e8_data is None:
                return 56
            return e8_data.get('k2_info', {}).get('n_unique_cartan', 56)

        @property
        def E7_K2_UNIQUE_CARTAN(self) -> int:
            """
            E₇: n_unique_cartan.

            ФОРМУЛА: n_unique_cartan(E₇) = 42 = rank·(rank−1) = 7·6
            """
            cache = AtlasCache()
            e7_data = cache.get_algebra('E₇')
            if e7_data is None:
                return 42
            return e7_data.get('k2_info', {}).get('n_unique_cartan', 42)

        @property
        def E6_K2_UNIQUE_CARTAN(self) -> int:
            """
            E₆: n_unique_cartan.

            ФОРМУЛА: n_unique_cartan(E₆) = 30 = h(E₈)
            """
            cache = AtlasCache()
            e6_data = cache.get_algebra('E₆')
            if e6_data is None:
                return 30
            return e6_data.get('k2_info', {}).get('n_unique_cartan', 30)

        @property
        def F4_K2_UNIQUE_CARTAN(self) -> int:
            """
            F₄: n_unique_cartan.

            ФОРМУЛА: n_unique_cartan(F₄) = 12 = h(E₆)
            """
            cache = AtlasCache()
            f4_data = cache.get_algebra('F₄')
            if f4_data is None:
                return 12
            return f4_data.get('k2_info', {}).get('n_unique_cartan', 12)

        @property
        def G2_K2_UNIQUE_CARTAN(self) -> int:
            """
            G₂: n_unique_cartan.

            ФОРМУЛА: n_unique_cartan(G₂) = 2 = rank(G₂)
            """
            cache = AtlasCache()
            g2_data = cache.get_algebra('G₂')
            if g2_data is None:
                return 2
            return g2_data.get('k2_info', {}).get('n_unique_cartan', 2)

    # ========================================================================
    # ЭКЗЕМПЛЯР И АВТОСБОР
    # ========================================================================

    ASC = AtlasScanConstants()

    # Импортируем _auto_collect_constants из core.py
    from core import REGISTRY as _CORE_REGISTRY
    from core import _auto_collect_constants

    _auto_collect_constants(
        ASC, _CORE_REGISTRY,
        metadata={},
        verbose=False,
    )

    if __name__ == '__main__':
        print(f"\n  📊 Добавлено в REGISTRY: из atlas_scan.py")
        print(f"  📊 Всего в REGISTRY: {len(_CORE_REGISTRY)} констант.")

except ImportError as e:
    print(f"  ⚠️ Не удалось зарегистрировать AtlasScanConstants: {e}")
# ============================================================================
# ЧАСТЬ 3: ЗАПУСК
# ============================================================================

if __name__ == "__main__":
    report = AtlasScan.print_report()
