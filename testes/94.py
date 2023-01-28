dic = dict()
lista = list()
lista_mulheres = list()
tot_pessoas = media = soma = 0
lista_media = list()
while True:
    dic['nome'] = str(input('nome  ➤ '))
    if dic['nome'] == dic['nome']:
        tot_pessoas += 1
    print('-'*20)
    while True:
        dic['sexo'] = str(input('sexo M/F ➤ ')).upper()
        if dic['sexo'] in 'F':
            lista_mulheres.append(dic['nome'])
        if dic['sexo'] in 'MF':
            break
        print ('🔴ERRO🔴 por favor, digite apenas M ou F ')
    print('-' * 20)
    dic['idade'] = int(input('idade  ➤ '))
    lista.append(dic.copy())
    soma += dic['idade']
    lista_media.append(media)
    print('-' * 20)
    while True:
        resp = str(input('continuar? S/N')).upper()
        if resp in 'SN':
            break
        print ('ERRO! RESPONDA APENAS S OU N.')
    if resp in 'N':
        print('FINALIZANDO PROGRAMA...')
        break

print (f'A) total de pessoas cadastradas {tot_pessoas}')
print (f'B) mulheres cadastradas ➤ {lista_mulheres}')
media = soma / len(lista_media)
print (f'C) a media de idade é de {media:5.2f}')
print()
print ('D) lista das pessoas acima da media:')
for p in lista:
    if p['idade'] >= media:
        print ('   ', end='')
        for k,v in p.items():
            print (f'{k} = {v}', end = '')
        print()