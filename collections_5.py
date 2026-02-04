from datetime import datetime, timedelta


def parse_date(date_str: str) -> datetime:
    """Prima datum u formatu 'YYYY-MM-DD' i vraća datetime."""
    return datetime.strptime(date_str, "%Y-%m-%d")


def format_date(dt: datetime) -> str:
    """Pretvara datetime u string 'YYYY-MM-DD'."""
    return dt.strftime("%Y-%m-%d")


def add_days(date_str: str, days: int) -> str:
    """Dodaje broj dana na datum (YYYY-MM-DD) i vraća novi datum (YYYY-MM-DD)."""
    dt = parse_date(date_str) + timedelta(days=days)
    return format_date(dt)


def add_hours_to_date(date_str: str, hours: int, hours_per_day: int = 8) -> str:
    """
    Dodaje sate na datum tako da sate pretvori u dane (ceil), pa doda dane na datum.
    Npr. 9 sati uz 8 sati/dan => 2 dana.
    """
    if hours <= 0:
        return date_str
    days = (hours + hours_per_day - 1) // hours_per_day  # ceil
    return add_days(date_str, days)


def is_weekend(date_str: str) -> bool:
    """Vraća True ako je datum subota ili nedjelja."""
    dt = parse_date(date_str)
    return dt.weekday() >= 5  # 5=Sat, 6=Sun


def zad05_ukupno_sati_i_kraj_procesa(nalozi: dict, hours_per_day: int = 8) -> tuple:
    """
    Tema: proizvodnja (nalozi)
    'nalozi' je rječnik:
        {
          "NALOG-1": {"start": "2026-02-01", "trajanje_sati": 12},
          "NALOG-2": {"start": "2026-02-03", "trajanje_sati": 7},
          ...
        }

    Zadatak:
    - Izračunaj ukupno sati (zbroj svih 'trajanje_sati').
    - Nađi datum završetka zadnjeg naloga.
      Za svaki nalog kraj računaš pomoću helpera:
         add_hours_to_date(start, trajanje_sati, hours_per_day)

    Vrati tuple: (ukupno_sati, krajnji_datum) gdje je krajnji_datum 'YYYY-MM-DD'.
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


nalozi = {
    "NALOG-1": {"start": "2026-02-01", "trajanje_sati": 12},  # 2 dana -> 2026-02-03
    "NALOG-2": {"start": "2026-02-03", "trajanje_sati": 7},   # 1 dan  -> 2026-02-04
    "NALOG-3": {"start": "2026-02-02", "trajanje_sati": 16},  # 2 dana -> 2026-02-04
}
assert zad05_ukupno_sati_i_kraj_procesa(nalozi, hours_per_day=8) == (35, "2026-02-04")
