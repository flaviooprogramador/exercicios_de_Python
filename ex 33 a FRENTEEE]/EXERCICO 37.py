casa = float(input('qual o valor da casa?'))
salario = float (input('qual o valor do seu salario?'))
anos = int (input('em quantos anos ira pagar a casa?'))
prestação = casa / (anos * 12)
minimo = salario = (salario *30 / 100)
print ('a prestação da casa é {:.2f} e sera paga em {}'.format (prestação ,anos))
if prestação <=minimo:
    print ('pagemnto aprovado')
else:
    print ('pagamento nao aprovado')