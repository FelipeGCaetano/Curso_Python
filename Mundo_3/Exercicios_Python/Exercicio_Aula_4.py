def dobra(lst):
    pos = 0
    while pos <len(lst):
        lst[pos]*=2
        pos += 1


valores = [1, 5, 7, 8, 4]
dobra(valores)
print(valores)