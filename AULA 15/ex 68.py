from random import randint
v = 0
while True:
    jogador = int (input ('escolha um numero:'))
    computador = randint (0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('par ou impar? [P/I]')).upper()
    print (f'voce jogou {jogador} e o computador {computador}.totoal de {total}')
    print ('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print ('você VENCEU!')
            v += 1
        else:
            print ('VOCE PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print ('VOCE venceu!')
            v += 1
        else:
            print ('voce PERDEU!')
            break
    print ('vamos jogar novamente...')
print (f'GAME OVER! voce venceu {v} vezes ')
