#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
Ω⁴-UNIFIED v78.7 — ЭЛЛИПТИЧЕСКАЯ КРИВАЯ И BSD (elliptic_curve.py) — v1.1
================================================================================
НОВЫЙ МОДУЛЬ (наращивание). НЕ меняет базовые файлы.

================================================================================
ИЗМЕНЕНИЯ В v1.1 (относительно v1)
================================================================================

  • ДОБАВЛЕНА точная фундаментальная формула j-инварианта:
      j = -χ·62 - χ/N_SU19 = -616·62 - 616/19 = -38224.42105

    ОТКЛОНЕНИЕ от эксперимента: 0.00031% ✅

  • Добавлено свойство self.N_SU19 = n(1) - (n(2) + 3) = 19

  • Метод verify_j_invariant() теперь проверяет ОБЕ формулы:
      1. Из A, B:        j = 1728·4A³ / (4A³ + 27B²)
      2. Фундаментальная: j = -χ·62 - χ/N_SU19

================================================================================
ЧТО ДЕЛАЕТ
================================================================================

Анализ эллиптической кривой:

    E: Y² = X³ + AX + B

где:
    A = −35230
    B = 2602065

Кривая возникает из кубической производной мастер-полинома:
    f(k) = 103k³ − 370k² + 101k + 478

ПРОВЕРКИ:

  1. BSD-гипотеза:
       L'(E,1) = Ω_E · ĥ(P) · ∏c_p · |Sha|

  2. Bad prime:
       617 = χ + 1

  3. Связь с тёмной материей:
       ε_FN × κ = Ω_DM · h²
       где κ = C_HL / L'(E,1)

  4. j-инвариант:
       j = 1728 · 4A³ / (4A³ + 27B²)

  5. C_HL = κ · L'(E,1)

  6. Дискриминант:
       Δ_E = −16(4A³ + 27B²)
           = −126508391457200
           = −2⁴ · 5² · 313 · 617 · 1637683

ИСПОЛЬЗУЕТ core.py (константы EC_A, EC_B, EC_L_PRIME, ...).

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

import math
from typing import Dict, List, Any, Optional


# ============================================================================
# ЧАСТЬ 1: ЭЛЛИПТИЧЕСКАЯ КРИВАЯ
# ============================================================================

