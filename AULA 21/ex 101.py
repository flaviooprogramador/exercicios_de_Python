def voto (ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos : NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'com {idade} anos: VOTO OPCIONALa'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO'

nsasc = int(input('"EM que anos voce nasceu?'))
print (voto(nsasc))