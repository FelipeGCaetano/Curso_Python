#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 até 20

cont=('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')


while True:
    while True:
        n=int(input(f'Digite um número entre 0 e 10: '))
        if  0 <= n <= 10:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {cont[n]}')
    escolha=' '
    while escolha not in 'SN':
        escolha=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
