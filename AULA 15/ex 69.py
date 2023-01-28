idade = 0
contador = 0
homens = 0
dmaior = 0
mulher = 0
mulheres = 0
while True:
    print('--' * 20)
    print('CADASTRE UMA PESSOA')
    print('--' * 20)
    idade = int(input('qual a sua idade?'))
    if idade > 18:
        dmaior += 1
    elif idade < 20:
        contador += 1
    sexo = str(input('qual o seu sexo [M/F]')).upper()
    if sexo == 'M':
        homens += 1
    if idade < 20:
        sexo == 'F'
        mulheres += 1
    continuar = str(input('deseja continuar? [S/N]')).upper()
    if continuar == 'N':
        break
print ('==' *20)
print ('pessoas cadastradas com SUCESSO')
print ('==' *20)
print (f'{dmaior} pessoas tem mais de 18 anos')
print (f'{homens} homens foram cadastrados:')
print (f'{mulheres} mulheres tem menos de 20 anos')
print ('==' *20)
'''sem pesquisas'''