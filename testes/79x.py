lista = []
cont = 0
while True:
    num = int(input('digite um valor == '))
    lista.append(num)
    resp = str(input('continuar? S/N'))
    if resp in 'Nn':
        break
print (f'{len(lista)} foram digitados')
lista.sort(reverse= True)
print (lista)
if 5 not in lista:
    print ('o valor 5 nao foi digtado')
else:
    print ('o valor 5 esta na lista')