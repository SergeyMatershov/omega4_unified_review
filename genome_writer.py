#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
Ω⁴-UNIFIED — ГЕНЕРАТОР АВТОМАТИЧЕСКОГО ГЕНОМА (genome_writer.py) — v1.1
================================================================================
НАЗНАЧЕНИЕ:
    Генерирует constants_genome_omega4.py из:
      • REGISTRY (заполняется модулями во время работы)
      • omega4_results.json (результаты системы)

ЗАПУСК:
    python genome_writer.py                  # создать constants_genome_omega4.py
    python genome_writer.py --dry-run        # показать, что будет создано
    python genome_writer.py --preview        # вывести первые 30 строк

АВТОМАТИЧЕСКИЙ ЗАПУСК:
    Из main.py в конце:
        from genome_writer import write_genome
        write_genome()

АВТОР:  Сергей Викторович Матершов
ORCID:  0009-0009-0641-1357
ВЕРСИЯ: 1.1 (включён CLI в автогеном)
ЛИЦЕНЗИЯ: CC BY-NC-ND 4.0 International
================================================================================
"""

import os
import json
import sys
from datetime import datetime
from typing import Any, Dict, Optional


# ============================================================================
# ЧАСТЬ 1: ЗАГРУЗКА ИСТОЧНИКОВ
# ============================================================================

def load_registry() -> Dict[str, Dict]:
    """Загрузить REGISTRY из core.py и всех зависимых модулей."""
    for module_name in ['core', 'atlas', 'physics', 'atlas_scan',
                        'vacuum_analysis', 'elliptic_curve', 'magic_numbers',
                        'quark_structure', 'modular_forms', 'system_metrics',
                        'extra_constants', 'topological_origin',
                        'quantum_gravity']:
        try:
            __import__(module_name)
        except ImportError as e:
            print(f"⚠️ Не удалось импортировать {module_name}: {e}")

    try:
        from core import REGISTRY
        return REGISTRY.all()
    except ImportError as e:
        print(f"⚠️ Не удалось загрузить REGISTRY из core.py: {e}")
        return {}
    except Exception as e:
        print(f"⚠️ Ошибка при получении REGISTRY: {e}")
        return {}


def load_results(path: str = 'omega4_results.json') -> Dict:
    """Загрузить результаты системы (опционально)."""
    if not os.path.exists(path):
        return {'version': '?', 'key_results': {}, 'summary': {}}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ Не удалось загрузить {path}: {e}")
        return {'version': '?', 'key_results': {}, 'summary': {}}


# ============================================================================
# ЧАСТЬ 2: ФОРМАТИРОВАНИЕ ЗНАЧЕНИЙ
# ============================================================================

def format_value(value: Any) -> str:
    """Привести значение к строке кода Python."""
    if value is None:
        return "None"
    if isinstance(value, bool):
        return str(value)
    if isinstance(value, (int, float)):
        return repr(value)
    if isinstance(value, str):
        escaped = value.replace("\\", "\\\\").replace("'", "\\'")
        return f"'{escaped}'"
    if isinstance(value, (list, tuple)):
        inner = ", ".join(format_value(v) for v in value)
        return f"[{inner}]"
    if isinstance(value, dict):
        inner = ", ".join(f"{format_value(k)}: {format_value(v)}"
                          for k, v in value.items())
        return f"{{{inner}}}"
    return repr(value)


def format_constant_entry(name: str, data: Dict) -> str:
    """Сгенерировать одну запись REGISTRY."""
    value_str = format_value(data.get('value'))
    unit = format_value(data.get('unit', ''))
    level = format_value(data.get('level', 'LOST'))

    formula = data.get('formula')
    if formula is None or formula == 'None':
        formula_str = f"lambda: {value_str}"
    else:
        if isinstance(formula, str):
            formula_str = formula
        else:
            formula_str = f"lambda: {value_str}"

    formula_repr = data.get('formula_repr', '')
    formula_repr_str = format_value(formula_repr)

    source = format_value(data.get('source', 'auto'))
    comment = format_value(data.get('comment', ''))
    depends_on = format_value(data.get('depends_on', []))
    derives_to = format_value(data.get('derives_to', []))
    status = format_value(data.get('status', '✅ auto'))

    lines = [
        f"    '{name}': {{",
        f"        'value': {value_str},",
        f"        'unit': {unit},",
        f"        'level': {level},",
        f"        'formula': {formula_str},",
        f"        'formula_repr': {formula_repr_str},",
        f"        'source': {source},",
        f"        'comment': {comment},",
        f"        'depends_on': {depends_on},",
        f"        'derives_to': {derives_to},",
        f"        'status': {status},",
        f"    }},",
    ]
    return '\n'.join(lines)


# ============================================================================
# ЧАСТЬ 3: ГЕНЕРАЦИЯ ФАЙЛА
# ============================================================================

def generate_content(registry: Dict[str, Dict], version: str) -> str:
    """Сгенерировать содержимое файла."""
    now = datetime.now().isoformat()
    n_total = len(registry)

    # Считаем по уровням
    by_level = {}
    for name, data in registry.items():
        lvl = data.get('level', 'UNKNOWN')
        by_level[lvl] = by_level.get(lvl, 0) + 1

    # ========================================================================
    # ШАГ 1: ЗАГОЛОВОК И РАСПРЕДЕЛЕНИЕ ПО УРОВНЯМ
    # ========================================================================
    lines = [
        '#!/usr/bin/env python3',
        '# -*- coding: utf-8 -*-',
        '"""',
        '=' * 78,
        'Ω⁴-UNIFIED — АВТОМАТИЧЕСКИ СГЕНЕРИРОВАННЫЙ ГЕНОМ',
        '=' * 78,
        f'ДАТА ГЕНЕРАЦИИ:   {now}',
        f'ВЕРСИЯ СИСТЕМЫ:   {version}',
        f'ВСЕГО КОНСТАНТ:   {n_total}',
        '',
        'РАСПРЕДЕЛЕНИЕ ПО УРОВНЯМ:',
    ]
    for lvl in sorted(by_level.keys(), key=str):
        lines.append(f'    {str(lvl):<10} {by_level[lvl]}')

    # ========================================================================
    # ШАГ 2: КОНСТАНТЫ ГЕНОМА
    # ========================================================================
    lines.extend([
        '',
        '⚠️  ВНИМАНИЕ:',
        '    Этот файл создаётся АВТОМАТИЧЕСКИ из main.py.',
        '    НЕ РЕДАКТИРУЙ ВРУЧНУЮ — правки будут перезаписаны.',
        '',
        '    Для правок используй core.py / physics.py — там',
        '    зарегистрируй константу через REGISTRY.register(...)',
        '=' * 78,
        'АВТОР:  Сергей Викторович Матершов',
        'ORCID:  0009-0009-0641-1357',
        'ЛИЦЕНЗИЯ: CC BY-NC-ND 4.0 International',
        '=' * 78,
        '"""',
        '',
        f'AUTO_GENOME_VERSION = "{version}"',
        f'AUTO_GENOME_DATE = "{now}"',
        f'AUTO_GENOME_TOTAL = {n_total}',
        '',
        'REGISTRY_AUTO = {',
    ])

    # ← ЦИКЛ ДОБАВЛЕНИЯ КОНСТАНТ
    for name in sorted(registry.keys()):
        data = registry[name]
        lines.append(format_constant_entry(name, data))

    # ========================================================================
    # ШАГ 3: ЗАКРЫТИЕ СЛОВАРЯ
    # ========================================================================
    lines.extend([
        '}',
        '',
        '# Обратная совместимость:',
        'REGISTRY = REGISTRY_AUTO',
        '',
        f'# Всего констант: {n_total}',
    ])

    # ========================================================================
    # ШАГ 4: CLI
    # ========================================================================
    lines.extend([
        '',
        '',
        '# ============================================================================',
        '# CLI (Command-Line Interface) для работы с автогеномом',
        '# ============================================================================',
        '#',
        '# ЗАПУСК:',
        '#   python constants_genome_omega4.py --summary      # краткая сводка',
        '#   python constants_genome_omega4.py --verify       # верификация',
        '#   python constants_genome_omega4.py --tasks        # задачи расчёта',
        '#   python constants_genome_omega4.py --search X     # поиск по имени',
        '#   python constants_genome_omega4.py --list         # список всех имён',
        '#   python constants_genome_omega4.py --help         # справка',
        '#',
        '# ============================================================================',
        '',
        '',
        'def _print_help():',
        '    """Печать справки."""',
        '    print("=" * 78)',
        '    print("  Ω⁴-UNIFIED — АВТОГЕНОМ (CLI)")',
        '    print("=" * 78)',
        '    print()',
        '    print("  ИСПОЛЬЗОВАНИЕ:")',
        '    print("    python constants_genome_omega4.py [КОМАНДА]")',
        '    print()',
        '    print("  КОМАНДЫ:")',
        '    print("    --summary         Краткая сводка по уровням и источникам")',
        '    print("    --verify          Верификация реестра (value ↔ formula)")',
        '    print("    --tasks           Список задач расчёта (⚠️)")',
        '    print("    --search СТРОКА   Поиск констант по имени/комментарию")',
        '    print("    --list            Список всех имён констант")',
        '    print("    --level N         Только константы уровня N")',
        '    print("    --source МОДУЛЬ   Только константы из модуля МОДУЛЬ")',
        '    print("    --help, -h        Эта справка")',
        '    print()',
        '    print("  ПРИМЕРЫ:")',
        '    print("    python constants_genome_omega4.py --summary")',
        '    print("    python constants_genome_omega4.py --search magic")',
        '    print("    python constants_genome_omega4.py --level 0")',
        '    print("    python constants_genome_omega4.py --source core")',
        '    print("=" * 78)',
        '',
        '',
        'def _print_summary():',
        '    """Краткая сводка."""',
        '    by_level = {}',
        '    by_status = {}',
        '    by_source = {}',
        '    by_unit = {}',
        '',
        '    for name, data in REGISTRY_AUTO.items():',
        '        lvl = data.get(\'level\', \'UNKNOWN\')',
        '        by_level[lvl] = by_level.get(lvl, 0) + 1',
        '',
        '        st = data.get(\'status\', \'?\')',
        '        by_status[st] = by_status.get(st, 0) + 1',
        '',
        '        src = data.get(\'source\', \'auto\')',
        '        src_key = src.split(\':\')[0].split(\'(\')[0].strip()',
        '        by_source[src_key] = by_source.get(src_key, 0) + 1',
        '',
        '        unit = data.get(\'unit\', \'\') or \'(без единицы)\'',
        '        by_unit[unit] = by_unit.get(unit, 0) + 1',
        '',
        '    n_total = len(REGISTRY_AUTO)',
        '    print("=" * 78)',
        '    print("  Ω⁴-UNIFIED — АВТОГЕНОМ (constants_genome_omega4.py)")',
        '    print("=" * 78)',
        '    print()',
        '    print(f"  Версия:            {AUTO_GENOME_VERSION}")',
        '    print(f"  Дата генерации:    {AUTO_GENOME_DATE}")',
        '    print(f"  Всего констант:    {n_total}")',
        '    print()',
        '    print("  ── ПО УРОВНЯМ ──")',
        '    for lvl in sorted(by_level.keys(), key=str):',
        '        n = by_level[lvl]',
        '        pct = n / n_total * 100',
        '        print(f"    {str(lvl):<10} {n:>4}  ({pct:>5.1f}%)")',
        '    print()',
        '    print("  ── ПО СТАТУСУ ──")',
        '    for st in sorted(by_status.keys()):',
        '        n = by_status[st]',
        '        pct = n / n_total * 100',
        '        print(f"    {st:<20} {n:>4}  ({pct:>5.1f}%)")',
        '    print()',
        '    print("  ── ПО ИСТОЧНИКАМ (top-10) ──")',
        '    sorted_src = sorted(by_source.items(), key=lambda x: -x[1])[:10]',
        '    for src, n in sorted_src:',
        '        pct = n / n_total * 100',
        '        print(f"    {src:<30} {n:>4}  ({pct:>5.1f}%)")',
        '    print()',
        '    print("  ── ПО ЕДИНИЦАМ ──")',
        '    sorted_unit = sorted(by_unit.items(), key=lambda x: -x[1])[:8]',
        '    for unit, n in sorted_unit:',
        '        print(f"    {unit:<20} {n:>4}")',
        '    print("=" * 78)',
        '',
        '',
        'def _print_verify():',
        '    """Верификация реестра."""',
        '    n_total = len(REGISTRY_AUTO)',
        '    n_value_ok = 0',
        '    n_level_ok = 0',
        '    n_status_ok = 0',
        '    n_unit_ok = 0',
        '    errors = []',
        '',
        '    valid_levels = {\'OBS\', \'0\', \'1\', \'2\', \'3\', \'CP\', \'LOST\', \'UNKNOWN\'}',
        '    valid_status_prefixes = (\'✅\', \'📜\', \'⚠️\', \'🟡\', \'❌\')',
        '',
        '    for name, data in REGISTRY_AUTO.items():',
        '        val = data.get(\'value\')',
        '        formula = data.get(\'formula\')',
        '        if callable(formula):',
        '            try:',
        '                fval = formula()',
        '                if isinstance(val, (int, float)) and isinstance(fval, (int, float)):',
        '                    ok = abs(float(val) - float(fval)) < 1e-9 * max(1.0, abs(float(val)))',
        '                else:',
        '                    ok = (val == fval)',
        '                if ok:',
        '                    n_value_ok += 1',
        '                else:',
        '                    errors.append(f"{name}: value={val}, formula()={fval}")',
        '            except Exception as e:',
        '                errors.append(f"{name}: формула выбросила {type(e).__name__}: {e}")',
        '        else:',
        '            n_value_ok += 1',
        '',
        '        lvl = str(data.get(\'level\', \'UNKNOWN\'))',
        '        if lvl in valid_levels:',
        '            n_level_ok += 1',
        '        else:',
        '            errors.append(f"{name}: недопустимый level={lvl}")',
        '',
        '        st = data.get(\'status\', \'\')',
        '        if any(st.startswith(p) for p in valid_status_prefixes):',
        '            n_status_ok += 1',
        '        else:',
        '            errors.append(f"{name}: недопустимый status={st!r}")',
        '',
        '        if isinstance(data.get(\'unit\', \'\'), str):',
        '            n_unit_ok += 1',
        '        else:',
        '            errors.append(f"{name}: unit не строка")',
        '',
        '    print("=" * 78)',
        '    print("  🔍 ВЕРИФИКАЦИЯ АВТОГЕНОМА")',
        '    print("=" * 78)',
        '    print(f"  Всего констант:  {n_total}")',
        '    print(f"  Проверок: 4 × {n_total} = {4 * n_total}")',
        '    print()',
        '    print(f"  Проверка 1: value ↔ formula()    {n_value_ok}/{n_total}")',
        '    print(f"  Проверка 2: level                {n_level_ok}/{n_total}")',
        '    print(f"  Проверка 3: status               {n_status_ok}/{n_total}")',
        '    print(f"  Проверка 4: unit                 {n_unit_ok}/{n_total}")',
        '    print()',
        '    if errors:',
        '        print(f"  ❌ ОШИБОК: {len(errors)}")',
        '        print()',
        '        for err in errors[:20]:',
        '            print(f"    • {err}")',
        '        if len(errors) > 20:',
        '            print(f"    ... и ещё {len(errors) - 20}")',
        '        print()',
        '        print("  ВЕРДИКТ: ❌ ЕСТЬ ОШИБКИ")',
        '    else:',
        '        print("  ВЕРДИКТ: ✅ ВСЁ ЧИСТО")',
        '    print("=" * 78)',
        '',
        '',
        'def _print_tasks():',
        '    """Задачи расчёта (⚠️)."""',
        '    tasks = []',
        '    for name, data in REGISTRY_AUTO.items():',
        '        st = data.get(\'status\', \'\')',
        '        if st.startswith(\'⚠️\') or \'TASK\' in name.upper() or \'_BARE\' in name:',
        '            tasks.append((name, data))',
        '',
        '    print("=" * 78)',
        '    print("  ⚠️ ЗАДАЧИ РАСЧЁТА В АВТОГЕНОМЕ")',
        '    print("=" * 78)',
        '    print(f"  Найдено: {len(tasks)}")',
        '    print()',
        '    if not tasks:',
        '        print("  (в автогеноме задач расчёта нет)")',
        '        print()',
        '        print("  ПРИМЕЧАНИЕ:")',
        '        print("    Задачи TASK-001…TASK-004 живут в РУЧНОМ реестре")',
        '        print("    (constants_genome.py), а не в автогеноме.")',
        '        print("    См.: python constants_genome.py --tasks")',
        '    else:',
        '        for name, data in tasks:',
        '            print(f"  • {name}")',
        '            print(f"      value: {data.get(\'value\')}")',
        '            print(f"      comment: {data.get(\'comment\', \'\')[:70]}")',
        '    print("=" * 78)',
        '',
        '',
        'def _print_search(query: str):',
        '    """Поиск по имени/комментарию/source/formula_repr."""',
        '    q = query.lower()',
        '    matches = []',
        '    for name, data in REGISTRY_AUTO.items():',
        '        haystack = " ".join([',
        '            name,',
        '            str(data.get(\'comment\', \'\')),',
        '            str(data.get(\'source\', \'\')),',
        '            str(data.get(\'formula_repr\', \'\')),',
        '        ]).lower()',
        '        if q in haystack:',
        '            matches.append((name, data))',
        '',
        '    print("=" * 78)',
        '    print(f"  🔍 ПОИСК: {query!r}")',
        '    print("=" * 78)',
        '    print(f"  Найдено: {len(matches)}")',
        '    print()',
        '    for name, data in matches[:40]:',
        '        v = data.get(\'value\')',
        '        lvl = data.get(\'level\')',
        '        fr = data.get(\'formula_repr\', \'\')[:50]',
        '        print(f"  {name:<30} {str(v):<15} lvl={lvl}  {fr}")',
        '    if len(matches) > 40:',
        '        print(f"  ... и ещё {len(matches) - 40}")',
        '    print("=" * 78)',
        '',
        '',
        'def _print_list():',
        '    """Список всех имён."""',
        '    names = sorted(REGISTRY_AUTO.keys())',
        '    print("=" * 78)',
        '    print(f"  СПИСОК ВСЕХ КОНСТАНТ: {len(names)}")',
        '    print("=" * 78)',
        '    for i, name in enumerate(names, 1):',
        '        print(f"  {i:>4}. {name}")',
        '    print("=" * 78)',
        '',
        '',
        'def _print_by_level(level_str: str):',
        '    """Константы заданного уровня."""',
        '    matches = []',
        '    for name, data in REGISTRY_AUTO.items():',
        '        if str(data.get(\'level\')) == level_str:',
        '            matches.append((name, data))',
        '',
        '    print("=" * 78)',
        '    print(f"  КОНСТАНТЫ УРОВНЯ {level_str!r}: {len(matches)}")',
        '    print("=" * 78)',
        '    for name, data in matches:',
        '        v = data.get(\'value\')',
        '        print(f"  {name:<35} {v}")',
        '    print("=" * 78)',
        '',
        '',
        'def _print_by_source(source_str: str):',
        '    """Константы из заданного модуля."""',
        '    s = source_str.lower()',
        '    matches = []',
        '    for name, data in REGISTRY_AUTO.items():',
        '        if s in str(data.get(\'source\', \'\')).lower():',
        '            matches.append((name, data))',
        '',
        '    print("=" * 78)',
        '    print(f"  КОНСТАНТЫ ИЗ {source_str!r}: {len(matches)}")',
        '    print("=" * 78)',
        '    for name, data in matches:',
        '        v = data.get(\'value\')',
        '        print(f"  {name:<35} {v}")',
        '    print("=" * 78)',
        '',
        '',
        'if __name__ == \'__main__\':',
        '    import sys',
        '    args = sys.argv[1:]',
        '',
        '    if not args or \'--help\' in args or \'-h\' in args:',
        '        _print_help()',
        '    elif \'--summary\' in args:',
        '        _print_summary()',
        '    elif \'--verify\' in args:',
        '        _print_verify()',
        '    elif \'--tasks\' in args:',
        '        _print_tasks()',
        '    elif \'--list\' in args:',
        '        _print_list()',
        '    elif \'--search\' in args:',
        '        idx = args.index(\'--search\')',
        '        q = args[idx + 1] if idx + 1 < len(args) else \'\'',
        '        _print_search(q)',
        '    elif \'--level\' in args:',
        '        idx = args.index(\'--level\')',
        '        lvl = args[idx + 1] if idx + 1 < len(args) else \'0\'',
        '        _print_by_level(lvl)',
        '    elif \'--source\' in args:',
        '        idx = args.index(\'--source\')',
        '        src = args[idx + 1] if idx + 1 < len(args) else \'core\'',
        '        _print_by_source(src)',
        '    else:',
        '        print(f"Неизвестная команда: {\' \'.join(args)}")',
        '        print("Используйте --help")',
    ])

    return '\n'.join(lines)


