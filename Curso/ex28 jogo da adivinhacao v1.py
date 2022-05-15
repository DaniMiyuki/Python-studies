# Escreva um programa que faca o computado "pensar" em um numero inteiro entre 0 e 5 e peca para o 
#usuario tentar descobrir qual foi o numero escolhido pelo computador. o programa devera escrever na tela
#se o usuario venceu ou perdeu.

from random import randint
from time import sleep

print('-=-' * 20)
print('vou pensar em um numero de 0 a 5. tente adivinhar...')
print('-=-' * 20)

num = randint(0, 5)
n = int(input('digite em que numero eu pensei: '))

print('processando.....')
sleep(5)

if num == n:
   print('voce venceu!')
else:
    print('vc perdeu, eu pensei em {} '.format(num))