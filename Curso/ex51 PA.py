# desenvolva um programa que leia o primeiro termo e a razao de uma PA.
# no final mostre os 10 primeiros termos dessa progressao.
a1 = int(input('digite o primeiro termo: '))
r = int(input('digite a razao: '))
a11 = a1 +(11 - 1) * r 
for c in range (a1,a11, r):
    print (c, end= '~')
print('acabou!!')