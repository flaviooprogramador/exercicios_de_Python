def ficha (jog = 'DESCONHECIDO', gol = 0):
    print (f'o jogador {jog} fez {gol} no campeonato')

n = str(input('NOME'))
g = str (input('GOLS'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)