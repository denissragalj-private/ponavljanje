def zad01_broj_neispravnih(serija: list) -> int:
    """
    Tema: proizvodnja
    U listi 'serija' su statusi komada: 'OK' ili 'NOK'.
    Vrati koliko ima 'NOK'.
    """
    # STUDENT CODE START
    return serija.count('NOK')
    # STUDENT CODE END


assert zad01_broj_neispravnih(["OK", "NOK", "OK", "NOK", "NOK"]) == 3
assert zad01_broj_neispravnih([]) == 0
