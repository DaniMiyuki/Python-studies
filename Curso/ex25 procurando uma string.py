# crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome.

nome = str(input('digite seu nome: ')).strip()

print('seu nome tem Silva? {}'.format('silva' in nome.lower()))