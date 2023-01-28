casa = float(input('qual o valor da casa que deseja comprar?'))
salario = float(input('qual o valor do seu salario?'))
anos = int (input('em quantos anos deseja pagar a casa?'))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print ('para pagar uma casa de {:.2f} em {} anos'.format(casa, anos))
print (' a prestação sera de R${:.2f}'.format (prestação))
if prestação <= minimo :
    print ('emprestimo pode ser concedido!')
else:
    print ('Emprestimo NEGADO!')