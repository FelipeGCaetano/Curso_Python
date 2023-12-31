'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''
import os

def ficha(nome='', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


n = str(input('Nome do jogador: '))

if n.strip() == '':
    os.system('cls')
    print('Nome do jogador não preenchido')
else:
    g = str(input('Número de gols: '))
    if g.isnumeric():
        g = int(g)
    else:
        g=0

    if n.strip() == '':
        ficha(gols=g)
    else:
        ficha(n, g)

