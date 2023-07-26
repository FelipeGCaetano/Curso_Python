import random

print('''
''')
print(f'Você irá tentar acertar o número que o computador pensar, tente até acertar!!')
chute = 0
cont = 0
numero=random.randint(0, 10)
while chute != numero:
    numero=random.randint(0, 10)
    chute=int(input('Chute um número de 0 a 10: '))
    cont+=1
    if chute == numero:
        print(f'Você acertou')
        print(f'Você teve que chutar {cont} vezes para acertar')
        print(f'O numero escolhido pelo computador foi {numero}')
    elif chute < 0 or chute > 10:
        print(f'Você digitou um número fora da margem')
    else:
        print(f'Você errou, tente novamente')
print('''
''')
    