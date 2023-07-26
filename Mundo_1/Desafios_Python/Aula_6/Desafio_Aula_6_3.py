#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR



numero=int(input(f'Digite um número inteiro: '))
resultado = numero % 2

if resultado == 1:
    print(f'O número {numero} é impar.')
else:
    print(f'O número {numero} é par.')

