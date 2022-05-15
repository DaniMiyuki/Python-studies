# faca um programa que leia o comprimento do cateto oposto e do catetoadjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

# outra opcao e
#from math import hypot
#.format(hypot(co, ca))

co = float(input('digite cateto oposto:'))
ca = float(input('digite cateto adjacente: '))
print('o valor da hipotenusa e  {:.2f}'.format((co ** 2 +ca ** 2)**(1/2)))

