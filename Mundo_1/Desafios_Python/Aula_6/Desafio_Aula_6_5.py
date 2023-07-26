#Faça um programa que leia um ano qualquer e mostre se ele é bissexto

ano=int(input("Insira um ano: "))
if (ano % 4 == 0):
    print("Esse ano é bissexto!")

else: 
    print("Esse ano não é bissexto!")