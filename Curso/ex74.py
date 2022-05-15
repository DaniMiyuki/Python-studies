'''crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.
depois disso mmostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estao na tupla
'''
import random

tupla = tuple(random.sample(range(1,10), k=5))
print(tupla)
print(f'{max(tupla)}')
print(f'{min(tupla)}')

'''from random import sample
a = tuple(sample(range(10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.'''