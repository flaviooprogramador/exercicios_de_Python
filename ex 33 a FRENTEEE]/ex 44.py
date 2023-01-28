print ('\033[1;33m                     ===--===--===--LOJAS FLAVIO===--===--===')
preço = float (input('\033[4;35m PREÇO DAS COMPRAS : R$'))
print ('''\033[1;33m[1;30m FORMAS DE PAGAMENTO
'[1] A VISTA DINHEIRO/CHEQUE'
'[2] A VISTA NO CARTÃO'
'[3] 2X NO CARTÃO'
'[4] 3X OU MAIS NO CARTÃO''')
opção = int (input('qual é a opção?'))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço *5/100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print ('\033[1;34m sua compra será parcelada em 2 vezes de R${:.2f}\033[1;34m SEM JUROS'.format (parcela))
elif opção == 4:
    total = preço + (preço *20 / 100)
    totalparc = int (input('\033[1;34m em quantas parcelas? \033[1;34mCOM JUROS'))
    parcela = total / totalparc
    print ('sua compra sera parcelada em {}x de R${:.2f}'.format (preço,total))
    print ('sua compra de ')
else:
    total = preço
    print ('\033[4;31m opção invalida de pagamento tente novamente')
print ('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format (preço, total))



