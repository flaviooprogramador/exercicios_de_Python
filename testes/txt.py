dic = dict()
lista = list()
dic['nome'] = str(input('nome do jogador ➤ '))
partidas = int(input(f'quantas partidas o jogador {dic["nome"]} jogou? ➤ '))
for c in range(0,partidas):
    lista.append(int(input(f'quantos gols foi feito na {c+1} partida? ')))
dic['gols'] = lista[:]
dic['total'] = sum(lista)
print (f'o jogador {dic["nome"]} jogou {partidas} partidas')
for i,v in enumerate(dic['gols']):
    print(f'➤ na partida {i}, fez {v} gols')
print (f'o total {dic["total"]}')
