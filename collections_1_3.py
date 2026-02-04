def zad01_broj_neispravnih(serija: list) -> int:
    """
    Tema: proizvodnja
    U listi 'serija' su statusi komada: 'OK' ili 'NOK'.
    Vrati koliko ima 'NOK'.
    """
    # STUDENT CODE START
    counter = 0
    for element in serija:
        if element == 'NOK':
            counter += 1

    return counter
    # STUDENT CODE END


assert zad01_broj_neispravnih(["OK", "NOK", "OK", "NOK", "NOK"]) == 3
assert zad01_broj_neispravnih([]) == 0
