# um professor quer sortear um dos seus quatro alunos para apagar o quadro. faca um programa que ajude ele, lendo o nome deles e escreva onome do escolhido.
import random
n1 = str(input('primeiro aluno: '))
n2 = str(input('seg aluno: '))
n3 = str(input('terc aluno: '))
n4 = str(input('quart aluno: '))

lista = [n1, n2, n3, n4]
print('o escolhido foi {}'.format(random.choice(lista)))