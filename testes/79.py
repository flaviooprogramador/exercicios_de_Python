lista = []
while True:
    numeros = int(input('digite um valor '))
    if numeros not in lista:
        lista.append(numeros)
    resp = str(input('continuar? S/N'))
    if resp in 'Nn':
        break
lista.sort()
print (lista)