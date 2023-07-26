#Faça um algoritmo que leia o preço de um produto e mostre o novo preço, com 5% de desconto.

p=float(input('Qual o preço do produto? R$'))

pcd=p-((p*5)/100)

print('O produto que custava R${}, na liquidação com o desconto de 5% passa a custar R${}'.format(p, pcd))