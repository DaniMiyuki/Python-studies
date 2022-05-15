# crie um programa onde o usuario possa digitar sete valores numericos e 
# cadastre os em uma lista unica que mantenha separados os valoreas pares e impares.
# no final, mostre valores pares e impares em ordem crescente.

lista = []
listap = []
listai = []

for x in range(0,7):
    n = int(input(f'{x}o numero: '))
    if n % 2 == 0:
        listap.append(n)
    else:
        listai.append(n)
lista.append(listap[:])
listap.clear()
lista.append(listai[:])
listai.clear()
print(lista)
print(f'lista par {sorted(lista[0])}')
print(f'lista impar {sorted(lista[1])}')