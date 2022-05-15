# faca um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento.

s = float(input(' digite o salario do funcionario: '))
a = (s * 0.15)

print('o salario de {} recebera um aumento de 15% e sera {}'.format(s, s + a))