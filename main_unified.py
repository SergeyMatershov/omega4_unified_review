#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
Ω⁴-UNIFIED — ОБЪЕДИНЁННЫЙ MAIN (main_unified.py) — v1.0
================================================================================
НАЗНАЧЕНИЕ:
    Единая точка входа, объединяющая три части:

        1. БАЗОВУЮ МОДЕЛЬ (main.py):
           • core, atlas, physics, quantum_gravity, compactification
           • 171/171 проверок
           • omega4_results.json

        2. ДОП-ПРОЕКТ (main_research.py v3.0):
           • 9 объединённых research-файлов
           • ~305 констант
           • research_results.json

        3. ДИАГНОСТИКУ FRG (check_frg_limit.py v2.0):
           • Таблица N_eff | g* | θ₁ | θ₂ | УФ-стаб.
           • Граница слома: между 7 и 8
           • Оба знака θ (стандарт FRG и старая конвенция)

    Плюс:

        4. АВТОГЕНОМ (genome_writer.py):
           • constants_genome_omega4.py
           • Полный REGISTRY: базовая модель + доп-проект

ПОРЯДОК РАБОТЫ:
    1. Базовая модель       → print_summary, save omega4_results.json
    2. Доп-проект           → print_report, save research_results.json
    3. check_frg_limit      → печать таблицы + compute_frg_boundary()
    4. Объединённый JSON    → unified_results.json
                              { "base_model": {...},
                                "research_project": {...},
                                "frg_boundary": {...},
                                "combined_summary": {...} }
    5. Автогеном            → constants_genome_omega4.py (один раз)

ВАЖНО:
    • main.py и main_research.py НЕ трогаем.
    • genome_writer вызывается ОДИН РАЗ — в самом конце.
    • check_frg_limit вызывается как модуль.
    • main.py НЕ вызывается как run_complete_analysis() — собираем
      по частям, чтобы отложить автогеном на конец.

ЗАПУСК:
    python main_unified.py
    python main_unified.py --no-genome
    python main_unified.py --no-save
    python main_unified.py --quiet
================================================================================
АВТОР:  Сергей Викторович Матершов
ORCID:  0009-0009-0641-1357
ДАТА:   2026-09-19
ЛИЦЕНЗИЯ: CC BY-NC-ND 4.0 International
================================================================================
ИСТОРИЯ ВЕРСИЙ:
    v1.0 — первая версия. Объединение main.py + main_research.py +
           check_frg_limit.py + genome_writer.py.
