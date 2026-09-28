#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
Ω⁴-UNIFIED — КВАНТОВАЯ ГРАВИТАЦИЯ ИЗ SU(26) (quantum_gravity.py) — v1.1
================================================================================
Объединённый модуль: Планковская масса, G, Λ, квантовые поправки, FRG-анализ.

ИСТОЧНИКИ:
  • quantum_gravity_su26_ru.py         — M_Pl, G, поправки, Λ
  • Ω⁴-UNIFIED ФИНАЛЬНЫЙ FRG АНАЛИЗ.py — FRG, фиксированные точки, N_eff

ЧТО ВНУТРИ:
  ЧАСТЬ 0: Константы модели
  ЧАСТЬ 1: Планковская масса    M_Pl = V_20 · exp(χ/(12φ) + 3π/4)
  ЧАСТЬ 2: Постоянная Ньютона   G = ħc/M_Pl²
  ЧАСТЬ 3: Квантовые поправки   ΔS₁ = α⁻¹/1020, ΔS₂ = (ΔS₁)²/(16π²)
  ЧАСТЬ 4: Космологическая Λ    Λ = exp(−S_eff)/L_Pl²
  ЧАСТЬ 5: FRG анализ           β_g, β_λ, фиксированные точки, θ₁, θ₂
  ЧАСТЬ 6: Зависимость N_eff    g*(N_eff), θ₁(N_eff), θ₂(N_eff)
  ЧАСТЬ 7: Обёртка для main.py  compute_all()
  ЧАСТЬ 8: Регистрация в REGISTRY (15 констант)

ВАЖНО:
  • БЕЗ ГРАФИКОВ — только вычисления для верификации.
  • Все константы регистрируются в REGISTRY при импорте.
  • Регистрация безопасна: если core.py недоступен, модуль работает.

