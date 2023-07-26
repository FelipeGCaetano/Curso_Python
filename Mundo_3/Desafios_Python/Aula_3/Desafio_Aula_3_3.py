from datetime import datetime

cadastro = dict()

cadastro['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
cadastro['Idade'] = datetime.now().year - nascimento
cadastro['Carteira'] = int(input('Carteira de Trabalho (0 não tem): '))

if cadastro['Carteira'] != 0:
    cadastro['Contratação'] = int(input('Ano da Contratação: '))
    cadastro['Salário'] = float(input('Salário: R$ '))
    cadastro['Idade de Aposentadoria'] = cadastro['Idade'] + 35

print('-='*25)
for k, v in cadastro.items():
    print(f'{k} = {v}')

