# faca um algoritmo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto.

p = float(input(' digite um preco: '))
d = (p * 0.05)
print('o produto de {} reais sera {} reais com desconto de 5% '.format(p, p - d))