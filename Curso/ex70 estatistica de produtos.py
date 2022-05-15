# crie um programa que leia o NOME e o PRECO de varios produtos.
#o programa devera perguntar se o usuario vai continuar.no final, mostre:

'''
A) qual e o TOTAL GASTO na compra.
B) quantos produtos custam MAIS de R$ 1000.
C) qual o NOME do produto mais BARATO.'''

total = np = menorvalor = cont = 0
pmb = ''
while True:
    nome = str(input('nome do produto: ')).strip().lower()
    preco = float(input('valor do produto: '))
    total += preco
    cont += 1
    if preco <= 1000.00:
        np += 1
    if cont == 1:
        menorvalor = preco
        pmb = nome
    else: 
        if preco < menorvalor:
            menorvalor = preco
            pmb = nome
    resposta = ' '
    while resposta not in 'sn':
        resposta = str(input('deseja continuar? [S/N]: ')).strip().lower()
    if resposta == 'n':
        break
    

print('fim do programa')
print(f'o total da compra foi R${total:.2f}')
print(f'temos {np} produtos custando menos de R$1000.00')
print(f'o produto mais barato foi {pmb} que custa R${menorvalor:.2f}')