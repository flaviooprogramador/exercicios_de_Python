nomes = ('pao', 0.50, 'celular', 500, 'bola', 5)
print (f'----'*10)
print (f'          LISTAGEM DE PREÇO     ')
print (f'----'*10)
for c in range(0, len(nomes)):
    if c % 2 == 0:
        print (f'{nomes[c]:.<30}', end= '')
    else:
        print (f'R${nomes[c]:>8.2f}')
        print (f'-'*40)
