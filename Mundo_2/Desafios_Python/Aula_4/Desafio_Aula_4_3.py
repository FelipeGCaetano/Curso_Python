#Faça um programa que jogue par ou impar com o computador. O joso só seré interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

import random

print('='*30)
print('VAMO JOGAR PAR OU IMPAR')
print('='*30)
v=0
while True:
    jogador=int(input(f'Escolha um número: '))
    pc=random.randint(0, 11)
    total=jogador+pc
    escolha=str(input(f'Par ou Ímpar? [P\I] ')).strip().upper()[0]
    while escolha not in 'PI':
        escolha=str(input(f'Par ou Ímpar? [P\I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {pc}. O total deu {total}')
    if escolha == 'P':
        if total % 2 == 0:
            print(f'Você VENCEU!')
            v+=1    
        else:
            print(f'Você PERDEU!')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print(f'Você VENCEU!')
            v+=1
        else:
            print(f'Você PERDEU!')
            break
    print('Vamos joga novamente...')
    print('='*30)
print('='*30)
print(f'GAME OVER, Você venceu {v} vezes!')

