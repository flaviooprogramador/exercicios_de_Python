lista = list ()
for c in range (0,5):
    n =int(input('digite um valor:'))
    if c == 0 or n > lista [-1]:
        lista.append (n)
    else:
        pos = 0
        while pos < len (lista):
            if n <= lista [pos]:
                lista.insert(pos, n)
                break
print (f'os valores digitados em ordem foram {lista}')