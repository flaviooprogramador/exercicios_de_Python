salario = float(input('informe seu salario ;'))
if salario <= 1250:
    novo = salario = (salario *10/100)
else:
    novo = salario (salario *10/100)
print ('seu antigo salario era de {:.2f} e agora passa a ser de {:2f}'.format (salario,novo))
