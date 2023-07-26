n=0
s=0
while True:
    n=int(input(f'Digite um número: '))
    if n==999:
        break
    s+=n
print(f'A soma vale {s}')