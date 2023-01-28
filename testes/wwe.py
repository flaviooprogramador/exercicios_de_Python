print ('='*40)
print (f'            FLAVIN APELAO')
print ('='*40)
palavras = ('pao', 'sidoka', 'flavio')
for c in palavras:
    print (f'\nas vogais da palavra {c.upper()} ', end = '')
    for e in c:
        if e in 'aeiou':
            print (f'{e}, ', end= '')