def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c>1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


n = int(input(f'Digite um número para ver seu fatorial: '))
escolha = str(input(f'Deseja ver a conta? [S/N] ')).strip().upper()[0]

if escolha == 'S':
    print(fatorial(n, show=True))
else:
    print(fatorial(n))
