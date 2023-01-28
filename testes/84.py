lista = []
contador = 0
while True:
    lista.append(str(input('nome =' )))
    if lista == lista:
        contador += 1
    lista.append(float(input('peso = ')))
    resp = str(input('continuar? S/N'))
    if resp in 'Nn':
        break
print (f'total de pessoas cadastradas {contador}')
print (f'pessoas mais pesadas {max(lista[1])}')