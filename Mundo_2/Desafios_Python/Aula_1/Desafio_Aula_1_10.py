import random


vc = int(input("Insira sua opção\n 1 para pedra\n 2 para papel\n 3 para tesoura\n Sua opção:"))  
pc = random.randint(1, 3)

if pc == 1 and vc == 1:
    print('Deu empate, ambos escolheram pedra.')

elif pc == 1 and vc == 2:
    print('Você venceu, escolheu papel e o computador pedra.')

elif pc == 1 and vc == 3:
    print('O computador venceu, escolheu pedra e você tesoura.')

elif pc == 2 and vc == 1:
    print('O computador venceu, escolheu papel e você pedra.')

elif pc == 2 and vc == 2:
    print('Deu empate, ambos escolheram papel.')

elif pc == 2 and vc == 3:
    print('Você venceu, escolheu tesoura e o computador papel.')

elif pc == 3 and vc == 1:
    print('Você venceu, escolheu pedra e o computador tesoura.')

elif pc == 3 and vc == 2:
    print('O computador venceu, escolheu tesoura e você papel.')

else :
    print('Empate, ambos escolheram tesoura.')




