# refaca o desafio 51, lendo o primeiro termo e a razao de uma PA, 
#mostrando os 10 primeiros termos da progressao usando a esruura while
r = int(input('digite a Razao da PA: '))
a1 = int(input('digite o primeiro termo da PA:  '))
a11 = a1 + (11 -1) * r
cont = a1

print('Os 10 primeiros termos da PA sao:')
while cont < a11:
    print(f'{cont}', end=' ~~~ ')
    cont += r