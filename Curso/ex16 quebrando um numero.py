# crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porcao inteira.

# outra opcao
#from math import trunc
#.format(n, trunc(n))

import math
n = float(input('digite um numero: '))
print('o numero {} tem a parte inteira {}'.format(n, math.trunc(n)))