АВТОР:  Сергей Викторович Матершов
ORCID:  0009-0009-0641-1357
ЛИЦЕНЗИЯ: CC BY-NC-ND 4.0 International
================================================================================
"""

import math
import numpy as np
from scipy.optimize import root
from typing import Dict, List, Any, Optional


# ============================================================================
# ЧАСТЬ 0: КОНСТАНТЫ МОДЕЛИ
# ============================================================================
#
# Это «входные» константы квантовой гравитации из SU(26).
# Все они уже присутствуют в core.py (Constants) или выводятся из них.
#
# ЗАЧЕМ: чтобы модуль работал автономно, даже если core.py недоступен.
# ============================================================================

CHI = 616                              # χ = 616 — эйлерова характеристика CY₃
PHI = (1 + math.sqrt(5)) / 2           # φ = 1.618... — золотое сечение
PI = math.pi                           # π = 3.14159...

V_20 = 19.2878                         # V_20 — масштаб SU(20)-конфайнмента (ТэВ)
ALPHA_INV = 137.035999084              # α⁻¹ — обратная постоянная тонкой структуры (CODATA)
ZETA3 = 1.2020569031595942             # ζ(3) — дзета-функция Римана
GEOMETRIC_FACTOR = 1020                # N_geom = dim(SU(32)) − dim(SU(2)) = 1023 − 3

# Экспериментальные значения (для сравнения)
M_PL_EXP = 1.220910e19                 # M_Pl (ГэВ) — CODATA 2018
G_EXP = 6.67430e-11                    # G (м³/(кг·с²)) — CODATA 2018
LAMBDA_EXP = 1.1056e-52                # Λ (м⁻²) — Planck 2018

# Фундаментальные физические константы
HBAR = 1.054571817e-34                 # ħ (Дж·с)
C_SPEED = 299792458                    # c (м/с)


# ============================================================================
# ЧАСТЬ 1: ПЛАНКОВСКАЯ МАССА
# ============================================================================
#
# ФОРМУЛА:
#     M_Pl = V_20 · exp(χ/(12φ) + 3π/4)
#
# ПРОИСХОЖДЕНИЕ:
#     • χ/(12φ) ≈ 31.7267 — вклад от математической структуры CY₃
#     • 3π/4 ≈ 2.3562 — геометрическая поправка от компактификации
#     • V_20 = 19.2878 ТэВ — масштаб SU(20)-сектора
#
# ФИЗИЧЕСКИЙ СМЫСЛ:
#     Экспоненциальный фактор возникает от суммы мод Калуцы-Клейна
#     при компактификации 26D → 4D + CY₃ + T¹⁶.
#
# ЧИСЛЕННО:
#     M_Pl ≈ 1.2215e19 ГэВ
#     Отклонение от CODATA 2018: 0.045%
# ============================================================================

def compute_planck_mass() -> Dict:
    """
    Вычисление Планковской массы из SU(26).

    Возвращает:
        dict с полями:
          • exponent         — показатель степени χ/(12φ) + 3π/4
          • M_Pl_GeV         — вычисленная M_Pl (ГэВ)
          • M_Pl_exp         — экспериментальная M_Pl (ГэВ)
          • deviation_percent — отклонение (%)
          • verified         — True, если отклонение < 0.1%
    """
    # Шаг 1: показатель степени
    exponent = CHI / (12 * PHI) + 3 * PI / 4

    # Шаг 2: M_Pl в ТэВ
    M_Pl_TeV = V_20 * math.exp(exponent)

    # Шаг 3: перевод в ГэВ
    M_Pl_GeV = M_Pl_TeV * 1000

    # Шаг 4: сравнение с экспериментом
    deviation = abs(M_Pl_GeV - M_PL_EXP) / M_PL_EXP * 100

    return {
        'exponent': exponent,
        'M_Pl_GeV': M_Pl_GeV,
        'M_Pl_exp': M_PL_EXP,
        'deviation_percent': deviation,
        'verified': deviation < 0.1,
    }


# ============================================================================
# ЧАСТЬ 2: ПОСТОЯННАЯ НЬЮТОНА
# ============================================================================
#
# ФОРМУЛА:
#     G = ħc / M_Pl²
#
# ФИЗИЧЕСКИЙ СМЫСЛ:
#     Классическое определение G через M_Pl.
#     Если M_Pl выведена из SU(26), то G — вычисляется, а не постулируется.
#
# ЧИСЛЕННО:
#     G ≈ 6.668e-11 м³/(кг·с²)
#     Отклонение от CODATA 2018: 0.094%
# ============================================================================

def compute_newton_constant(M_Pl_GeV: float) -> Dict:
    """
    Вычисление постоянной Ньютона через M_Pl.

    Параметры:
        M_Pl_GeV — Планковская масса в ГэВ

    Возвращает:
        dict с полями:
          • G_computed        — вычисленная G
          • G_exp             — экспериментальная G
          • deviation_percent — отклонение (%)
          • verified          — True, если отклонение < 0.1%
    """
    # Шаг 1: перевод ГэВ → кг
    GeV_to_kg = 1.78266192e-27
    M_Pl_kg = M_Pl_GeV * GeV_to_kg

    # Шаг 2: G = ħc / M_Pl²
    G = HBAR * C_SPEED / (M_Pl_kg ** 2)

    # Шаг 3: сравнение
    deviation = abs(G - G_EXP) / G_EXP * 100

    return {
        'G_computed': G,
        'G_exp': G_EXP,
        'deviation_percent': deviation,
        'verified': deviation < 0.1,
    }


# ============================================================================
# ЧАСТЬ 3: КВАНТОВЫЕ ПОПРАВКИ
# ============================================================================
#
# ФОРМУЛЫ:
#     S_base = χ/(2φ) + α⁻¹/2 + ln(χ) + 12ζ(3)
#     ΔS₁    = α⁻¹/1020
#     ΔS₂    = (ΔS₁)²/(16π²)
#     S_eff  = S_base + ΔS₁ + ΔS₂
#
# ПРОИСХОЖДЕНИЕ:
#     • S_base — базовое действие (энтропия де Ситтера)
#     • ΔS₁ — однопетлевая поправка (геометрический фактор 1020)
#     • ΔS₂ — двухпетлевая поправка (подавление 1/(16π²))
#
# ЧИСЛЕННО:
#     S_base = 279.7204
#     ΔS₁    = 0.1343
#     ΔS₂    = 1.14e-4
#     S_eff  = 279.8549
#     Отношение ΔS₂/ΔS₁ = 0.00085 — ряд сходится быстро
# ============================================================================

def compute_quantum_corrections() -> Dict:
    """
    Вычисление квантовых поправок до двух петель.

    Возвращает:
        dict с полями:
          • S_base            — базовое действие
          • delta_S1          — однопетлевая поправка
          • delta_S2          — двухпетлевая поправка
          • S_eff             — полное эффективное действие
          • convergence_ratio — ΔS₂/ΔS₁
          • series_converges  — True, если отношение < 0.01
    """
    # Шаг 1: базовое действие
    S_base = CHI / (2 * PHI) + ALPHA_INV / 2 + math.log(CHI) + 12 * ZETA3

    # Шаг 2: однопетлевая поправка
    delta_S1 = ALPHA_INV / GEOMETRIC_FACTOR

    # Шаг 3: двухпетлевая поправка
    delta_S2 = (delta_S1 ** 2) / (16 * PI ** 2)

    # Шаг 4: полное действие
    S_eff = S_base + delta_S1 + delta_S2

    return {
        'S_base': S_base,
        'delta_S1': delta_S1,
        'delta_S2': delta_S2,
        'S_eff': S_eff,
        'convergence_ratio': delta_S2 / delta_S1,
        'series_converges': delta_S2 / delta_S1 < 0.01,
    }


# ============================================================================
# ЧАСТЬ 4: КОСМОЛОГИЧЕСКАЯ ПОСТОЯННАЯ
# ============================================================================
#
# ФОРМУЛА:
#     Λ = exp(−S_eff) / L_Pl²
#
# ПРОИСХОЖДЕНИЕ:
#     • S_eff — эффективное действие (энтропия де Ситтера)
#     • L_Pl — Планковская длина
#     • Экспоненциальное подавление exp(−S_eff) — главный результат
#
# ЧИСЛЕННО:
#     Λ ≈ 1.1055e-52 м⁻²
#     Отклонение от Planck 2018: 0.0092%
# ============================================================================

def compute_cosmological_constant(S_eff: float) -> Dict:
    """
    Вычисление космологической постоянной через S_eff.

    Параметры:
        S_eff — эффективное действие

    Возвращает:
        dict с полями:
          • Lambda            — вычисленная Λ
          • Lambda_exp        — экспериментальная Λ
          • deviation_percent — отклонение (%)
          • verified          — True, если отклонение < 0.01%
    """
    # Шаг 1: Планковская длина
    L_Pl = math.sqrt(HBAR * G_EXP / C_SPEED**3)

    # Шаг 2: Λ = exp(−S_eff) / L_Pl²
    Lambda = math.exp(-S_eff) / L_Pl**2

    # Шаг 3: сравнение
    deviation = abs(Lambda - LAMBDA_EXP) / LAMBDA_EXP * 100

    return {
        'Lambda': Lambda,
        'Lambda_exp': LAMBDA_EXP,
        'deviation_percent': deviation,
        'verified': deviation < 0.01,
    }


# ============================================================================
# ЧАСТЬ 5: FRG АНАЛИЗ
# ============================================================================
#
# ФУНКЦИОНАЛЬНАЯ РЕНОРМГРУППА (FRG):
#     Эффективное среднее действие Γ_k удовлетворяет уравнению Веттериха.
#     Для безразмерных констант:
#       g = G·k²        — безразмерная константа Ньютона
#       λ = Λ·k⁻²       — безразмерная космологическая постоянная
#
# БЕТА-ФУНКЦИИ:
#     β_g = 2g − g²(1−λ²) + g³/(6π) + (N_eff/48π)g³
#     β_λ = −2λ + gλ(1−λ) + g²λ²/(12π) − (N_eff/24π)g²λ
#
# ЧЛЕНЫ:
#     • 2g — каноническая размерность g
#     • −g²(1−λ²) — однопетлевой гравитационный вклад
#     • g³/(6π) — двухпетлевой стабилизирующий
#     • (N_eff/48π)g³ — вклад материи
#
# КРИТИЧЕСКИЕ ЭКСПОНЕНТЫ (стандарт FRG):
#     θ_i = eigenvalue_i(J)
#     Re θ_i > 0 для всех i → УФ-притяжение (асимптотическая безопасность)
#     Re θ_i < 0 для всех i → ИК-притяжение
#     смешанные знаки → седловая точка
#
# ЗАМЕЧАНИЕ О КОНВЕНЦИИ:
#     В ранних версиях (v1.0) использовалась обратная конвенция
#     θ_i = −eigenvalue_i(J). Обе конвенции дают одну и ту же
#     границу УФ-стабильности (N_eff = 7/8). В v1.1 приведено
#     к стандарту FRG — см. подробный комментарий в analyze_stability.
# ============================================================================

class FinalFRGAnalysis:
    """
    Функциональная ренормгруппа (FRG) для квантовой гравитации.

    Атрибуты:
        нет (N_eff передаётся в методы)

    Методы:
        beta_g(g, lam, N_eff)              — β_g
        beta_lambda(g, lam, N_eff)         — β_λ
        find_all_fixed_points(N_eff)       — список фиксированных точек
        analyze_stability(g, lam, N_eff)   — стабильность точки
        analyze_N_eff_dependence(...)      — зависимость от N_eff
    """

    def beta_g(self, g: float, lam: float, N_eff: float = 1.0) -> float:
        """
        Бета-функция безразмерной константы Ньютона g.

        ФОРМУЛА:
            β_g = 2g − g²(1−λ²) + g³/(6π) + (N_eff/48π)g³

        Параметры:
            g     — безразмерная константа Ньютона
            lam   — безразмерная космологическая постоянная λ
            N_eff — эффективное число степеней свободы материи

        Возвращает:
            float — значение β_g
        """
        # Каноническая размерность (масштабная инвариантность)
        beta = 2 * g

        # Однопетлевой гравитационный вклад
        beta -= g**2 * (1 - lam**2)

        # Двухпетлевой стабилизирующий вклад
        beta += g**3 / (6 * PI)

        # Вклад материи (N_eff степеней свободы)
        beta += (N_eff / (48 * PI)) * g**3

        return beta

    def beta_lambda(self, g: float, lam: float, N_eff: float = 1.0) -> float:
        """
        Бета-функция безразмерной космологической постоянной λ.

        ФОРМУЛА:
            β_λ = −2λ + gλ(1−λ) + g²λ²/(12π) − (N_eff/24π)g²λ

        Параметры:
            g     — безразмерная константа Ньютона
            lam   — безразмерная космологическая постоянная λ
            N_eff — эффективное число степеней свободы материи

        Возвращает:
            float — значение β_λ
        """
        # Каноническая размерность
        beta = -2 * lam

        # Гравитационный вклад
        beta += g * lam * (1 - lam)

        # Высший порядок
        beta += g**2 * lam**2 / (12 * PI)

        # Вклад материи
        beta -= (N_eff / (24 * PI)) * g**2 * lam

        return beta

    def find_all_fixed_points(self, N_eff: float = 1.0) -> List[Dict]:
        """
        Поиск всех фиксированных точек β_g = β_λ = 0.

        АЛГОРИТМ:
          1. Гауссова точка (0, 0) — тривиальная.
          2. Аналитически для λ = 0: решаем квадратное уравнение.
          3. Численно для λ ≠ 0: сканируем сетку начальных точек.

        Параметры:
            N_eff — эффективное число степеней свободы

        Возвращает:
            list[dict] — список фиксированных точек, каждая с полями:
              • g, lambda — координаты точки
              • type      — тип точки (Gaussian / Non-Gaussian)
              • stability — результат analyze_stability()
        """
        points = []

        # --- Гауссова точка (0, 0) ---
        points.append({
            'g': 0.0,
            'lambda': 0.0,
            'type': 'Gaussian',
            'stability': self.analyze_stability(0.0, 0.0, N_eff),
        })

        # --- Аналитическое решение для λ = 0 ---
        # β_g = 2g − g² + (1/(6π) + N_eff/(48π))g³ = 0
        # g·(2 − g + coeff·g²) = 0 → coeff·g² − g + 2 = 0
        coeff = 1 / (6 * PI) + N_eff / (48 * PI)
        discriminant = 1 - 8 * coeff

        if discriminant >= 0:
            g1 = (1 + np.sqrt(discriminant)) / (2 * coeff)
            g2 = (1 - np.sqrt(discriminant)) / (2 * coeff)
            for g_star in [g1, g2]:
                if g_star > 0:
                    stability = self.analyze_stability(g_star, 0.0, N_eff)
                    points.append({
                        'g': float(g_star),
                        'lambda': 0.0,
                        'type': 'Non-Gaussian (λ=0)',
                        'stability': stability,
                    })

        # --- Численный поиск для λ ≠ 0 ---
        def equations(x):
            return [
                self.beta_g(x[0], x[1], N_eff),
                self.beta_lambda(x[0], x[1], N_eff),
            ]

        for g_init in np.linspace(0.5, 20, 40):
            for lam_init in np.linspace(0.01, 0.4, 20):
                try:
                    sol = root(equations, [g_init, lam_init], method='hybr')
                    if sol.success:
                        g_star, lam_star = sol.x
                        if 0.01 < g_star < 100 and 0.001 < lam_star < 0.49:
                            # Проверка, что это действительно решение
                            bg = self.beta_g(g_star, lam_star, N_eff)
                            bl = self.beta_lambda(g_star, lam_star, N_eff)
                            if abs(bg) < 1e-6 and abs(bl) < 1e-6:
                                # Проверка уникальности
                                is_new = True
                                for p in points:
                                    if (abs(p['g'] - g_star) < 0.1 and
                                        abs(p['lambda'] - lam_star) < 0.01):
                                        is_new = False
                                        break
                                if is_new:
                                    stability = self.analyze_stability(
                                        g_star, lam_star, N_eff
                                    )
                                    points.append({
                                        'g': float(g_star),
                                        'lambda': float(lam_star),
                                        'type': 'Non-Gaussian (λ≠0)',
                                        'stability': stability,
                                    })
                except Exception:
                    pass

        return points

    def analyze_stability(self, g_star: float, lam_star: float,
                          N_eff: float = 1.0) -> Dict:
        """
        Анализ стабильности фиксированной точки через матрицу Якоби.

        МЕТОД:
            J_ij = ∂β_i/∂x_j — численно (центральные разности).
            θ_i — критические экспоненты (стандарт FRG).

        ══════════════════════════════════════════════════════════════════════
        КОНВЕНЦИЯ ЗНАКА θ (важно!)
        ══════════════════════════════════════════════════════════════════════

        В FRG-литературе (Reuter, Percacci, Litim, Wetterich) ПРИНЯТО:

            θ_i = eig_i(J)              — критические экспоненты
            Re θ_i > 0  для всех i      — УФ-притяжение (асимптотическая
                                          безопасность)
            Re θ_i < 0  для всех i      — ИК-притяжение
            смешанные знаки             — седловая точка

        В РАННИХ ВЕРСИЯХ этого файла (v1.0) использовалась ДРУГАЯ
        конвенция:

            θ_i = −eig_i(J)             — «критические экспоненты»
            uv_stable = all(eig_i > 0)  — что эквивалентно all(θ_i < 0)

        Это НЕ ошибка физики — обе конвенции дают ОДНУ И ТУ ЖЕ
        границу УФ-стабильности (проверено: граница между N_eff = 7
        и N_eff = 8 воспроизводится в обеих конвенциях). Но числа
        θ отличаются знаком.

        В v1.1 приведено к СТАНДАРТУ FRG: θ = eig(J), uv_stable = θ > 0.

        ПОЧЕМУ ЭТО ВАЖНО:
            • Единая конвенция нужна, чтобы числа θ были одинаковыми
              в quantum_gravity.py, topology_spectrum_limit.py и
              check_frg_limit.py.
            • Читатель FRG-литературы ожидает θ > 0 для УФ-стабильности.
            • Без унификации любое сравнение выводов двух модулей
              даёт ложное расхождение по знаку.

        ══════════════════════════════════════════════════════════════════════

        Параметры:
            g_star   — координата точки g*
            lam_star — координата точки λ*
            N_eff    — эффективное число степеней свободы

        Возвращает:
            dict с полями:
              • eigenvalues        — собственные значения J
              • critical_exponents — критические экспоненты θ = eig(J)
              • uv_stable          — True, если все Re(θ) > 0
              • ir_stable          — True, если все Re(θ) < 0
              • saddle             — True, если точка седловая
        """
        eps = 1e-6
        J = np.zeros((2, 2))

        # Численное дифференцирование (центральные разности)
        J[0, 0] = (self.beta_g(g_star + eps, lam_star, N_eff) -
                   self.beta_g(g_star - eps, lam_star, N_eff)) / (2 * eps)
        J[0, 1] = (self.beta_g(g_star, lam_star + eps, N_eff) -
                   self.beta_g(g_star, lam_star - eps, N_eff)) / (2 * eps)
        J[1, 0] = (self.beta_lambda(g_star + eps, lam_star, N_eff) -
                   self.beta_lambda(g_star - eps, lam_star, N_eff)) / (2 * eps)
        J[1, 1] = (self.beta_lambda(g_star, lam_star + eps, N_eff) -
                   self.beta_lambda(g_star, lam_star - eps, N_eff)) / (2 * eps)

        # ─── Собственные значения J ─────────────────────────────────────
        eigenvalues = np.linalg.eigvals(J)

        # ─── Критические экспоненты по СТАНДАРТУ FRG: θ = eig(J) ────────
        # (Раньше здесь было θ = −eig(J) — нестандартная конвенция.
        #  Приведено к стандарту в v1.1.)
        critical_exponents = eigenvalues

        # ─── Классификация точки ────────────────────────────────────────
        # УФ-стабильность: все Re(θ) > 0
        # ИК-стабильность: все Re(θ) < 0
        # Седло:           смешанные знаки
        uv_stable = all(np.real(ce) > 0 for ce in critical_exponents)
        ir_stable = all(np.real(ce) < 0 for ce in critical_exponents)

        return {
            'eigenvalues': [complex(ev) for ev in eigenvalues],
            'critical_exponents': [complex(ce) for ce in critical_exponents],
            'uv_stable': uv_stable,
            'ir_stable': ir_stable,
            'saddle': (not uv_stable and not ir_stable),
        }

    def analyze_N_eff_dependence(self,
                                  N_eff_values: Optional[List[float]] = None
                                  ) -> List[Dict]:
        """
        Зависимость УФ-стабильной точки от N_eff.

        Для каждого N_eff находит УФ-точку и записывает g*, λ*, θ₁, θ₂.

        Параметры:
            N_eff_values — список значений N_eff (по умолчанию 0...5 с шагом 0.5)

        Возвращает:
            list[dict] — для каждого N_eff:
              • N_eff, g_star, lambda_star, theta1, theta2, uv_stable
        """
        if N_eff_values is None:
            N_eff_values = list(np.arange(0, 5.1, 0.5))

        results = []
        for N_eff in N_eff_values:
            points = self.find_all_fixed_points(N_eff)
            uv_point = None
            for p in points:
                if p['stability']['uv_stable']:
                    uv_point = p
                    break

            if uv_point:
                results.append({
                    'N_eff': float(N_eff),
                    'g_star': uv_point['g'],
                    'lambda_star': uv_point['lambda'],
                    'theta1': float(np.real(
                        uv_point['stability']['critical_exponents'][0]
                    )),
                    'theta2': float(np.real(
                        uv_point['stability']['critical_exponents'][1]
                    )),
                    'uv_stable': True,
                })
            else:
                results.append({
                    'N_eff': float(N_eff),
                    'g_star': None,
                    'lambda_star': None,
                    'theta1': None,
                    'theta2': None,
                    'uv_stable': False,
                })

        return results


# ============================================================================
# ЧАСТЬ 6: ОБЁРТКА ДЛЯ main.py
# ============================================================================
#
# Эти функции возвращают результаты в формате, понятном main.py.
# Они не содержат новой физики — только упаковывают вычисления.
# ============================================================================

def compute_frg_results(N_eff: float = 1.0) -> Dict:
    """
    FRG анализ для одного значения N_eff (обёртка).

    Параметры:
        N_eff — эффективное число степеней свободы (по умолчанию 1.0 — СМ)

    Возвращает:
        dict с полями:
          • verified     — True, если найдена УФ-стабильная точка
          • n_points     — число найденных точек
          • g_star       — координата УФ-точки g*
          • lambda_star  — координата УФ-точки λ*
          • theta1, theta2 — критические экспоненты
          • all_points   — полный список точек
    """
    frg = FinalFRGAnalysis()
    points = frg.find_all_fixed_points(N_eff)

    # Ищем УФ-стабильную точку
    uv_point = None
    for p in points:
        if p['stability']['uv_stable']:
            uv_point = p
            break

    if uv_point is None:
        return {
            'verified': False,
            'n_points': len(points),
            'error': 'УФ-стабильная точка не найдена',
        }

    ce1 = uv_point['stability']['critical_exponents'][0]
    ce2 = uv_point['stability']['critical_exponents'][1]

    return {
        'verified': True,
        'n_points': len(points),
        'g_star': uv_point['g'],
        'lambda_star': uv_point['lambda'],
        'theta1': float(np.real(ce1)),
        'theta2': float(np.real(ce2)),
        'all_points': points,
    }


def compute_string_sector() -> Dict:
    """
    СТРУННЫЙ СЕКТОР — что есть и чего нет.

    ПРОБЛЕМА (STRUCTURAL_ARGUMENT, не PROVEN):
        Модель Ω⁴ использует D = 26 и SU(26), но это
        ЭФФЕКТИВНАЯ ТЕОРИЯ ПОЛЯ (EFT), а не струнная теория
        в строгом смысле.

    ЧТО ЕСТЬ:
        • D = 26 (критическая размерность бозонной струны);
        • SU(26) — калибровочная группа;
        • Компактификация 26D → 4D + CY₃ + T¹⁶;
        • χ = 616 = 26·24 − 8.

    ЧЕГО НЕТ:
        • Действие Полякова S = −(1/4πα') ∫ d²σ √(−h) h^{ab} ∂_a X^μ ∂_b X^ν g_{μν};
        • Вершинные операторы V(k) = :e^{ik·X}:;
        • Спектр замкнутых струн M² = (2/α')(N + Ñ − 2);
        • Инстантоны мирового листа;
        • Топологическая струнная сигма-модель.

    ВЫВОД:
        Модель — EFT с SU(26), а не струнная теория.
        Это честное признание предела.

    СТАТУС: STRUCTURAL_ARGUMENT (не PROVEN).
    """
    return {
        'has_26D': True,
        'has_SU26': True,
        'has_compactification': True,
        'has_polyakov_action': False,
        'has_vertex_operators': False,
        'has_closed_string_spectrum': False,
        'is_EFT_not_string_theory': True,
        'status': 'STRUCTURAL_ARGUMENT',
        'comment': (
            'Модель — EFT с SU(26), а не струнная теория в строгом смысле. '
            'STATUS: STRUCTURAL_ARGUMENT (не PROVEN).'
        ),
    }


def compute_all(N_eff: float = 1.0,
                include_N_eff_dependence: bool = True) -> Dict:
    """
    ПОЛНАЯ ВЕРИФИКАЦИЯ квантовой гравитации (обёртка для main.py).
    ...
    """
    planck = compute_planck_mass()
    newton = compute_newton_constant(planck['M_Pl_GeV'])
    corrections = compute_quantum_corrections()
    lambda_cc = compute_cosmological_constant(corrections['S_eff'])
    frg = compute_frg_results(N_eff)
    string_sector = compute_string_sector()  # ← НОВОЕ

    result = {
        'planck_mass': planck,
        'newton_constant': newton,
        'quantum_corrections': corrections,
        'cosmological_constant': lambda_cc,
        'frg': frg,
        'string_sector': string_sector,  # ← НОВОЕ
        'all_verified': all([
            planck['verified'],
            newton['verified'],
            corrections['series_converges'],
            lambda_cc['verified'],
            frg['verified'],
            # string_sector НЕ входит в all_verified — это STRUCTURAL_ARGUMENT
        ]),
    }

    if include_N_eff_dependence:
        frg_obj = FinalFRGAnalysis()
        result['N_eff_dependence'] = frg_obj.analyze_N_eff_dependence()

    return result


# ============================================================================
# ЧАСТЬ 7: РЕГИСТРАЦИЯ В REGISTRY
# ============================================================================
#
# Все ключевые константы квантовой гравитации регистрируются в REGISTRY
# при импорте модуля. Это позволяет им автоматически попасть в автогеном.
#
# УРОВНИ:
#   • '0' — фундаментальные (g*, θ₁, θ₂ — параметры УФ-точки)
#   • '1' — вычисленные (M_Pl, G, Λ, S_eff, ...)
#
# ВАЖНО: если core.py недоступен — модуль продолжает работать без регистрации.
# ============================================================================

def _register_qg_constants(verbose: bool = False) -> int:
    """
    Регистрирует константы QG в REGISTRY.

    Возвращает:
        int — число зарегистрированных констант (0 при ошибке).
    """
    try:
        from core import REGISTRY
    except ImportError:
        if verbose:
            print("  ⚠️ quantum_gravity: core.REGISTRY недоступен")
        return 0

    # Вычисляем всё один раз
    planck = compute_planck_mass()
    newton = compute_newton_constant(planck['M_Pl_GeV'])
    corrections = compute_quantum_corrections()
    lambda_cc = compute_cosmological_constant(corrections['S_eff'])
    frg = compute_frg_results(N_eff=1.0)

    n_registered = 0

    # ─── M_Pl ──────────────────────────────────────────────────────────
    REGISTRY.register(
        'QG_M_PL', planck['M_Pl_GeV'],
        unit='ГэВ', level='1',
        formula_repr='V_20 * exp(CHI/(12*PHI) + 3*PI/4)',
        source='quantum_gravity.py: M_Pl из SU(26)',
        comment=f'M_Pl = {planck["M_Pl_GeV"]:.4e} ГэВ, '
                f'откл. {planck["deviation_percent"]:.4f}% от CODATA',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'QG_M_PL_DEV', planck['deviation_percent'],
        unit='%', level='1',
        formula_repr='abs(M_Pl - M_Pl_exp) / M_Pl_exp * 100',
        source='quantum_gravity.py: отклонение M_Pl',
        comment=f'Отклонение M_Pl от CODATA: {planck["deviation_percent"]:.4f}%',
        overwrite=True,
    )
    n_registered += 1

    # ─── G ─────────────────────────────────────────────────────────────
    REGISTRY.register(
        'QG_G', newton['G_computed'],
        unit='м³/(кг·с²)', level='1',
        formula_repr='hbar * c / M_Pl^2',
        source='quantum_gravity.py: G из M_Pl',
        comment=f'G = {newton["G_computed"]:.4e} м³/(кг·с²), '
                f'откл. {newton["deviation_percent"]:.4f}% от CODATA',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'QG_G_DEV', newton['deviation_percent'],
        unit='%', level='1',
        formula_repr='abs(G - G_exp) / G_exp * 100',
        source='quantum_gravity.py: отклонение G',
        comment=f'Отклонение G от CODATA: {newton["deviation_percent"]:.4f}%',
        overwrite=True,
    )
    n_registered += 1

    # ─── Квантовые поправки ────────────────────────────────────────────
    REGISTRY.register(
        'QG_S_BASE', corrections['S_base'],
        unit='', level='1',
        formula_repr='CHI/(2*PHI) + ALPHA_INV/2 + ln(CHI) + 12*ZETA3',
        source='quantum_gravity.py: базовое действие',
        comment=f'S_base = {corrections["S_base"]:.4f}',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'QG_DELTA_S1', corrections['delta_S1'],
        unit='', level='1',
        formula_repr='ALPHA_INV / 1020',
        source='quantum_gravity.py: однопетлевая поправка',
        comment=f'ΔS₁ = {corrections["delta_S1"]:.6f}',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'QG_DELTA_S2', corrections['delta_S2'],
        unit='', level='1',
        formula_repr='(ΔS₁)^2 / (16*π^2)',
        source='quantum_gravity.py: двухпетлевая поправка',
        comment=f'ΔS₂ = {corrections["delta_S2"]:.6e}',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'QG_S_EFF', corrections['S_eff'],
        unit='', level='1',
        formula_repr='S_base + ΔS₁ + ΔS₂',
        source='quantum_gravity.py: полное действие',
        comment=f'S_eff = {corrections["S_eff"]:.4f}',
        overwrite=True,
    )
    n_registered += 1

    # ─── Λ ─────────────────────────────────────────────────────────────
    REGISTRY.register(
        'QG_LAMBDA', lambda_cc['Lambda'],
        unit='м⁻²', level='1',
        formula_repr='exp(-S_eff) / L_Pl^2',
        source='quantum_gravity.py: Λ из S_eff',
        comment=f'Λ = {lambda_cc["Lambda"]:.4e} м⁻², '
                f'откл. {lambda_cc["deviation_percent"]:.4f}% от Planck',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'QG_LAMBDA_DEV', lambda_cc['deviation_percent'],
        unit='%', level='1',
        formula_repr='abs(Λ - Λ_exp) / Λ_exp * 100',
        source='quantum_gravity.py: отклонение Λ',
        comment=f'Отклонение Λ от Planck: {lambda_cc["deviation_percent"]:.4f}%',
        overwrite=True,
    )
    n_registered += 1

    # ─── FRG: УФ-точка ─────────────────────────────────────────────────
    REGISTRY.register(
        'QG_FRG_G_STAR', frg.get('g_star', 0.0),
        unit='', level='0',
        formula_repr='корень β_g(g*, 0) = 0',
        source='quantum_gravity.py: УФ-точка FRG',
        comment=f'g* = {frg.get("g_star", 0.0):.4f}',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'QG_FRG_LAMBDA_STAR', frg.get('lambda_star', 0.0),
        unit='', level='0',
        formula_repr='корень β_λ(g*, λ*) = 0',
        source='quantum_gravity.py: УФ-точка FRG',
        comment=f'λ* = {frg.get("lambda_star", 0.0):.4f}',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'QG_FRG_THETA1', frg.get('theta1', 0.0),
        unit='', level='0',
        formula_repr='eigenvalue₁(J)',
        source='quantum_gravity.py: критическая экспонента (v1.1)',
        comment=f'θ₁ = {frg.get("theta1", 0.0):.4f}',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'QG_FRG_THETA2', frg.get('theta2', 0.0),
        unit='', level='0',
        formula_repr='eigenvalue₂(J)',
        source='quantum_gravity.py: критическая экспонента (v1.1)',
        comment=f'θ₂ = {frg.get("theta2", 0.0):.4f}',
        overwrite=True,
    )
    n_registered += 1

    REGISTRY.register(
        'QG_FRG_N_POINTS', frg.get('n_points', 0),
        unit='', level='1',
        formula_repr='len(find_all_fixed_points(1.0))',
        source='quantum_gravity.py: число фиксированных точек',
        comment=f'Найдено точек: {frg.get("n_points", 0)}',
        overwrite=True,
    )
    n_registered += 1

    if verbose:
        print(f"  📊 quantum_gravity: зарегистрировано {n_registered} констант")

    return n_registered


# Автоматическая регистрация при импорте
_REGISTERED_COUNT = _register_qg_constants(verbose=False)


# ============================================================================
# ЧАСТЬ 8: ТОЧКА ВХОДА
# ============================================================================

if __name__ == '__main__':
    print("=" * 70)
    print("  КВАНТОВАЯ ГРАВИТАЦИЯ ИЗ SU(26)")
    print("  Полная верификация")
    print("=" * 70)

    results = compute_all(N_eff=1.0)

    # 1. Планковская масса
    pm = results['planck_mass']
    print(f"\n[1/6] Планковская масса")
    print(f"  M_Pl = {pm['M_Pl_GeV']:.4e} ГэВ")
    print(f"  Отклонение: {pm['deviation_percent']:.4f}%")
    print(f"  Верификация: {'✅' if pm['verified'] else '❌'}")

    # 2. Постоянная Ньютона
    nc = results['newton_constant']
    print(f"\n[2/6] Постоянная Ньютона")
    print(f"  G = {nc['G_computed']:.4e} м³/(кг·с²)")
    print(f"  Отклонение: {nc['deviation_percent']:.4f}%")
    print(f"  Верификация: {'✅' if nc['verified'] else '❌'}")

    # 3. Квантовые поправки
    qc = results['quantum_corrections']
    print(f"\n[3/6] Квантовые поправки")
    print(f"  ΔS₁ = {qc['delta_S1']:.6f}")
    print(f"  ΔS₂ = {qc['delta_S2']:.2e}")
    print(f"  S_eff = {qc['S_eff']:.4f}")
    print(f"  Ряд сходится: {'✅' if qc['series_converges'] else '❌'}")

    # 4. Космологическая постоянная
    lc = results['cosmological_constant']
    print(f"\n[4/6] Космологическая постоянная")
    print(f"  Λ = {lc['Lambda']:.4e} м⁻²")
    print(f"  Отклонение: {lc['deviation_percent']:.4f}%")
    print(f"  Верификация: {'✅' if lc['verified'] else '❌'}")

    # 5. FRG анализ
    frg = results['frg']
    print(f"\n[5/6] FRG анализ")
    print(f"  Найдено точек: {frg['n_points']}")
    if frg['verified']:
        print(f"  УФ-точка: g* = {frg['g_star']:.4f}")
        print(f"            λ* = {frg['lambda_star']:.4f}")
        print(f"            θ₁ = {frg['theta1']:.4f}")
        print(f"            θ₂ = {frg['theta2']:.4f}")
    print(f"  Асимптотическая безопасность: {'✅' if frg['verified'] else '❌'}")

    # 6. Зависимость от N_eff
    print(f"\n[6/6] Зависимость от N_eff")
    print(f"  {'N_eff':>6} | {'g*':>8} | {'θ₁':>8} | {'θ₂':>8} | УФ-стаб.")
    print(f"  " + "-" * 50)
    for row in results['N_eff_dependence']:
        if row['uv_stable']:
            print(f"  {row['N_eff']:>6.1f} | {row['g_star']:>8.4f} | "
                  f"{row['theta1']:>8.4f} | {row['theta2']:>8.4f} | ✅")
        else:
            print(f"  {row['N_eff']:>6.1f} | {'---':>8} | {'---':>8} | "
                  f"{'---':>8} | ❌")

    # Регистрация констант
    print(f"\n  📊 Зарегистрировано в REGISTRY: {_REGISTERED_COUNT} констант")

    print("\n" + "=" * 70)
    if results['all_verified']:
        print("  ✅ ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ")
        print("  ✅ КВАНТОВАЯ ГРАВИТАЦИЯ ИЗ SU(26) ВЕРИФИЦИРОВАНА")
    else:
        print("  ❌ НЕКОТОРЫЕ ПРОВЕРКИ НЕ ПРОЙДЕНЫ")
    print("=" * 70)
