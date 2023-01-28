import funcao


num = int(input('digite um numero'))
print(f'o dobro de {num} e {funcao.moeda(funcao.dobro(num))}')
print(f'a metade de {num} e {funcao.moeda(funcao.metade(num))}')
print(f'aumentando 10%, temos de {funcao.moeda(funcao.aumentar(num,10))}')
