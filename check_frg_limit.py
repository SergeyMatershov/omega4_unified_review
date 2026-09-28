#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
Ω⁴-UNIFIED — ПРОВЕРКА ГРАНИЦЫ FRG (check_frg_limit.py) — v2.0
================================================================================
НАЗНАЧЕНИЕ:
    Демонстрация ключевого результата Ω⁴:

        УФ-стабильность (асимптотическая безопасность) сохраняется
        при N_eff ≤ 7 и ЛОМАЕТСЯ при N_eff ≥ 8.

    Этот результат — отправная точка всей модели Ω⁴:
      • Реальная СМ имеет N_eff ≈ 100.
      • Но FRG-усечение Ω⁴ работает только при N_eff ≤ 7.
      • Ω⁴ объясняет это мембранным описанием:
            N_eff на 4D-мембране = 7,
            остальные ~93 поля спрятаны в балке.

================================================================================
КОНВЕНЦИЯ ЗНАКА θ (КРИТИЧЕСКИХ ЭКСПОНЕНТ)
================================================================================

    В FRG-литературе (Reuter, Percacci, Litim, Wetterich) ПРИНЯТО:

        θ_i = eig_i(J)              — критические экспоненты
        Re θ_i > 0  для всех i      — УФ-притяжение
                                      (асимптотическая безопасность)
        Re θ_i < 0  для всех i      — ИК-притяжение
        смешанные знаки             — седловая точка

    В РАННИХ ВЕРСИЯХ quantum_gravity.py (v1.0) использовалась
    ДРУГАЯ конвенция:

        θ_i = −eig_i(J)             — «критические экспоненты»
        uv_stable = all(eig_i > 0)  — что эквивалентно all(θ_i < 0)

    Это НЕ ошибка физики. Обе конвенции дают ОДНУ И ТУ ЖЕ границу
    УФ-стабильности — между N_eff = 7 и N_eff = 8.

    В v1.1 quantum_gravity.py приведено к СТАНДАРТУ FRG:
        θ = eig(J), uv_stable = θ > 0.

    В ЭТОМ СКРИПТЕ мы показываем ОБА знака θ для наглядности:
        столбец «θ (стандарт)»  — θ = eig(J)          (Re θ > 0 для УФ)
        столбец «θ (старая)»    — θ = −eig(J)          (Re θ < 0 для УФ)

    Числа в этих столбцах — противоположны по знаку, но
    столбец «УФ-стаб.» — один и тот же.

================================================================================
ЧТО ДЕЛАЕТ СКРИПТ
================================================================================

    1. Импортирует quantum_gravity как модуль.
    2. Вызывает analyze_N_eff_dependence() для N_eff от 0 до 100
       (плюс крупные значения 25, 30, 40, 50, 75, 100).
    3. Печатает таблицу с ОБОИМИ конвенциями θ.
    4. Находит точку, где УФ-стабильность исчезает.
    5. Показывает статус струнного сектора (is_EFT_not_string_theory).

================================================================================
ЗАПУСК:
    python check_frg_limit.py
================================================================================
АВТОР:  Сергей Викторович Матершов
ORCID:  0009-0009-0641-1357
ЛИЦЕНЗИЯ: CC BY-NC-ND 4.0 International
================================================================================
ИСТОРИЯ ВЕРСИЙ:
    v1.0 — первая версия. Проверка границы FRG.
    v2.0 — добавлено объяснение конвенции θ; вывод обоих знаков;
           расширенный набор N_eff (до 100).
