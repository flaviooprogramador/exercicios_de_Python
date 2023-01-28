dicionario = dict ()
lista = list ()
while True:
    dicionario['nome'] = str(input('nome do jogador => '))
    partidas = int(input(f'quantas partidas o {dicionario["nome"]} jogou? '))
    for c in range(0,partidas):
        lista.append(int(input(f'gols feito na {c+1} partida =>')))
    dicionario['gols'] = lista[:]
    dicionario['total'] = sum(lista)
    lista.append(dicionario.copy())
    print(f'o jogador {dicionario["nome"]} jogou {partidas} partidas')
    for i,v in enumerate (dicionario['gols']):
        print (f'Na partida {i}, fez {v} gols')
    print (f'o total de gols foi {dicionario["total"]}')
    while True:
        resp = str(input('CONTINUAR? S/N')).upper()[0]
        if resp in 'SN':
            break
        print ('ERRO!digite apenas S ou N')
    if resp == 'N':
        break