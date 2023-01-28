dicionario = {}
lista = list ()
media = soma = 0
while True:
    dicionario['nome'] = str(input('NOME =>'))
    while True:
        dicionario['sexo'] = str(input('sexo M/F =>')).upper()
        if dicionario['sexo'] in 'MF':
                break
        print('POR FAVOR, USE M/F')
    dicionario['idade'] = int(input('IDADE =>'))
    soma += dicionario["idade"]
    lista.append(dicionario.copy())
    while True:
        resp = str(input('CONTINUAR S/N')).upper()
        if resp in 'SN':
            break
        print ('dados invalidos, POR FAVOR USE (S/N)')
    if resp == 'N':
        print ('FINALIZANDO PROGRAMA...')
        break

print ('==' *30)

print (f'{len(lista)} pessoas foram cadastradas')
media = soma / len(dicionario)
print (f' a media das idades {media} das pessoas')
for c in lista:
    if c['sexo'] in 'F':
        print (f'{c["nome"]}', end = ' ')
for u in lista:
    if u['idade'] >= media:
        print (' ')