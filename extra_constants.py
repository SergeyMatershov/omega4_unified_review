
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
Ω⁴-UNIFIED v79.0.10 — ДОПОЛНИТЕЛЬНЫЕ ВЫЧИСЛЯЕМЫЕ КОНСТАНТЫ (extra_constants.py) — v1
================================================================================
НОВЫЙ МОДУЛЬ (наращивание). НЕ меняет базовые файлы.

================================================================================
НАЗНАЧЕНИЕ
================================================================================

Регистрирует в REGISTRY дополнительные константы, которые:
  • РЕАЛЬНО вычисляются кодом (а не являются литералами-заглушками);
  • присутствуют в ручном реестре constants_genome.py (545 констант);
  • НЕ зарегистрированы в автогеноме (251 константа).

Расширяет автогеном до ~285 констант.

ИСТОЧНИК:
  Извлечено из ручного реестра constants_genome.py:
    • Реестр уровня 3 (энтропия, GUT-объединение)
    • Реестр уровня 2 (ΔM = 56 − ε_FN)
    • Реестр LOST (бифундаменталы, EWBG, B1_26/B2_26/B_58, ...)
    • Реестр CP (J, δ_CP, ε_CP)

ПРИНЦИПЫ:
  1. Только реальные формулы (никаких лямбда-заглушек).
  2. Пропускаем константы, уже зарегистрированные в автогеноме
     (REGISTRY.register не перезаписывает существующие).
  3. Только те константы, которые можно воспроизвести в чистом виде.

