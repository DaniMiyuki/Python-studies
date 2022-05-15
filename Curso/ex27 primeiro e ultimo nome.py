# faca um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o ultimo nome separadamente.

# (quando usa -1 para a funcao len(), acha-se o numero ou letra que esta em ultimo)

nome =str(input('digite seu nome completo: '))
ns = nome.split()

print('seu prim nome e {} '.format(ns[0]))
print('seu seg nome e {}'.format(ns[len(ns)-1]))
