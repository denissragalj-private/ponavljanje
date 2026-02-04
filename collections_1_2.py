def zad01_broj_neispravnih(serija: list) -> int:
    """
    Tema: proizvodnja
    U listi 'serija' su statusi komada: 'OK' ili 'NOK'.
    Vrati koliko ima 'NOK'.
    """
    # STUDENT CODE START
    if len(serija) == 0:
        return 0

    index = 0
    counter = 0
    while True:
        if serija[index] == 'NOK':
            counter += 1
        index += 1

        if index == len(serija):
            break

    return counter
    # STUDENT CODE END


assert zad01_broj_neispravnih(["OK", "NOK", "OK", "NOK", "NOK"]) == 3
assert zad01_broj_neispravnih([]) == 0
