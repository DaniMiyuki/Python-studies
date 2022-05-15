lista = []
lista_f = []
while True:
    lista_f.append(str(input('nome: ')))
    lista_f.append(float(input('nota 1: ')))
    lista_f.append(float(input('nota 2: ')))
    lista.append(lista_f[:])
    lista_f.clear()
    pergunta = str(input('quer continuar? [S/N] '))
    if pergunta in 'Nn':
        break
print(lista)
print('-=-'*12)
print('No.', ' '*5, 'NOME', ' '*5, 'MEDIA')
print('-=-'*12)
for cada_lista in range(len(lista)):
    for item in range(len(lista[cada_lista])):        
        print(cada_lista, ' '*7, lista[cada_lista][item], ' '*9, (lista[cada_lista][1]+lista[cada_lista][2])/2, end=' ')
        print()
        break
print('-=-'*12)
while True:
    revisao = int(input('mostrar nota do aluno (999 interrompe): '))
    if revisao == 999:
        break
    else:
        cada_lista = revisao
        print(f'notas de {lista[cada_lista][0]} sao {lista[cada_lista][1]}, {lista[cada_lista][2]}')
        print()
        