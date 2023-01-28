from random import randint
from time import sleep
itens = ('pedra', 'papel' , 'tesoura')
computador = randint (0, 2)
print ('''\033[4;33m SUAS OPÇÕES
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
print ('\033[31m -=-=-' *40)
jogador = int(input ('qual é a sua jogada?'))
print ('-=-=' *40)
print ('\033[4;31m JO')
sleep (1)
print ('\033[4;32m KEN')
sleep (1)
print ('\033[34m PO!!!')
sleep (1)
print ('Computador jogou {}'.format(itens[computador]))
print ('jogador jogou {}'.format(itens[jogador]))
if computador == 0:
    if jogador == 0:
        print ('EMPATE')
    elif jogador == 1:
        print ('JOGADOR VENCE')
    elif jogador == 2:
        print ('COMPUTADOR VENCE')
elif computador == 1:
    if jogador == 0:
        print ('JOGADOR VENCEU')
    elif jogador == 1:
        print ('EMPATE')
    elif jogador == 2:
        print ('JOGADOR VENCEU')
elif computador == 2:
    if jogador == 0:
        print ('JOGADOR VENCEU')
    elif jogador == 1:
        print ('COMPUTADOR VENCEU')
    elif jogador == 2:
        print ('EMPATE')
    else:
        print ('JOGADA INVALIDA')
print ('=--=' *40)
print ('=--=' *40)
print ('\033[4;33m                              JOAO É GAAYY     LEO É GAAYY')
