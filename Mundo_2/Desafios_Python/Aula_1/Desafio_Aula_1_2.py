#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal

n=int(input(f'Digite um número inteiro: '))
print(f'Escolha:\n 1 para binário\n 2 para octal\n 3 para hexadecimal\n  ')
opção=int(input(f'Sua opção: '))

if opção == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n) [2:]}')
elif opção == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n) [2:]}')
elif opção == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n) [2:]}')
else:
    print(f'Opção inválida')
