from random import randint
from time import sleep
print('-'*50)
print('   '*5, 'JOGA NA MEGA SENA','   '*5)
print('-'*50)
pergunta = int(input('quantos jogos vc quer sortear? '))
print()
print('-=-'*5, f'SORTEANDO {pergunta} jogos', '-=-'*5, '\n')

lista_de_jogos = []
lista_falsa = []
for jogo in range(pergunta): #quantidade de jogos
    for item in range(6): #quantidade de itens dentro de cada jogo
        cada_numero =(randint(1,61))
        if cada_numero in lista_falsa:
            pass
            cada_numero =(randint(1,61))
            lista_falsa.append(cada_numero)
        else:
            lista_falsa.append(cada_numero)
            

    lista_de_jogos.append(sorted(lista_falsa[:]))
    lista_falsa.clear()

for jogo in range(pergunta):
    print('sorteando', end='')    
    for x in range(5):
        sleep(1)
        print('.', end='')
    print()
    print(f'jogo {jogo+1}:', lista_de_jogos[jogo])