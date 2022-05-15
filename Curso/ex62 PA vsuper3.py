# melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos
# O programa encerra quando ele disser que quer mostrar 0 termos.

a1 = int(input('primeiro termo da PA: '))
r = int(input('razao da PA: '))
a11 = a1 + (11 - 1) * r
cont = a1
totpa = 0
c = 1
while c != 0:
    while cont < a11:
        print(f'{cont}', end='~~~')
        cont += r       
    print('Pausa', end='\n')    
    c = int(input('quantos termos vc quer mostrar a mais? '))
    totpa = 10
    a11 = a11 + (3 * c)
    totpa += 1
print(f'o total de numeros de Pas {totpa - 1}')
#print(f'progressao finalizada com {ntermos} termos mostrados')