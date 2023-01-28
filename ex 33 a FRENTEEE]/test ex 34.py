salario = float (input('informe o seu salario'))
if salario<=1250:
    novo = salario +(salario * 15 / 100)
else:
    novo = salario +(salario * 10 / 100)
print('o seu antigo salario era de {:.2f} e passa a ser {:.2f}' .format (salario,novo))

