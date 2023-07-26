def escreva(msg):
    linhas = len(msg) + 4
    print('-' * linhas) 
    print(f'  {msg}')
    print('-' * linhas)

#programa principal
while True:
    mensagem = str(input('Escreva a mensagem que quer exibir: '))
    escreva(mensagem)

    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input(f'Quer escrever uma nova mensagem? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break