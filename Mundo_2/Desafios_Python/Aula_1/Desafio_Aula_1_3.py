#Escreva um programa que leia dois número inteiros e compare-os, mostrando na tela uma mensagem:

#O primeiro valor é maior
#O segundo valor é maior
#Não existe maior, os dois são iguais

n1=float(input('Digite o primeiro número: '))
n2=float(input('Digite o segundo número: '))

if n1>n2:
    print(f'O primeiro número é maior')
elif n2>n1:
    print(f'O segundo número é maior')
else:
    print(f'Não existe valor maior, os números são iguais')
    