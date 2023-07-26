#Desenvolva um pragrama que pergunte a distância de uma viagem em km.
#Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200km e R$0,45 para viagens mais longas


distancia=float(input(f'Qual a distância da viagem em km? '))

if distancia<=200:
    print(f'O preço da passagem será de {distancia*0.50}')
else:
    print(f'O preço da passagem será de {distancia*0.45}')
