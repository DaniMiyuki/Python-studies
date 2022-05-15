#faca um programa que leia um numero qualquer e mostre o seu fatorial
'''from math import factorial
n = int(input('digite um numero: '))
print(f'o fatorial de {n}! e {factorial(n)}')'''

'''c = n
   while c > 0
   c -= 1'''

n = int(input('digite um numero: '))
f = 1
print(f'o fatorial de {n}! = ', end='' )
for x in range((n),0,-1):
    
    print(f'{x}', end='')
    print(' x ' if x > 1 else ' = ', end='')
    f *= x
print(f'{f}')