#Crie um programa que leia vários numeros inteiros pelo teclado, o programa só irá parar quando o usuario digitar 999
#No final, mostre quantos números foram digitados e qual foi a soma entre eles


n=0
cont=0
s=0
while True:
    n=int(input(f'Digite um número inteiro (999 para parar): '))
    if n == 999:
        break
    s+=n
    cont+=1
print(f'A soma dos {cont} valores foi {s}!')
