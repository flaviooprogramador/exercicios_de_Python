lista = [[], []]
par = impar = 0
for c in range (0,7):
    num = int(input(f'digite um valor na posição {c} = '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print (f'os numeros pares foram  {lista[0]}')
print (f'os numeros impares foram {lista[1]}')