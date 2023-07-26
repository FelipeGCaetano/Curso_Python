from random import randint

numeros = list()
pares = list()


def sorteia():
    for n in range(0,5):
        numeros.append(randint(0, 10))
    print(f'Os números sorteador foram {numeros}')

def somaPar():   
    i=0
    for p in numeros:
        if numeros[i] % 2 == 0:
            pares.append(i)
        i+=1  
    soma_pares = sum(pares)
    return soma_pares
    
sorteia()
a = somaPar()
print(f'A soma dos valores pares sorteador foi {a}')
