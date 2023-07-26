import enum
from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador 1': randint(1, 6), 
        'jogador 2': randint(1, 6), 
        'jogador 3': randint(1, 6), 
        'jogador 4': randint(1, 6)}

ranking = list()

print('== VALORES SORTEADOS ==')

for k, v in jogo.items():
    print(f'A {k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #sorted para organizar o dicionario, key 1 para ordenar pelo número randomizado e reverse para inverter a ordem
print('-='*15)
print('== RANKING DOS JOGADORES ==')
print('-='*15)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
