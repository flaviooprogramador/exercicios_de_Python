n1 = int (input('digite o primeiro valor:'))
n2 = int (input('digite o segundo valor:'))
if n1 > n2:
    print ('{} é o numero maior'.format (n1))
elif n1 == n2:
    print ('os dois numeros tem o mesmo valor')

else:
    print ('{} é o numero maior'.format (n2))