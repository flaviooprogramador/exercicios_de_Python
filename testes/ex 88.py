from random import randint
from time import sleep
jogador = int(input('quantos jogos serão gerados ? '))
print ('--'*20)
print('            JOGA NA MEGA SENA      ')
print('--'*20)
for c in range(1,jogador +1):
    sleep(0.5)
    print (f'jogo {c}: [{randint(1, 60)}, {randint(1, 60)}, {randint(1, 60)},'
           f' {randint(1, 60)}, {randint(1, 60)}, {randint(1, 60)}]')