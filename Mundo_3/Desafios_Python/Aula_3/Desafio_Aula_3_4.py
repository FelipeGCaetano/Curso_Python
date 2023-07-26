jogador = dict()
partidas = list()


jogador['Nome'] = str(input('Nome: '))

jogos = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, jogos):
    partidas.append(int(input(f'Quantos gols foram feitos no {c+1}º jogo? ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)

print('-=' * 30)

print(jogador)

for k, v in jogador.items():
    print(f'{k} = {v}')

print('-=' * 30)

print(f'O jogador {jogador["Nome"]} jogou {jogos} partidas')
for i, v in enumerate(jogador['Gols']):
    print(f'Na partida {i+1} fez {v} gol(s)')

print(f'{jogador["Nome"]} fez um total de {jogador["Total"]} gols')