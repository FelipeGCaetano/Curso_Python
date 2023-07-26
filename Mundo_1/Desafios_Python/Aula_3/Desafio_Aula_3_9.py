#Faça um algoritmo que leiao salário de um funcionário e mostre seu novo salário com 15% de aumento.

s=float(input('Qual é o seu salário? R$'))

sca=s+(s*20/100)

print('O seu salário com aumento de 20% passa a ser R${}'.format(sca))