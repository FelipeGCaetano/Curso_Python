#Crie um programa que leia dois valores e mostre na tela um menu:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa

n1=int(input(f'Primeiro valor: '))
n2=int(input(f'Segundo valor: '))

escolha = 0
while escolha !=5:
    print(f'Escolha uma opção:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    escolha=int(input(f'Sua escolha: '))
    if escolha == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif escolha == 2:
        print(f'{n1} * {n2} = {n1*n2}')
    elif escolha == 3:
        if n1>n2:
            print(f'O maior número entre {n1} e {n2} = {n1}')
        else:
            print(f'O maior número entre {n1} e {n2} = {n2}')
    elif escolha  == 4:
        print(f'Informe os números novamente')
        n1=int(input(f'Primeiro valor: '))
        n2=int(input(f'Segundo valor: '))
    elif escolha == 5:
        print(f'FINALIZANDO')
    else:
        print(f'Opção inválida. Tente novamente')
    print('=-=' * 15)
print('Fim do Programa')

