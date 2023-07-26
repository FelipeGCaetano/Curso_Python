galera = list()
dados = list()

totp = mais_pesadas = mais_leves = 0
escolha = ' '

while True:
    dados.append(str(input('Nome: ')))
    totp +=1
    dados.append(int(input('Peso: ')))
    galera.append(dados[:])

    for p in galera:
        if dados[1] > mais_pesadas:
            mais_pesadas = dados[0]

    for p in galera:
        if dados[1] < mais_leves:
            mais_leves = dados[0]

    escolha=' '
    while escolha not in 'SN':
        escolha=str(input('Quer cadastar uma nova pessoa? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
    break

print(f'A pessoa mais pesada é {mais_pesadas} e a mais leve é {mais_leves}')
