dados = list ()
povo = list ()
peso = list ()
while True:
    dados.append(str(input('nome:')))
    dados.append(float(input('peso:')))
    povo.append(dados[:])
    peso.append(dados[1])
    dados.clear()
    resp = str(input('continuar S/N:')).upper()
    if resp == 'N':
        break
print (f'pessoas {len(povo)} foram cadastradas.')
print (f'as pessoas mais pesadas {max(peso)}', end = '')
for p in povo:
    if p[1] == max(peso):
        print (f'{p[0]}', end = '')
        print(f'as pessoas mais leves {min(peso)}' )
    if p[1] == min(peso):
        print(f'{p[0]}', end = '')
