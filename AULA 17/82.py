numeros = list ()
pares = list ()
impar = list ()
while True:
    n = int(input('digite um numero'))
    if n not in numeros:
        numeros.append(n)
    resp = str(input('continuar? S/N')).upper()
    par = list ()
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impar.append(n)
    if resp in 'N':
        print ('finalizando programa...')
        break


print (f'a lista com os numeroos pares {pares}')
print (f'a lista completa contem {numeros} ')
print (f'a lista com os numeros impares {impar}')