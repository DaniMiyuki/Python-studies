'''mehore o des 28 onde o computador vai "pensar" em um numero entre 0 e 10.
so que agora o jogador vai tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer'''

from random import randint
import time
print('----Vamos Brincar comigo?----')
print('eu vou pensar em um numero e quero que vc adivinhe!!!vamos comecar!!!')
qtd = 0
comp = randint(0,10)
time.sleep(2)
n = int(input('digite seu palpite: '))
while n < comp:
    print('o valor e maior...')
    
    n = int(input('digite seu palpite novamente: '))
    while n > comp:
        print('o valor e menor...')
        n = int(input('digite seu palpite novamente: '))
    qtd += 1 + 1
print(f'vc acertou com {qtd} tentativas!! parabens eu escolhi o numero {comp}!!')