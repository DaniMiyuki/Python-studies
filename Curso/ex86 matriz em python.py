# crie um programa que crie uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado.
# no final, mostre a matriz na tela, com a formatacao correta
lista = []
listaO =[]
for x in range(0,3):       
    for y in range(0,3):
        lista.append(int(input(f'numero {[x,y]}: ')))
    listaO.append(lista[:])
    lista.clear()
for x in range(0,3):       
    for y in range(0,3):
        print(f'[{listaO[x][y]}]', end=' ')
    print()

'''
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for x in range(0,3):
    for y in range(0, 3):
        matriz[x][y] = int(input(f'numero [{x}, {y}]: '))
for x in range(0,3):
    for y in range(0, 3):
        print(f'[{matriz[x][y]:^5}]', end='')
    print()
'''