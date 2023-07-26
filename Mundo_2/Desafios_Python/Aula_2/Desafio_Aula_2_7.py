#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

n=int(input(f'Digite um número para saber se é primo ou não: '))
tot = 0

for c  in range(1, n+1):
    if n % c == 0:
       tot += 1

print(f'O número {n} foi divisivel {tot} vezes')

if tot == 2:
    print(f'E por isso ele é primo.')
else:
    print(f'E por isso ele não é primo.')

