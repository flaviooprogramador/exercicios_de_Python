pessoa = dict()
soma = media = 0
galera = list ()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('nome = '))
    while True:
        pessoa['sexo'] = str(input('sexo M/F')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print (f'ERR0! por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade:'))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print ('ERRO! responda apenas com S/N.')
    if resp == 'N':
        break
print ('-'*70)
print (f'Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print (f'A media de idade é de {media:5.2f} anos')
print ('As mulheres cadastradas foram ',end = '')
for p in galera:
    if p['sexo'] in 'Ff':
        print (f'{p["nome"]}', end = ',')
print ()
print ('Lista das pessoas que estão acima da media:', end = '')
for p in galera:
    if p['idade'] >= media:
        print ('   ')
        for k, v in p.items():
            print (f'{k} = {v}', end = '')
        print ()

