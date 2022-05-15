# o mesmo professor do desafio anterior quer sortear a ordem de apresentacao dde trabalhos dos alunos. faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import sample
n1 = str(input('primeiro aluno: '))
n2 = str(input('seg aluno: '))
n3 = str(input('terc aluno: '))
n4 = str(input('quart aluno: '))

lista = [n1, n2, n3, n4]
print('a ordem escolhida foi {}'.format(sample(lista,k=4)))