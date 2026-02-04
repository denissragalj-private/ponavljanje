lista = ['OK', 'NOK', 'NOK', 'OK', 'OK', 'OK', 'NOK', 'NOK']

# koliko ima NOK elemenatra u listi?
broj_pojavljivanja = lista.count('NOK')
print(broj_pojavljivanja)



index = 0
counter = 0
while True:
    if lista[index] == 'NOK':
        counter += 1
    index += 1

    if index == len(lista):
        break

print(counter)



counter = 0
for element in lista:
    if element == 'NOK':
        counter += 1

print(counter)



