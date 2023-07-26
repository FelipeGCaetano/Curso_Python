#Um professor quer sortear um dos seus quatro alunos ara apagar o quadro. Faça um programa que lea o nome dos alunos e escreva o nome do escolhido.

import random

a1=str(input('Digite o nome do primeiro aluno: '))
a2=str(input('Digite o nome do segundo aluno: '))
a3=str(input('Digite o nome do terceiro aluno: '))
a4=str(input('Digite o nome do quarto aluno: '))

lista=[a1, a2, a3, a4]

escolhido=random.choice(lista)

print('O aluno escolhido foi o {}'.format(escolhido))