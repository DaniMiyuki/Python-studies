from random import randint

def sortear(lista):   
    for num in range(5):
        lista.append(randint(1,9))
    print(f'sorteando 5 valores da lista: ', end='')
    for num in lista:
        print(num, end=' ')
    print('PRONTO!')
        

def somapar(lista):
    soma = 0
    for x in lista:
        if x % 2 == 0:
            soma += x
    print(f'Somando os valores pares de {lista}, temos {soma}')


# programm principal
numeros = list()
sortear(numeros)
somapar(numeros)
