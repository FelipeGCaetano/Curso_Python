#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

from re import A


a=float(input(f'Digite o primeiro número: '))
b=float(input(f'Digite o segundo número: '))
c=float(input(f'Digite o terceiro número: '))

menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c

maior=b
if a>b and a>c:
    maior=a
if c>b and c>a:
    maior=c
print(f'O menor número digitado foi {menor}')
print(f'O maior número digitado foi {maior}')
