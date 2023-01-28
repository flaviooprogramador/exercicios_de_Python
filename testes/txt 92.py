dic = dict()
lista = list ()
dic['nome'] = str(input('nome do jogador ➤ '))
partidas = int(input('quantas partidas jagadas? '))
for c in range(0, partidas):
    lista.append(int(input(f'quantos gols feitos na {c + 1} partida?')))
dic['gol'] = lista[:]
dic['total'] = sum(lista)
for c,v in enumerate (dic['gol']):
    print (f'na partida {c+ 1}, foram feito {v} gols')
print (f'total de gols marcados {dic["total"]}')