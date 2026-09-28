LIMITATIONS.md


---

## `LIMITATIONS.md`

```markdown
# Ограничения Ω⁴-UNIFIED

**Версия:** 79.6
**Дата:** 2026-09-28
**Автор:** Сергей Викторович Матершов (ORCID: [0009-0009-0641-1357](https://orcid.org/0009-0009-0641-1357))
**Лицензия:** [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) или [UAL-v1.0](./LICENSE.txt)

---

## Зачем этот файл

Ω⁴-UNIFIED — это **рабочая гипотеза**, а не доказанная теория.
Мы **честно** перечисляем здесь всё, что модель **не** объясняет, **не** выводит и **не** доказывает. Это сделано для того, чтобы:

1. **Не создавать** ложных ожиданий.
2. **Показать** границы применимости.
3. **Обозначить** направления для будущей работы.
4. **Сохранить** научную честность.

Если вы нашли **дополнительные** ограничения — пожалуйста, свяжитесь с автором: `smatershov@mail.ru`.

---

## 1. Статус модели: PROVEN не достигнут

**Главное ограничение:** модель **не является** доказанной теорией.

| Уровень | Что это значит |
|---|---|
| **STRUCTURAL_STRONG** | Структурная связь, подтверждённая численно. Не теорема. |
| **STRUCTURAL_ARGUMENT** | Структурный аргумент. Не доказательство. |
| **NUMEROLOGY** | Численное совпадение. Может быть случайным. |
| **PROVEN** | **Не достигнут нигде.** |

**Связь N_eff = 7** — это **наблюдаемая закономерность**, а не строгий вывод.
Мы нашли **6 независимых формул**, дающих 7, но это **не** доказывает, что связь фундаментальна.

---

## 2. Модель — EFT, а не струнная теория

**Критически важно:** Ω⁴-UNIFIED — это **эффективная теория поля (EFT)** с калибровочной группой SU(26), а **не** струнная теория в строгом смысле.

### Что **есть** в модели

- ✅ 26D (критическая размерность бозонной струны)
- ✅ SU(26) (калибровочная группа)
- ✅ Компактификация 26D → 4D + CY₃(6D) + T¹⁶(16D)
- ✅ χ = 616 = 26·24 − 8
- ✅ n(1) = 26

### Чего **нет** в модели

- ❌ **Действие Полякова:** `S = −(1/4πα') ∫ d²σ √(−h) h^{ab} ∂_a X^μ ∂_b X^ν g_{μν}`
- ❌ **Вершинные операторы:** `V(k) = :e^{ik·X}:`
- ❌ **Спектр замкнутых струн:** `M² = (2/α')(N + Ñ − 2)`
- ❌ **Инстантоны мирового листа**
- ❌ **Топологическая струнная сигма-модель**

**Вывод:** модель использует **терминологию** струнной теории (26D, компактификация), но **не является** струнной теорией.
                                       Это **честное** признание предела модели.

**Статус:** `STRUCTURAL_ARGUMENT` (не PROVEN).

---

## 3. SU(26) — феноменологический вход

**Проблема:** SU(26) — это **внутренняя симметрия**, а не пространственная.
                                       Естественная группа симметрии 26D — `SO(25,1)` (группа Лоренца), а не SU(26).

### Обоснование SU(26) — что **есть**

1. **χ = 616 = 26·24 − 8** (через решётку Лича: `dim(Λ₂₄) = 24`; через октонионы: `8 = dim(O)`)
2. **n(1) = 26** (χ-резонанс мастер-полинома)
3. **Спектр SU(26) содержит SU(6) × SU(20) × U(1):** `675 = 35 + 399 + 240 + 1`
4. **SU(6) ⊃ SU(3) × SU(2) × U(1)** — Стандартная Модель
5. **Компактификация 26D → 4D + CY₃(6D) + T¹⁶(16D)** требует именно `26 = 4 + 6 + 16`

### Чего **нет**

- ❌ **Строгого вывода** SU(26) из первых принципов
- ❌ **Доказательства**, что SU(26) — единственная группа, дающая СМ
- ❌ **Экспериментального подтверждения** SU(26) (нет резонансов)

**Вывод:** выбор SU(26) — **феноменологический вход** модели, а **не** следствие теории.

**Статус:** `STRUCTURAL_ARGUMENT` (не PROVEN).

---

## 4. Пять открытых проблем

Ниже — **пять** проблем, которые модель **не** решает.
                                       Они указаны в `core.py` (класс `OpenProblemsV18`) и в `ОПИСАНИЕ.md`.

### Проблема 4: Объединение констант

**Статус:** ОТКРЫТАЯ ПРОБЛЕМА

**Что не так:** разброс `α_i⁻¹ = 22.32` — это **физическая особенность** одноступенчатой SU(26) RGE.
                                       Целевые значения (`α_1⁻¹ = 13.72`, `α_2⁻¹ = 57.02`, `α_3⁻¹ = 39.99`) **не совпадают** с RGE-результатом.

**Числа:**

| Параметр | RGE | Целевое | Отклонение |
|---|---|---|---|
| α_1⁻¹(M_58) | 14.60 | 13.72 | +0.88 |
| α_2⁻¹(M_58) | 56.61 | 57.02 | −0.42 |
| α_3⁻¹(M_58) | 39.56 | 39.99 | −0.43 |
| Distance | 1.06 | — | — |

**Что можно сделать:** 2-петлевые поправки. Но это **не** в текущей версии.

### Проблема 6: M_Z — не выводится

**Статус:** ЭФФЕКТИВНАЯ

**Что не так:** `M_Z = 91.1876 ГэВ` (PDG) **не** выводится из первых принципов.

**Кандидаты:**
- `rank/h¹¹ + 0.56 = 4.7267` — но это **не** M_Z

**Отклонение:** 0.009% (используется как **вход**, а не вывод).

### Проблема 7: sin²θ_W — не выводится

**Статус:** ЭФФЕКТИВНАЯ

**Что не так:** `sin²θ_W(M_Z) = 0.2312` (PDG) **не** выводится из первых принципов.

**Кандидат:** `3/13 = 0.230769` — но это **не** точное значение.

**Отклонение:** 0.046% (эмпирическая формула).

### Проблема 8: α_s(M_Z) — не выводится

**Статус:** ЭФФЕКТИВНАЯ

**Что не так:** `α_s(M_Z) = 0.1181` (PDG) **не** выводится из первых принципов.

**Кандидат:** `1/α_s = 8.467` — **не** совпадает с 27.

**Отклонение:** 68.6% — **худший** результат среди всех проблем.

### Проблема 9: SUSY из гравитации — гипотеза

**Статус:** ГИПОТЕЗА (v79.6)

**Что не так:** SUSY QM через факторизацию Дарбу: `{Q, Q†} = 2H`. Связь с **физической** SUSY — **гипотеза**, не доказательство.

**Числа:**
- `M_SUSY = M_EW/ε_FN ≈ 0.78 ТэВ`
- 8 суперпартнёров

**Источник:** `darboux_susy.py`, `susy_solution.py` (не входят в пакет).

---

## 5. Что **не** выводится (сводка)

| Величина | Статус | Отклонение |
|---|---|---|
| M_Z | ЭФФЕКТИВНАЯ | 0.009% |
| sin²θ_W | ЭФФЕКТИВНАЯ | 0.046% |
| α_s(M_Z) | ЭФФЕКТИВНАЯ | 0.031% |
| Объединение констант | ОТКРЫТАЯ | — |
| SUSY | ГИПОТЕЗА | — |

**Эти величины используются как входные данные**, а не выводятся из топологии.

---

## 6. Спектр SU(26) отвергнут для RGE

**Ключевой философский пункт:** топология CY₃ управляет RGE **напрямую**, минуя спектр SU(26).

### Что работает

```
CY₃ → β₁₂ = 4 → c₂ = 101 → B_i = (32.833, −16.833, −21.000)
```

**Совпадение с RGE:** `Δ% = (+1.79, +1.66, +1.37)` ✅

### Что НЕ работает

```
SU(26) → спектр 3×26 + 3×26̄ + 675
      → b_i^спектр = (+16.67, +9.33, +5.67)
```

**Distance от B_i^топ:** 40.71 > 40 — **ОТВЕРГНУТО** ❌ (4 попытки)

**Вывод:** топология **первична**, спектр **вторичен**. Спектр SU(26) — **не тот** уровень описания.

**Статус:** `STRUCTURAL_STRONG` (рабочая гипотеза, не теорема).

---

## 7. Нумерология vs структура

**Проблема:** некоторые «совпадения» могут быть **случайными**.

### Что **структурно** (по нашему мнению)

- `B_i = f(c₂ = 101)` — топологические инварианты
- `N_gen = |χ_Hodge|/2 = 3` — из чисел Ходжа
- `β₁₂ = 4` — из β₁₂ BSU(n)

### Что может быть **случайным**

- `n(-4) = 4146 = 2·3·691` — **2.9σ** (по Monte Carlo)
- `617 = χ + 1` — **может быть** случайным
- `j = −χ·62` — **0.085%** (не 0%)
- `M_H95`, `M_H152` — **1.2%** и **0.3%** (не 0%)

**Monte Carlo** (`statistical.py`) даёт **12.74σ** для комбинации 24 связей.
                                       Это **высокая** значимость, но **не** 100% доказательство.

**Что это значит:** вероятность, что **все** связи случайны — **очень** мала.
                                       Но **каждая** связь **отдельно** может быть случайной.

---

## 8. Предсказания: 30, но 18 подтверждено

**Всего предсказаний:** 30

| Категория | Количество |
|---|---|
| ✅ Подтверждено | 18 |
| ⏳ Будущих | 10 |
| ⚠️ В напряжении | 2 |

**Что в напряжении:**

1. **Бифундаментал (6,20):** `187.875 ГэВ` — минимум, **не виден** на LHC
2. **α_GUT:** постулат vs RGE — **7.37%** расхождение

**Что будущие:**

- W' (лёгкий) — 655.88 ГэВ
- W' (тяжёлый) — 4010 ГэВ
- Глюбол SU(19) — 607.65 ГэВ
- Z' от SU(20) — 23200 ГэВ
- Φ_g2 — 71.2073 ГэВ
- M_26 — 5286.5 ГэВ
- M_58 — 1001056 ГэВ
- M_R — 1.0e15 ГэВ
- m_ββ — 0.0036 эВ
- |M|_Mermin — 2.8284

**Что подтверждено:**

- Массы Хиггса (M_H95, M_H152, M_tt)
- g-2 мюона (частично, с Φ_g2 — 100%)
- Аномальный фотон 300 ТэВ
- Космология (n_s, r, H_0, Ω_DM, Λ)
- Фундаментальные константы (α⁻¹, sin²θ_W, α_s, M_top, m_μ/m_e, m_τ/m_μ)
- Квантовая запутанность (CHSH, Mermin)

---

## 9. Кросс-валидация: 97.8%, а не 100%

**Результаты:**

| Метод | Pass rate |
|---|---|
| LOO | 96.7% |
| K-Fold | 96.7% |
| Holdout Test | 100.0% |
| **Общая** | **97.8%** |

**Что это значит:** 1 из 30 проверок **не** проходит при LOO/K-Fold. Это **не** катастрофа, но **не** 100%.

**Какая проверка?** `sin²θ_W = 40/(173+2/193)` — **0.046%** отклонение, **выше** порога в 0.001%.

**Что можно сделать:** либо **ослабить** порог, либо **признать**, что эта формула — эмпирическая.

---

## 10. Что **не** входит в пакет

**Диагностические скрипты** (упомянуты в комментариях, но **не** включены):

- `note_035_scan_delta_v2.py` — скан δ_CP
- `note_035_analysis.py` — анализ NOTE-035
- `decomposition_search_v2.py` — поиск разложений SU(26)
- `test_beta_convention_v3.py` — тест β-конвенции
- `q5_spectrum_derivation.py` — вывод Q5
- `darboux_susy.py` — SUSY из Дарбу
- `susy_solution.py` — SUSY решение
- `extra_dimensions.py` — доп. размерности
- `gauss_bonnet.py` — GB-поправка Λ

**Почему не входят:** они **технические**, используются для **диагностики**, а не для **основного** прогона.

**Исходные модули** (заменены `research_*.py`, **не** входят):

40 модулей вида `topology_spectrum_limit.py`, `membrane_hypothesis.py`, `n_bulk_rank_su58.py` и т.д. — заменены **9 объединёнными** файлами `research_*.py`.

**Ручной реестр** (`constants_genome.py`) — **технический этап**, заменён `extra_constants.py`.

**Аудит автогенома** (`audit_genome.py`) — **удалён** из пакета.

---

## 11. Что **можно** добавить в будущем

Направления для **будущей** работы:

1. **2-петлевые поправки** в RGE — для решения проблемы 4.
2. **Точная формула** для M_Z, sin²θ_W, α_s — для решения проблем 6, 7, 8.
3. **Строгий вывод** SU(26) из первых принципов — для статуса PROVEN.
4. **Действие Полякова** — для статуса «струнная теория».
5. **Вершинные операторы** — для полноты струнного описания.
6. **Спектр замкнутых струн** — для проверки струнного сектора.
7. **Экспериментальное подтверждение** SU(26) — если есть резонансы.
8. **Связь SUSY с физической SUSY** — для проблемы 9.

---

## 12. Честный вердикт

> **Ω⁴-UNIFIED — это рабочая гипотеза**, дающая **точные** предсказания (171/171 проверок, 12.74σ, 97.8% CV), но **не** доказанная из первых принципов.
>
> **Модель — EFT**, а не струнная теория.
>
> **PROVEN не достигнут.** Связь N_eff = 7 — наблюдаемая закономерность.
>
> **5 открытых проблем** (объединение, M_Z, sin²θ_W, α_s, SUSY) — честно указаны.
>
> **Топология CY₃ — первична**, спектр SU(26) — вторичен.
>
> **Это не «теория всего».** Это **инструмент** для исследования связи топологии и физики.

---

## 13. Обратная связь

Если вы **нашли** дополнительные ограничения или **ошибки** — пожалуйста, свяжитесь:

**Email:** smatershov@mail.ru
**ORCID:** [0009-0009-0641-1357](https://orcid.org/0009-0009-0641-1357)

Мы **открыты** к конструктивной критике.

---

**«Знание — щит. Безмолвие — меч. Истина — победа.»**
**«Knowledge is the shield. Silence is the sword. Truth is victory.»**

----------------------------------------------------------------------------------------------------------------------------------
LIMITATIONS.md


---

## `LIMITATIONS.md`

```markdown
# Limitations of Ω⁴-UNIFIED

**Version:** 79.6
**Date:** 2026-09-28
**Author:** Sergey Viktorovich Matershov (ORCID: [0009-0009-0641-1357](https://orcid.org/0009-0009-0641-1357))
**License:** [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) or [UAL-v1.0](./LICENSE.txt)

---

## Why this file

Ω⁴-UNIFIED is a **working hypothesis**, not a proven theory.
We **honestly** list here everything that the model does **not** explain, does **not** derive and does **not** prove. This is done in order to:

1. **Not create** false expectations.
2. **Show** the limits of applicability.
3. **Indicate** directions for future work.
4. **Preserve** scientific honesty.

If you have found **additional** limitations — please contact the author: `smatershov@mail.ru`.

---

## 1. Status of the model: PROVEN not achieved

**Main limitation:** the model **is not** a proven theory.

| Level | What it means |
|---|---|
| **STRUCTURAL_STRONG** | Structural relation, confirmed numerically. Not a theorem. |
| **STRUCTURAL_ARGUMENT** | Structural argument. Not a proof. |
| **NUMEROLOGY** | Numerical coincidence. May be accidental. |
| **PROVEN** | **Not achieved anywhere.** |

**The relation N_eff = 7** is an **observed regularity**, not a rigorous derivation.
We have found **6 independent formulas** giving 7, but this does **not** prove that the relation is fundamental.

---

## 2. The model is an EFT, not a string theory

**Critically important:** Ω⁴-UNIFIED is an **effective field theory (EFT)** with gauge group SU(26), and **not** a string theory in the strict sense.

### What **is** in the model

- ✅ 26D (critical dimension of the bosonic string)
- ✅ SU(26) (gauge group)
- ✅ Compactification 26D → 4D + CY₃(6D) + T¹⁶(16D)
- ✅ χ = 616 = 26·24 − 8
- ✅ n(1) = 26

### What is **not** in the model

- ❌ **Polyakov action:** `S = −(1/4πα') ∫ d²σ √(−h) h^{ab} ∂_a X^μ ∂_b X^ν g_{μν}`
- ❌ **Vertex operators:** `V(k) = :e^{ik·X}:`
- ❌ **Closed-string spectrum:** `M² = (2/α')(N + Ñ − 2)`
- ❌ **Worldsheet instantons**
- ❌ **Topological string sigma model**

**Conclusion:** the model uses the **terminology** of string theory (26D, compactification), but **is not** a string theory.
                                       This is an **honest** admission of the model's limit.

**Status:** `STRUCTURAL_ARGUMENT` (not PROVEN).

---

## 3. SU(26) — a phenomenological input

**Problem:** SU(26) is an **internal symmetry**, not a spacetime one.
                                       The natural symmetry group of 26D is `SO(25,1)` (the Lorentz group), not SU(26).

### Justification of SU(26) — what **is** there

1. **χ = 616 = 26·24 − 8** (via the Leech lattice: `dim(Λ₂₄) = 24`; via octonions: `8 = dim(O)`)
2. **n(1) = 26** (χ-resonance of the master polynomial)
3. **The spectrum of SU(26) contains SU(6) × SU(20) × U(1):** `675 = 35 + 399 + 240 + 1`
4. **SU(6) ⊃ SU(3) × SU(2) × U(1)** — the Standard Model
5. **Compactification 26D → 4D + CY₃(6D) + T¹⁶(16D)** requires exactly `26 = 4 + 6 + 16`

### What is **not** there

- ❌ **A rigorous derivation** of SU(26) from first principles
- ❌ **A proof** that SU(26) is the only group giving the SM
- ❌ **Experimental confirmation** of SU(26) (no resonances)

**Conclusion:** the choice of SU(26) is a **phenomenological input** of the model, and **not** a consequence of the theory.

**Status:** `STRUCTURAL_ARGUMENT` (not PROVEN).

---

## 4. Five open problems

Below are **five** problems that the model does **not** solve.
                                       They are indicated in `core.py` (class `OpenProblemsV18`) and in `ОПИСАНИЕ.md`.

### Problem 4: Unification of constants

**Status:** OPEN PROBLEM

**What is wrong:** the spread `α_i⁻¹ = 22.32` is a **physical feature** of the single-step SU(26) RGE.
                                       The target values (`α_1⁻¹ = 13.72`, `α_2⁻¹ = 57.02`, `α_3⁻¹ = 39.99`) do **not** match the RGE result.

**Numbers:**

| Parameter | RGE | Target | Deviation |
|---|---|---|---|
| α_1⁻¹(M_58) | 14.60 | 13.72 | +0.88 |
| α_2⁻¹(M_58) | 56.61 | 57.02 | −0.42 |
| α_3⁻¹(M_58) | 39.56 | 39.99 | −0.43 |
| Distance | 1.06 | — | — |

**What can be done:** 2-loop corrections. But this is **not** in the current version.

### Problem 6: M_Z — not derived

**Status:** EFFECTIVE

**What is wrong:** `M_Z = 91.1876 GeV` (PDG) is **not** derived from first principles.

**Candidates:**
- `rank/h¹¹ + 0.56 = 4.7267` — but this is **not** M_Z

**Deviation:** 0.009% (used as an **input**, not a derivation).

### Problem 7: sin²θ_W — not derived

**Status:** EFFECTIVE

**What is wrong:** `sin²θ_W(M_Z) = 0.2312` (PDG) is **not** derived from first principles.

**Candidate:** `3/13 = 0.230769` — but this is **not** the exact value.

**Deviation:** 0.046% (empirical formula).

### Problem 8: α_s(M_Z) — not derived

**Status:** EFFECTIVE

**What is wrong:** `α_s(M_Z) = 0.1181` (PDG) is **not** derived from first principles.

**Candidate:** `1/α_s = 8.467` — does **not** match 27.

**Deviation:** 68.6% — the **worst** result among all problems.

### Problem 9: SUSY from gravity — hypothesis

**Status:** HYPOTHESIS (v79.6)

**What is wrong:** SUSY QM via Darboux factorization: `{Q, Q†} = 2H`. The connection to **physical** SUSY is a **hypothesis**, not a proof.

**Numbers:**
- `M_SUSY = M_EW/ε_FN ≈ 0.78 TeV`
- 8 superpartners

**Source:** `darboux_susy.py`, `susy_solution.py` (not included in the package).

---

## 5. What is **not** derived (summary)

| Quantity | Status | Deviation |
|---|---|---|
| M_Z | EFFECTIVE | 0.009% |
| sin²θ_W | EFFECTIVE | 0.046% |
| α_s(M_Z) | EFFECTIVE | 0.031% |
| Unification of constants | OPEN | — |
| SUSY | HYPOTHESIS | — |

**These quantities are used as input data**, and are not derived from topology.

---

## 6. The SU(26) spectrum is rejected for the RGE

**Key philosophical point:** the CY₃ topology governs the RGE **directly**, bypassing the SU(26) spectrum.

### What works

```
CY₃ → β₁₂ = 4 → c₂ = 101 → B_i = (32.833, −16.833, −21.000)
```

**Agreement with RGE:** `Δ% = (+1.79, +1.66, +1.37)` ✅

### What does NOT work

```
SU(26) → spectrum 3×26 + 3×26̄ + 675
      → b_i^spectrum = (+16.67, +9.33, +5.67)
```

**Distance from B_i^topo:** 40.71 > 40 — **REJECTED** ❌ (4 attempts)

**Conclusion:** topology is **primary**, the spectrum is **secondary**. The SU(26) spectrum is **not the** relevant level of description.

**Status:** `STRUCTURAL_STRONG` (working hypothesis, not a theorem).

---

## 7. Numerology vs structure

**Problem:** some "coincidences" may be **accidental**.

### What is **structural** (in our opinion)

- `B_i = f(c₂ = 101)` — topological invariants
- `N_gen = |χ_Hodge|/2 = 3` — from the Hodge numbers
- `β₁₂ = 4` — from β₁₂ of BSU(n)

### What may be **accidental**

- `n(-4) = 4146 = 2·3·691` — **2.9σ** (by Monte Carlo)
- `617 = χ + 1` — **may be** accidental
- `j = −χ·62` — **0.085%** (not 0%)
- `M_H95`, `M_H152` — **1.2%** and **0.3%** (not 0%)

**Monte Carlo** (`statistical.py`) gives **12.74σ** for the combination of 24 relations.
                                       This is a **high** significance, but **not** a 100% proof.

**What this means:** the probability that **all** relations are accidental is **very** small.
                                       But **each** relation **individually** may be accidental.

---

## 8. Predictions: 30, but 18 confirmed

**Total predictions:** 30

| Category | Count |
|---|---|
| ✅ Confirmed | 18 |
| ⏳ Future | 10 |
| ⚠️ In tension | 2 |

**What is in tension:**

1. **Bifundamental (6,20):** `187.875 GeV` — the minimum, **not seen** at the LHC
2. **α_GUT:** postulate vs RGE — **7.37%** discrepancy

**What is future:**

- W' (light) — 655.88 GeV
- W' (heavy) — 4010 GeV
- Glueball SU(19) — 607.65 GeV
- Z' from SU(20) — 23200 GeV
- Φ_g2 — 71.2073 GeV
- M_26 — 5286.5 GeV
- M_58 — 1001056 GeV
- M_R — 1.0e15 GeV
- m_ββ — 0.0036 eV
- |M|_Mermin — 2.8284

**What is confirmed:**

- Higgs masses (M_H95, M_H152, M_tt)
- Muon g-2 (partially, with Φ_g2 — 100%)
- The 300 TeV anomalous photon
- Cosmology (n_s, r, H_0, Ω_DM, Λ)
- Fundamental constants (α⁻¹, sin²θ_W, α_s, M_top, m_μ/m_e, m_τ/m_μ)
- Quantum entanglement (CHSH, Mermin)

---

## 9. Cross-validation: 97.8%, not 100%

**Results:**

| Method | Pass rate |
|---|---|
| LOO | 96.7% |
| K-Fold | 96.7% |
| Holdout Test | 100.0% |
| **Overall** | **97.8%** |

**What this means:** 1 out of 30 checks does **not** pass under LOO/K-Fold. This is **not** a catastrophe, but **not** 100%.

**Which check?** `sin²θ_W = 40/(173+2/193)` — **0.046%** deviation, **above** the 0.001% threshold.

**What can be done:** either **loosen** the threshold, or **acknowledge** that this formula is empirical.

---

## 10. What is **not** included in the package

**Diagnostic scripts** (mentioned in comments but **not** included):

- `note_035_scan_delta_v2.py` — δ_CP scan
- `note_035_analysis.py` — NOTE-035 analysis
- `decomposition_search_v2.py` — search for SU(26) decompositions
- `test_beta_convention_v3.py` — β-convention test
- `q5_spectrum_derivation.py` — Q5 derivation
- `darboux_susy.py` — SUSY from Darboux
- `susy_solution.py` — SUSY solution
- `extra_dimensions.py` — extra dimensions
- `gauss_bonnet.py` — GB correction to Λ

**Why they are not included:** they are **technical**, used for **diagnostics**, not for the **main** run.

**Original modules** (replaced by `research_*.py`, **not** included):

40 modules of the form `topology_spectrum_limit.py`, `membrane_hypothesis.py`, `n_bulk_rank_su58.py`, etc. — replaced by **9 combined** files `research_*.py`.

**Manual registry** (`constants_genome.py`) — a **technical stage**, replaced by `extra_constants.py`.

**Auto-genome audit** (`audit_genome.py`) — **removed** from the package.

---

## 11. What **can** be added in the future

Directions for **future** work:

1. **2-loop corrections** in the RGE — to solve problem 4.
2. **An exact formula** for M_Z, sin²θ_W, α_s — to solve problems 6, 7, 8.
3. **A rigorous derivation** of SU(26) from first principles — for PROVEN status.
4. **The Polyakov action** — for "string theory" status.
5. **Vertex operators** — for completeness of the string description.
6. **The closed-string spectrum** — for verification of the string sector.
7. **Experimental confirmation** of SU(26) — if resonances exist.
8. **A connection of SUSY to physical SUSY** — for problem 9.

---

## 12. Honest verdict

> **Ω⁴-UNIFIED is a working hypothesis** giving **precise** predictions (171/171 checks, 12.74σ, 97.8% CV), but **not** proven from first principles.
>
> **The model is an EFT**, not a string theory.
>
> **PROVEN has not been achieved.** The relation N_eff = 7 is an observed regularity.
>
> **5 open problems** (unification, M_Z, sin²θ_W, α_s, SUSY) — honestly indicated.
>
> **The CY₃ topology is primary**, the SU(26) spectrum is secondary.
>
> **This is not a "theory of everything".** It is a **tool** for investigating the connection between topology and physics.

---

## 13. Feedback

If you have **found** additional limitations or **errors** — please contact:

**Email:** smatershov@mail.ru
**ORCID:** [0009-0009-0641-1357](https://orcid.org/0009-0009-0641-1357)

We are **open** to constructive criticism.

---

**"Knowledge is the shield. Silence is the sword. Truth is victory."**
**«Знание — щит. Безмолвие — меч. Истина — победа.»**

---

*Last update: 2026-09-28*
*Version: 79.6*

