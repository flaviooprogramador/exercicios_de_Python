salario = float (input('informe seu salario:'))
if salario<=1250:
    novo = salario+ (salario *15 / 100)
else:
    novo = salario + (salario *10/100)
print ('seu antigo salario era de R${:.2f} e passa a ser de R${:.2f}'.format (salario,novo))
print ('continue se dedicando, futuros aumentos virão')
print ('...')
print ('>>><<<' *10)

