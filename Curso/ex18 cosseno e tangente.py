# faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
import math
a = float(input('digite um angulo: '))
print ('sen {:.2f}'.format(math.sin(math.radians(a))))
print ('cos{:.2f}'.format( math.cos(math.radians(a))))
print ('tang{:.2f}'.format( math.tan(math.radians(a))))