# faca um programa que mostre a tabua de varios numeros, um de cada vez, para cada 
#valor digitado, pelo usuario.o programa sera interrompido quando o numero solicitado for NEGATIVO.

n = int(input('digite a tabuada que deseja ver?: '))
while True:
    for cont in range(1, 11):
        print(f'{n} x {cont} = {n * cont}')
        if cont == 10:
            n = int(input('qual tabuada mais deseja ver?: '))
    if n < 0:
        break
print('programa encerrado!!!')