def write_genome(
    output_path: str = 'constants_genome_omega4.py',
    dry_run: bool = False,
    verbose: bool = True,
) -> str:
    """
    Сгенерировать constants_genome_omega4.py.

    Параметры:
        output_path: путь для записи
        dry_run:     если True — не писать файл
        verbose:     печатать отчёт

    Возвращает: путь к созданному файлу (или '' при ошибке).
    """
    if verbose:
        print()
        print("─" * 78)
        print("  🌱 ГЕНЕРАЦИЯ АВТОМАТИЧЕСКОГО ГЕНОМА")
        print("─" * 78)

    registry = load_registry()
    results = load_results()

    if not registry:
        if verbose:
            print("  ⚠️ REGISTRY пустой — нечего генерировать")
        return ''

    version = results.get('version', '?')

    if verbose:
        print(f"  Источник: core.REGISTRY  ({len(registry)} констант)")
        print(f"  Версия системы: {version}")

    content = generate_content(registry, version)

    if dry_run:
        if verbose:
            print()
            print(f"  [DRY RUN] Файл бы содержал {len(content)} символов")
            print()
            print("  Первые 30 строк:")
            for line in content.split('\n')[:30]:
                print(f"    {line}")
        return ''

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        if verbose:
            print()
            print(f"  ✅ Создан: {output_path}")
            print(f"     Размер: {len(content)} символов")
            print(f"     Строк:  {content.count(chr(10)) + 1}")
    except OSError as e:
        if verbose:
            print(f"  ❌ Ошибка записи: {e}")
        return ''

    return output_path


# ============================================================================
# ЧАСТЬ 4: ТОЧКА ВХОДА
# ============================================================================

if __name__ == '__main__':
    dry_run = '--dry-run' in sys.argv
    preview = '--preview' in sys.argv

    if preview:
        registry = load_registry()
        results = load_results()
        version = results.get('version', '?')
        content = generate_content(registry, version)
        print(content[:3000])
    else:
        write_genome(dry_run=dry_run)
