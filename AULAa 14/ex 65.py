num = cont = soma = 0
while num != 999:
    num = int(input('digite um numero[999 para parar]:'))
    soma += num
    cont += 1
print ('voce digitou {} numeros e a soma entre eles foi {}'.format(cont - 1, soma - 999))
