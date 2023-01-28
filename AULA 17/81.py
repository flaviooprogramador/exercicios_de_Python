numeros = list ()
cont = 0
cinco = 0
while True:
    n = int(input('digite um numero:'))
    if n not in numeros:
        numeros.append(n)
        cont += n
    resp = str(input('continuar? S/N')).upper()
    if resp == 'N':
        print ('encerrando...')
        break
numeros.sort(reverse=True)
print (f'os numeros em forma decrescente {numeros}')
print (f'{cont} total de numeros digitados:')
print (f'voce digitou  {len(numeros)}  elementos')
if 5 in numeros:
    print ('o valor 5 faz parte da lista')
else:
    print ('o valor 5 nao faz parte da lista')