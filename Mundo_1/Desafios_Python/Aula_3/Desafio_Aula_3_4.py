#Escreva um porgrama que leia um valor em metros e o exiba convertido em centimetros e millimetros

n1=float(input('Digite um número: '))

c=n1*100
m=n1*1000

print('Convertendo {} metros em centimetros temos {} e em milimetro temos {}'.format(n1, c, m))