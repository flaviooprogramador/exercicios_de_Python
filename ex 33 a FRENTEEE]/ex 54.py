maiores = 0
for b in range(1, 8):
    nascimento = int(input('Digite a {}° data de nascimento: '.format(b)))
    if nascimento == 2004 or nascimento < 2004:
        maiores += 1
menores = b - maiores
print('{} pessoa(s) já atingiu/atingiram a maioridade enquanto {} ainda não atingiram. '.format(maiores, menores))
