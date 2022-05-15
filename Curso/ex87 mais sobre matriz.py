lista = []
listaO =[]
somapares = 0
soma3coluna = 0
maior2linha = 0
for x in range(0,3):       
    for y in range(0,3):
        lista.append(int(input(f'numero {[x,y]}: ')))
    listaO.append(lista[:])
    lista.clear()
for x in range(0,3):       
    for y in range(0,3):
        if y == 2:
            soma3coluna += listaO[x][2]
        if listaO[x][y] % 2 == 0:
            somapares += listaO[x][y]
        if y == 0:            
            maior2linha = listaO[1][0]
        elif listaO[1][x] > maior2linha:
                maior2linha = listaO[1][x]
                    
        print(f'[{listaO[x][y]}]', end=' ')
    print()
print(f'soma dos pares {somapares}')
print(f'soma 3 coluna {soma3coluna}')
print(f'maior 2 linha {maior2linha}')