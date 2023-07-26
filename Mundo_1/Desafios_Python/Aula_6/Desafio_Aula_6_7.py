#Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%
#Para salários inferiores, calcule um aumento de 15%

salario=float(input(f'Digite o seu salário R$'))


if salario>1250:
    aumento=(salario*10)/100
    print(f'O seu salário com aumento de 10% fica em {aumento + salario}')
else:
    aumento=(salario*15)/100
    print(f'O seu salário com aumento de 15% fica em {aumento + salario}')
    
