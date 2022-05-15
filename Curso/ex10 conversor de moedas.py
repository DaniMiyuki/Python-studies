# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# considere US$1.00 = R$3.27

d = float(input(' digete um valor em reais: '))
print ('ovalor {} reais e {:.2f} doalares'.format(d, (d/ 3.27)))