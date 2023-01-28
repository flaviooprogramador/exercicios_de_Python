num = cont = 0
soma = 0
while True:
    num = int (input('digite um numero:[999 para parar]'))
    if num==999:
       break
    soma += 1
    cont += num
print (f'a soma dos {soma} desses numeros é {cont} ')