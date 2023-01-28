jogador = dict ()
partidas = list ()
jogador['nome'] = str(input('nome do jogador: '))
tot = int(input(f'quantas partidas {jogador["nome"]} jogou?'))
for c in range (0, tot):
    partidas.append(int(input(f'QUANTOS gols na partida {c}??')))
jogador['gols'] = partidas [:]
jogador ['total'] = sum(partidas)
for a, b in jogador.items():
    print (f'o campo {a} tem o valor {b}')
print (f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
