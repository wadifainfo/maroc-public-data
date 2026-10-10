"""Moroccan public holidays, school breaks, civil-service concours and salaries from the free Wadifa Info API.

    >>> import maroc_public_data as m
    >>> m.is_holiday("2026-11-18")          # Fête de l'Indépendance
    True
    >>> [h["name_fr"] for h in m.holidays(2027)][:2]

No API key, no dependencies (standard library only). Data licence: CC BY 4.0 — show
"Source : Wadifa Info" with a link (https://www.wadifa-info.com) wherever you display it.
Docs: https://www.wadifa-info.com/developpeurs
"""
import datetime as _dt
import json as _json
import urllib.request as _req

__version__ = "0.1.0"
BASE = "https://www.wadifa-info.com/api/v1/"
_UA = {"User-Agent": "maroc-public-data/" + __version__}
_cache = {}


def _get(path):
    if path not in _cache:
        with _req.urlopen(_req.Request(BASE + path, headers=_UA), timeout=30) as r:
            _cache[path] = _json.loads(r.read().decode("utf-8"))
    return _cache[path]


def holidays(year=None):
    """Public holidays (this year and next). Each item: date, name_fr, name_ar, religious, approximate.
    Islamic holidays stay approximate=True until the Ministry of Habous confirms the moon sighting."""
    items = _get("jours-feries")["holidays"]
    return [h for h in items if year is None or h["date"].startswith(str(year))]


def is_holiday(day):
    """True if `day` (date or 'YYYY-MM-DD') is a Moroccan public holiday."""
    day = day.isoformat() if isinstance(day, (_dt.date, _dt.datetime)) else str(day)[:10]
    return any(h["date"] == day for h in holidays())


def school_breaks():
    """School breaks of the current school year (start, end inclusive, name_fr, name_ar)."""
    return _get("vacances-scolaires")["breaks"]


def concours(lang="fr", limit=100):
    """Open public-service recruitment exams: id, grade, employer, posts, published, deadline, url, official_notice."""
    return _get("concours?lang=%s&limit=%d" % (lang, limit))["items"]


def salaries():
    """Indicative net monthly salary at the 1st échelon for each civil-service grade (official simulator basis)."""
    return _get("salaires")["items"]


if __name__ == "__main__":   # smoke test against the live API
    assert any(h["date"].endswith("-11-18") for h in holidays()), "Independence Day missing"
    assert is_holiday("2026-11-18") and not is_holiday("2026-11-17")
    assert school_breaks() and "start" in school_breaks()[0]
    assert salaries() and "net_monthly_mad" in salaries()[0]
    c = concours(limit=3)
    assert isinstance(c, list) and (not c or "deadline" in c[0])
    print("ok", len(holidays()), "holidays,", len(salaries()), "grades,", len(concours()), "open concours")
