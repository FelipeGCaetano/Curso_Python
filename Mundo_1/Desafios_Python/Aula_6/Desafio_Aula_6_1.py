#Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#o programa deverá escrever na tela se o usuáriovenceu ou perdeu.

import random



while (True):

    jogar=int(input(f'Digite 1 para jogar e 2 para parar: '))
    if (jogar == 1):
        numero=random.randint(0, 5)
        chute=int(input('Chute um número de 0 a 5: '))
        if chute == numero:
            print(f'Você acertou')
            print(f'O numero escolhido pelo computador foi {numero}')
        elif chute < 0 or chute > 5:
            print(f'Você digitou um número fora da margem')
        else:
            print(f'você errou')
            print(f'O numero escolhido pelo computador foi {numero}')
    elif (jogar == 2):
        print(f'--FIM--')
        break


