def linha(tamanho = 42):
    return  '-' * tamanho


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())