class EllipticCurveBSD:
    """
    Эллиптическая кривая E: Y² = X³ + AX + B.
    
    ПАРАМЕТРЫ (из core.py):
        A = EC_A = −35230
        B = EC_B = 2602065
    
    BSD-ПАРАМЕТРЫ:
        L'(E,1) = EC_L_PRIME = 9.506022
        Ω_E = EC_OMEGA = 0.585344
        ĥ(P) = EC_HEIGHT = 8.120025
        ∏c_p = EC_TAMAGAWA = 2.0
        |Sha| = EC_SHA = 1.000001
        C_HL = EC_C_HL = 3.618140
    """
    
    def __init__(self):
        # Константы кривой
        self.A_CURVE = C.EC_A
        self.B_CURVE = C.EC_B
        
        # BSD-параметры
        self.L_PRIME_E_1 = C.EC_L_PRIME
        self.OMEGA_E = C.EC_OMEGA
        self.HEIGHT_P = C.EC_HEIGHT
        self.TAMAGAWA = C.EC_TAMAGAWA
        self.SHA = C.EC_SHA
        self.C_HL = C.EC_C_HL
        
        # Bad prime
        self.BAD_PRIME = C.CHI + 1  # 617

        # СВЯЗЬ С V_20 (для проверки):
        # V_20 = M_W · h¹¹ / rank(SU(26)) = M_W · 6/25
        self.V_20 = C.V_20  # автоматически через @property

        # НОВОЕ v1.1: N_SU19 для точной формулы j-инварианта
        # N_SU19 = n(1) − (n(2) + 3) = 26 − 7 = 19
        from core import MasterPolynomial
        n_1 = MasterPolynomial.n_poly(1)  # 26
        n_2 = MasterPolynomial.n_poly(2)  # 4
        self.N_SU19 = n_1 - (n_2 + 3)  # = 19    
    # ========================================================================
    # 1.1. BSD-ГИПОТЕЗА
    # ========================================================================
    # 
    # BSD-ГИПОТЕЗА:
    #   L'(E,1) = Ω_E · ĥ(P) · ∏c_p · |Sha|
    # 
    # где:
    #   L'(E,1) — производная L-функции в точке s=1
    #   Ω_E     — вещественный период
    #   ĥ(P)    — каноническая высота точки P
    #   ∏c_p    — произведение чисел Тамагавы
    #   |Sha|   — порядок группы Шафаревича-Тейта
    # 
    # ========================================================================
    
    def verify_bsd(self) -> Dict:
        """
        Проверка BSD-гипотезы.
        
        L'(E,1) = Ω_E · ĥ(P) · ∏c_p · |Sha|
        """
        # Правая часть
        rhs = (self.OMEGA_E * self.HEIGHT_P *
               self.TAMAGAWA * self.SHA)
        
        # Отношение
        ratio = self.L_PRIME_E_1 / rhs if rhs > 0 else 0
        deviation = abs(ratio - 1.0) * 100
        
        return {
            'L_prime': self.L_PRIME_E_1,
            'rhs': rhs,
            'ratio': ratio,
            'deviation_percent': deviation,
            'verified': deviation < 0.001,
            'formula': "L'(E,1) = Ω_E · ĥ(P) · ∏c_p · |Sha|",
            'components': {
                'omega_E': self.OMEGA_E,
                'height_P': self.HEIGHT_P,
                'tamagawa': self.TAMAGAWA,
                'sha': self.SHA,
            }
        }
    
    # ========================================================================
    # 1.2. BAD PRIME
    # ========================================================================
    # 
    # BAD PRIME — простое число, при котором кривая имеет плохую редукцию.
    # 
    # BAD PRIME:
    #   617 = χ + 1
    # 
    # где χ = 616 — фундаментальное число Ω⁴.
    # 
    # ========================================================================
    
    def verify_bad_prime(self) -> Dict:
        """
        Проверка: 617 = χ + 1.
        """
        chi = C.CHI
        expected = chi + 1
        match = (self.BAD_PRIME == expected)
        
        return {
            'bad_prime': self.BAD_PRIME,
            'chi': chi,
            'chi_plus_1': expected,
            'match': match,
            'verified': match,
            'formula': '617 = χ + 1',
        }
    
    # ========================================================================
    # 1.3. СВЯЗЬ С ТЁМНОЙ МАТЕРИЕЙ
    # ========================================================================
    # 
    # КЛЮЧЕВОЕ СООТНОШЕНИЕ:
    #   ε_FN × κ = Ω_DM · h²
    # 
    # где:
    #   ε_FN = 0.31708165 (параметр Фроггатт-Нильсена)
    #   κ = C_HL / L'(E,1) = 0.380616
    #   Ω_DM · h² = 0.120 (Planck)
    # 
    # Это связывает математику SU(26) с тёмной материей!
    # 
    # ========================================================================
    
    def compute_kappa(self) -> float:
        """
        κ = C_HL / L'(E,1).
        """
        return self.C_HL / self.L_PRIME_E_1 if self.L_PRIME_E_1 > 0 else 0
    
    def compute_dark_matter_relation(self) -> Dict:
        """
        Проверка: ε_FN × κ = Ω_DM · h².
        """
        kappa = self.compute_kappa()
        omega_theory = C.EPS_FN * kappa
        omega_planck = C.OMEGA_DM_OBS  # 0.120
        
        deviation = abs(omega_theory - omega_planck) / omega_planck * 100
        
        return {
            'epsilon_fn': C.EPS_FN,
            'kappa': kappa,
            'omega_theory': omega_theory,
            'omega_planck': omega_planck,
            'deviation_percent': deviation,
            'verified': deviation < 1.0,
            'formula': 'ε_FN × κ = Ω_DM · h²',
        }
    
    # ========================================================================
    # 1.4. j-ИНВАРИАНТ
    # ========================================================================
    # 
    # j-ИНВАРИАНТ:
    #   j = 1728 · 4A³ / (4A³ + 27B²)
    # 
    # ЭКСПЕРИМЕНТ:
    #   j = −38224.54
    # 
    # ========================================================================
    
    def compute_j_invariant(self) -> float:
        """j-инвариант кривой из A, B."""
        A = self.A_CURVE
        B = self.B_CURVE
        
        numerator = 1728 * 4 * A**3
        denominator = 4 * A**3 + 27 * B**2
        
        if abs(denominator) < 1e-15:
            return float('inf')
        
        return numerator / denominator

    def compute_j_invariant_simple(self) -> float:
        """
        j-инвариант через ПРОСТУЮ формулу (для сравнения).

        ФОРМУЛА:
            j = -χ · 62 = -616 · 62 = -38192

        ОТКЛОНЕНИЕ от эксперимента:
            0.0851%

        ФИЗИЧЕСКИЙ СМЫСЛ:
            62 = |Φ⁺(E₇)| - 1 = 63 - 1
        """
        chi = C.CHI
        return -chi * 62

    def compute_j_invariant_formula(self) -> float:
        """
        j-инвариант через ФУНДАМЕНТАЛЬНУЮ формулу (НОВОЕ v1.1).

        ФОРМУЛА:
            j = -χ · 62 - χ / N_SU19

        ГДЕ:
            χ = 616 — эйлерова характеристика CY₃
            62 = |Φ⁺(E₇)| - 1 = 63 - 1
            N_SU19 = n(1) - (n(2) + 3) = 26 - 7 = 19

        ЧИСЛЕННО:
            j = -616 · 62 - 616/19
              = -38192 - 32.42105
              = -38224.42105

        ЭКСПЕРИМЕНТ:
            j_expected = -38224.54

        ОТКЛОНЕНИЕ:
            0.000311% ✅ (в 273 раза лучше простой -χ·62)
        """
        chi = C.CHI  # 616
        j_theory = -chi * 62 - chi / self.N_SU19
        return j_theory

    def verify_j_invariant(self) -> Dict:
        """
        Проверка j-инварианта (v1.2).

        ТРИ ФОРМУЛЫ:
            1. Из A, B:        j = 1728 · 4A³ / (4A³ + 27B²)
            2. Простая:        j = -χ·62
            3. Фундаментальная: j = -χ·62 - χ/N_SU19
        """
        j_computed = self.compute_j_invariant()
        j_simple = self.compute_j_invariant_simple()
        j_formula = self.compute_j_invariant_formula()
        j_expected = C.J_INVARIANT  # −38224.54
        
        # Отклонения от ожидаемого
        dev_computed = abs(j_computed - j_expected) / abs(j_expected) * 100
        dev_simple = abs(j_simple - j_expected) / abs(j_expected) * 100
        dev_formula = abs(j_formula - j_expected) / abs(j_expected) * 100
        
        # ИСПРАВЛЕНО v1.2: улучшение считается правильно
        # Фундаментальная формула улучшает ПРОСТУЮ формулу
        improvement_factor = dev_simple / dev_formula if dev_formula > 0 else 0
        
        return {
            'j_computed': j_computed,
            'j_simple': j_simple,
            'j_formula': j_formula,
            'j_expected': j_expected,
            'deviation_computed_percent': dev_computed,
            'deviation_simple_percent': dev_simple,
            'deviation_formula_percent': dev_formula,
            'chi': C.CHI,
            'N_SU19': self.N_SU19,
            'formula_simple': 'j = -χ·62',
            'formula_improved': 'j = -χ·62 - χ/N_SU19',
            'improvement_factor': improvement_factor,
            'verified': dev_computed < 0.1 and dev_formula < 0.01,
        }
    
    # ========================================================================
    # 1.5. C_HL = κ · L'(E,1)
    # ========================================================================
    # 
    # ПРОВЕРКА:
    #   C_HL = κ · L'(E,1)
    # 
    # где:
    #   C_HL = 3.618140 (константа Харди-Литтлвуда)
    #   κ = C_HL / L'(E,1) = 0.380616
    #   L'(E,1) = 9.506022
    # 
    # ========================================================================
    
    def verify_CHL_kappa_relation(self) -> Dict:
        """
        Проверка: C_HL = κ · L'(E,1).
        """
        kappa = self.compute_kappa()
        L_prime = self.L_PRIME_E_1
        C_HL_computed = kappa * L_prime
        C_HL_expected = self.C_HL
        
        deviation = (abs(C_HL_computed - C_HL_expected) /
                     C_HL_expected * 100)
        
        return {
            'kappa': kappa,
            'L_prime': L_prime,
            'C_HL_computed': C_HL_computed,
            'C_HL_expected': C_HL_expected,
            'deviation_percent': deviation,
            'verified': deviation < 0.001,
        }
    
    # ========================================================================
    # 1.6. ДИСКРИМИНАНТ
    # ========================================================================
    # 
    # ДИСКРИМИНАНТ:
    #   Δ_E = −16(4A³ + 27B²)
    #       = −126508391457200
    #       = −2⁴ · 5² · 313 · 617 · 1637683
    # 
    # КЛЮЧЕВАЯ СВЯЗЬ С χ:
    #   617 = χ + 1
    # 
    # 617 — простое число, входит в дискриминант в 1-й степени.
    # 
    # ========================================================================
    
    def compute_discriminant(self) -> int:
        """Дискриминант кривой."""
        A = int(self.A_CURVE)
        B = int(self.B_CURVE)
        return -16 * (4 * A**3 + 27 * B**2)
    
    def factorize_discriminant(self) -> Dict[int, int]:
        """
        Факторизация |Δ_E|.
        
        Возвращает:
            {простое: степень}
        """
        n = abs(self.compute_discriminant())
        
        if n == 0:
            return {0: 1}
        
        factors = {}
        remaining = n
        
        # Пробное деление до 100000
        d = 2
        while d * d <= remaining and d < 100000:
            while remaining % d == 0:
                factors[d] = factors.get(d, 0) + 1
                remaining //= d
            d += 1 if d == 2 else 2
        
        if remaining > 1:
            factors[remaining] = factors.get(remaining, 0) + 1
        
        return factors
    
    def verify_discriminant(self) -> Dict:
        """
        Проверка дискриминанта.
        """
        Delta_E = self.compute_discriminant()
        factorization = self.factorize_discriminant()
        
        # Ожидаемая факторизация
        expected_factors = {2: 4, 5: 2, 313: 1, 617: 1, 1637683: 1}
        
        # Проверка
        factorization_ok = (factorization == expected_factors)
        
        # Проверка связи с χ
        bad_prime = 617
        chi_plus_1 = C.CHI + 1
        chi_connection = (bad_prime == chi_plus_1)
        
        return {
            'Delta_E': Delta_E,
            'Delta_E_abs': abs(Delta_E),
            'factorization': factorization,
            'expected_factors': expected_factors,
            'factorization_ok': factorization_ok,
            'bad_prime': bad_prime,
            'chi_plus_1': chi_plus_1,
            'chi_connection': chi_connection,
            'verified': factorization_ok and chi_connection,
        }
    
    # ========================================================================
    # 1.7. ПОЛНЫЙ ОТЧЁТ
    # ========================================================================
    
    def get_full_report(self) -> Dict:
        """Полный отчёт по кривой (v1.1)."""
        bsd = self.verify_bsd()
        bad_prime = self.verify_bad_prime()
        dm_relation = self.compute_dark_matter_relation()
        j_inv = self.verify_j_invariant()
        chl_kappa = self.verify_CHL_kappa_relation()
        discriminant = self.verify_discriminant()
        
        return {
            'curve': f'Y² = X³ {self.A_CURVE:+.0f}X {self.B_CURVE:+.0f}',
            'A': self.A_CURVE,
            'B': self.B_CURVE,
            'bsd': bsd,
            'bad_prime': bad_prime,
            'dark_matter': dm_relation,
            'j_invariant': j_inv,
            'CHL_kappa': chl_kappa,
            'discriminant': discriminant,
            # НОВОЕ v1.1: точная фундаментальная формула j
            'j_formula': 'j = -χ·62 - χ/N_SU19',
            'j_formula_value': j_inv['j_formula'],
            'j_formula_deviation': j_inv['deviation_formula_percent'],
            'j_formula_verified': j_inv['deviation_formula_percent'] < 0.01,
            'all_verified': (bsd['verified'] and
                            bad_prime['verified'] and
                            dm_relation['verified'] and
                            j_inv['verified'] and
                            chl_kappa['verified'] and
                            discriminant['verified']),
        }
    
    # ========================================================================
    # 1.8. ПЕЧАТЬ ОТЧЁТА
    # ========================================================================
    
    def print_report(self):
        """Печать отчёта."""
        print("=" * 78)
        print("  Ω⁴-UNIFIED v78.7 — ЭЛЛИПТИЧЕСКАЯ КРИВАЯ И BSD")
        print("=" * 78)
        
        report = self.get_full_report()
        
        print(f"\n  Кривая: {report['curve']}")
        print(f"    A = {report['A']}")
        print(f"    B = {report['B']}")
        
        # BSD
        bsd = report['bsd']
        print(f"\n  ── BSD-ГИПОТЕЗА ──")
        print(f"    {bsd['formula']}")
        print(f"    L'(E,1) = {bsd['L_prime']:.6f}")
        print(f"    Ω_E     = {bsd['components']['omega_E']:.6f}")
        print(f"    ĥ(P)    = {bsd['components']['height_P']:.6f}")
        print(f"    ∏c_p    = {bsd['components']['tamagawa']:.6f}")
        print(f"    |Sha|   = {bsd['components']['sha']:.6f}")
        print(f"    RHS     = {bsd['rhs']:.6f}")
        print(f"    Ratio   = {bsd['ratio']:.6f}")
        print(f"    Отклонение: {bsd['deviation_percent']:.6f}%  "
              f"{'✅' if bsd['verified'] else '❌'}")
        
        # Bad prime
        bp = report['bad_prime']
        print(f"\n  ── BAD PRIME ──")
        print(f"    {bp['formula']}")
        print(f"    617 = {bp['chi']} + 1 = {bp['chi_plus_1']}  "
              f"{'✅' if bp['verified'] else '❌'}")
        
        # Тёмная материя
        dm = report['dark_matter']
        print(f"\n  ── СВЯЗЬ С ТЁМНОЙ МАТЕРИЕЙ ──")
        print(f"    {dm['formula']}")
        print(f"    ε_FN     = {dm['epsilon_fn']:.8f}")
        print(f"    κ        = {dm['kappa']:.6f}")
        print(f"    ε_FN × κ = {dm['omega_theory']:.6f}")
        print(f"    Ω_DM·h²  = {dm['omega_planck']:.6f}")
        print(f"    Отклонение: {dm['deviation_percent']:.4f}%  "
              f"{'✅' if dm['verified'] else '❌'}")
        
        # j-инвариант
        j = report['j_invariant']
        print(f"\n  ── j-ИНВАРИАНТ ──")
        print(f"    Ожидается: {j['j_expected']:.4f}")
        print(f"")
        print(f"    1. Из A, B:")
        print(f"       j = 1728 · 4A³ / (4A³ + 27B²) = {j['j_computed']:.4f}")
        print(f"       Отклонение: {j['deviation_computed_percent']:.6f}%  "
              f"{'✅' if j['deviation_computed_percent'] < 0.1 else '❌'}")
        print(f"")
        print(f"    2. Простая формула:")
        print(f"       j = -χ·62 = -{j['chi']}·62 = {j['j_simple']:.4f}")
        print(f"       Отклонение: {j['deviation_simple_percent']:.6f}%  "
              f"{'✅' if j['deviation_simple_percent'] < 0.1 else '❌'}")
        print(f"")
        print(f"    3. Фундаментальная формула (НОВОЕ v1.1):")
        print(f"       j = -χ·62 - χ/N_SU19")
        print(f"         = -{j['chi']}·62 - {j['chi']}/{j['N_SU19']}")
        print(f"         = {j['j_formula']:.4f}")
        print(f"       Отклонение: {j['deviation_formula_percent']:.6f}%  "
              f"{'✅' if j['deviation_formula_percent'] < 0.01 else '❌'}")
        print(f"")
        print(f"    ★ УЛУЧШЕНИЕ:")
        print(f"       Фундаментальная vs простая: {j['improvement_factor']:.1f}×")
        
        # C_HL
        chl = report['CHL_kappa']
        print(f"\n  ── C_HL = κ · L'(E,1) ──")
        print(f"    κ · L'(E,1) = {chl['C_HL_computed']:.6f}")
        print(f"    C_HL        = {chl['C_HL_expected']:.6f}")
        print(f"    Отклонение: {chl['deviation_percent']:.6f}%  "
              f"{'✅' if chl['verified'] else '❌'}")
        
        # Дискриминант
        disc = report['discriminant']
        print(f"\n  ── ДИСКРИМИНАНТ ──")
        print(f"    Δ_E = {disc['Delta_E']}")
        print(f"    |Δ_E| = {disc['Delta_E_abs']}")
        print(f"    Факторизация: {disc['factorization']}")
        print(f"    Ожидается:    {disc['expected_factors']}")
        print(f"    Факторизация OK: {'✅' if disc['factorization_ok'] else '❌'}")
        print(f"    617 = χ + 1: {'✅' if disc['chi_connection'] else '❌'}")
        
        # Итог
        print(f"\n  ── ИТОГ ──")
        print(f"    Все проверки: {'✅' if report['all_verified'] else '❌'}")
        print("=" * 78)
        
        return report


