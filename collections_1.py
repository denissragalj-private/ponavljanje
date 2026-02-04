lista = ['OK', 'NOK', 'OK', 'OK', 'NOK']

# koliko ima 'OK' u listi

broj_ok = lista.count('OK')
print(f'Broj OK je: {broj_ok}')


index = 0
counter = 0
while True:
    counter = 0
    if lista[index] == 'NOK':
        counter += 1
    index += 1
    if index == len(lista):
        break
    
    
print(f'Broj NOK je: {counter}')
