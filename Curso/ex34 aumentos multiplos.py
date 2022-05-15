# escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
#para salario superiores a R$ 1250,00, calcule um aumento de 10%.
# #para os inferiores ou iguais, o aumento e de 15%

s = float(input('digite o valor do seu salario: ')) 
a = s * 0.15
b = s * 0.10
if s <= 1250.00:
    print('seu salario de R${:.2f} tera um aumento de 15% passando para R${:.2f}'.format(s,(s + a)))
else:
    print('seu salario de R${:.2f} tera um aumento de 10% passando para R${:.2f}'.format(s,(s + b)))    