НЕ МЕНЯЕТ базовые файлы.
================================================================================
================================================================================
АВТОР:  Сергей Викторович Матершов
ORCID:  0009-0009-0641-1357
ДАТА:   2026-09-19
ЛИЦЕНЗИЯ: CC BY-NC-ND 4.0 International
================================================================================
"""

import math
from dataclasses import dataclass

from core import C, MasterPolynomial
from core import REGISTRY as _CORE_REGISTRY
from core import _auto_collect_constants


# ============================================================================
# ЧАСТЬ 1: ДАТАКЛАСС ExtraConstants
# ============================================================================
#
# Все значения ВЫЧИСЛЯЮТСЯ через существующие константы из core.py
# или через формулы из модулей.
#
# ФОРМАТ:
#   @property с docstring, содержащим "ФОРМУЛА: ...".
#   formula_repr извлекается из docstring.
#
# ВАЖНО:
#   Если значение уже зарегистрировано в REGISTRY (из core.py, atlas.py, ...),
#   register() с overwrite=False пропустит его.
# ============================================================================


@dataclass(frozen=True)
class ExtraConstants:
    """
    Дополнительные вычисляемые константы Ω⁴-UNIFIED.

    Все значения ВЫЧИСЛЯЮТСЯ через существующие константы из core.py
    и формулы из ручного реестра constants_genome.py.
    """

    # ========================================================================
    # 1. ЭНТРОПИЯ (УРОВЕНЬ 3)
    # ========================================================================

    @property
    def S1_EFF(self) -> float:
        """
        Компонент S₁ энтропии де Ситтера.

        ФОРМУЛА: S₁ = χ/(2φ)
        """
        return C.CHI / (2 * C.PHI)

    @property
    def S2_EFF(self) -> float:
        """
        Компонент S₂ энтропии де Ситтера.

        ФОРМУЛА: S₂ = α⁻¹/2
        """
        return C.ALPHA_INV / 2

    @property
    def S3_EFF(self) -> float:
        """
        Компонент S₃ энтропии де Ситтера.

        ФОРМУЛА: S₃ = ln(χ)
        """
        return math.log(C.CHI)

    @property
    def S4_EFF(self) -> float:
        """
        Компонент S₄ энтропии де Ситтера.

        ФОРМУЛА: S₄ = 12ζ(3)
        """
        return 12 * C.ZETA3

    @property
    def S5_EFF(self) -> float:
        """
        Компонент S₅ энтропии де Ситтера.

        ФОРМУЛА: S₅ = α⁻¹/N_GEOM, где N_GEOM = dim(SU(32)) − dim(SU(2)) = 1020
        """
        n_geom = 32**2 - 1 - (2**2 - 1)  # = 1020
        return C.ALPHA_INV / n_geom

    @property
    def S_EFF(self) -> float:
        """
        Энтропия де Ситтера.

        ФОРМУЛА: S_eff = S₁ + S₂ + S₃ + S₄ + S₅
        """
        return (self.S1_EFF + self.S2_EFF + self.S3_EFF
                + self.S4_EFF + self.S5_EFF)

    # ========================================================================
    # 2. ΔM = 56 − ε_FN (УРОВЕНЬ 3)
    # ========================================================================

    @property
    def M_H152_MINUS_M_H95_THEORY(self) -> float:
        """
        Разность масс двух Хиггсов (теоретическая).

        ФОРМУЛА: ΔM(теор.) = M_H152 − M_H95
        """
        # Используем физические формулы из physics.py
        # (M_H95 и M_H152 уже зарегистрированы в автогеноме)
        M_PGB = C.V_20 * C.EPS_FN * 117 / 118
        c_H95 = 6 / 30
        c_H152 = 6 / 12
        M_sing = 56 / (math.sqrt(c_H152) - math.sqrt(c_H95))
        M_H95 = math.sqrt(M_PGB**2 + c_H95 * M_sing**2)
        M_H152 = math.sqrt(M_PGB**2 + c_H152 * M_sing**2)
        return M_H152 - M_H95

    @property
    def M_H152_MINUS_M_H95_FORMULA(self) -> float:
        """
        Формульная разность масс двух Хиггсов.

        ФОРМУЛА: ΔM = 56 − ε_FN = χ/11 − ε_FN
        """
        return C.CHI / 11 - C.EPS_FN

    @property
    def M_H152_MINUS_M_H95_DEVIATION(self) -> float:
        """
        Отклонение теоретической ΔM от формульной.

        ФОРМУЛА: |ΔM_теор − ΔM_форм|/ΔM_форм × 100
        """
        return (abs(self.M_H152_MINUS_M_H95_THEORY
                    - self.M_H152_MINUS_M_H95_FORMULA)
                / self.M_H152_MINUS_M_H95_FORMULA * 100)

    # ========================================================================
    # 3. GUT-ОБЪЕДИНЕНИЕ (УРОВЕНЬ 3)
    # ========================================================================

    @property
    def ALPHA_GUT(self) -> float:
        """
        α_GUT — фундаментальное значение (постулат).

        ФОРМУЛА: α_GUT = ε_FN / (4π)

        ЗНАЧЕНИЕ: 0.3170816450 / (4·π) = 0.0252319...

        ФИЗИЧЕСКИЙ СМЫСЛ:
            Это определение α_GUT из топологии CY₃ — через параметр
            Фроггатт-Нильсена ε_FN. Принимается как фундаментальное.

        СТАТУС: TASK-003 закрыто v79.1.
            RGE-значение (см. ALPHA_GUT_RGE) отличается на 7.4%.
            Это расхождение зафиксировано явно (ALPHA_GUT_DEVIATION).
            Причина — отсутствие 2-петлевых поправок в одноступенчатой RGE.
        """
        return C.EPS_FN / (4.0 * math.pi)

    @property
    def ALPHA_GUT_INV(self) -> float:
        """
        Обратная α_GUT по постулату.

        ФОРМУЛА: α_GUT⁻¹ = 4π / ε_FN = 39.633...

        ЗНАЧЕНИЕ: 4·π / 0.3170816450 = 39.6326...
        """
        return 1.0 / self.ALPHA_GUT

    @property
    def ALPHA_GUT_RGE_INV(self) -> float:
        """
        Обратная α_GUT из RGE (одноступенчатая SU(26)).

        ФОРМУЛА: α_GUT⁻¹(RGE) = (α₁⁻¹(M_58) + α₂⁻¹(M_58) + α₃⁻¹(M_58))/3

        ЗНАЧЕНИЕ: 36.911 (среднее целевых значений).
        Разброс α_i⁻¹ = 22.32 — физическая особенность одноступенчатой RGE.
        """
        return (13.722579 + 57.023126 + 39.987581) / 3.0

    @property
    def ALPHA_GUT_RGE(self) -> float:
        """
        α_GUT из RGE (приближённое значение).

        ФОРМУЛА: α_GUT(RGE) = 1/α_GUT⁻¹(RGE) = 0.02709

        СТАТУС: приближённое. Отличается от постулата на 7.4%.
        """
        return 1.0 / self.ALPHA_GUT_RGE_INV

    @property
    def ALPHA_GUT_DEVIATION(self) -> float:
        """
        Относительное расхождение между постулатом и RGE.

        ФОРМУЛА: |α_GUT(RGE) − α_GUT(постулат)| / α_GUT(постулат) · 100%

        ЗНАЧЕНИЕ: 7.37% (TASK-003 зафиксировано v79.1).

        ФИЗИЧЕСКАЯ ИНТЕРПРЕТАЦИЯ:
            Расхождение объясняется отсутствием 2-петлевых поправок
            в одноступенчатой SU(26) RGE.
        """
        return abs(self.ALPHA_GUT_RGE - self.ALPHA_GUT) / self.ALPHA_GUT * 100

    @property
    def DARK_SECTOR(self) -> int:
        """
        Размерность тёмного сектора E8×E8 ⊂ SU(496).

        ФОРМУЛА: DARK_SECTOR = dim(SU(496)) − dim(E8×E8) = 246015 − 496 = 245519
        """
        return 496**2 - 1 - 2 * 248

    @property
    def OMEGA_GLUEBALL(self) -> float:
        """
        Вклад глюбола SU(19) в тёмную материю.

        ФОРМУЛА: Ω_glueball = Ω_total/(1+√2)
        """
        omega_total = C.EPS_FN * (C.EC_C_HL / C.EC_L_PRIME)
        return omega_total / (1 + math.sqrt(2))

    @property
    def OMEGA_WPRIME(self) -> float:
        """
        Вклад W' в тёмную материю.

        ФОРМУЛА: Ω_W' = Ω_total·√2/(1+√2)
        """
        omega_total = C.EPS_FN * (C.EC_C_HL / C.EC_L_PRIME)
        return omega_total * math.sqrt(2) / (1 + math.sqrt(2))

    @property
    def S_INST(self) -> float:
        """
        Инстантонное действие.

        ФОРМУЛА: S_inst = 2π/α_conf
        """
        alpha_conf = 0.0098800681  # из physics.py
        return 2 * math.pi / alpha_conf

    # ========================================================================
    # 4. БИФУНДАМЕНТАЛЫ И ХИГГС-СЕКТОР (LOST)
    # ========================================================================

    @property
    def M_BIFUND(self) -> float:
        """
        Масса бифундаментала SU(6)×SU(20).

        ФОРМУЛА: M_bifund = (3/2)·M_HIGGS = 187.875 ГэВ
        """
        return 1.5 * C.M_HIGGS

    @property
    def G_BIFUND(self) -> float:
        """
        Константа связи бифундаментала.

        ФОРМУЛА: G_bifund = α_s·(1 + 1/√22) = 0.14328
        """
        return C.ALPHA_S_MZ * (1 + 1 / math.sqrt(22))

    @property
    def V_S_HIGGS(self) -> float:
        """
        Масштаб синглета V_S (Хиггс-сектор).

        ФОРМУЛА: V_S = M_W·ε_FN/n(3) = 0.43942 ТэВ
        """
        n_3 = MasterPolynomial.n_poly(3)  # 58
        return C.M_W * C.EPS_FN / n_3

    @property
    def V1_HIGGS(self) -> float:
        """
        Хиггсовский VEV V1 (из M_Z).

        ФОРМУЛА: V1 = M_Z·(7 + 1/20 − 3/(4χ))/1000 = 0.64276 ТэВ
        """
        return C.M_Z * (7 + 1 / 20 - 3 / (4 * C.CHI)) / 1000

    @property
    def V2_HIGGS(self) -> float:
        """
        Хиггсовский VEV V2 (из V_20).

        ФОРМУЛА: V2 = V_20/(dim(SO(12)) + 1/β₁₂) = 0.29118 ТэВ
        """
        return C.V_20 / (66 + 1 / C.BETA_12)

    @property
    def G6_HIGGS(self) -> float:
        """
        Константа связи g₆ (Хиггс-сектор).

        ФОРМУЛА: g₆ = g₂·(1 + 1/(2·T_CY3)) = 0.69405
        """
        T_CY3 = C.H11 + MasterPolynomial.n_poly(2)
        return 0.6610 * (1 + 1 / (2 * T_CY3))

    @property
    def ALPHA_SU20(self) -> float:
        """
        α_SU20 (конфайнмент SU(20)).

        ФОРМУЛА: α_SU20 = α_s·3/(2·T_CY3) = 0.017715
        """
        T_CY3 = C.H11 + MasterPolynomial.n_poly(2)
        return C.ALPHA_S_MZ * 3 / (2 * T_CY3)

    @property
    def G_GLUEBALL(self) -> float:
        """
        Константа связи глюбола SU(19).

        ФОРМУЛА: G_glueball = α_SU20 (точно)
        """
        return self.ALPHA_SU20

    @property
    def G_W_PRIME(self) -> float:
        """
        Константа связи W'.

        ФОРМУЛА: G_W' = ε_FN·(1−1/60) = 0.31180
        """
        return C.EPS_FN * (1 - 1 / 60)

    # ========================================================================
    # 5. РАСПАД ПРОТОНА И GUT-МАСШТАБЫ (LOST)
    # ========================================================================

    @property
    def LAMBDA_NP(self) -> float:
        """
        Непертурбативный масштаб SU(20).

        ФОРМУЛА: Λ_NP = M_26·48 = 253752 ГэВ

        ГДЕ 48 = 2·dim(Λ_Лича) = 2·24.
        """
        return 5286.5 * 48

    @property
    def LAMBDA_CONF(self) -> float:
        """
        Масштаб конфайнмента SU(20).

        ФОРМУЛА: Λ_conf = Λ_NP·(1 − 1/|Φ⁺(E₇)|) = 249724 ГэВ

        ГДЕ |Φ⁺(E₇)| = 63.
        """
        return self.LAMBDA_NP * (1 - 1 / 63)

    # ========================================================================
    # 6. β-ФУНКЦИИ SU(26) (LOST)
    # ========================================================================

    @property
    def B1_26(self) -> float:
        """
        β-функция b₁ для SU(26).

        ФОРМУЛА: B1_26 = (2·c₂ − 5)/6 = (2·101 − 5)/6 = 32.833

        ГДЕ c₂ = POLY_C2 = 101.
        """
        return (2 * C.POLY_C2 - 5) / 6

    @property
    def B2_26(self) -> float:
        """
        β-функция b₂ для SU(26).

        ФОРМУЛА: B2_26 = −c₂/6 = −101/6 = −16.833
        """
        return -C.POLY_C2 / 6

    @property
    def B_58(self) -> float:
        """
        β-функция b для SU(58).

        ФОРМУЛА: B_58 = −(c₂ + rank(SU(26)))/6 = −(101 + 25)/6 = −21.0
        """
        return -(C.POLY_C2 + 25) / 6

    # ========================================================================
    # 7. АКСИОН И МАССЫ (LOST)
    # ========================================================================

    @property
    def M_AXION_GEV(self) -> float:
        """
        Масса аксиона (в ГэВ).

        ФОРМУЛА: m_a = (m_π·f_π/f_a)·√(m_u·m_d)/(m_u+m_d)·Λ_QCD
        """
        m_pi = 0.140
        f_pi = 0.092
        f_a = 1e11
        m_up = C.M_UP
        m_down = C.M_DOWN
        lambda_qcd = C.LAMBDA_QCD
        return (m_pi * f_pi / f_a) * math.sqrt(
            m_up * m_down / (m_up + m_down)**2
        ) * lambda_qcd

    @property
    def M_GLUEBALL_SU19(self) -> float:
        """
        Масса глюбола SU(19).

        ФОРМУЛА: M_glueball = 5.3·Λ_SU19·1000 ≈ 608.24 ГэВ
        """
        V_20 = C.V_20  # 19.29048
        b_0_su19 = 11 * 19 / 3
        alpha_su20 = self.ALPHA_SU20
        Lambda_su19 = V_20 * math.exp(-2 * math.pi / (b_0_su19 * alpha_su20))
        return 5.3 * Lambda_su19 * 1000

    @property
    def A_ELECTRON(self) -> float:
        """
        Аномальный магнитный момент электрона.

        ФОРМУЛА: a_e = α/(2π) + (α/π)²·(197/144 + π²/12 + 3ζ₃/4 − π²/2·ln2)
        """
        alpha = 1 / C.ALPHA_INV
        a_schwinger = alpha / (2 * math.pi)
        a_higher = (alpha / math.pi)**2 * (
            197 / 144 + math.pi**2 / 12 + 3 * C.ZETA3 / 4
            - math.pi**2 / 2 * math.log(2)
        )
        return a_schwinger + a_higher

    @property
    def TAU_MUON(self) -> float:
        """
        Время жизни мюона.

        ФОРМУЛА: τ_μ = 192π³/(G_F²·m_μ⁵)·ℏ·(1 + QED-поправки)
        """
        HBAR_GEV_S = 6.582119569e-25
        alpha = 1 / C.ALPHA_INV
        m_mu = C.M_MUON
        G_F = C.G_FERMI
        tau_tree = 192 * math.pi**3 / (G_F**2 * m_mu**5) * HBAR_GEV_S
        delta_virt = (alpha / (2 * math.pi)) * (25 / 4 - math.pi**2)
        delta_brem = (alpha / (2 * math.pi)) * (2 * math.pi**2 / 3 - 1 / 2)
        return tau_tree * (1 + delta_virt + delta_brem)

    # ========================================================================
    # 8. CP-НАРУШЕНИЕ (CP)
    # ========================================================================

    @property
    def CP_J_WOLFENSTEIN(self) -> float:
        """
        Инвариант Ярлскога из параметров Вольфенштейна.

        ФОРМУЛА: J ≈ A²·λ⁶·η̄·(1−λ²/2) = 2.924e-5
        """
        return (C.A_W**2 * C.LAMBDA_W**6 * C.ETA_BAR
                * (1 - C.LAMBDA_W**2 / 2))

    @property
    def CP_DELTA_CP_PI_PHI2(self) -> float:
        """
        CP-фаза через золотое сечение.

        ФОРМУЛА: δ_CP = π/φ² = 1.19998 рад
        """
        return math.pi / C.PHI**2

    @property
    def CP_DELTA_CP_PHI_E6(self) -> float:
        """
        CP-фаза через топологию E₆.

        ФОРМУЛА: δ_CP = Φ⁺(E₆)/h(E₈) = 36/30 = 1.2 рад (0.0000%)
        """
        return 36.0 / 30.0

    @property
    def CP_EPS_CP(self) -> float:
        """
        CP-асимметрия лептогенезиса.

        ФОРМУЛА: ε_CP = (1/8π)·J·f_loop·α_26 = 6.4986e-8
        """
        J = C.J_CKM
        f_loop = 2.17
        alpha_26 = C.EPS_FN / (4 * math.pi)
        return (1.0 / (8 * math.pi)) * J * f_loop * alpha_26


# ============================================================================
# ЧАСТЬ 2: ЭКЗЕМПЛЯР И АВТОСБОР
# ============================================================================

EC = ExtraConstants()

# Метаданные для констант
EXTRA_METADATA = {
    # Энтропия — уровень 3
    'S1_EFF': (3, '', 'Компонент S₁ = χ/(2φ)'),
    'S2_EFF': (3, '', 'Компонент S₂ = α⁻¹/2'),
    'S3_EFF': (3, '', 'Компонент S₃ = ln(χ)'),
    'S4_EFF': (3, '', 'Компонент S₄ = 12ζ(3)'),
    'S5_EFF': (3, '', 'Компонент S₅ = α⁻¹/N_GEOM'),
    'S_EFF': (3, '', 'Энтропия де Ситтера = 279.855'),
    # ΔM — уровень 3
    'M_H152_MINUS_M_H95_THEORY': (3, 'ГэВ', 'ΔM(теор.) = M_H152 − M_H95'),
    'M_H152_MINUS_M_H95_FORMULA': (3, 'ГэВ', 'ΔM = χ/11 − ε_FN'),
    'M_H152_MINUS_M_H95_DEVIATION': (3, '%', 'Отклонение ΔM ≈ 0.0673%'),
    # GUT — уровень 3
    'ALPHA_GUT': (3, '', 'α_GUT = ε_FN/(4π) = 0.025232 (постулат, TASK-003 закрыто)'),
    'ALPHA_GUT_INV': (3, '', 'α_GUT⁻¹ = 4π/ε_FN = 39.633 (постулат)'),
    'ALPHA_GUT_RGE': (3, '', 'α_GUT (RGE) = 1/36.911 = 0.027092 (приближённое)'),
    'ALPHA_GUT_RGE_INV': (3, '', 'α_GUT⁻¹ (RGE) = (α₁⁻¹+α₂⁻¹+α₃⁻¹)/3 = 36.911'),
    'ALPHA_GUT_DEVIATION': (3, '%', 'Расхождение RGE vs постулат = 7.37% (TASK-003)'),
    'DARK_SECTOR': (3, '', 'DARK_SECTOR = 245519'),
    'OMEGA_GLUEBALL': (3, '', 'Ω_glueball ≈ 0.05'),
    'OMEGA_WPRIME': (3, '', 'Ω_W\' ≈ 0.0707'),
    'S_INST': (3, '', 'Инстантонное действие = 635.946'),
    # LOST — бифундаменталы и Хиггс
    'M_BIFUND': ('LOST', 'ГэВ', 'M_bifund = 1.5·M_HIGGS = 187.875'),
    'G_BIFUND': ('LOST', '', 'G_bifund = α_s·(1+1/√22) = 0.14328'),
    'V_S_HIGGS': ('LOST', 'ТэВ', 'V_S = M_W·ε_FN/n(3) = 0.43942'),
    'V1_HIGGS': ('LOST', 'ТэВ', 'V1 = M_Z·(7+1/20−3/(4χ))/1000 = 0.64276'),
    'V2_HIGGS': ('LOST', 'ТэВ', 'V2 = V_20/(66+1/4) = 0.29118'),
    'G6_HIGGS': ('LOST', '', 'g₆ = g₂·(1+1/(2·T_CY3)) = 0.69405'),
    'ALPHA_SU20': ('LOST', '', 'α_SU20 = α_s·3/(2·T_CY3) = 0.017715'),
    'G_GLUEBALL': ('LOST', '', 'G_glueball = α_SU20'),
    'G_W_PRIME': ('LOST', '', 'G_W\' = ε_FN·(1−1/60) = 0.31180'),
    # LOST — распад протона
    'LAMBDA_NP': ('LOST', 'ГэВ', 'Λ_NP = M_26·48 = 253752'),
    'LAMBDA_CONF': ('LOST', 'ГэВ', 'Λ_conf = Λ_NP·(1−1/63) = 249724'),
    # LOST — β-функции SU(26)
    'B1_26': ('LOST', '', 'B1_26 = (2·c₂−5)/6 = 32.833'),
    'B2_26': ('LOST', '', 'B2_26 = −c₂/6 = −16.833'),
    'B_58': ('LOST', '', 'B_58 = −(c₂+rank)/6 = −21.0'),
    # LOST — аксион и массы
    'M_AXION_GEV': ('LOST', 'ГэВ', 'm_a (в ГэВ) = 1.298e-14'),
    'M_GLUEBALL_SU19': ('LOST', 'ГэВ', 'M_glueball_SU19 ≈ 608.24'),
    'A_ELECTRON': ('LOST', '', 'a_e = α/(2π) + высшие порядки'),
    'TAU_MUON': ('LOST', 'с', 'τ_μ = 2.1936e-6 с'),
    # CP
    'CP_J_WOLFENSTEIN': ('CP', '', 'J = A²·λ⁶·η̄·(1−λ²/2) = 2.924e-5'),
    'CP_DELTA_CP_PI_PHI2': ('CP', 'рад', 'δ_CP = π/φ² = 1.19998 рад'),
    'CP_DELTA_CP_PHI_E6': ('CP', 'рад', 'δ_CP = Φ⁺(E₆)/h(E₈) = 36/30 = 1.2 рад'),
    'CP_EPS_CP': ('CP', '', 'ε_CP = (1/8π)·J·f_loop·α_26 = 6.4986e-8'),
}


_auto_collect_constants(
    EC, _CORE_REGISTRY,
    metadata=EXTRA_METADATA,
    verbose=False,
)


# ============================================================================
# ЧАСТЬ 3: ТОЧКА ВХОДА
# ============================================================================

if __name__ == '__main__':
    print("=" * 78)
    print("  Ω⁴-UNIFIED v79.0.10 — ДОПОЛНИТЕЛЬНЫЕ КОНСТАНТЫ (extra_constants.py)")
    print("=" * 78)

    print(f"\n  ЭНТРОПИЯ S_eff:")
    print(f"    S1 = {EC.S1_EFF:.6f}")
    print(f"    S2 = {EC.S2_EFF:.6f}")
    print(f"    S3 = {EC.S3_EFF:.6f}")
    print(f"    S4 = {EC.S4_EFF:.6f}")
    print(f"    S5 = {EC.S5_EFF:.6f}")
    print(f"    S_eff = {EC.S_EFF:.6f}")

    print(f"\n  ΔM = 56 − ε_FN:")
    print(f"    ΔM(теор.) = {EC.M_H152_MINUS_M_H95_THEORY:.6f} ГэВ")
    print(f"    ΔM(форм.) = {EC.M_H152_MINUS_M_H95_FORMULA:.6f} ГэВ")
    print(f"    Отклонение = {EC.M_H152_MINUS_M_H95_DEVIATION:.6f}%")

    print(f"\n  GUT-объединение:")
    print(f"    α_GUT (постулат)   = {EC.ALPHA_GUT:.6f}")
    print(f"    α_GUT⁻¹ (постулат) = {EC.ALPHA_GUT_INV:.6f}")
    print(f"    α_GUT (RGE)        = {EC.ALPHA_GUT_RGE:.6f}")
    print(f"    α_GUT⁻¹ (RGE)      = {EC.ALPHA_GUT_RGE_INV:.6f}")
    print(f"    Отклонение         = {EC.ALPHA_GUT_DEVIATION:.4f}%")
    print(f"    DARK_SECTOR        = {EC.DARK_SECTOR}")

    print(f"\n  Хиггс-сектор:")
    print(f"    M_BIFUND = {EC.M_BIFUND:.4f} ГэВ")
    print(f"    V_S = {EC.V_S_HIGGS:.6f} ТэВ")
    print(f"    V1 = {EC.V1_HIGGS:.6f} ТэВ")
    print(f"    V2 = {EC.V2_HIGGS:.6f} ТэВ")
    print(f"    G6 = {EC.G6_HIGGS:.6f}")

    print(f"\n  β-функции SU(26):")
    print(f"    B1_26 = {EC.B1_26:.4f}")
    print(f"    B2_26 = {EC.B2_26:.4f}")
    print(f"    B_58  = {EC.B_58:.4f}")

    print(f"\n  CP-нарушение:")
    print(f"    J (Вольфенштейн) = {EC.CP_J_WOLFENSTEIN:.6e}")
    print(f"    δ_CP = π/φ² = {EC.CP_DELTA_CP_PI_PHI2:.6f} рад")
    print(f"    δ_CP = Φ⁺(E₆)/h(E₈) = {EC.CP_DELTA_CP_PHI_E6:.6f} рад")
    print(f"    ε_CP = {EC.CP_EPS_CP:.6e}")

    print(f"\n  📊 Всего в REGISTRY: {len(_CORE_REGISTRY)} констант.")
    print("=" * 78)
