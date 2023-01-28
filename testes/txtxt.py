num = (int(input('digite um numero')),
       int(input('digite um numero')),
        int(input('digite um numero')),
        int(input('digite um numero')))

print (f'voce digitou os valores {num}')
print (f'o valor 9 foi digitado {num.count(9)} vezes')
print (f'o valor 3 apareceu na posição {num.index(3)}')
print (f'os valores pares foram')
for n in num:
    if n % 2 == 0:
        print (n)