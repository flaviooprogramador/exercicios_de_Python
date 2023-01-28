lista = []
for c in range (0, 5):
    numeros = int(input('digite um valor:'))
    lista.append(numeros)
print ('--'*20)
print (f'o maior valor digitado foi {max(lista)}')
print ('--'*20)
print (f'o menor valor digitado foi {min(lista)}')
print ('--'*20)
for v,c in enumerate(lista):
    print (f'o valor {c} está na posição {v}')
