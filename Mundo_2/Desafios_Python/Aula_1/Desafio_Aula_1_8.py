#Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e ostre seu status:

#Abaixo de 18.5: abaixo do peso
#Entre 18.5 e 25: peso ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade móbida

peso=float(input(f'Qual o seu peso? '))
altura=float(input(f'Qual sua altura? '))

imc=peso/(altura*altura)

if imc<18.5:
    print(f'Abaixo do peso.')
elif imc <= 25:
    print(f'Peso  ideal.')
elif imc <= 30:
    print(f'Sobrepeso')
elif imc <= 40:
    print(f'Obesidade')
else:
    print(f'Obesidade Mórbida')