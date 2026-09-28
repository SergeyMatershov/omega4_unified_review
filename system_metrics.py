#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
Ω⁴-UNIFIED v79.0 — СИСТЕМНЫЕ МЕТРИКИ (system_metrics.py) — v1
================================================================================
НОВЫЙ МОДУЛЬ (наращивание). НЕ меняет базовые файлы.

================================================================================
НАЗНАЧЕНИЕ
================================================================================

Регистрирует СИСТЕМНЫЕ метрики Ω⁴-модели в REGISTRY:
  • Статистическая значимость (σ)
  • Кросс-валидация (%)
  • Предсказания (всего/подтв./будущих/напряж.)
  • Чувствительность v1 (χ, β₁₂)
  • Benchmark (эффективность)

ИСТОЧНИК ДАННЫХ:
  omega4_results.json — файл, создаваемый main.py.
  Если файла нет — используются дефолтные значения (для автономности).

ЗАЧЕМ:
  Константы физических модулей уже собраны в REGISTRY через свои
  @dataclass-обёртки. Осталось собрать мета-константы (метрики качества).

ФОРМАТ:
  Все метрики — уровень 1 (выведенные из анализа).

НЕ МЕНЯЕТ базовые файлы.
================================================================================
================================================================================
АВТОР:  Сергей Викторович Матершов
ORCID:  0009-0009-0641-1357
ДАТА:   2026-09-19
ЛИЦЕНЗИЯ: CC BY-NC-ND 4.0 International
================================================================================
"""

import os
import json
from typing import Dict, Any, Optional

from core import REGISTRY as _CORE_REGISTRY
from core import _auto_collect_constants


# ============================================================================
# ЧАСТЬ 1: ЗАГРУЗКА РЕЗУЛЬТАТОВ ИЗ omega4_results.json
# ============================================================================

def load_omega4_results(path: str = 'omega4_results.json') -> Optional[Dict]:
    """
    Загрузить результаты системы.

    Возвращает:
        dict или None (если файла нет / ошибка чтения).
    """
    if not os.path.exists(path):
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"  ⚠️ system_metrics: не удалось загрузить {path}: {e}")
        return None


# ============================================================================
# ЧАСТЬ 2: ДЕФОЛТНЫЕ ЗНАЧЕНИЯ
# ============================================================================
#
# Если omega4_results.json отсутствует, используем значения из
# ОПИСАНИЕ.md / документации проекта. Это гарантирует, что геном
# не сломается.
# ============================================================================

DEFAULTS = {
    # statistical.py
    'stat_n_samples': 10000,
    'stat_n_links': 24,
    'stat_n_3sigma': 11,
    'stat_combined_sigma': 12.741392786198375,

    # cross_validation.py
    'cv_loo_rate': 100.0,
    'cv_kfold_rate': 100.0,
    'cv_test_rate': 100.0,
    'cv_overall': 100.0,

    # predictions.py
    'pred_total': 30,
    'pred_confirmed': 18,
    'pred_future': 10,
    'pred_tension': 2,

    # sensitivity.py (v1)
    'sens_worst_chi': 74.19354838709677,
    'sens_worst_beta': 96.7741935483871,
    'sens_best_chi': 633,
    'sens_best_beta': 4,
    'sens_n_stable': 12,
    'sens_n_total': 100,

    # benchmark.py
    'bench_n_models': 6,
    'bench_omega4_efficiency': 242.755,
}


# ============================================================================
# ЧАСТЬ 3: СИСТЕМНЫЕ МЕТРИКИ — ДАТАКЛАСС
# ============================================================================

from dataclasses import dataclass


@dataclass(frozen=True)
class SystemMetricsConstants:
    """
    Единые системные метрики Ω⁴ (v79.0).

    Все значения читаются из omega4_results.json (key_results),
    либо из DEFAULTS.

    УРОВЕНЬ: 1 (выведенные метрики).
    """

    # Храним результаты как атрибут класса (frozen позволяет через
    # object.__setattr__, но проще передать снаружи)
    _results: Optional[Dict] = None

    # ========================================================================
    # 1. СТАТИСТИКА (Monte Carlo, Fisher's method)
    # ========================================================================

    @property
    def stat_combined_sigma(self) -> float:
        """
        Комбинированная статистическая значимость (σ).

        ФОРМУЛА: Fisher's method (log-space)
            χ² = -2·Σ ln(p_i)
            σ = sqrt(2) · erfinv(1 - p_combined)

        ЗНАЧЕНИЕ: 12.74σ (> 5σ — уровень открытия)
        """
        return self._get('stat_combined_sigma')

    @property
    def stat_n_samples(self) -> int:
        """
        Число случайных полиномов в Monte Carlo.

        ЗНАЧЕНИЕ: 10000
        """
        return self._get('stat_n_samples')

    @property
    def stat_n_links(self) -> int:
        """
        Число связей в Monte Carlo анализе.

        ЗНАЧЕНИЕ: 24
        """
        return self._get('stat_n_links')

    @property
    def stat_n_3sigma(self) -> int:
        """
        Число связей со значимостью > 3σ.

        ЗНАЧЕНИЕ: 11
        """
        return self._get('stat_n_3sigma')

    # ========================================================================
    # 2. КРОСС-ВАЛИДАЦИЯ
    # ========================================================================

    @property
    def cv_overall(self) -> float:
        """
        Общая оценка кросс-валидации (%).

        ФОРМУЛА: среднее из LOO, K-Fold, Holdout

        ЗНАЧЕНИЕ: 100.0% (нет переобучения)
        """
        return self._get('cv_overall')

    @property
    def cv_loo_rate(self) -> float:
        """
        Leave-One-Out pass rate (%).

        ЗНАЧЕНИЕ: 100.0%
        """
        return self._get('cv_loo_rate')

    @property
    def cv_kfold_rate(self) -> float:
        """
        K-Fold mean pass rate (%).

        ЗНАЧЕНИЕ: 100.0%
        """
        return self._get('cv_kfold_rate')

    @property
    def cv_test_rate(self) -> float:
        """
        Holdout Test pass rate (%).

        ЗНАЧЕНИЕ: 100.0%
        """
        return self._get('cv_test_rate')

    # ========================================================================
    # 3. ПРЕДСКАЗАНИЯ
    # ========================================================================

    @property
    def pred_total(self) -> int:
        """
        Общее число предсказаний модели.

        ЗНАЧЕНИЕ: 30
        """
        return self._get('pred_total')

    @property
    def pred_confirmed(self) -> int:
        """
        Число подтверждённых предсказаний.

        ЗНАЧЕНИЕ: 18
        """
        return self._get('pred_confirmed')

    @property
    def pred_future(self) -> int:
        """
        Число будущих предсказаний (проверка в будущем).

        ЗНАЧЕНИЕ: 10
        """
        return self._get('pred_future')

    @property
    def pred_tension(self) -> int:
        """
        Число предсказаний в напряжении с экспериментом.

        ЗНАЧЕНИЕ: 2
        """
        return self._get('pred_tension')

    # ========================================================================
    # 4. ЧУВСТВИТЕЛЬНОСТЬ v1
    # ========================================================================

    @property
    def sens_worst_chi(self) -> float:
        """
        Худшая устойчивость к χ (%).

        ЗНАЧЕНИЕ: 74.19%
        """
        return self._get('sens_worst_chi')

    @property
    def sens_worst_beta(self) -> float:
        """
        Худшая устойчивость к β₁₂ (%).

        ЗНАЧЕНИЕ: 96.77%
        """
        return self._get('sens_worst_beta')

    @property
    def sens_best_chi(self) -> int:
        """
        Лучшее значение χ для устойчивости.

        ЗНАЧЕНИЕ: 633
        """
        return self._get('sens_best_chi')

    @property
    def sens_best_beta(self) -> int:
        """
        Лучшее значение β₁₂ для устойчивости.

        ЗНАЧЕНИЕ: 4
        """
        return self._get('sens_best_beta')

    @property
    def sens_n_stable(self) -> int:
        """
        Число точек в области стабильности (≥ 80%).

        ЗНАЧЕНИЕ: 12
        """
        return self._get('sens_n_stable')

    @property
    def sens_n_total(self) -> int:
        """
        Общее число точек в сетке чувствительности.

        ЗНАЧЕНИЕ: 100
        """
        return self._get('sens_n_total')

    # ========================================================================
    # 5. BENCHMARK
    # ========================================================================

    @property
    def bench_n_models(self) -> int:
        """
        Число моделей в benchmark.

        ЗНАЧЕНИЕ: 6 (СМ, MSSM, струны, LQG, AS, Ω⁴)
        """
        return self._get('bench_n_models')

    @property
    def bench_omega4_efficiency(self) -> float:
        """
        Эффективность Ω⁴ в benchmark.

        ФОРМУЛА: (N_checks × σ) / N_params = (47 × 10.33) / 2

        ЗНАЧЕНИЕ: 242.755
        """
        return self._get('bench_omega4_efficiency')

    # ========================================================================
    # ВНУТРЕННИЙ МЕТОД
    # ========================================================================

    def _get(self, key: str):
        """Получить значение из key_results или DEFAULTS."""
        if self._results is not None:
            kr = self._results.get('key_results', {})
            if key in kr:
                return kr[key]
        return DEFAULTS.get(key, 0.0)


# ============================================================================
# ЧАСТЬ 4: ЭКЗЕМПЛЯР И АВТОСБОР
# ============================================================================

_results = load_omega4_results()

# frozen dataclass нельзя изменить в __init__, но можно через object.__setattr__
SMC = SystemMetricsConstants()
object.__setattr__(SMC, '_results', _results)

if _results is not None:
    print(f"  📊 system_metrics: загружено из omega4_results.json")
else:
    print(f"  📊 system_metrics: используется DEFAULTS (файла нет)")


_auto_collect_constants(
    SMC, _CORE_REGISTRY,
    metadata={
        # Статистика — уровень 1
        'stat_combined_sigma': (1, 'σ', 'Комбинированная значимость: 12.74σ'),
        'stat_n_samples': (1, '', 'Monte Carlo: 10000 полиномов'),
        'stat_n_links': (1, '', 'Связей в анализе: 24'),
        'stat_n_3sigma': (1, '', 'Связей > 3σ: 11'),
        # Кросс-валидация — уровень 1
        'cv_overall': (1, '%', 'Кросс-валидация: 100.0%'),
        'cv_loo_rate': (1, '%', 'LOO pass rate: 100.0%'),
        'cv_kfold_rate': (1, '%', 'K-Fold pass rate: 100.0%'),
        'cv_test_rate': (1, '%', 'Holdout test rate: 100.0%'),
        # Предсказания — уровень 1
        'pred_total': (1, '', 'Всего предсказаний: 30'),
        'pred_confirmed': (1, '', 'Подтверждено: 18'),
        'pred_future': (1, '', 'Будущих: 10'),
        'pred_tension': (1, '', 'В напряжении: 2'),
        # Чувствительность — уровень 1
        'sens_worst_chi': (1, '%', 'Худшая устойчивость к χ: 74.19%'),
        'sens_worst_beta': (1, '%', 'Худшая устойчивость к β₁₂: 96.77%'),
        'sens_best_chi': (1, '', 'Лучшая χ: 633'),
        'sens_best_beta': (1, '', 'Лучшая β₁₂: 4'),
        'sens_n_stable': (1, '', 'Точек в области стабильности: 12'),
        'sens_n_total': (1, '', 'Всего точек: 100'),
        # Benchmark — уровень 1
        'bench_n_models': (1, '', 'Моделей в benchmark: 6'),
        'bench_omega4_efficiency': (1, '', 'Эффективность Ω⁴: 242.755'),
    },
    verbose=False,
)


# ============================================================================
# ЧАСТЬ 5: ТОЧКА ВХОДА
# ============================================================================

if __name__ == '__main__':
    print("=" * 78)
    print("  Ω⁴-UNIFIED v79.0 — СИСТЕМНЫЕ МЕТРИКИ (system_metrics.py)")
    print("=" * 78)

    print(f"\n  Источник данных: "
          f"{'omega4_results.json' if _results else 'DEFAULTS'}")

    print(f"\n  ── СТАТИСТИКА ──")
    print(f"    Комбинированная σ: {SMC.stat_combined_sigma:.2f}σ")
    print(f"    Полиномов:         {SMC.stat_n_samples}")
    print(f"    Связей в анализе:  {SMC.stat_n_links}")
    print(f"    Связей > 3σ:       {SMC.stat_n_3sigma}")

    print(f"\n  ── КРОСС-ВАЛИДАЦИЯ ──")
    print(f"    LOO:       {SMC.cv_loo_rate:.1f}%")
    print(f"    K-Fold:    {SMC.cv_kfold_rate:.1f}%")
    print(f"    Test:      {SMC.cv_test_rate:.1f}%")
    print(f"    Общая:     {SMC.cv_overall:.1f}%")

    print(f"\n  ── ПРЕДСКАЗАНИЯ ──")
    print(f"    Всего:       {SMC.pred_total}")
    print(f"    Подтв.:      {SMC.pred_confirmed}")
    print(f"    Будущих:     {SMC.pred_future}")
    print(f"    Напряж.:     {SMC.pred_tension}")

    print(f"\n  ── ЧУВСТВИТЕЛЬНОСТЬ v1 ──")
    print(f"    Худшая (χ):    {SMC.sens_worst_chi:.2f}%")
    print(f"    Худшая (β₁₂):  {SMC.sens_worst_beta:.2f}%")
    print(f"    Лучшая точка:  χ = {SMC.sens_best_chi}, "
          f"β₁₂ = {SMC.sens_best_beta}")
    print(f"    Область:       {SMC.sens_n_stable}/{SMC.sens_n_total}")

    print(f"\n  ── BENCHMARK ──")
    print(f"    Моделей:       {SMC.bench_n_models}")
    print(f"    Эффективность: {SMC.bench_omega4_efficiency:.3f}")

    print(f"\n  📊 Всего в REGISTRY: {len(_CORE_REGISTRY)} констант.")
    print("=" * 78)
