lista = []
par = []
impar = []
while True:
    num = int(input('digite um numero = '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    resp = str(input('continuar? S/N'))
    if resp in 'Nn':
        break
print (lista)
print (par)
print (impar)