================================================================================
"""

import sys
import json
from datetime import datetime
from typing import Dict, Any


# ============================================================================
# ЧАСТЬ 1: ИМПОРТЫ
# ============================================================================

# ─── Базовая модель (main.py) ──────────────────────────────────────────────
from main import (
    Omega4Unified,
    HAS_QUANTUM_GRAVITY,
    HAS_COMPACTIFICATION,
    HAS_TOPOLOGICAL_ORIGIN,
)

# ─── Доп-проект (main_research.py v3.0) ────────────────────────────────────
from main_research import (
    run_all_research_files,
    research_summary,
    print_research_report,
    save_research_results,
    formulas_for_7,
    RESEARCH_FILES,
)

# ─── Диагностика FRG (check_frg_limit.py v2.0) ─────────────────────────────
try:
    import check_frg_limit
    HAS_CHECK_FRG = True
except ImportError:
    check_frg_limit = None
    HAS_CHECK_FRG = False


# ============================================================================
# ЧАСТЬ 2: ЗАПУСК БАЗОВОЙ МОДЕЛИ
# ============================================================================

def run_base_model(verbose: bool = True) -> Dict[str, Any]:
    """
    Запуск базовой модели (main.py) БЕЗ автогенома.

    ВАЖНО:
        run_all_checks() возвращает вложенную структуру БЕЗ единой
        пары (total_pass, total_checks). Эти числа появляются только
        внутри build_summary_table(). Поэтому мы:

        1. Запускаем run_all_checks()          — как раньше.
        2. Печатаем print_summary()            — как раньше.
        3. Сохраняем omega4_results.json       — как раньше.
        4. ВЫЗЫВАЕМ build_summary_table()      — чтобы получить
           компактный summary с total_pass/total_checks/all_verified.
           Возвращаем его в base_results['__summary__'], чтобы
           _extract_base_summary мог его прочитать.
    """
    if verbose:
        print()
        print("=" * 80)
        print("  ЧАСТЬ 1: БАЗОВАЯ МОДЕЛЬ (main.py)")
        print("=" * 80)
        print()

    model = Omega4Unified()
    base_results = model.run_all_checks()

    if verbose:
        model.print_summary(base_results)

    # Сохраняем omega4_results.json (свой файл базовой модели)
    model.save_results(base_results, filename='omega4_results.json')

    # ─── Извлекаем компактный summary через build_summary_table() ────
    # build_summary_table возвращает dict вида:
    #   {'total_pass': 171, 'total_checks': 171, 'all_verified': True, ...}
    try:
        summary_table = model.build_summary_table(base_results)
        base_results['__summary__'] = {
            'total_pass': summary_table.get('total_pass'),
            'total_checks': summary_table.get('total_checks'),
            'all_verified': summary_table.get('all_verified'),
        }
    except Exception as e:
        base_results['__summary__'] = {
            'total_pass': None,
            'total_checks': None,
            'all_verified': None,
            'error': str(e),
        }

    return base_results

# ============================================================================
# ЧАСТЬ 3: ЗАПУСК ДОП-ПРОЕКТА
# ============================================================================

def run_research_project(verbose: bool = True) -> Dict[str, Any]:
    """
    Запуск доп-проекта (main_research.py v3.0).

    Печатает полный отчёт и сохраняет research_results.json.
    Возвращает summary из research_summary() — для unified JSON.
    """
    if verbose:
        print()
        print("=" * 80)
        print("  ЧАСТЬ 2: ДОП-ПРОЕКТ (main_research.py v3.0)")
        print("=" * 80)
        print()

    # Запуск 9 файлов (без печати их отчётов — только загрузка)
    run_result = run_all_research_files(verbose=verbose, print_reports=False)

    if verbose:
        print()
        print(f"  Всего файлов:     {run_result['n_total']}")
        print(f"  Загружено:        {run_result['n_loaded']}")
        print(f"  Проверено:        {run_result['n_verified']}")

    # Печать полного отчёта
    if verbose:
        print_research_report(verbose=False)

    # Сохраняем research_results.json
    save_research_results(output_path='research_results.json', verbose=True)

    # Возвращаем summary
    return research_summary()


# ============================================================================
# ЧАСТЬ 4: ЗАПУСК ДИАГНОСТИКИ FRG
# ============================================================================

def run_frg_diagnostics(verbose: bool = True) -> Dict[str, Any]:
    """
    Запуск check_frg_limit.py.

    Печатает полный отчёт (check_frg_limit.main()).
    Возвращает структурированный dict (compute_frg_boundary()).
    """
    if verbose:
        print()
        print("=" * 80)
        print("  ЧАСТЬ 3: ДИАГНОСТИКА FRG (check_frg_limit.py v2.0)")
        print("=" * 80)

    if not HAS_CHECK_FRG:
        if verbose:
            print("\n  ⚠️ check_frg_limit.py недоступен — пропуск.")
        return {
            'available': False,
            'error': 'check_frg_limit not importable',
        }

    # Полный отчёт (таблица + граница + струнный сектор)
    if verbose:
        check_frg_limit.main()

    # Структурированные данные для JSON
    if hasattr(check_frg_limit, 'compute_frg_boundary'):
        boundary = check_frg_limit.compute_frg_boundary()
    else:
        boundary = {
            'available': False,
            'error': 'compute_frg_boundary() отсутствует в check_frg_limit.py',
        }

    return boundary


# ============================================================================
# ЧАСТЬ 5: ОБЪЕДИНЁННЫЙ JSON
# ============================================================================

def _extract_base_summary(base_results: Dict[str, Any]) -> Dict[str, Any]:
    """
    Извлечь компактную сводку из результатов базовой модели.

    ВАЖНО:
        В run_base_model() мы вызываем build_summary_table() и
        сохраняем его результат в base_results['__summary__'].
        Здесь просто читаем оттуда. Если ключа нет — возвращаем None.
    """
    if not isinstance(base_results, dict):
        return {}

    s = base_results.get('__summary__')
    if not isinstance(s, dict):
        return {
            'total_pass': None,
            'total_checks': None,
            'all_verified': None,
        }

    return {
        'total_pass': s.get('total_pass'),
        'total_checks': s.get('total_checks'),
        'all_verified': s.get('all_verified'),
    }

def _extract_research_summary(research_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Извлечь компактную сводку из research_summary().

    ВАЖНО:
        research_summary() из main_research.py v3.0 возвращает ПЛОСКИЙ
        dict с ключами 'N_eff_max', 'N_bulk', 'N_hidden', 'N_membrane',
        'status_overall', ... — БЕЗ вложенного 'summary'.
        Поэтому сначала проверяем плоскую структуру, потом — вложенную.
    """
    if not isinstance(research_data, dict):
        return {}

    # Плоская структура (то, что реально возвращает research_summary())
    if 'N_eff_max' in research_data or 'status_overall' in research_data:
        return {
            'N_eff_max': research_data.get('N_eff_max'),
            'N_bulk': research_data.get('N_bulk'),
            'N_hidden': research_data.get('N_hidden'),
            'N_membrane': research_data.get('N_membrane'),
            'status_overall': research_data.get('status_overall'),
        }

    # Вложенная структура — на всякий случай, если research_summary()
    # поменяется и станет возвращать {'summary': {...}, 'details': {...}}
    summary = research_data.get('summary')
    if isinstance(summary, dict):
        return summary

    return {}


