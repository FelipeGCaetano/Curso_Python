#crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar.
#No final, mostre:

#Qual é o total gasto na compra.
#Quantos produtos custam mais de 1000 reais
#Qual é o nome do produto mais barato

total=0
totmil=0
menor=0
cont=0
barato = ' '
while True:
    produto=str(input(f'Nome do produto: '))
    valor=float(input(f'Valor: R$'))
    cont+=1
    total+=valor
    if valor>1000:
        totmil+=1
    if cont == 1 or valor < menor:
        menor=valor
        barato = produto
    escolha= ' '
    while escolha not in 'SN':
        escolha=str(input(f'Quer continuar comprando? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print(' '*10)
print(f'O total gasto em compras foi de R${total:.2f}')
print(f'Ao todo {totmil} produto(s) custam mais que R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
print(' '*10)