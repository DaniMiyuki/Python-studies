# crie um programa que leia varios numeros inteiros pelo teclado.
#o programa so vai parar quando o usuario digitar o valor 999, que
#e a condicao de parada. no final, mostre quantos numeros foram digitados e qual foi a soma
#entre eles (desconsiderando o flag).

n = cont = soma = 0
while n != 999:   
    n = int(input('digite um numero [999 para parar]: '))
    if n == 999:
        break 
    cont += 1
    soma += n         
print (f'vc digitou {cont} numeros e a soma e {soma}')

# neste caso, nao contatenou e nem somou 999 pq [cont e soma] estao DEPOIS do break, caso esteja ANTES ira ADICIONAR no calculo!!!!!