#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cdastrada, o programa deverá perguntar se o usuário quer ou não continuar
#No final, mostre:

#Quantas pessoas tem mais de 18 anos.
#Quantos homens foram cadastrados
#Quantas mulheres que tenha menos de 20 anos


tot18=0
totH=0
totM20=0
print('-'*30)
print('   CADASTRE UMA PESSOA    ')
print('-'*30)
while True:
    idade=int(input(f'Idade: '))

    sexo=' '
    while sexo not in 'MF':
        sexo=str(input(f'Sexo? [M/F] ')).strip().upper()[0]

    if idade >=18:
        tot18+=1
    elif sexo == 'M':
        totH+=1
    elif sexo =='F' and idade < 20:
        totM20+=1

    escolha=' '
    while escolha not in 'SN':
        escolha=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-'*30)
        print('   CADASTRE UMA PESSOA    ')
        print('-'*30)
    if escolha == 'N':
        break
    
print(' '*10)
print(f'Total de pessoas com mais de 18 anos cadastradas foi: {tot18}')
print(f'Total de homens cadastrados foi: {totH}')
print(f'Total de mulheres com menos de 20 cadastradas foi: {totM20}')
print(' '*10)
