#Deselvonva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares


soma = 0
for c in range(1, 7):
    c=int(input(f'Digite um número inteiro: '))
    if c % 2 == 0:
        soma += c
print(f'A soma dos números pares é: {soma}')
