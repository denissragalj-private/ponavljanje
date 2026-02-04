"""
PONAVLJANJE KOLEKCIJA (tuple, list, dict, set) — 15 zadataka
Pravila:
- Student smije pisati SAMO unutar tijela funkcije (između STUDENT CODE START/END).
- Pomoćne funkcije su već gotove i student ih smije koristiti.
- Provjera rješenja radi se preko assert testova na dnu.
"""

from datetime import datetime, timedelta


# ------------------------------------------------------------
# POMOĆNE FUNKCIJE (student ih smije koristiti, ali ne mijenjati)
# ------------------------------------------------------------

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


# ------------------------------------------------------------
# ZADACI (student piše samo unutar funkcija)
# ------------------------------------------------------------

def zad01_broj_neispravnih(serija: list) -> int:
    """
    Tema: proizvodnja
    U listi 'serija' su statusi komada: 'OK' ili 'NOK'.
    Vrati koliko ima 'NOK'.
    """
    # STUDENT CODE START
    # Napiši petlju i brojač.
    pass
    # STUDENT CODE END


def zad02_najduzi_zastoj(zastoje_min: tuple) -> int:
    """
    Tema: proizvodnja
    U tuple-u su trajanja zastoja u minutama.
    Vrati najveći zastoj (max).
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


def zad03_filtriraj_temperaturu(mjerenja: list, prag: float) -> list:
    """
    Tema: proizvodnja / kontrola kvalitete
    'mjerenja' je lista temperatura (float).
    Vrati novu listu koja sadrži samo temperature strogo veće od 'prag'.
    Redoslijed mora ostati isti.
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


def zad04_top3_najvecih_potrosaca(potrosnja: dict) -> list:
    """
    Tema: proizvodnja / energija
    'potrosnja' je rječnik {naziv_stroja: kWh}.
    Vrati listu naziva 3 stroja s najvećom potrošnjom.
    Ako ima manje od 3 stroja, vrati sve (sortirano od najvećeg prema manjem).
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


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


def zad06_skup_materijala(nalozi: list) -> set:
    """
    Tema: proizvodnja / skladište
    'nalozi' je lista naloga, svaki nalog je dict:
        {"id": "N1", "materijali": ["ALU", "VIJAK", "BOJA"]}

    Vrati set svih jedinstvenih materijala koji se pojavljuju u svim nalozima.
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


def zad07_materijali_koji_nedostaju(potrebno: set, dostupno: set) -> set:
    """
    Tema: skladište
    Vrati set materijala koji su potrebni, ali nisu dostupni.
    (razlika skupova)
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


def zad08_spoji_serije(serija_a: list, serija_b: list) -> list:
    """
    Tema: proizvodnja
    Dvije serije mjerenja (liste brojeva).
    Vrati novu listu gdje su elementi naizmjenično:
    [a0, b0, a1, b1, ...]
    Ako je jedna lista duža, ostatak se dodaje na kraj.
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


def zad09_rjecnik_kolicina_po_artiklu(stavke: list) -> dict:
    """
    Tema: proizvodnja / narudžbe
    'stavke' je lista tuple-ova: (sifra_artikla, kolicina)
    Npr. [("A1", 2), ("A2", 1), ("A1", 3)]
    Vrati rječnik ukupnih količina po artiklu: {"A1": 5, "A2": 1}
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


def zad10_korisnici_duznici(pretplate: dict) -> tuple:
    """
    Tema: pretplate
    'pretplate' je rječnik:
      {
        "ana": {"status": "NEPLACENO", "iznos": 20.0},
        "marko": {"status": "PLACENO", "iznos": 20.0},
        ...
      }

    Zadatak:
    - Vrati tuple (duznici_lista, ukupno_dugovanje)
    - duznici_lista: sortirana lista korisnika koji su NEPLACENO (abecedno)
    - ukupno_dugovanje: zbroj iznosa za NEPLACENO
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


def zad11_ukupno_naplaceno(pretplate: dict) -> float:
    """
    Tema: pretplate
    Iz istog formata kao zad10.
    Vrati ukupno naplaćeno (zbroj iznosa gdje je status 'PLACENO').
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


def zad12_najcesci_status(dogadaji: list) -> str:
    """
    Tema: proizvodnja / logovi
    'dogadaji' je lista stringova statusa, npr. ["START", "STOP", "STOP", "PAUSE"]
    Vrati status koji se najčešće pojavljuje.
    Ako su izjednačeni, vrati onaj koji je prvi abecedno.
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


def zad13_izdvoji_radne_dane(datumi: tuple) -> list:
    """
    Tema: raspored proizvodnje
    'datumi' je tuple stringova datuma 'YYYY-MM-DD'.
    Vrati listu samo onih datuma koji NISU vikend (pon-pet).
    Pomoć: is_weekend(date_str)
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


def zad14_normaliziraj_tagove(tagovi: list) -> set:
    """
    Tema: obrada podataka
    'tagovi' je lista stringova (mogu imati razmake i različita velika/mala slova).
    Vrati set normaliziranih tagova:
      - trim (ukloni razmake s početka/kraja)
      - pretvori u lower-case
      - ignoriraj prazne nakon trimanja
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