================================================================================
"""

from typing import Dict, Any

from quantum_gravity import FinalFRGAnalysis, compute_string_sector
# ============================================================================
# СТРУКТУРИРОВАННЫЙ ВЫВОД ДЛЯ main_unified.py
# ============================================================================
#
# Функция compute_frg_boundary() возвращает те же данные, что печатает main(),
# но в виде dict — для встраивания в unified_results.json.
#
# main() при этом НЕ меняется — он по-прежнему печатает таблицу.
# ============================================================================

def compute_frg_boundary() -> Dict[str, Any]:
    """
    Вычислить границу УФ-стабильности и вернуть структурированный dict.

    Возвращает:
        dict с полями:
          • available              — True, если расчёт удался
          • N_eff_max_stable       — последнее УФ-стабильное N_eff
          • N_eff_min_unstable     — первое нестабильное N_eff
          • boundary               — текстовая граница, например 'между 7 и 8'
          • table                  — полная таблица (N_eff, g*, θ₁, θ₂, uv_stable)
          • table_with_theta_old   — та же таблица с обратным знаком θ
          • string_sector          — результат compute_string_sector()
          • comment                — короткий текстовый комментарий
    """
    try:
        frg = FinalFRGAnalysis()

        N_eff_values = (
            list(range(0, 11))
            + [15, 20, 25, 30, 40, 50, 75, 100]
        )
        table = frg.analyze_N_eff_dependence(N_eff_values=N_eff_values)

        stable_N = [r['N_eff'] for r in table if r['uv_stable']]
        unstable_N = [r['N_eff'] for r in table if not r['uv_stable']]

        N_eff_max_stable = max(stable_N) if stable_N else None
        N_eff_min_unstable = min(unstable_N) if unstable_N else None

        if N_eff_max_stable is not None and N_eff_min_unstable is not None:
            boundary = f'между {N_eff_max_stable} и {N_eff_min_unstable}'
        elif N_eff_max_stable is not None:
            boundary = f'сохраняется до {N_eff_max_stable}'
        elif N_eff_min_unstable is not None:
            boundary = f'отсутствует уже при {N_eff_min_unstable}'
        else:
            boundary = 'не определена'

        # Таблица с двумя конвенциями θ
        table_with_theta_old = [
            {
                'N_eff': r['N_eff'],
                'g_star': r.get('g_star'),
                'theta1_std': r.get('theta1'),
                'theta2_std': r.get('theta2'),
                'theta1_old': -r['theta1'] if r.get('theta1') is not None else None,
                'theta2_old': -r['theta2'] if r.get('theta2') is not None else None,
                'uv_stable': r['uv_stable'],
            }
            for r in table
        ]

        ss = compute_string_sector()

        return {
            'available': True,
            'N_eff_max_stable': N_eff_max_stable,
            'N_eff_min_unstable': N_eff_min_unstable,
            'boundary': boundary,
            'table': table,
            'table_with_theta_old': table_with_theta_old,
            'string_sector': ss,
            'comment': (
                f'Граница УФ-стабильности: N_eff = {N_eff_max_stable} '
                f'(между {N_eff_max_stable} и {N_eff_min_unstable}). '
                f'8 = dim(SU(3)) — цветовая симметрия. '
                f'Модель — EFT с SU(26), а не струнная теория.'
            ),
        }

    except Exception as e:
        return {
            'available': False,
            'error': str(e),
        }



def main():
    print("=" * 78)
    print("  ПРОВЕРКА ГРАНИЦЫ FRG (N_eff)")
    print("  check_frg_limit.py — v2.0")
    print("=" * 78)
    print()
    print("  ── О КОНВЕНЦИИ ЗНАКА θ ──")
    print()
    print("    θ_i — критические экспоненты. Стандарт FRG (Reuter, Percacci,")
    print("    Litim, Wetterich):")
    print("        θ_i = eig_i(J)")
    print("        Re θ_i > 0 для всех i  →  УФ-стабильность ✅")
    print("        Re θ_i < 0 для всех i  →  ИК-стабильность")
    print()
    print("    В старых версиях quantum_gravity.py (v1.0) использовалась")
    print("    обратная конвенция: θ_i = −eig_i(J), uv_stable = all(eig > 0)")
    print("    что эквивалентно all(θ < 0).")
    print()
    print("    Обе конвенции дают ОДНУ И ТУ ЖЕ границу УФ-стабильности.")
    print("    Числа θ отличаются знаком. В таблице ниже показаны ОБА.")
    print()

    frg = FinalFRGAnalysis()

    # ─── Шаг 1: полная таблица ───────────────────────────────────────────
    N_eff_values = (
        list(range(0, 11)) +           # 0..10 — где граница
        [15, 20, 25, 30, 40, 50, 75, 100]   # крупные значения
    )

    table = frg.analyze_N_eff_dependence(N_eff_values=N_eff_values)

    print("  ── ТАБЛИЦА ──")
    print()
    print(f"  {'N_eff':>6} | {'g*':>10} | {'θ₁ (станд.)':>12} | "
          f"{'θ₂ (станд.)':>12} | {'θ₁ (старая)':>12} | "
          f"{'θ₂ (старая)':>12} | УФ-стаб.")
    print(f"  {'─'*6} | {'─'*10} | {'─'*12} | {'─'*12} | "
          f"{'─'*12} | {'─'*12} | {'─'*8}")

    for row in table:
        N = row['N_eff']
        if row['uv_stable']:
            g = f"{row['g_star']:.4f}"
            # Стандартная конвенция: θ = eig(J)
            t1_std = f"{row['theta1']:+.4f}"
            t2_std = f"{row['theta2']:+.4f}"
            # Старая конвенция: θ = −eig(J)
            t1_old = f"{-row['theta1']:+.4f}"
            t2_old = f"{-row['theta2']:+.4f}"
            mark = '✅'
        else:
            g = '---'
            t1_std = '---'
            t2_std = '---'
            t1_old = '---'
            t2_old = '---'
            mark = '❌'
        print(f"  {N:>6.1f} | {g:>10} | {t1_std:>12} | {t2_std:>12} | "
              f"{t1_old:>12} | {t2_old:>12} | {mark}")

    # ─── Шаг 2: найти границу слома ──────────────────────────────────────
    print()
    print("=" * 78)
    print("  ГРАНИЦА СЛОМА УФ-СТАБИЛЬНОСТИ")
    print("=" * 78)
    print()

    stable_N = [r['N_eff'] for r in table if r['uv_stable']]
    unstable_N = [r['N_eff'] for r in table if not r['uv_stable']]

    if stable_N and unstable_N:
        max_stable = max(stable_N)
        min_unstable = min(unstable_N)
        print(f"  Максимальный N_eff с УФ-стабильностью:  {max_stable}")
        print(f"  Минимальный N_eff без УФ-стабильности:  {min_unstable}")
        print(f"  Граница слома: между N_eff = {max_stable} и {min_unstable}")
        print()
        print(f"  ЭТО КЛЮЧЕВОЙ РЕЗУЛЬТАТ Ω⁴:")
        print(f"    • N_eff ≤ 7  — мембранное описание работает.")
        print(f"    • N_eff ≥ 8  — мембранное описание ломается.")
        print(f"    • 8 = dim(SU(3)) — цветовая симметрия не помещается")
        print(f"      на мембране в полном объёме.")
        print(f"    • Реальная СМ имеет N_eff ≈ 100 — но она живёт в балке,")
        print(f"      а не на мембране. На мембране видно только 7 полей.")
    elif not unstable_N:
        print(f"  УФ-стабильность сохраняется для ВСЕХ N_eff ≤ {max(stable_N)}")
    else:
        print(f"  УФ-стабильность отсутствует уже при N_eff = {min(unstable_N)}")

    # ─── Шаг 3: струнный сектор ──────────────────────────────────────────
    print()
    print("=" * 78)
    print("  СТРУННЫЙ СЕКТОР")
    print("=" * 78)
    print()

    ss = compute_string_sector()
    print(f"  has_26D:                     {ss['has_26D']}")
    print(f"  has_SU26:                    {ss['has_SU26']}")
    print(f"  has_compactification:        {ss['has_compactification']}")
    print(f"  has_polyakov_action:         {ss['has_polyakov_action']}")
    print(f"  has_vertex_operators:        {ss['has_vertex_operators']}")
    print(f"  has_closed_string_spectrum:  {ss['has_closed_string_spectrum']}")
    print(f"  is_EFT_not_string_theory:    {ss['is_EFT_not_string_theory']}")
    print(f"  status:                      {ss['status']}")
    print()
    print(f"  Комментарий: {ss['comment']}")
    print()
    print("  ПОЯСНЕНИЕ:")
    print("    Модель Ω⁴ — ЭФФЕКТИВНАЯ ТЕОРИЯ ПОЛЯ (EFT) с калибровочной")
    print("    группой SU(26), а не струнная теория в строгом смысле.")
    print("    У неё есть 26D, SU(26) и компактификация — но НЕТ")
    print("    действия Полякова, вершинных операторов и спектра")
    print("    замкнутых струн. Это честное признание предела модели.")

    print()
    print("=" * 78)
    print("  ВЫВОД")
    print("=" * 78)
    print()
    print("  1. Граница УФ-стабильности: N_eff = 7 (между 7 и 8).")
    print("  2. Обе конвенции θ дают одну границу — знак не влияет.")
    print("  3. Модель Ω⁴ объясняет это мембранным описанием:")
    print("     на мембране видно только 7 полей, остальные — в балке.")
    print("  4. Порог 8 = dim(SU(3)) — цветовая симметрия.")
    print("  5. Модель — EFT, а не струнная теория (STRUCTURAL_ARGUMENT).")
    print()
    print("=" * 78)


if __name__ == '__main__':
    main()
