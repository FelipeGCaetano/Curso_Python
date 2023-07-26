#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

import math
a=float(input('Digite um ângulo qualquer para saber o seu seno, cosseno e tangente: '))

math.radians

s=math.sin(math.radians(a))
c=math.cos(math.radians(a))
t=math.tan(math.radians(a))

print("O ângulo {} tem o seno {:.2f}".format(a, s))
print("O ângulo {} tem o cosseno {:.2f}".format(a, c))
print("O ângulo {} tem a tangente {:.2f}".format(a, t))