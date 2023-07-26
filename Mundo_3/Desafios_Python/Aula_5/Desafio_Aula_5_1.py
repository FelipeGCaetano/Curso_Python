'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

from datetime import datetime

def voto(nascimento):
    idade = datetime.now().year - nascimento
    if idade >= 18:
        return  ["VOTO OBRIGATÓRIO", idade]
    elif idade <=17:
        return ["NÃO VOTA", idade]
    else: 
        return ["VOTO OPCIONAL", idade]



nasc = int(input(f'Digite seu ano de nascimento: '))
x = voto(nasc)
print(f'Com {x[1]} anos: {x[0]}')
