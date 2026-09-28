#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
Ω⁴-UNIFIED v78.1 — СТРУКТУРА КВАРКОВ (quark_structure.py) — v1
================================================================================
НОВЫЙ МОДУЛЬ (наращивание). НЕ меняет базовые файлы.

================================================================================
ЧТО ДЕЛАЕТ
================================================================================

Проверяет, что n_q (спектральный индекс кварка) выводится из n(k),
и что массы кварков выражаются через ε_FN^(-n_q/4).

================================================================================
СВЯЗИ n_q С n(k)
================================================================================

  d: n_q = N_gen           = 3
  s: n_q = n(1)/2          = 13
  c: n_q = n(1) − n(2)     = 22
  b: n_q = n(1)            = 26
  t: n_q = n(1) + n(1)/2   = 39

================================================================================
КЛЮЧЕВАЯ СВЯЗЬ
================================================================================

  b-кварк:
    n_q · dim(SU(3)) = 26 · 8 = 208 = A(Pb)
    
  ГДЕ:
    A(Pb) = β₁₂ · dim(F₄) = 4 · 52 = 208
    208 — массовое число Pb-208 (дважды магическое ядро)

  ЭТО СВЯЗЫВАЕТ:
    • Кварковую структуру (b-кварк)
    • Размерности групп Ли (SU(3))
    • Ядерную физику (Pb-208)
    • Числа Бетти (β₁₂)
    • Исключительные алгебры (F₄)

================================================================================
ФОРМУЛА ДЛЯ МАСС
================================================================================

  M_q/M_u = ε_FN^(-n_q/4)

  ПРИМЕРЫ:
    M_d/M_u = ε_FN^(-3/4)  = 2.367  (эксп: 2.162, откл. 9.46%)
    M_s/M_u = ε_FN^(-13/4) = 41.80  (эксп: 43.06, откл. 2.91%)
    M_c/M_u = ε_FN^(-22/4) = 554.1  (эксп: 587.9, откл. 5.77%)
    M_b/M_u = ε_FN^(-26/4) = 1747.4 (эксп: 1935.2, откл. 9.70%)
    M_t/M_u = ε_FN^(-39/4) = 73043  (эксп: 79981, откл. 8.67%)

================================================================================
ИСТОЧНИК
================================================================================

  Из Ω⁴-UNIFIED COMPLETE v18.1:
    class QuarkStructure:
        N_Q = {'d': 3, 's': 13, 'c': 22, 'b': 26, 't': 39}
        ...5 связей n_q с n(k), ключевая b ↔ A(Pb)

================================================================================
ИСПОЛЬЗУЕТ
================================================================================

  • core.py — C, MasterPolynomial, LieGroupDimensions

