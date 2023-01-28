produto = 0
valor = 0
total = 0
produtomil = 0
prodbaratin = 0
contador = 0
menor = 0
barato = ''
while True:
    print ('======LOJA DO FLAVINHO=====')
    produto = str (input('qual o nome do produto?')).upper()
    valor = float (input('qual o valor do produto?'))
    valor +1
    total += valor
    if valor > 1000:
        produtomil += 1
    if contador == 1 or valor < menor:
        menor = valor
        barato = produto
    continuar = str (input('vai continuar ?  [S/N]')).upper()
    if continuar == 'N':
        print ('finalizando sistema, VOLTE SEMPRE...')
        break
print ('----' *15)
print (f'{total} valor total dos produtos')
print (f'{produtomil} custam mais que mil')
print (f'{produto} é o produto mais barato:')
print ('----' *15)