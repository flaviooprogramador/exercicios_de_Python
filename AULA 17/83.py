expr = str (input('digite uma expressão:'))
pilha = list ()
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb:
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('sua expressão esta valida!')
else:
    print ('sua expressão esta errada!')