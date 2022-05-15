# faca um programa que leia nome e peso de varias pessoas, 
# guardando tudo em uma lista.no final, mostre:
# A) quantas pessoas foram cadastradas.
# B) uma listagem com as pessoas mais pesadas.
# C) uma listagem com as pessoas mais leves.

lista = []
listaN = []
maior = menor = 0
while True:
    listaN.append(str(input('Nome: ')))
    listaN.append(float(input('Peso: ')))
    lista.append(listaN[:])
    listaN.clear()
    print(lista)
    for cada_lista in lista:
        if len(lista)== 1:
            maior = menor = lista[0][1]
        else:
            if cada_lista[1] > maior:
                maior = cada_lista[1]
            if cada_lista[1] < menor:
                menor = cada_lista[1]
    print(maior, menor)
    pergunta = str(input('deseja continuar? [S/N] '))
    if pergunta in 'nN':
        break    
print(f'vc cadastrou: {len(lista)} pessoas')
print(f'maior peso foi {maior:.1f}', end=' ')
for cada_lista in lista:
    if maior == cada_lista[1]:
        print(f'{cada_lista[0]}', end=' ')
print()
print(f'menor peso foi {menor:.1f}', end=' ')
for cada_lista in lista:
    if menor == cada_lista[1]:
        print(f'{cada_lista[0]}', end=' ')