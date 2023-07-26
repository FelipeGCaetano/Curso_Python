#Faça um programa que mostre a tabada de vários números, um de cada vez.
#para cada valor digitado pelo usuário. O prgama será interrompido quando o número soliictado for negativo.

t=0
c=1
while True:
    n=int(input(f'Quer ver a tabuada de qual valor? '))
    if n<0:
        break
    print('='*40)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
        c+=1
    print('='*40)
print(f'PROGRAMA TABUADA ENCERRADO')
   
   