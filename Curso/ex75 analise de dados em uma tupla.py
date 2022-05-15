'''desenvolva um programa que leia quatro valores pelo teclado e guarde os em uma tupla. no final mostre:

A) quantas vezes apareceu 
B) em que posicao foi digitado o primeiro valor 3
C) quais foram os numeros pares
'''
print("="*10,'DIGITE 4 NUMEROS',"="*10)



tupla = (int(input('n1: ')),int(input('n2: ')),int(input('n3: ')),int(input('n4: ')))



print('os valores digitados foram: ', tupla)
if 9 in tupla:
    print(f'o numero 9 apareceu {tupla.count(9)} vez(es)')
if 3 in tupla:
    print(f'o valor 3 apareceu na primeira vez na posicao {tupla.index(3)+1}')
print('os valores pares sao: ', end=' ')
for x in tupla:
    if x % 2 == 0:
        print(x, end=' ')
