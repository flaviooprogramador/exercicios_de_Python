from datetime import date
atual = date.today() .year
nasc = int(input('ANO DE NASCIMENTO:'))
idade = atual - nasc
print ('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print ('voce tem que se alistar IMEIDATAMENTE!')
elif idade < 18:
    print ('')
elif idade > 18:
    saldo = idade - 18:
    print ('voce ja deverida ter se alistado ha {} anos'.format (saldo))
