# escreva um programa que converta uma temperaura digitada em 'C e converta para 'F.

c = float(input('digite uma temperatura em celsius: '))
print('a temperatura {} "C e {} "F '.format(c, (c * 9)/5+ 32))