# faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.

#no = int(input('digite um numero de 0 a 9999: '))
#n = str(no)
#print('uni {} dez{} cent{} e milhar{}'.format(n[3], n[2], n[1], n[0]))

num = int(input('digite um numero de 0 a 9999: '))

print('u = {}'.format(num // 1 % 10))
print('d = {}'.format(num // 10 % 10))
print('c = {}'.format(num // 100 % 10))
print('m = {}'.format(num // 1000 % 10))