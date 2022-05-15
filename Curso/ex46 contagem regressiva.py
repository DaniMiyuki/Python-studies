#faca um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 ate 0, com uma pausa de 1 seg entre eles.

from time import sleep
print('Contagem regressiva!!!')

for cont in range(10,-1,-1): #o terceiro -1 significa que ele esta decaindo 1 em 1 
    print(cont)
    sleep(1)
print('Bum! BUm! Pooow!')