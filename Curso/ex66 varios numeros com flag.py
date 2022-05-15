# crie um programa que leia varios numeros inteiros pelo teclado.
#o programa so vai parar quando o usuario digitar o valor 999, que
#e a condicao de parada. no final, mostre quantos numeros foram digitados e qual foi a soma
#entre eles (desconsiderando o flag).

n = cont = soma = 0
while True:   
    n = int(input('digite um numero [999 para parar]: '))
    if n != 999:
        cont += 1
        soma += n 
    elif n == 999:
        break 
print (f'a soma dos {cont} numeros e {soma}')