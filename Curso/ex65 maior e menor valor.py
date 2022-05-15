# crie um programa que leia varios numeros inteiros pelo teclado.
#no final da execucao, mostre a media entre todos osvalores e qual foi MAIOR e o MENOR valores lidos.
#o rpograma deve perguntar ao usuario se ele quer ou nao CONTINUAR a digitar valores.

cont = soma = 0
n = int(input('digite um valor: '))
resposta = str(input('quer continuar? ')).strip().lower()
lista = []
while resposta != 'n':   
    if resposta == 's':
        n = int(input('digite um valor: '))
        resposta = str(input('quer continuar[S/N]? ')).strip().lower()        
    else:
        resposta = str(input('resposta errada!!! quer continuar [S/N]? ')).strip().lower()
    cont += 1
    soma += n
    lista += [n]
print(f'vc digitou {cont} numeros e a media foi {(soma/cont):.1f}')
print(f'o maior valor digitado foi {max(lista)} e o menor foi {min(lista)}')
print(f'lista = {lista}')