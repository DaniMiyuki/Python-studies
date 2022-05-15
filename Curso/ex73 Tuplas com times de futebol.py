'''crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol
na ordem de colocacao.depois mostre:

A) os 5 primeiros
B)os ultimos 4 colocados
C) time em ordem alfabetica
D) em que posicao esta o time da Chapecoense'''

	
times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
        'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos',
        'Ceará', 'Internacional','São Paulo', 'Athletico-PR', 'Cuiabá',
        'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')


print(f'os cinco primeiros {times[:5]}')
print(f'os ultimos 4 colocados sao {times[-4 :]}')
print(f'time em ordem sao {sorted(times)}')
print(f'o chepecoense esta em {times.index("Chapecoense")+1} posicao')
