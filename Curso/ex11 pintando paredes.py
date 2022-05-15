# faca um programa que leia a largura e a altura de uma parede em metros, 
    #calcule a sua area e a quantidade de tinta necessaria para pinta-la, 
    # sabendo que cada litro de tinta, pinta uma area de 2m2.

ap = float(input('digite alt da parede: '))    
lp = float(input('digite lar da parede: '))
p = ap * lp
print('a parede tem {} metros e eh necessaria {} litros de tinta'.format(p, p/2))