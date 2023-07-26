#Crie um algoritmo que leia o seu dobro, tripli e raiz quadrada.

n1=float(input('Digite um número: '))
d=n1*2
t=n1*3
r=n1**(1/2)

print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(n1, d, t, r))