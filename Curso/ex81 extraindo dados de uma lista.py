#crie um programa que vai ler varios numeros e colocar em uma lista.depois disso, mostre:
# A) quantos numeros foram digitados.
# B) a lista de valores, ordenada de forma decrescente.
# C) se o valor 5 foi digitado e esta ou nao na lista.

lista = []
quantidade = 0
while True:   
    n= int(input('digite um numero: '))
    lista += [n]
    quantidade += 1
    resposta = str(input('deseja continuar?[S/N] ')).strip().lower()
    if resposta == 'n':
        break
    
lista.sort()
lista.reverse()
print(f'foram digitados {quantidade} numeros')
print(f'lista decrescente e {lista}')
if 5 in lista:
 print(f'o numero 5 esta na lista')
else:
    print(f'o numero 5 nao esta na lista')


'''
valores = []
while True:
    valores.append(int(input("digite um valor: ")
    resp = str(input("quer continuar")
    if resp in "nN":
        break
print(f': vc digitiu {len(valores)} elementos')
valores.sort(reverse=True)
print(f'os valores em ordem decrescente sao {valores}
if 5 in lista:
 print(f'o numero 5 esta na lista')
else:
    print(f'o numero 5 nao esta na lista')'''