cadastro = {}
gol =[]
soma = 0
while True:
    cadastro["nome"] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
    for cada_partida in range(partidas):
        gol.append(int(input(f'{" ":<5}quantos gols na partida {cada_partida}? ')))
        soma += gol[cada_partida]
    break
cadastro["gols"] = gol
cadastro["total"]= soma        # ----> cadastro["total"] = sum(gol)
print('-=-'*15)
print(cadastro)
print('-=-'*15)
for k, v in cadastro.items():
    print(f'o campo {k} tem o valor {v}')
print('-=-'*15)
for parte in range(len(cadastro['gols'])):         #  ---> for i, v in enumerate(cadastro["gols"]):
    print(f'{" ":<5} ==> Na partida {parte}, fez {cadastro["gols"][parte]} gols.')
print(f'Foi um total de {cadastro["total"]} gols')