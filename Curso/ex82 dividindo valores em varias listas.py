#crie um programa que vai ter varios numeros e colocar em uma lista.
#depois disso, crie duas listas extras que vao conter apenas os valores
#pares e os valores impares digitados, respectivamente.
#ao final, mostre o conteudo das tres listas geradas.

lista1 =[]
lista2 = []
lista3 = []
while True:
    n=(int(input('digite um numero: ')))
    lista1.append(n)
    if n % 2 == 0:
        lista2.append(n)
    else:
        lista3.append(n)
    resposta = str(input('deseja continuar?[S/N] '))
    if resposta in 'nN':
        break
print(f'lista completa e {lista1}')
print(f'lista de pares e {lista2}')
print(f'lista de impares {lista3}')


'''
lista1 =[]
lista2 = []
lista3 = []
while True:
    lista1.append(int(input('digite um numero: ')))
    resposta = str(input('deseja continuar?[S/N] '))
    if resposta in 'nN':
        break
for i, v in enumerate(lista1)             #indice e valor
    if v % 2 == 0:
        lista2.append(v)
    elif v % 2 == 1
        lista3.append(v)
    
print(f'lista completa e {lista1}')
print(f'lista de pares e {lista2}')
print(f'lista de impares {lista3}')'''