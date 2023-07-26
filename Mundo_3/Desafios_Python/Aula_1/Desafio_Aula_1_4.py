
valores=(int(input('Digite 1 valor: ')),   
        int(input('outro: ')), 
        int(input('outro: ')), 
        int(input('Ultimo: ')))
print('-='*40)
print(f'O valores sorteados foram: {valores}')
print('-='*40)
print(f'O número 9 apareceu {valores.count(9)} vezes')
print('-='*40)
if 3 in valores:
    print(f'O valor 3 apareceu pela primeira vez na {valores.index(3)+1}ª')
else:
    print(f'O valor 3 não foi digitado nenhuma vez')
print('-='*40)
print('Os valores pares digitador foram:', end=' ')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
print(' '*40)
