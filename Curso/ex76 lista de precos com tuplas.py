'''crie um programa que tenha uma tupla unica com nomes de produtos
e seus respectivos precos, na sequencia. no final
mostre uma listagem de precos, organizando os dados em forma tabular.'''

print(f'{("LISTA DE PRECOS"):-^80}')

lista = ('Lapis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)
for x in range(0, len(lista)):
    if x % 2 == 0:
        print(f'{lista[x]:.<30}', end='')
    else:
        print(f'R${lista[x]:>7.2f}')
