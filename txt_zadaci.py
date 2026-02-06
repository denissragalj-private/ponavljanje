"""
RAD S TXT DATOTEKAMA (bez OOP-a) — 7 zadataka + assert testovi

Pravila:
- Student smije pisati SAMO unutar tijela funkcije (STUDENT CODE START/END).
- Ne mijenjati pomoćne funkcije i testove.
- Testovi koriste privremene datoteke (tempfile) da ne ostavljaju ništa na disku.
"""

import os
import tempfile


# ------------------------------------------------------------
# POMOĆNE FUNKCIJE (ne mijenjati)
# ------------------------------------------------------------

def write_text(path: str, text: str) -> None:
    """Upiše tekst u datoteku (UTF-8), overwrite."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def read_text(path: str) -> str:
    """Pročita cijeli tekst iz datoteke (UTF-8)."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def read_lines(path: str) -> list:
    """Pročita sve linije bez '\n' na kraju."""
    with open(path, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f.readlines()]


def append_line(path: str, line: str) -> None:
    """Doda jednu liniju na kraj datoteke (s newline)."""
    with open(path, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def to_int_safe(text: str, default: int = 0) -> int:
    try:
        return int(text)
    except Exception:
        return default


# ------------------------------------------------------------
# ZADACI (bez OOP-a)
# ------------------------------------------------------------

def zad01_count_lines(path: str) -> int:
    """
    Vrati broj linija u txt datoteci.
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


def zad02_count_nonempty_lines(path: str) -> int:
    """
    Vrati broj linija koje nisu prazne nakon strip().
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


def zad03_sum_numbers(path: str) -> int:
    """
    Datoteka sadrži po jedan broj u svakoj liniji.
    Vrati zbroj svih brojeva.
    Napomena: linije mogu imati razmake, koristite strip().
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


def zad04_filter_lines_containing(path_in: str, path_out: str, keyword: str) -> int:
    """
    Iz path_in pročitaj sve linije i u path_out upiši samo one koje sadrže keyword (case-sensitive).
    Svaka linija u izlazu mora završiti s '\n'.
    Vrati broj upisanih linija.
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


def zad05_last_n_lines(path: str, n: int) -> list:
    """
    Vrati listu zadnjih n linija (bez '\n').
    Ako datoteka ima manje od n linija, vrati sve.
    Ako je n <= 0, vrati praznu listu.
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


def zad06_log_subscription_payment(path_log: str, user: str, amount: int) -> None:
    """
    U log datoteku dodaj liniju u formatu: "<user>|<amount>"
    Npr. "ana|20"
    Dodaje se na kraj (append).
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


def zad07_total_paid_from_log(path_log: str) -> int:
    """
    Log format: "<user>|<amount>" po liniji.
    Vrati ukupno naplaćeno (zbroj amount).
    Napomena:
    - ignoriraj prazne linije
    - ako linija nema '|', ignoriraj
    - amount može biti neispravan -> tretiraj kao 0 (to_int_safe)
    """
    # STUDENT CODE START
    pass
    # STUDENT CODE END


# ------------------------------------------------------------
# ASSERT TESTOVI (koriste privremeni folder)
# ------------------------------------------------------------

with tempfile.TemporaryDirectory() as tmp:
    p1 = os.path.join(tmp, "a.txt")
    p2 = os.path.join(tmp, "out.txt")
    plog = os.path.join(tmp, "log.txt")

    # priprema a.txt
    write_text(p1, "Prva\n\nDruga  \n  \nTreca\n")
    assert read_lines(p1) == ["Prva", "", "Druga  ", "  ", "Treca"]

    # ZAD01
    assert zad01_count_lines(p1) == 5

    # ZAD02
    assert zad02_count_nonempty_lines(p1) == 3

    # priprema numbers.txt
    pn = os.path.join(tmp, "numbers.txt")
    write_text(pn, "10\n 20\n-5\n0\n")
    assert zad03_sum_numbers(pn) == 25

    # ZAD04
    write_text(p2, "")  # prazni output
    count = zad04_filter_lines_containing(p1, p2, "Dr")
    assert count == 1
    assert read_text(p2) == "Druga  \n"

    # ZAD05
    assert zad05_last_n_lines(p1, 2) == ["  ", "Treca"]
    assert zad05_last_n_lines(p1, 10) == ["Prva", "", "Druga  ", "  ", "Treca"]
    assert zad05_last_n_lines(p1, 0) == []
    assert zad05_last_n_lines(p1, -3) == []

    # ZAD06 + ZAD07
    write_text(plog, "")  # start empty
    zad06_log_subscription_payment(plog, "ana", 20)
    zad06_log_subscription_payment(plog, "marko", 25)
    zad06_log_subscription_payment(plog, "ana", 10)
    assert read_lines(plog) == ["ana|20", "marko|25", "ana|10"]

    # ubaci malo "loših" linija
    append_line(plog, "")
    append_line(plog, "neispravno")
    append_line(plog, "iva|xx")

    assert zad07_total_paid_from_log(plog) == 55

print("TXT datoteke (bez OOP) — testovi prolaze kad su funkcije implementirane.")
