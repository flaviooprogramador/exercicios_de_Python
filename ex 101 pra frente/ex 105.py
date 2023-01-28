def notas(*n, sit=False):
    r = dict()
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['total'] = len(n)
    r['media'] = sum(n) / len(n)


resp = notas(3, 5, 2, 2, sit=True)
print(resp)


