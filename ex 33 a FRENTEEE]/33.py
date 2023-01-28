                                      #DESAFIO 33
print ('<<<>>>' *30) # deixar mais legalzin
print ('<<<>>>>' *30)
a = int (input('primeiro valor: '))
b = int(input('segundo valor:'))
c = int(input('terceiro valor:'))
# VERIFICANDO QUEM É O MENOR VALOR
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print ('o menor valor digitado foi {}'.format (menor))
print ('<<<>>' *30)
print ('<<>>' *30)
# VERIFICANDO QUEM É O MAIOR
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print ('o maior numero foi {}.'.format (maior))
print ('>><<' *30)
print ('>><<' *30) # deixar mais bunito

