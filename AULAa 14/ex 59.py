n1 = int (input('digite um valor:'))
n2 = int (input('digite outro valor:'))
opção = 0
while opção != 5:
    print ('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')
    opção = int (input('qual é a sua opção'))
    if opção == 1:
        soma = n1 + n2
        print ('a soma entre {} e {} é {}'.format(n1,n2, soma))
    elif opção == 2:
        multiplicar = n1 * n2
        print ('a multiplicação entre {} e {} é {}'.format (n1,n2, multiplicar))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print ('entre {} e {} o maior é {}'.format (n1,n2,maior))
    elif opção == 4:
        print ('informe os numeros novamente:')
        n1 = int(input ('digite o primeiro valor:'))
        n2 = int (input('digite o segundo valor:'))
    elif opção == 5:
        print ('finalizando...')
    else:
        print ('opção invalida. tente novamente')
    print ('-=-=-=- '*10)
print ('fim do programa! volte sempre!')