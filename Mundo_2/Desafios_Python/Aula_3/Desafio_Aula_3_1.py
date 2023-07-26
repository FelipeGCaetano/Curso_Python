#Faça o programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
#Caso esteja errado, peça a digitação novamente até o valor correto


sexo = str(input(f'Informe seu sexo: [M\F] ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor digite seu sexo: ')).strip().upper[0]
print(f'Sexo {sexo} registrado com sucesso!')


