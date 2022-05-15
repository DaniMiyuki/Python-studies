
from random import randint
from operator import itemgetter
from time import sleep

jogadores = {}
for x in range(1,5):
    jogadores[f'jogador{x}'] = randint(1,6)

print(f'{" ":<15}','VALORES SORTEADOS')
for key in jogadores.keys(): #(.keys()  --> chama somente a chave(nomenclatura para cada valor)
    print(f'{" ":<10}{key}, tirou {jogadores[key]} no dado')

'''for key, value in jogadores.items(): #(.items()  --> chama o conjunto (keys and values)
    print(key, value)'''

print('-=-'*15)
print(f'{" ":<12} RANKING DOS JOGADORES')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
#jogadore.items() ---> chama o item(key e valor), depois com o metodo escolhe quem deseja ordenar
# key=itemgetter(0) ou (1) --> sendo 0 a key de jogadore e 1 o numero do dado

for indice, itens in enumerate(ranking): # usa enumerate pq ranking e uma lista
    sleep(2.5)
    print(f'{" ":<10}{indice +1}. lugar: {itens[0]} com {itens[1]}')    