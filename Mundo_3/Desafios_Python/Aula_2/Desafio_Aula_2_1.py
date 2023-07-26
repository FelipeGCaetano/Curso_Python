#Faça um programa que leia 5 valores númericos e guarde em uma lista
#No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista



valores = list()
mai=0
men=0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai=men=valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]

print(f'Os valores digitados foram {valores}')
print(f'O maior valor é o {mai} na posição ', end='')

for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}... ', end='')
print()

print(f'O menor valor é o {men} nas posições ', end='')   
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...', end='')
print()
