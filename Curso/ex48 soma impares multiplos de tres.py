#faca um programa que calcule a soma entre todos os numeros impares 
# que sao multiplos de tres e que se encontram no intervalo de 1 ate 500.

soma = 0
cont = 0
for x in range(1,501):
    if x % 2 > 0 and x % 3 == 0: 
        print (x, end=' ')
        soma = soma + x #tbm pode ser escrito soma += x
        cont = cont + 1  # cont += 1
print('\n a soma de todos os {} valores solicitados e {}'.format(cont, soma))