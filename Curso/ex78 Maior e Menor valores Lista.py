# Faca um programa que leia 5 valores numericos e guarde-os em uma lista.
#no final, mostre qual foi o MAIOR e o MENOR valor digitado e suas
# respectivas POSICOES na lista.

x = [int(input('Digite um valor para p 0: ')),
     int(input('Digite um valor para p 1: ')),
     int(input('Digite um valor para p 2: ')),
     int(input('Digite um valor para p 3: ')),
     int(input('Digite um valor para p 4: '))]

maiorN = max(x)
menorN = min(x)
print(f'{("=-")*20}=')
print(f'voce digitou os valores {x}')
print(f'o maior valor digitado foi {maiorN} nas posicoes ', end='')

for posicao in range(0,5):
     if x[posicao] == maiorN:
          print(f'{posicao}...', end='')
print()
print(f'o menor valor digitado foi {menorN} nas posicoes ', end='')
for posicao in range(0, 5):
     if x[posicao] == menorN:
          print(f'{posicao}...', end='')

'''outra forma
x = []
maiorN = 0
menorN = 0
for posicao in range(0, 5):
     x.append(int(input(f"digite um valor para a posicao {posicao}: ")))
     if posicao ==0
          mai = men = x(posicao)
     else:
          if x(posicao) > maiorN:
               maiorN = x(posicao)
          if x(posicao) < menorN:
               menorN = x(posicao)
print('=-' *30)
print(f'voce digitou os valores {x}')
print(f'o maior valor digitado foi {maiorN} nas posicoes ', end='')

for i, v in enumarate(x):
     if v == maiorN:
          print(f'{i}...', end='')
print()
print(f'o menor valor digitado foi {menorN} nas posicoes ', end='')
for i,v in enumarate(x):
     if v == menorN:
          print(f'{i}...', end='')
          '''




