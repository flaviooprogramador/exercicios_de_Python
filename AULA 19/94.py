pessoa = {}
galera = list ()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('NOME =>'))
    while True:
        pessoa['sexo'] = str(input('sexo [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print ('ERRO! por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('IDADE:'))
    soma += pessoa['idade']

    galera.append(pessoa.copy())
    while True:
        resp = str(input('quer continuar S/N')).upper()[0]
        if resp in 'SN':
            break
        print ('ERRO! RESPONDA APENAS COM S OU N')
    if resp == 'N':
        break
print (f'Ao todo temos {len(galera)} cadastrada.')
media = soma / len(galera)
print (f'a media de idade é de {media:5.2f} anos')
print ('as mulheres cadastradas foram  ', end = '')
for p in galera:
    if p['sexo'] in 'Ff':
        print (f'{p["nome"]}', end ='')
print ()
print ('lista das pessoas que estao acima da media:', end='')
for p in galera:
    if p['idade'] >= media:
        print ('   ')
        for k, v in p.items():
            print (f'{k} = {v};', end='')
        print ()
print ('<<encerrado>>')
