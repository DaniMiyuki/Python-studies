# crie um programa que faca o computador jogar jyankenpou com vc.
import random
from time import sleep
print('vamos jogar jyankenpou?!!')

r = str(input('digite pedra, tesoura ou papel: '))

comp = ("pedra", "tesoura", "papel")

print('..')
sleep(5)

print('o computador escolheu {}'.format(random.choice(comp)))

if r == comp:
    print('empate')
elif r == 'pedra' and comp == 'tesoura':
    print('vc ganhou!!')
elif r == 'tesoura' and comp == 'papel':
    print('vc ganhou!!')
elif r == 'papel' and comp == 'pedra':
    print('vc ganhou!!')
else:
    print('vc perdeu!!!')