def build_unified_json(
    base_results: Dict[str, Any],
    research_data: Dict[str, Any],
    frg_boundary: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Построить unified_results.json.

    Структура:
        {
          "version": "1.0",
          "timestamp": "...",
          "base_model":       {...},
          "research_project": {...},
          "frg_boundary":     {...},
          "combined_summary": {...}
        }
    """
    base_summary = _extract_base_summary(base_results)
    research_summary_compact = _extract_research_summary(research_data)

    combined = {
        'base_model_all_verified': base_summary.get('all_verified'),
        'base_model_total_pass': base_summary.get('total_pass'),
        'base_model_total_checks': base_summary.get('total_checks'),
        'research_status_overall': research_summary_compact.get('status_overall'),
        'research_N_eff_max': research_summary_compact.get('N_eff_max'),
        'research_N_bulk': research_summary_compact.get('N_bulk'),
        'research_N_hidden': research_summary_compact.get('N_hidden'),
        'research_N_membrane': research_summary_compact.get('N_membrane'),
        'frg_boundary_available': isinstance(frg_boundary, dict) and frg_boundary.get('available'),
        'frg_N_eff_max_stable': frg_boundary.get('N_eff_max_stable') if isinstance(frg_boundary, dict) else None,
        'frg_N_eff_min_unstable': frg_boundary.get('N_eff_min_unstable') if isinstance(frg_boundary, dict) else None,
        'frg_boundary_text': frg_boundary.get('boundary') if isinstance(frg_boundary, dict) else None,
    }

    unified = {
        '_author': 'Сергей Викторович Матершов',
        '_orcid': '0009-0009-0641-1357',
        '_license': 'CC BY-NC-ND 4.0 International',
        'version': '1.0',
        'timestamp': datetime.now().isoformat(),
        'description': 'Ω⁴-UNIFIED: базовая модель + доп-проект + FRG-диагностика',
        'base_model': {
            'results': base_results,
            'summary': base_summary,
        },
        'research_project': {
            'summary': research_summary_compact,
            'details': research_data.get('details', {}) if isinstance(research_data, dict) else {},
            'files': [spec['name'] for spec in RESEARCH_FILES],
            'formulas_for_7': formulas_for_7(),
        },
        'frg_boundary': frg_boundary if isinstance(frg_boundary, dict) else {'available': False},
        'combined_summary': combined,
    }

    return unified


def save_unified_json(
    unified: Dict[str, Any],
    output_path: str = 'unified_results.json',
    verbose: bool = True,
) -> str:
    """Сохранить unified_results.json."""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(unified, f, indent=2, ensure_ascii=False, default=str)
        if verbose:
            print(f"\n  💾 Объединённый JSON сохранён: {output_path}")
        return output_path
    except OSError as e:
        if verbose:
            print(f"\n  ❌ Ошибка сохранения unified JSON: {e}")
        return ''


# ============================================================================
# ЧАСТЬ 6: ФИНАЛЬНАЯ СВОДКА
# ============================================================================

def print_final_summary(
    base_results: Dict[str, Any],
    research_data: Dict[str, Any],
    frg_boundary: Dict[str, Any],
) -> None:
    """Печать финальной сводки по трём частям."""
    print()
    print("=" * 80)
    print("  ФИНАЛЬНАЯ СВОДКА (main_unified.py v1.0)")
    print("=" * 80)
    print()

    # ─── Базовая модель ────────────────────────────────────────────────
    base_summary = _extract_base_summary(base_results)

    print("  ── 1. БАЗОВАЯ МОДЕЛЬ (main.py) ──")
    print(f"    Проверок:      {base_summary.get('total_pass', '?')}/"
          f"{base_summary.get('total_checks', '?')}")
    print(f"    Статус:        "
          f"{'✅ ГОТОВО' if base_summary.get('all_verified') else '⚠️ ЕСТЬ ОШИБКИ'}")
    print()

    # ─── Доп-проект ────────────────────────────────────────────────────
    research_summary_compact = _extract_research_summary(research_data)

    print("  ── 2. ДОП-ПРОЕКТ (main_research.py v3.0) ──")
    print(f"    Файлов:        {len(RESEARCH_FILES)}")
    print(f"    N_eff_max:     {research_summary_compact.get('N_eff_max', '?')}")
    print(f"    N_bulk:        {research_summary_compact.get('N_bulk', '?')}")
    print(f"    N_hidden:      {research_summary_compact.get('N_hidden', '?')}")
    print(f"    N_membrane:    {research_summary_compact.get('N_membrane', '?')}")
    print(f"    Статус:        {research_summary_compact.get('status_overall', '?')}")
    print()

    # ─── FRG-диагностика ───────────────────────────────────────────────
    print("  ── 3. ДИАГНОСТИКА FRG (check_frg_limit.py v2.0) ──")
    if isinstance(frg_boundary, dict) and frg_boundary.get('available'):
        print(f"    N_eff_max_stable:     {frg_boundary.get('N_eff_max_stable', '?')}")
        print(f"    N_eff_min_unstable:   {frg_boundary.get('N_eff_min_unstable', '?')}")
        print(f"    Граница:              {frg_boundary.get('boundary', '?')}")
    else:
        print(f"    ⚠️ недоступна")
    print()

    # ─── Итог ──────────────────────────────────────────────────────────
    print("  ── ИТОГ ──")
    print(f"    Ω⁴-UNIFIED v79.4 + main_research v3.0 + check_frg_limit v2.0")
    print(f"    Все три части завершены.")
    print(f"    unified_results.json сохранён.")
    print()
    print("=" * 80)


# ============================================================================
# ЧАСТЬ 7: ТОЧКА ВХОДА
# ============================================================================

def main():
    """Полный объединённый прогон."""
    args = sys.argv[1:]

    save_json = '--no-save' not in args
    no_genome = '--no-genome' in args
    verbose = '--quiet' not in args

    print("=" * 80)
    print("  Ω⁴-UNIFIED — ОБЪЕДИНЁННЫЙ MAIN (main_unified.py) — v1.0")
    print("=" * 80)
    print()
    print("  Три части:")
    print("    1. Базовая модель       (main.py)               — 171/171")
    print("    2. Доп-проект           (main_research.py v3.0)  — 9 файлов")
    print("    3. FRG-диагностика      (check_frg_limit.py v2.0) — граница 7/8")
    print()
    print("  Порядок:")
    print("    1 → 2 → 3 → unified_results.json → genome_writer")
    print()
    print("  Аргументы:")
    print("    --no-genome  — не генерировать автогеном")
    print("    --no-save    — не сохранять unified_results.json")
    print("    --quiet      — минимум вывода")
    print()
    print("=" * 80)

    # ─── 1. Базовая модель ─────────────────────────────────────────────
    base_results = run_base_model(verbose=verbose)

    # ─── 2. Доп-проект ─────────────────────────────────────────────────
    research_data = run_research_project(verbose=verbose)

    # ─── 3. FRG-диагностика ────────────────────────────────────────────
    frg_boundary = run_frg_diagnostics(verbose=verbose)

    # ─── 4. Объединённый JSON ──────────────────────────────────────────
    if save_json:
        unified = build_unified_json(
            base_results=base_results,
            research_data=research_data,
            frg_boundary=frg_boundary,
        )
        # Убираем служебный ключ __summary__ из копии, чтобы не портить
        # оригинальный base_results (нужен для print_final_summary ниже).
        results_copy = dict(unified['base_model']['results'])
        results_copy.pop('__summary__', None)
        unified['base_model']['results'] = results_copy
        save_unified_json(unified, output_path='unified_results.json', verbose=verbose)

    # ─── 5. Финальная сводка ───────────────────────────────────────────
    print_final_summary(base_results, research_data, frg_boundary)

    # ─── 6. Автогеном (один раз, в самом конце) ────────────────────────
    if not no_genome:
        try:
            from genome_writer import write_genome
            from core import REGISTRY

            print()
            print("─" * 80)
            print("  🌱 ГЕНЕРАЦИЯ АВТОМАТИЧЕСКОГО ГЕНОМА")
            print("─" * 80)
            print(f"  Источник: core.REGISTRY  ({len(REGISTRY)} констант)")
            write_genome(
                output_path='constants_genome_omega4.py',
                dry_run=False,
                verbose=True,
            )
        except ImportError as e:
            print(f"\n  ⚠️ genome_writer.py недоступен: {e}")
        except Exception as e:
            print(f"\n  ⚠️ Ошибка генерации автогенома: {e}")


if __name__ == '__main__':
    main()
