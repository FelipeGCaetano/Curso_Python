
pessoas = dict()
cadastros = list()
mulheres = list()
acima_media = list()

cont = 0
idades = 0

while True:
    pessoas['Nome'] = str(input('Nome: '))
    pessoas['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoas['Idade'] = int(input('Idade: '))
    
    cadastros.append(pessoas.copy()) #adicionar informações do dicionario na lista

    if pessoas['Sexo'] == 'F': #add as mulheres do grupo
        mulheres.append(pessoas['Nome'])

    cont+=1 #Quantidade de pessoas

    idades += pessoas['Idade'] #Soma das idades

    escolha =' ' #Looping
    while escolha not in 'SN':
        escolha=str(input('Quer cadastar uma nova pessoa? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break

media = idades / cont #media de idades

print('-=' * 25)
print(cadastros)
print('-=' * 25)
print(f'No grupo temos {cont} pessoas.')
print(f'A média de idade do grupo é {media:.2f} anos')
print(f'As mulheres do grupo são: {mulheres}')
