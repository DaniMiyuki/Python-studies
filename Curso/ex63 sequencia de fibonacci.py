# escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros termos de uma sequencia de fibonac

n = int(input('digite um numero: '))
cont = 0
soma = 1
lista = [1]
n1 = 1
n2 = 1
while cont != n -1:
    lista += [soma]
    soma =  n1 + n2
    cont += 1
    n1 = n2
    n2 = soma   
print(f'{lista}')