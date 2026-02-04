def zad01_broj_neispravnih(serija: list) -> int:
    # STUDENT CODE START
    brojac = 0
    for status in serija:
        if status == "NOK":
            brojac += 1
    return brojac
    # STUDENT CODE END


def zad02_najduzi_zastoj(zastoje_min: tuple) -> int:
    # STUDENT CODE START
    najveci = zastoje_min[0]
    for x in zastoje_min:
        if x > najveci:
            najveci = x
    return najveci
    # STUDENT CODE END


def zad03_filtriraj_temperaturu(mjerenja: list, prag: float) -> list:
    # STUDENT CODE START
    rezultat = []
    for t in mjerenja:
        if t > prag:
            rezultat.append(t)
    return rezultat
    # STUDENT CODE END


def zad04_top3_najvecih_potrosaca(potrosnja: dict) -> list:
    # STUDENT CODE START
    # sortiramo parove (stroj, kWh) po kWh silazno
    parovi = list(potrosnja.items())
    parovi.sort(key=lambda p: p[1], reverse=True)

    rezultat = []
    limit = 3
    if len(parovi) < 3:
        limit = len(parovi)

    for i in range(limit):
        rezultat.append(parovi[i][0])
    return rezultat
    # STUDENT CODE END


def zad05_ukupno_sati_i_kraj_procesa(nalozi: dict, hours_per_day: int = 8) -> tuple:
    # STUDENT CODE START
    ukupno_sati = 0
    krajnji_datum = None  # string "YYYY-MM-DD"

    for _, podaci in nalozi.items():
        start = podaci["start"]
        trajanje = podaci["trajanje_sati"]

        ukupno_sati += trajanje

        kraj = add_hours_to_date(start, trajanje, hours_per_day)

        if krajnji_datum is None:
            krajnji_datum = kraj
        else:
            # usporedba datuma kao datetime (sigurno)
            if parse_date(kraj) > parse_date(krajnji_datum):
                krajnji_datum = kraj

    return (ukupno_sati, krajnji_datum)
    # STUDENT CODE END


def zad06_skup_materijala(nalozi: list) -> set:
    # STUDENT CODE START
    svi = set()
    for nalog in nalozi:
        for mat in nalog["materijali"]:
            svi.add(mat)
    return svi
    # STUDENT CODE END


def zad07_materijali_koji_nedostaju(potrebno: set, dostupno: set) -> set:
    # STUDENT CODE START
    return potrebno - dostupno
    # STUDENT CODE END


def zad08_spoji_serije(serija_a: list, serija_b: list) -> list:
    # STUDENT CODE START
    rezultat = []
    i = 0

    # dok imamo oba
    while i < len(serija_a) and i < len(serija_b):
        rezultat.append(serija_a[i])
        rezultat.append(serija_b[i])
        i += 1

    # dodaj ostatak A
    while i < len(serija_a):
        rezultat.append(serija_a[i])
        i += 1

    # dodaj ostatak B
    while i < len(serija_b):
        rezultat.append(serija_b[i])
        i += 1

    return rezultat
    # STUDENT CODE END


def zad09_rjecnik_kolicina_po_artiklu(stavke: list) -> dict:
    # STUDENT CODE START
    rezultat = {}
    for sifra, kolicina in stavke:
        if sifra not in rezultat:
            rezultat[sifra] = 0
        rezultat[sifra] += kolicina
    return rezultat
    # STUDENT CODE END


def zad10_korisnici_duznici(pretplate: dict) -> tuple:
    # STUDENT CODE START
    duznici = []
    ukupno = 0.0

    for korisnik, podaci in pretplate.items():
        if podaci["status"] == "NEPLACENO":
            duznici.append(korisnik)
            ukupno += podaci["iznos"]

    duznici.sort()
    return (duznici, ukupno)
    # STUDENT CODE END


def zad11_ukupno_naplaceno(pretplate: dict) -> float:
    # STUDENT CODE START
    ukupno = 0.0
    for podaci in pretplate.values():
        if podaci["status"] == "PLACENO":
            ukupno += podaci["iznos"]
    return ukupno
    # STUDENT CODE END


def zad12_najcesci_status(dogadaji: list) -> str:
    # STUDENT CODE START
    brojac = {}
    for s in dogadaji:
        if s not in brojac:
            brojac[s] = 0
        brojac[s] += 1

    # pronađi max frekvenciju
    max_count = None
    for c in brojac.values():
        if max_count is None or c > max_count:
            max_count = c

    # kandidati koji imaju max_count
    kandidati = []
    for s, c in brojac.items():
        if c == max_count:
            kandidati.append(s)

    kandidati.sort()  # abecedno
    return kandidati[0]
    # STUDENT CODE END


def zad13_izdvoji_radne_dane(datumi: tuple) -> list:
    # STUDENT CODE START
    rezultat = []
    for d in datumi:
        if not is_weekend(d):
            rezultat.append(d)
    return rezultat
    # STUDENT CODE END


def zad14_normaliziraj_tagove(tagovi: list) -> set:
    # STUDENT CODE START
    rezultat = set()
    for t in tagovi:
        x = t.strip().lower()
        if x != "":
            rezultat.add(x)
    return rezultat
    # STUDENT CODE END


def zad15_kupi_pakete(korisnici: dict) -> dict:
    # STUDENT CODE START
    rezultat = {}

    for _, podaci in korisnici.items():
        paket = podaci["paket"]
        cijena = podaci["cijena"]

        if paket not in rezultat:
            rezultat[paket] = {"broj": 0, "ukupno": 0}

        rezultat[paket]["broj"] += 1
        rezultat[paket]["ukupno"] += cijena

    return rezultat
    # STUDENT CODE END