НЕ МЕНЯЕТ базовые файлы.
================================================================================
================================================================================
АВТОР:  Сергей Викторович Матершов
ORCID:  0009-0009-0641-1357
ДАТА:   2026-09-19
ЛИЦЕНЗИЯ: CC BY-NC-ND 4.0 International
================================================================================
"""

from core import (
    C, MasterPolynomial, LieGroupDimensions,
)

import math
from typing import Dict, List, Any, Optional


# ============================================================================
# ЧАСТЬ 1: СТРУКТУРА КВАРКОВ
# ============================================================================

class QuarkStructure:
    """
    Кварки через n_q из n(k).
    
    ★ ОБНОВЛЕНО v79.1 (проблема 5):
    
    ФОРМУЛА:
        M_q/M_u = ε_FN^(-n_q'/4)
    
    ГДЕ n_q' — скорректированные индексы:
        d: n_d' = N_gen − ε_FN = 3 − ε_FN = 2.68292
        s: n_s' = n_s · (1 + ε_FN/40) = 13 · 1.007927 = 13.10305
        c: n_c' = n_c · (1 + ε_FN/40) = 22 · 1.007927 = 22.17440
        b: n_b' = n_b · (1 + ε_FN/40) + ε_FN/2 = 26.36459
        t: n_t' = n_t · (1 + ε_FN/40) = 39 · 1.007927 = 39.30915
    
    ОТКЛОНЕНИЯ (было → стало):
        d: 9.46% → 0.065%  (в 145×)
        s: 2.91% → 0.004%  (в 728×)
        c: 5.77% → 0.93%   (в 6.2×)
        b: 9.70% → 0.26%   (в 37×)
        t: 8.67% → 0.20%   (в 43×)
        Среднее: 7.30% → 0.29% (в 25×)
    
    ФИЗИЧЕСКИЙ СМЫСЛ:
        ε_FN/40 = ε_FN/(β₁₂·T_CY3) — топологический фактор CY₃.
        ε_FN/2 — спиновая поправка для b-кварка.
        N_gen − ε_FN — особая формула для d-кварка.
    """
    
    # Базовые n_q (из master polynomial)
    N_Q: Dict[str, int] = {
        'd': 3,
        's': 13,
        'c': 22,
        'b': 26,
        't': 39,
    }
    
    # Топологический фактор CY₃
    BETA_12 = 4
    T_CY3 = 10
    CY3_FACTOR = BETA_12 * T_CY3  # = 40
    
    # Экспериментальные массы (МэВ)
    M_EXP: Dict[str, float] = {
        'd': 4.67,
        's': 93.0,
        'c': 1270.0,
        'b': 4180.0,
        't': 172760.0,
    }
    
    # Масса u-кварка (эталон)
    M_U: float = 2.16  # МэВ
    
    # ========================================================================
    # 1.1. Проверка n_q через n(k)
    # ========================================================================
    
    @classmethod
    def verify_nq_d(cls) -> Dict:
        """d: n_q = N_gen = 3."""
        computed = C.N_GEN
        expected = cls.N_Q['d']
        
        return {
            'quark': 'd',
            'formula': 'N_gen',
            'computed': computed,
            'expected': expected,
            'verified': computed == expected,
            'note': f'N_gen = {computed}',
        }
    
    @classmethod
    def verify_nq_s(cls) -> Dict:
        """s: n_q = n(1)/2 = 13."""
        n_1 = MasterPolynomial.n_poly(1)  # 26
        computed = n_1 // 2
        expected = cls.N_Q['s']
        
        return {
            'quark': 's',
            'formula': 'n(1)/2',
            'computed': computed,
            'expected': expected,
            'verified': computed == expected,
            'note': f'n(1)/2 = {n_1}/2 = {computed}',
        }
    
    @classmethod
    def verify_nq_c(cls) -> Dict:
        """c: n_q = n(1) − n(2) = 22."""
        n_1 = MasterPolynomial.n_poly(1)  # 26
        n_2 = MasterPolynomial.n_poly(2)  # 4
        computed = n_1 - n_2
        expected = cls.N_Q['c']
        
        return {
            'quark': 'c',
            'formula': 'n(1) − n(2)',
            'computed': computed,
            'expected': expected,
            'verified': computed == expected,
            'note': f'n(1) − n(2) = {n_1} − {n_2} = {computed}',
        }
    
    @classmethod
    def verify_nq_b(cls) -> Dict:
        """b: n_q = n(1) = 26."""
        n_1 = MasterPolynomial.n_poly(1)  # 26
        computed = n_1
        expected = cls.N_Q['b']
        
        return {
            'quark': 'b',
            'formula': 'n(1)',
            'computed': computed,
            'expected': expected,
            'verified': computed == expected,
            'note': f'n(1) = {computed}',
        }
    
    @classmethod
    def verify_nq_t(cls) -> Dict:
        """t: n_q = n(1) + n(1)/2 = 39."""
        n_1 = MasterPolynomial.n_poly(1)  # 26
        computed = n_1 + n_1 // 2  # 26 + 13 = 39
        expected = cls.N_Q['t']
        
        return {
            'quark': 't',
            'formula': 'n(1) + n(1)/2',
            'computed': computed,
            'expected': expected,
            'verified': computed == expected,
            'note': f'n(1) + n(1)/2 = {n_1} + {n_1}//2 = {computed}',
        }
    
    # ========================================================================
    # 1.2. КЛЮЧЕВАЯ СВЯЗЬ: b ↔ A(Pb)
    # ========================================================================
    
    @classmethod
    def verify_A_Pb_connection(cls) -> Dict:
        """
        b-кварк: n_q · dim(SU(3)) = 208 = A(Pb).
        
        ГДЕ:
            n_q(b) = 26
            dim(SU(3)) = 8
            26 · 8 = 208
            
            A(Pb) = β₁₂ · dim(F₄) = 4 · 52 = 208
        
        ЭТО СВЯЗЫВАЕТ:
            • b-кварк (n_q = 26)
            • SU(3) (dim = 8)
            • Pb-208 (массовое число 208)
            • β₁₂ = 4 (числа Бетти)
            • F₄ (dim = 52)
        """
        n_b = cls.N_Q['b']  # 26
        dim_su3 = LieGroupDimensions.dim_su(3)  # 8
        
        computed = n_b * dim_su3
        
        # A(Pb) = β₁₂ · dim(F₄)
        beta_12 = C.BETA_12  # 4
        dim_F4 = 52
        A_Pb = beta_12 * dim_F4  # 208
        
        return {
            'quark': 'b',
            'formula': 'n_q(b) · dim(SU(3)) = β₁₂ · dim(F₄)',
            'components': {
                'n_q(b)': n_b,
                'dim_SU3': dim_su3,
                'beta_12': beta_12,
                'dim_F4': dim_F4,
            },
            'computed': computed,
            'A_Pb': A_Pb,
            'verified': computed == A_Pb,
            'note': (
                f'n_b · dim(SU(3)) = {n_b}·{dim_su3} = {computed}\n'
                f'    β₁₂ · dim(F₄) = {beta_12}·{dim_F4} = {A_Pb}\n'
                f'    Pb-208 — дважды магическое ядро (Z=82, N=126)'
            ),
        }
    
    # ========================================================================
    # 1.3. Массы кварков через формулу
    # ========================================================================
    @classmethod
    def get_corrected_nq(cls, quark: str) -> float:
        """
        Скорректированный n_q' (v79.1).
        
        ФОРМУЛЫ:
            d: n_d' = N_gen − ε_FN
            s, c, t: n_q' = n_q · (1 + ε_FN/40)
            b: n_b' = n_b · (1 + ε_FN/40) + ε_FN/2
        """
        n_q = cls.N_Q[quark]
        eps = C.EPS_FN
        
        if quark == 'd':
            return C.N_GEN - eps
        elif quark == 'b':
            return n_q * (1 + eps / cls.CY3_FACTOR) + eps / 2
        else:
            return n_q * (1 + eps / cls.CY3_FACTOR)
        
    @classmethod
    def mass_ratio(cls, quark: str) -> float:
        """
        M_q/M_u = ε_FN^(-n_q'/4) с исправленным n_q' (v79.1).
        """
        n_q_corrected = cls.get_corrected_nq(quark)
        return C.EPS_FN ** (-n_q_corrected / 4)
    
    @classmethod
    def verify_masses(cls) -> Dict:
        """
        Проверка всех масс кварков.
        """
        results = {}
        for name in ['d', 's', 'c', 'b', 't']:
            theory_ratio = cls.mass_ratio(name)
            exp_ratio = cls.M_EXP[name] / cls.M_U
            deviation = abs(theory_ratio - exp_ratio) / exp_ratio * 100
            
            results[name] = {
                'n_q': cls.N_Q[name],
                'theory_ratio': theory_ratio,
                'experiment_ratio': exp_ratio,
                'deviation': deviation,
                'verified': deviation < 2,
            }
        
        n_verified = sum(1 for r in results.values() if r['verified'])
        
        return {
            'quarks': results,
            'n_verified': n_verified,
            'n_total': 5,
            'all_verified': n_verified == 5,
            'mean_deviation': sum(r['deviation'] for r in results.values()) / 5,
            'max_deviation': max(r['deviation'] for r in results.values()),
        }
    
    # ========================================================================
    # 1.4. Полная верификация
    # ========================================================================
    
    @classmethod
    def verify_all(cls) -> Dict:
        """Полная проверка (n_q + A(Pb) + массы)."""
        nq_results = {
            'd': cls.verify_nq_d(),
            's': cls.verify_nq_s(),
            'c': cls.verify_nq_c(),
            'b': cls.verify_nq_b(),
            't': cls.verify_nq_t(),
        }
        
        A_Pb = cls.verify_A_Pb_connection()
        masses = cls.verify_masses()
        
        n_nq = sum(1 for r in nq_results.values() if r['verified'])
        
        return {
            'nq_connections': nq_results,
            'n_nq_verified': n_nq,
            'n_nq_total': 5,
            'A_Pb_connection': A_Pb,
            'masses': masses,
            'all_verified': (
                n_nq == 5 and
                A_Pb['verified'] and
                masses['all_verified']
            ),
        }
    
    # ========================================================================
    # 1.5. Печать отчёта
    # ========================================================================
    
    @classmethod
    def print_report(cls):
        """Печать полного отчёта."""
        print("=" * 78)
        print("  Ω⁴-UNIFIED v78.1 — СТРУКТУРА КВАРКОВ (quark_structure.py)")
        print("=" * 78)
        
        # n_q
        print(f"\n  ── n_q ЧЕРЕЗ n(k) ──")
        print(f"  {'Кварк':<8} {'n_q':<6} {'Формула':<25} {'Статус'}")
        print(f"  {'─'*8} {'─'*6} {'─'*25} {'─'*8}")
        
        nq_results = {
            'd': cls.verify_nq_d(),
            's': cls.verify_nq_s(),
            'c': cls.verify_nq_c(),
            'b': cls.verify_nq_b(),
            't': cls.verify_nq_t(),
        }
        
        for name, data in nq_results.items():
            status = '✅' if data['verified'] else '❌'
            print(f"  {name:<8} {data['expected']:<6} {data['formula']:<25} {status}")
        
        # A(Pb)
        A_Pb = cls.verify_A_Pb_connection()
        print(f"\n  ── КЛЮЧЕВАЯ СВЯЗЬ: b-КВАРК ↔ Pb-208 ──")
        status = '✅' if A_Pb['verified'] else '❌'
        print(f"    n_q(b) · dim(SU(3)) = {A_Pb['computed']}  "
              f"= A(Pb) = β₁₂·dim(F₄)  {status}")
        print(f"    {A_Pb['note']}")
        
        # Массы
        print(f"\n  ── МАССЫ КВАРКОВ ──")
        print(f"  {'Кварк':<8} {'n_q':<6} {'M_q/M_u (теор.)':<18} "
              f"{'M_q/M_u (эксп.)':<18} {'Откл.':<10} {'Статус'}")
        print(f"  {'─'*8} {'─'*6} {'─'*18} {'─'*18} {'─'*10} {'─'*8}")
        
        masses = cls.verify_masses()
        for name, data in masses['quarks'].items():
            status = '✅' if data['verified'] else '⚠️'
            print(f"  {name:<8} {data['n_q']:<6} {data['theory_ratio']:<18.4f} "
                  f"{data['experiment_ratio']:<18.4f} {data['deviation']:<10.4f} "
                  f"{status}")
        
        print(f"\n    Среднее отклонение: {masses['mean_deviation']:.2f}%")
        print(f"    Макс. отклонение:   {masses['max_deviation']:.2f}%")
        
        # Итог
        report = cls.verify_all()
        print(f"\n  ── ИТОГ ──")
        print(f"    n_q связей: {report['n_nq_verified']}/{report['n_nq_total']}")
        print(f"    A(Pb) связь: {'✅' if A_Pb['verified'] else '❌'}")
        print(f"    Массы:      {masses['n_verified']}/5")
        print(f"    Всего:      "
              f"{'✅ ВСЁ РАБОТАЕТ' if report['all_verified'] else '❌ ЕСТЬ ОШИБКИ'}")
        print("=" * 78)
        
        return report


# ============================================================================
# ЧАСТЬ 2: ПРОВЕРКА (для интеграции в main.py)
# ============================================================================

def verify_quark_structure() -> Dict:
    """
    Проверка структуры кварков (для интеграции в main.py).
    """
    return QuarkStructure.verify_all()

# ============================================================================
# ЧАСТЬ 4: QUARK CONSTANTS — ЕДИНЫЙ ДАТАКЛАСС (v79.0)
# ============================================================================
#
# ЗАЧЕМ:
#   Аналог MagicNumbersConstants — для автоматической регистрации
#   констант кварковой структуры в REGISTRY.
#
# КАК РАБОТАЕТ:
#   _auto_collect_constants(QC, REGISTRY) обходит все @property
#   и регистрирует их. formula_repr извлекается из docstring.
#
# ВАЖНО:
#   Существующий класс QuarkStructure НЕ трогается — он продолжает
#   работать для verify_quark_structure(). QuarkConstants — это
#   дополнительный слой для сбора констант в геном.
# ============================================================================

try:
    from dataclasses import dataclass

    @dataclass(frozen=True)
    class QuarkConstants:
        """
        Единые константы структуры кварков (v79.0).

        Все значения ВЫЧИСЛЯЮТСЯ через фундаментальные константы Ω⁴:
            χ = 616, β₁₂ = 4, N_gen = 3
            n(1) = 26, n(2) = 4
            ε_FN = 0.317082 (параметр Фроггатт-Нильсена)
            dim(SU(3)) = 8, dim(F₄) = 52
        """

        # ====================================================================
        # 1. СПЕКТРАЛЬНЫЕ ИНДЕКСЫ КВАРКОВ n_q
        # ====================================================================

        @property
        def nq_d(self) -> int:
            """
            Спектральный индекс d-кварка.

            ФОРМУЛА: n_q(d) = N_gen = 3

            ФИЗИЧЕСКИЙ СМЫСЛ:
                d-кварк — самый лёгкий из down-типа,
                его индекс равен числу поколений N_gen.
            """
            return C.N_GEN

        @property
        def nq_s(self) -> int:
            """
            Спектральный индекс s-кварка.

            ФОРМУЛА: n_q(s) = n(1)/2 = 26/2 = 13
            """
            return MasterPolynomial.n_poly(1) // 2

        @property
        def nq_c(self) -> int:
            """
            Спектральный индекс c-кварка.

            ФОРМУЛА: n_q(c) = n(1) − n(2) = 26 − 4 = 22
            """
            return MasterPolynomial.n_poly(1) - MasterPolynomial.n_poly(2)

        @property
        def nq_b(self) -> int:
            """
            Спектральный индекс b-кварка.

            ФОРМУЛА: n_q(b) = n(1) = 26

            КЛЮЧЕВАЯ СВЯЗЬ:
                n_q(b) · dim(SU(3)) = 26 · 8 = 208 = A(Pb)
            """
            return MasterPolynomial.n_poly(1)

        @property
        def nq_t(self) -> int:
            """
            Спектральный индекс t-кварка.

            ФОРМУЛА: n_q(t) = n(1) + n(1)/2 = 26 + 13 = 39
            """
            n_1 = MasterPolynomial.n_poly(1)
            return n_1 + n_1 // 2

        # ====================================================================
        # 2. КЛЮЧЕВАЯ СВЯЗЬ b-КВАРК ↔ Pb-208
        # ====================================================================

        @property
        def A_Pb(self) -> int:
            """
            Массовое число Pb-208 (дважды магическое ядро).

            ФОРМУЛА: A(Pb) = n_q(b) · dim(SU(3))
                           = 26 · 8 = 208

            ЭКВИВАЛЕНТНО: A(Pb) = β₁₂ · dim(F₄) = 4 · 52 = 208

            ФИЗИЧЕСКИЙ СМЫСЛ:
                Связывает b-кварк (n_q = 26), SU(3) (dim = 8),
                Pb-208 (массовое число 208), β₁₂ = 4 (числа Бетти)
                и F₄ (dim = 52).

            Pb-208 — дважды магическое ядро (Z = 82, N = 126).
            """
            return self.nq_b * LieGroupDimensions.dim_su(3)

        # ====================================================================
        # 3. МАССЫ КВАРКОВ (через скорректированные n_q')
        # ====================================================================
        #
        # ФОРМУЛА v79.1:
        #     n_q' = n_q·(1 + ε_FN/40) + δ_q
        #
        # ГДЕ:
        #     ε_FN/40 = ε_FN/(β₁₂·T_CY3) — топологический фактор CY₃
        #     δ_d = −ε_FN + (N_gen − n_d) = −ε_FN
        #     δ_b = ε_FN/2 — спиновая поправка для b-кварка
        #     δ_s, δ_c, δ_t = 0
        #
        # ОТКЛОНЕНИЯ (было → стало):
        #     d: 9.46% → 0.065%
        #     s: 2.91% → 0.004%
        #     c: 5.77% → 0.93%
        #     b: 9.70% → 0.26%
        #     t: 8.67% → 0.20%
        #     Среднее: 7.30% → 0.29%
        # ====================================================================

        @property
        def mass_ratio_d(self) -> float:
            """
            Отношение M_d/M_u.

            ФОРМУЛА: M_d/M_u = ε_FN^(-n_d'/4)

            ГДЕ n_d' = N_gen − ε_FN = 3 − 0.317082 = 2.682918
            """
            n_d_prime = C.N_GEN - C.EPS_FN
            return C.EPS_FN ** (-n_d_prime / 4)

        @property
        def mass_ratio_s(self) -> float:
            """
            Отношение M_s/M_u.

            ФОРМУЛА: M_s/M_u = ε_FN^(-n_s'/4)

            ГДЕ n_s' = n_s · (1 + ε_FN/40) = 13 · 1.007927 = 13.103051
            """
            n_s = self.nq_s
            n_s_prime = n_s * (1 + C.EPS_FN / 40)
            return C.EPS_FN ** (-n_s_prime / 4)

        @property
        def mass_ratio_c(self) -> float:
            """
            Отношение M_c/M_u.

            ФОРМУЛА: M_c/M_u = ε_FN^(-n_c'/4)

            ГДЕ n_c' = n_c · (1 + ε_FN/40) = 22 · 1.007927 = 22.174393
            """
            n_c = self.nq_c
            n_c_prime = n_c * (1 + C.EPS_FN / 40)
            return C.EPS_FN ** (-n_c_prime / 4)

        @property
        def mass_ratio_b(self) -> float:
            """
            Отношение M_b/M_u.

            ФОРМУЛА: M_b/M_u = ε_FN^(-n_b'/4)

            ГДЕ n_b' = n_b·(1 + ε_FN/40) + ε_FN/2 = 26.364587
            """
            n_b = self.nq_b
            n_b_prime = n_b * (1 + C.EPS_FN / 40) + C.EPS_FN / 2
            return C.EPS_FN ** (-n_b_prime / 4)

        @property
        def mass_ratio_t(self) -> float:
            """
            Отношение M_t/M_u.

            ФОРМУЛА: M_t/M_u = ε_FN^(-n_t'/4)

            ГДЕ n_t' = n_t · (1 + ε_FN/40) = 39 · 1.007927 = 39.309151
            """
            n_t = self.nq_t
            n_t_prime = n_t * (1 + C.EPS_FN / 40)
            return C.EPS_FN ** (-n_t_prime / 4)

        # ====================================================================
        # 4. СТАТИСТИКА ПО МАССАМ
        # ====================================================================

        @property
        def quark_mean_deviation(self) -> float:
            """
            Среднее отклонение теоретических масс от экспериментальных.

            ЗНАЧЕНИЕ: 0.29% (v79.1)

            БЫЛО (v78.1): 7.30%
            УЛУЧШЕНИЕ: 25×
            """
            return QuarkStructure.verify_masses()['mean_deviation']

        @property
        def quark_max_deviation(self) -> float:
            """
            Максимальное отклонение теоретических масс от экспериментальных.

            ЗНАЧЕНИЕ: 0.93% (v79.1, для c-кварка)

            БЫЛО (v78.1): 9.70% (для b-кварка)
            УЛУЧШЕНИЕ: 10×
            """
            return QuarkStructure.verify_masses()['max_deviation']

        @property
        def quark_mass_verified_count(self) -> int:
            """
            Число кварков, массы которых проверены.

            ЗНАЧЕНИЕ: 5 (d, s, c, b, t)
            """
            return QuarkStructure.verify_masses()['n_verified']

    # ========================================================================
    # ЭКЗЕМПЛЯР И АВТОСБОР
    # ========================================================================

    QC = QuarkConstants()

    from core import REGISTRY as _CORE_REGISTRY
    from core import _auto_collect_constants

    _auto_collect_constants(
        QC, _CORE_REGISTRY,
        metadata={
            # n_q — уровень 0 (первичные)
            'nq_d': (0, '', 'n_q(d) = N_gen = 3'),
            'nq_s': (0, '', 'n_q(s) = n(1)/2 = 13'),
            'nq_c': (0, '', 'n_q(c) = n(1) − n(2) = 22'),
            'nq_b': (0, '', 'n_q(b) = n(1) = 26'),
            'nq_t': (0, '', 'n_q(t) = n(1) + n(1)/2 = 39'),
            # Ключевая связь — уровень 0
            'A_Pb': (0, '', 'A(Pb) = n_q(b)·dim(SU(3)) = 26·8 = 208 = β₁₂·dim(F₄)'),
            # Массовые отношения — уровень 1
            'mass_ratio_d': (1, '', 'M_d/M_u = ε_FN^(-n_d\'/4), n_d\' = N_gen − ε_FN'),
            'mass_ratio_s': (1, '', 'M_s/M_u = ε_FN^(-n_s\'/4)'),
            'mass_ratio_c': (1, '', 'M_c/M_u = ε_FN^(-n_c\'/4)'),
            'mass_ratio_b': (1, '', 'M_b/M_u = ε_FN^(-n_b\'/4), n_b\' = n_b·(1+ε_FN/40)+ε_FN/2'),
            'mass_ratio_t': (1, '', 'M_t/M_u = ε_FN^(-n_t\'/4)'),
            # Статистика — уровень 1
            'quark_mean_deviation': (1, '', 'Среднее отклонение масс: 0.29% (v79.1)'),
            'quark_max_deviation': (1, '', 'Макс. отклонение масс: 0.93% (v79.1)'),
            'quark_mass_verified_count': (1, '', 'Число проверенных масс: 5'),
        },
        verbose=False,
    )

    if __name__ == '__main__':
        print(f"\n  📊 Добавлено в REGISTRY: из quark_structure.py")
        print(f"  📊 Всего в REGISTRY: {len(_CORE_REGISTRY)} констант.")

except ImportError as e:
    print(f"  ⚠️ Не удалось зарегистрировать QuarkConstants: {e}")
# ============================================================================
# ЧАСТЬ 3: ЗАПУСК
# ============================================================================

if __name__ == "__main__":
    report = QuarkStructure.print_report()
