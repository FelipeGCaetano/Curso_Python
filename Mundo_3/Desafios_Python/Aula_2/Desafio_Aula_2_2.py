#Crie um programa onde o usuário possa digitar vários valores númericos e adiicone a uma lista.
#Caso o número já exista, não adicionar e ao final mostrar todos os números em ordem crescente

numero=[]
while True:
    n = int(input(f'Digite um valor: '))

    r = str(input(f'Quer continuar? [S/N]'))
    if r in 'Nn':
        break