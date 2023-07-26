#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc

n=float(input('Digite um número: '))

ni=trunc(n)
print('O valor digitado foi {} e sua versão inteira é {}'.format(n, ni))