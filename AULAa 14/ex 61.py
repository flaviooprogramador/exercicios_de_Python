print ('gerador de PA')
print ('-=' *10)
primeiro = int (input('primeiro termo:'))
razão = int(input('razão de PÁ:'))
termo = primeiro
cont = 1
while cont <= 10:
    print ('{}'.format (termo))
    termo += razão
    cont += 1
