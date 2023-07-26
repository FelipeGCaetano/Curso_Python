#faça um programa que mostre a tabuada de um número que o usuário escolher


n=int(input(f'Digite um número inteiro: '))

for c in range (1, 11):
    print(f'{n} X {c} = {n*c}')
