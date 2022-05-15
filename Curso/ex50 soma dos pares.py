# desenvolva um programa que leia seis numeros interos e mostre a soma apenas daqueles que forem pares.
#se o valor digitado for impar, desconsidere-o.

soma = 0
for c in range(1,7):
    n = int(input('digite o {} valor: '.format(c)))
    if c % 2 == 0:
        soma += c
print('a soma dos valores e {}'.format(soma))
