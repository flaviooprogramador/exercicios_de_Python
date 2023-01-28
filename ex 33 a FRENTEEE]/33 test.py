a = int(input('primeiro valor:'))
b = int(input('segundo valor:'))
c = int(input('terceiro valor:'))
# VERIFICANDO O MENOR VALOR
menor = a
if  b<a and b<c:
    menor = b
if  c<b and c<a:
    menor = c
#VERIFICANDO O MAIOR NUMERO
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
# RESULTADOS DOS VALORES
print ('o menor valor é {}'.format (menor))
print ('o maior valor é {}'.format (maior))