def zad15_kupi_pakete(korisnici: dict) -> dict:
    """
    Tema: pretplate / izvještaj
    'korisnici' je rječnik:
      {
        "ana": {"paket": "BASIC", "cijena": 10},
        "marko": {"paket": "PRO", "cijena": 25},
        ...
      }

    Vrati novi rječnik grupiran po paketu:
      {
        "BASIC": {"broj": 2, "ukupno": 20},
        "PRO": {"broj": 1, "ukupno": 25}
      }

    Napomena: 'broj' je broj korisnika u paketu, 'ukupno' je suma cijena.
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


# ------------------------------------------------------------
# ASSERT TESTOVI (ne mijenjati)
# ------------------------------------------------------------

# Zad01
assert zad01_broj_neispravnih(["OK", "NOK", "OK", "NOK", "NOK"]) == 3
assert zad01_broj_neispravnih([]) == 0

# Zad02
assert zad02_najduzi_zastoj((5, 12, 3, 12, 1)) == 12
assert zad02_najduzi_zastoj((0,)) == 0

# Zad03
assert zad03_filtriraj_temperaturu([21.0, 22.5, 19.9, 23.1], 22.0) == [22.5, 23.1]
assert zad03_filtriraj_temperaturu([], 10.0) == []

# Zad04
pot = {"S1": 10, "S2": 50, "S3": 20, "S4": 30}
assert zad04_top3_najvecih_potrosaca(pot) == ["S2", "S4", "S3"]
assert zad04_top3_najvecih_potrosaca({"S1": 5, "S2": 1}) == ["S1", "S2"]

# Zad05
nalozi = {
    "NALOG-1": {"start": "2026-02-01", "trajanje_sati": 12},  # 2 dana -> 2026-02-03
    "NALOG-2": {"start": "2026-02-03", "trajanje_sati": 7},   # 1 dan  -> 2026-02-04
    "NALOG-3": {"start": "2026-02-02", "trajanje_sati": 16},  # 2 dana -> 2026-02-04
}
assert zad05_ukupno_sati_i_kraj_procesa(nalozi, hours_per_day=8) == (35, "2026-02-04")

# Zad06
nal = [
    {"id": "N1", "materijali": ["ALU", "VIJAK"]},
    {"id": "N2", "materijali": ["BOJA", "ALU"]},
]
assert zad06_skup_materijala(nal) == {"ALU", "VIJAK", "BOJA"}

# Zad07
assert zad07_materijali_koji_nedostaju({"A", "B", "C"}, {"B"}) == {"A", "C"}
assert zad07_materijali_koji_nedostaju(set(), {"X"}) == set()

# Zad08
assert zad08_spoji_serije([1, 2, 3], [10, 20]) == [1, 10, 2, 20, 3]
assert zad08_spoji_serije([], [7, 8]) == [7, 8]

# Zad09
assert zad09_rjecnik_kolicina_po_artiklu([("A1", 2), ("A2", 1), ("A1", 3)]) == {"A1": 5, "A2": 1}
assert zad09_rjecnik_kolicina_po_artiklu([]) == {}

# Zad10
pret = {
    "ana": {"status": "NEPLACENO", "iznos": 20.0},
    "marko": {"status": "PLACENO", "iznos": 20.0},
    "iva": {"status": "NEPLACENO", "iznos": 15.5},
}
assert zad10_korisnici_duznici(pret) == (["ana", "iva"], 35.5)

# Zad11
assert zad11_ukupno_naplaceno(pret) == 20.0
assert zad11_ukupno_naplaceno({}) == 0.0

# Zad12
assert zad12_najcesci_status(["START", "STOP", "STOP", "PAUSE", "PAUSE"]) == "PAUSE"  # tie STOP/PAUSE -> PAUSE abecedno?
# Provjera: "PAUSE" < "STOP" => True, pa treba "PAUSE"
assert zad12_najcesci_status(["X", "Y", "X"]) == "X"

# Zad13
assert zad13_izdvoji_radne_dane(("2026-02-06", "2026-02-07", "2026-02-08", "2026-02-09")) == ["2026-02-06", "2026-02-09"]
# 2026-02-07 i 2026-02-08 su vikend (sub/ned)

# Zad14
assert zad14_normaliziraj_tagove(["  Hitno ", "HITNO", "  ", "Grad "]) == {"hitno", "grad"}
assert zad14_normaliziraj_tagove([]) == set()

# Zad15
kor = {
    "ana": {"paket": "BASIC", "cijena": 10},
    "marko": {"paket": "PRO", "cijena": 25},
    "iva": {"paket": "BASIC", "cijena": 10},
}
assert zad15_kupi_pakete(kor) == {
    "BASIC": {"broj": 2, "ukupno": 20},
    "PRO": {"broj": 1, "ukupno": 25},
}

print("Svi testovi su prošli (kada studenti implementiraju funkcije).")
