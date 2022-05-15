#crie um programa que leia um numero inteiro e mostre na tela se ele e impar ou par.

 
n = int(input('digite um numero: '))

r = n % 2
if r == 1:
    print('o nunero {} e impar'.format(n))
else:
    print('o numero {} e par'.format(n))    