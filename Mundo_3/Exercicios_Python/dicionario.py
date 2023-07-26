
'''pessoas = {'nome': 'Felipe', 'sexo': 'M', 'idade': 18}
del pessoas['sexo'] deletar uma key
pessoas['nome'] = 'David' mudar um valor 
pessoas['peso'] = 70.0 adicionar uma key
for k, v in pessoas.items():
    print(f'{k} = {v}')

print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos')'''


'''brasil = []
estado = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2= {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}

brasil.append(estado)
brasil.append(estado2)

print(brasil[1]['sigla'])'''

estado = dict()
brasil = list()
for c in range (0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
        
