casa = float (input('qual o valor da casa que deseja comprar?'))
salario = float (input('qual o valor do seu salario?'))
anos = int (input('em quantos anos você vai pagar a casa?'))
prestaçao =  casa / (anos * 12)
minimo = salario * 30 / 100
print ('para pagar uma casa de R${:.2f} em {} anos'.format (casa,anos))
print ('a prestação será de R${:.2f}'. format (prestaçao))
if prestaçao <= minimo :
    print ('emprestimo pode ser concedido!')
else:
    print ('EMPRESTIMO NEGADO!')