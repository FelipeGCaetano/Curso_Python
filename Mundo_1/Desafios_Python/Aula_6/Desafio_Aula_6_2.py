#Faça um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7.00 por cada km acima do limite

velocidade=float(input('Digite a velocidade do seu carro: '))

if velocidade>80:
    print(f'Você está acima do limite de velocidade, portanto, será multado em R${(velocidade - 80)*7}.')
else:
    print(f'Você está dentro do limite de velocidade')