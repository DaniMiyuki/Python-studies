# crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print ('o dobro e {} e, o triplo e {} e a raiz e {:.0f}'.format(d, t, r))
print ('o dobro e {}, o triplo {}, a raiz e {}'.format((n*2), (n*3), pow(n, 1/2)))