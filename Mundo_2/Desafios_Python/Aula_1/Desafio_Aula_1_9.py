#Elabore um porgrama que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:

#À vista dinheiro/cheque: 10% de desconto
#À vista no cartão: 5% de desconto
#Em até 2x no cartão: Preço normal
#3x ou mais no cartão: 20% de juros

produto=float(input(f'Qual o preço do produto? R$'))

print(f'''Escolha uma opção de pagamento:
1 para pagar no dinheiro/cheque
2 para pagar à vista no cartão
3 para parcelar em 2x no cartão
4 para parcelar em 3x ou mais no cartão''')
opção=int(input('Opção: '))

if opção==1:
    print(f'O preço com 10% de desconto fica em R${produto-((produto*10)/100):.2f}')
elif opção==2:
    print(f'O preço com 5% de desconto fica em R${produto-((produto*5)/100):.2f}')
elif opção==3:
    print(f'O preço fica em R${produto}')
elif opção==4:
    print(f'O preço com 20% de juros fica em R${produto+((produto*20)/100):.2f}')
else:
    print(f'Opção inválida')



