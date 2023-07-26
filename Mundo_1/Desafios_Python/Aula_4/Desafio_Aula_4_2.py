#Faça um programa que leia o comprimeiro do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

co=float(input('Digite o comprimento do cateto oposto: '))
ca=float(input('Digite o comprimento do cateto adjacente: '))


h=hypot(co, ca)



print(f"A hipotenusa vai medir {h}")