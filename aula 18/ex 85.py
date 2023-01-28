num = [[], []]
cont = 0
for c in range (1,8):
    cont = int(input(f'digite o {c}o valor:'))
    if cont % 2 == 0:
        num[0].append(cont)
    else:
        num[1].append(cont)
num[0].sort()
num[1].sort()
print (f'os numeros pares foram {num[0]}')
print (f'os numeros impares foram {num[1]}')