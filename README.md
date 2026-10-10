# maroc-public-data

Moroccan **public holidays**, **school breaks**, open **civil-service concours** and **salaries by grade**, in Python or JavaScript. It is a thin client for the free [Wadifa Info API](https://www.wadifa-info.com/developpeurs): no key, no dependencies.

## Python

```bash
pip install git+https://github.com/wadifainfo/maroc-public-data
```

```python
import maroc_public_data as m

m.is_holiday("2026-11-18")        # True: Fête de l'Indépendance
m.holidays(2027)                  # [{'date': '2027-01-01', 'name_fr': 'Nouvel An', 'name_ar': ..., 'approximate': False}, ...]
m.school_breaks()                 # 2026/2027 breaks (décision ministérielle 047.26)
m.concours(limit=20)              # open recruitment exams with deadline and official notice
m.salaries()                      # indicative net monthly salary per grade (official simulator basis)
```

## JavaScript (Node 18+ / browsers)

```js
import { isHoliday, holidays, schoolBreaks, concours, salaries } from "./js/index.mjs";
await isHoliday("2026-11-18");    // true
```

## Data

| Function | Endpoint | Notes |
|---|---|---|
| `holidays()` | `/api/v1/jours-feries` | This year and next. Islamic holidays stay `approximate: true` until the Ministry of Habous confirms the moon sighting |
| `school_breaks()` | `/api/v1/vacances-scolaires` | Current school year, end dates inclusive |
| `concours()` | `/api/v1/concours` | Open concours from emploi-public.ma notices, updated hourly |
| `salaries()` | `/api/v1/salaires` | 370 grades. Pay by échelon: [CSV](https://www.wadifa-info.com/data/salaires-par-echelon-fonction-publique-maroc.csv) |

Calendar feeds you can subscribe to:
- holidays: `https://www.wadifa-info.com/agenda/jours-feries` (add `?lang=ar` for Arabic)
- school breaks: `https://www.wadifa-info.com/agenda/vacances-scolaires`

## Attribution

The **code** is MIT. The **data** is CC BY 4.0: wherever you display it, show "Source : Wadifa Info" with a link to https://www.wadifa-info.com, or to each item's `url`.

Datasets with DOI: [10.5281/zenodo.23078290](https://doi.org/10.5281/zenodo.23078290). More open data: [morocco-public-jobs-data](https://github.com/wadifainfo/morocco-public-jobs-data).
