#Escreva um programa para aprovar um emprestimo bancáro.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.

valor=float(input(f'Qual o valor da casa? R$'))
salario=float(input(f'Qual é o seu salário? R$'))
anos=int(input(f'Em quantos anos pensar em pagar? '))

meses=anos*12
prestacao=valor/meses

if prestacao<=(salario*30)/100:
    print(f'O empréstimo foi autorizado!')
else:
    print(f'O empréstimo foi negado.')




