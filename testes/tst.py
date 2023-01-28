cont = ('zero', 'um', 'dois', 'trez', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze','treze', 'quatorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('digite um numero entre 0 e 20:'))
    if 0 <= num <= 20:
        break
    print ('ERRO digite novamente')

print (f'o numero digitado foi {cont[num]}')