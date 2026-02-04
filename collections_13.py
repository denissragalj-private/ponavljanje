from datetime import datetime, timedelta


def parse_date(date_str: str) -> datetime:
    """Prima datum u formatu 'YYYY-MM-DD' i vraća datetime."""
    return datetime.strptime(date_str, "%Y-%m-%d")


def is_weekend(date_str: str) -> bool:
    """Vraća True ako je datum subota ili nedjelja."""
    dt = parse_date(date_str)
    return dt.weekday() >= 5  # 5=Sat, 6=Sun


def zad13_izdvoji_radne_dane(datumi: tuple) -> list:
    """
    Tema: raspored proizvodnje
    'datumi' je tuple stringova datuma 'YYYY-MM-DD'.
    Vrati listu samo onih datuma koji NISU vikend (pon-pet).
    Pomoć: is_weekend(date_str)
    """
    # STUDENT CODE START

    # OPCIJA
    # return [datum for datum in datumi if not is_weekend(datum)]

    radni_dani = []

    for datum in datumi:
        if not is_weekend(datum):
            radni_dani.append(datum)

    return radni_dani
    # STUDENT CODE END


assert zad13_izdvoji_radne_dane(("2026-02-06", "2026-02-07", "2026-02-08", "2026-02-09")) == ["2026-02-06", "2026-02-09"]
