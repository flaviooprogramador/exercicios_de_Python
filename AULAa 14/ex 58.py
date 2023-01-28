from random import randint
computador = randint (0,10)
acertou = False
palpites = 0
print ('acabei de pensar em um numero de 0 a 10:')
print ('consegue advinhar qual foi?')
while not  acertou:
    jogador = int(input('em que numero eu pensei?'))
    palpites +=1
    if jogador < computador:
        print ('mais...tente mais uma vez.')
    elif jogador > computador:
        print ('menos ... tente mais uma vez:')

    if jogador == computador:
        acertou = True
print ('acertou:')
print ('voce tentou {} vezes '.format(palpites))