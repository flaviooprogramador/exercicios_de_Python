from time import sleep


def maior (* num):
    cont = maior = 0
    print ('\nanalisando os valores passados...')
    for valor in num:
        print (f'{valor} ', end = ',' )
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print (f'\nForam informados {cont} valores ')
    print (f'O maior valor informado foi {maior}')

#programa principal
maior(2, 9, 4, 5, 7, 1)
maior (2,4,2,1,2,3,5,6,5,342)