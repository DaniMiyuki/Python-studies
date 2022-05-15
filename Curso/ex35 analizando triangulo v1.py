# desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo
from time import sleep

r1 = float(input('primeiro seguimento: '))
r2 = float(input('seg seg: '))
r3 = float(input('terc seg: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('analisando um triangulo....')
    sleep(5)
    print('os seg podem formar um triangulo !')
else:
    print('os seg n podem formar um triangulo')   