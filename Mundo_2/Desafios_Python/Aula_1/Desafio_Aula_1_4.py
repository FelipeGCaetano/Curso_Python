#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

#Se ele ainda vai se alistar ao exercito.
#Se é a hoa de se alistar
#Se já passou do tempo de alistamento.

#O programa também deverá mostrar quanto tempo falta ou que passou do prazo.

ano=int(input(f'Qual seu ano de nascimento? '))

if ano>2004:
    print(f'Você ainda irá se alistar ao serviço militar!')
    print(f'Faltam {18-(2022-ano)} anos')
elif ano == 2004:
    print(f'Está na hora de se alistar!')
elif ano == 2003:
    print(f'Ja passou do tempo de alistamento!')
    print(f'Já se passou 1 ano')
else: 
    print(f'Ja passou do tempo de alistamento!')
    print(f'Já se passaram {2022-(ano+18)} anos')
    



