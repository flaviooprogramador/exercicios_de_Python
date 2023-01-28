#7 a mais aprovado abaixo reprovado
dicionario = {}
nome = str(input('nome = '))
media = float(input(f'media de {nome} =  '))
print (f'Nome é igual a {nome}')
print (f'Media é igual a {media}')
if media >= 7:
    print (f'a situação de {nome} é igual a aprovado')
elif media <= 7:
    print (f'a situação de {nome} é igual a reprovado')