#desenvolva um programa que leia o nome, idade e sexo
#de 4 pessoas. no final do programa mostre:

#a media de idade do grupo       qual e o nome do homem mais velho     quantas mulheres tem menos de 20 anos

lenN = []
lenI = []
lenS = []
id = 0
maior = 0
maisvelho = 0
menor21 = 0
for x in range(1,5):
    print('-----{} pessoa-----'.format(x))
    n = str(input(print('nome: ')))
    i = int(input(print('idade: ')))
    s = str(input(print('sexo [M/F]: '))).lower().strip()

    id += i
    lenN += [n]
    lenI += [i]
    lenS += [s]

    if s == 'm' and x == 1:
        maior = i
        maisvelho = n    
    if i > maior and s == 'm':
        maior = i
        maisvelho = n
    if i < 20 and s == 'f':
        menor21 += 1

lista1 = [lenN[0], lenI[0], lenS[0]]
lista2 = [lenN[1], lenI[1], lenS[1]]
lista3 = [lenN[2], lenI[2], lenS[2]]



print('lista1 {}'.format(lista1))
print('lis de lenN {}'. format(lenN))
print('{} media'.format(id/4))
print('o primeiro nome digitado foi {}'.format(lenN[1]))



print('a media de idade do grupo e de {:.0f} anos'.format(id/4))

print('o homem mais velho do grupo tem {} e se chama {}'.format(maior, maisvelho))

print('ao todo sao {} mulheres com menos de 20 anos'.format(menor21))