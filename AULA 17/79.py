numeros = list ()
while True:
    n = int(input('digite um numero:'))
    if n not in numeros:
        numeros.append(n)
        print ('numero registrado com SUCESSO!!!')
    else:
        print ('numero duplicado... nao vou registrar')
    r = str (input('CONTINUAR? S/N ')).upper()
    if r == 'N':
        print ('programa encerrado...')
        print ('-=-=' *20)
        break
numeros.sort()
print (f'os valores digitados foram {numeros}:')
print ('-=-=' *20)