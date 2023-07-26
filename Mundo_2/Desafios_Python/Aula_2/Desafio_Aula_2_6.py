#Deselvova um programa que leia o primeiro termo e a razão de uma PA, No final, mostre os 10 primeiros termos dessa PA.

primeiro = int(input(f'Primeiro termo: '))
razão = int(input(f'Razão: '))
décimo = primeiro + (10-1) * razão
for c in range(primeiro, décimo, razão):
    print(f'{c}', end=' -> ')
print('ACABOU')
