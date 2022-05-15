# refaca o desafio 009, mostrando a tabuada de um numero que o usuario escolher, so que agora utikizando um laco for.

n = int(input('digite um numero: '))

for x in range (1,11):
    print('{} x {} = {}'.format(n, x, n*x))