#Crie uma tupla preenchida com os 10 primeiros colocados do brasileirão. Na ordem de colocação.
#Depois mostre:

#Apenas os 5 primeiros colocados
#Os ultimos 4 colocados na tabela
#Uma lista com os times em ordem alfabetica
#Em que posição na tabela está o time da chapecoense.


print('=' * 30)
print('        BRASILEIRÃO        ')
print('=' * 30)
times = ('São Paulo', 'Fluminense', 'Vasco', 'Palmeiras', 'Chapecoense',
         'Corinthians', 'Flamengo', 'Atlético-MG', 'Atlético-PR', 'Cruzeiro')

print(f'Os 5 primeiros colocados são: ')
for cont in range(0, 5):
    print(times[cont])
print('=' * 30)

print(f'Os 4 ultimos colocados são: ')
for cont in range(6, 10):
    print(times[cont])
print('=' * 30)

print(f'Times em ordem alfábetica: {sorted(times)}') 
print('=' * 30)

print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição')
print('=' * 30)

