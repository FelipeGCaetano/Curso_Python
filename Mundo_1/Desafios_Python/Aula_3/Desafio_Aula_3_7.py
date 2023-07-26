#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade necessária de tinta para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2.

l=float(input('Digite a largura da parede em metros: '))
a=float(input('Digite a altura da parede em metros: '))

area=l*a
qt=area/2
print('Sabendo que a área dessa parede é de {} metros quadrados, a quantidade de tinta necessária para pintar essa parede é {} litros'.format(area, qt))
