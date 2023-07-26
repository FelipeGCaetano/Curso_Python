
from tkinter import N


def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'APROVADO'
        else:
            r['situação'] = 'REPROVADO'
    return r

resp = notas(5.6, 6.7, 5.7, 2, sit=True)
print(resp)