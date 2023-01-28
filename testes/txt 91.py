dic = dict ()
lista = list ()
dic['nome'] = str(input('nome do jogador ➤ '))
partidas = int(input(f'quantas partidas o {dic["nome"]} jogou? ➤ '))
for c in range(0, partidas):
    lista.append(int(input(f'quantos gols foram feito na {c + 1} partida ➤ ')))
dic['gols'] = sum(lista)
dic['tot_lista'] = lista[:]
for c,i in enumerate (dic['tot_lista']):
    print (f'na partida {c + 1}, foram feitos {i} gols ')
print (f'total de gols marcado ➤ {dic["gols"]}')