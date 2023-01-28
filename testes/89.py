lista = []
while True:
    nome = str(input('nome do aluno'))
    nota1 = float(input('nota 1 do aluno'))
    nota2 = float(input('nota 2 do aluno'))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resp = str(input('continuar? S/N')).upper()
    if resp in 'N':
        break
print ('=-'*20)
print (f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print ('-'*20)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('mostrar dados de qual aluno? (999 IMTERROMPE:)'))
    if opc == 999:
        break
    if opc <= len(ficha) -1:
        print(f'notas de {ficha[opc]} são {cad[opc][1]}')