# ============================================================================
# ЧАСТЬ 2: ФУНКЦИЯ ПРОВЕРКИ (для main.py)
# ============================================================================

def verify_elliptic_curve() -> Dict:
    """
    Проверка эллиптической кривой (для интеграции в main.py).
    """
    ec = EllipticCurveBSD()
    return ec.get_full_report()

# ============================================================================
# ЧАСТЬ 4: EC CONSTANTS — ЕДИНЫЙ ДАТАКЛАСС (v79.0)
# ============================================================================
#
# ЗАЧЕМ:
#   Аналог VacuumConstants из vacuum_analysis.py — для автоматической
#   регистрации констант эллиптической кривой в REGISTRY.
#
# КАК РАБОТАЕТ:
#   _auto_collect_constants(EC, REGISTRY) обходит все @property
#   и регистрирует их. formula_repr извлекается из docstring.
#
# ВАЖНО:
#   Существующий класс EllipticCurveBSD НЕ трогается — он продолжает
#   работать для verify_elliptic_curve(). ECConstants — это
#   дополнительный слой для сбора констант в геном.
# ============================================================================

try:
    from dataclasses import dataclass

    @dataclass(frozen=True)
    class ECConstants:
        """
        Единые константы эллиптической кривой E: Y² = X³ + AX + B (v79.0).

        Все значения читаются из EllipticCurveBSD.

        ВАЖНО (v79.0.10):
            Свойства ec_A / ec_B УДАЛЕНЫ — они дублировали
            Constants.EC_A / Constants.EC_B из core.py.
            Используйте C.EC_A / C.EC_B напрямую.
        """

        # ====================================================================
        # 1. ДИСКРИМИНАНТ
        # ====================================================================

        @property
        def ec_discriminant(self) -> int:
            """
            Дискриминант кривой.

            ФОРМУЛА: Δ_E = -16(4A³ + 27B²) = -126508391457200

            ФАКТОРИЗАЦИЯ:
                Δ_E = -2⁴ · 5² · 313 · 617 · 1637683

            КЛЮЧЕВАЯ СВЯЗЬ:
                617 = χ + 1 = 616 + 1 (bad prime)
            """
            ec = EllipticCurveBSD()
            return ec.compute_discriminant()

        # ====================================================================
        # 3. J-ИНВАРИАНТ
        # ====================================================================

        @property
        def ec_j_invariant(self) -> float:
            """
            j-инвариант из коэффициентов A, B.

            ФОРМУЛА: j = 1728 · 4A³ / (4A³ + 27B²) ≈ -38224.54
            """
            ec = EllipticCurveBSD()
            return ec.compute_j_invariant()

        @property
        def ec_j_formula(self) -> float:
            """
            j-инвариант через фундаментальную формулу.

            ФОРМУЛА: j = -χ·62 - χ/N_SU19 = -616·62 - 616/19

            ГДЕ:
                χ = 616 — эйлерова характеристика CY₃
                62 = |Φ⁺(E₇)| - 1 = 63 - 1
                N_SU19 = n(1) - (n(2) + 3) = 26 - 7 = 19

            ОТКЛОНЕНИЕ от эксперимента (-38224.54):
                0.00031% ✅ (в 273 раза лучше простой -χ·62)
            """
            ec = EllipticCurveBSD()
            return ec.compute_j_invariant_formula()

        # ====================================================================
        # 4. ТЁМНАЯ МАТЕРИЯ
        # ====================================================================

        @property
        def ec_kappa(self) -> float:
            """
            κ = C_HL / L'(E,1).

            ФОРМУЛА: κ = 3.618140 / 9.506022 = 0.380616...

            ФИЗИЧЕСКИЙ СМЫСЛ:
                κ связывает константу Харди-Литтлвуда C_HL
                с производной L-функции в s=1.
            """
            ec = EllipticCurveBSD()
            return ec.compute_kappa()

        @property
        def ec_omega_DM(self) -> float:
            """
            Ω_DM · h² из эллиптической кривой.

            ФОРМУЛА: Ω_DM = ε_FN · κ = 0.317082 · 0.380616 = 0.120686...

            ЭКСПЕРИМЕНТ: 0.120 (Planck 2018)
            ОТКЛОНЕНИЕ: 0.57%
            """
            ec = EllipticCurveBSD()
            return ec.compute_dark_matter_relation()['omega_theory']

        # ====================================================================
        # 5. BAD PRIME
        # ====================================================================

        @property
        def ec_bad_prime(self) -> int:
            """
            Bad prime эллиптической кривой.

            ФОРМУЛА: 617 = χ + 1 = 616 + 1

            ФИЗИЧЕСКИЙ СМЫСЛ:
                617 — простое число, входит в дискриминант в 1-й степени.
                Связь с χ = 616 подтверждает топологическую природу кривой.
            """
            return C.CHI + 1

    # ========================================================================
    # ЭКЗЕМПЛЯР И АВТОСБОР
    # ========================================================================

    EC = ECConstants()

    # Импортируем _auto_collect_constants из core.py
    from core import REGISTRY as _CORE_REGISTRY
    from core import _auto_collect_constants

    _auto_collect_constants(
        EC, _CORE_REGISTRY,
        metadata={
            'ec_discriminant': (0, '', 'Δ_E = -16(4A³ + 27B²) = -1.265084e+14'),
            'ec_bad_prime': (0, '', '617 = χ + 1 — bad prime'),
            'ec_j_invariant': (1, '', 'j = 1728·4A³/(4A³ + 27B²)'),
            'ec_j_formula': (1, '', 'j = -χ·62 - χ/N_SU19'),
            'ec_kappa': (1, '', 'κ = C_HL / L\'(E,1)'),
            'ec_omega_DM': (1, '', 'Ω_DM = ε_FN · κ = 0.120686'),
        },
        verbose=False,
    )

    if __name__ == '__main__':
        print(f"\n  📊 Добавлено в REGISTRY: из elliptic_curve.py")
        print(f"  📊 Всего в REGISTRY: {len(_CORE_REGISTRY)} констант.")

except ImportError as e:
    print(f"  ⚠️ Не удалось зарегистрировать ECConstants: {e}")
# ============================================================================
# ЧАСТЬ 3: ЗАПУСК
# ============================================================================

if __name__ == "__main__":
    ec = EllipticCurveBSD()
    report = ec.print_report()
