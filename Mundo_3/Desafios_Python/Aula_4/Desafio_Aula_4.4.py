def maior(*núm):
    maior = max(valores)
    print(f'Os número digitados foram {valores} e o maior número é o {maior}')


#programa principa
valores = []
while True:
    numero = float(input('Digite um número: '))
    valores.append(numero)
    
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer adicionar um valor? ')).strip().upper()[0]
    if escolha == 'N':
        break

maior(valores)

