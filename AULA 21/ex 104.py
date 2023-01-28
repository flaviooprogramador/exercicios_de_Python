def leia(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print ('DIGITE UM NUMERO VALIDO')
        if ok:
            break
    return valor

n = leia('DIGITE UM NUMERO')
print (f'voce acabou de digitar o n {n}')