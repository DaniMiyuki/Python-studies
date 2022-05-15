#crie um programa onde o usuario possa digitar cinco valores numericos
#e cadastre-os em uma lista, ja na posicao correta (sem usar o sort()).
#no final, mostre a lista ordenada na tela

lista = []
for ind in range(0,5):
    n =  int(input('dig o valor: '))
    if ind == 0:
        lista.insert(0,n)
        print('inicio')
    for i, valor in enumerate(lista):       
        if n < valor:
            lista.insert(i,n)
            print(f'posicao {i}')
            break
    else:
        if n > lista[-1]:
            lista.append(n)
            print('final')
print(f'os valores adicionados em ordem crescente: {lista} ')


'''lista = []
for sequencia in range(0,5):
    n=int(input('digite um numero: '))   
    inseriu = False
    for ind in range(len(lista)):
        if n < lista[ind]:
            lista.insert(ind, n)
            inseriu = True
            break
    if not inseriu:
        lista.append(n)
    
print(lista) '''


''' resolucao prof
lista = []
for num in range(0,5):
    n = int(input('digite um numero: '))
    if num == 0 or n > lista[len(lista)-1]:
        lista.append(n)
        print('adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'foi adicionado na posicao {pos} da lista')
                break
            pos += 1
         
       
    
print(f'os valores digitados foram {lista}')'''