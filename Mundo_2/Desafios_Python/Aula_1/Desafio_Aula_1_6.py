#A confederação Nacional de natação precisa de um programa que leia o ano de nascimento e mostre sua categoria:

#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 20 anos: SÊNIOR
#Acima: MASTER

ano=int(input(f'Qual seu ano de nascimento? '))

if ano == 2013:
    print(f'Sua categoria é MIRIM')

elif ano == 2008:
    print(f'Sua categoria é INFANTIL')

elif ano == 2003:
    print(f'Sua categoria é JUNIOR')

elif ano == 2002:
    print(f'Sua categoria é SÊNIOR')

else:
    print(f'Sua categoria é MASTER')

