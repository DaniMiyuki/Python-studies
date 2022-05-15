#faca um programa que leia o peso de cinco pessoas.
#no final, mostre qua o maior e o menor peso lidos.

lista = []
for x in range(1,6):
    peso = float(input('digite o peso da {} pessoa: '.format(x)))
    lista += [peso]
print('o maior peso foi {} e o menor foi {}'.format(max(lista),min(lista)))

# outra forma:
# maior = 0
# menor = 0
# for x in range(1,6):
#     peso = float(input('digite o peso da {} pessoa: '.format(x)))
#     if x == 1:   ~~~~o primeiro numero da lista digitado
#           maior = peso    ~~~sera maior e menor
#           menor = peso
#     else:    ~~~~apartir do segundo sera comparado aos anteriores
#         if peso > maior:
#                 maior = peso
#        if peso < menor:
#                 menor = peso
# print('o maior peso foi {} e o menor foi {}'.format(maior,menor)