#Crie um programa que leia o nome completo de uma pessoa e mostre:
#1.O nome com todas as letras maiúsculas
#2.O nome com todas as letras maiúsculas
#3.Quantas letras ao todo (sem considerar espaços)
#4.Quantas letras tem o primeiro nome


nome=str(input('Digite seu nome completo: ')).strip()
print('analisando seu nome...')
print('seu nome em maiúsculo é {}'.format(nome.upper()))
print('seu nome em minusculo é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))

