jogador = []
cadastro = {}
lista_gol =[]
while True:
    cadastro["nome"] = str(input('nome do Jogador: '))
    partidas = int(input('Quantas partidas jogou? '))
    for n in range(partidas):
        lista_gol.append (int(input(f'{" ":<5}Quantos gols na partida {n+1}? ')))
    cadastro["gols"] = lista_gol[:]
    lista_gol.clear()
    jogador.append(cadastro.copy())

    while True:
        pergunta = str(input('Quer continuar? [S/N] '))
        if pergunta in 'SsNn':
            break
        print('Erro, tente novamente!')
    if pergunta in 'Nn':
        break
print(jogador)
print('-=-'*15)
print(f' {"COD":^6} {"NOME":^15}{"GOLS":^15}{"TOTAL":^7}')
print('-'*45)
for num in range(len(jogador)):
    print(f'{(num):^10}', end='')
    for key,valor in jogador[num].items():
        print(f'{str(valor):^15}', end='')
    print(f'{(sum(jogador[num]["gols"])):^7}')
    print()    

while True:
    mostrar = int(input('mostrar dados de qual jogador? [999 para PARAR] '))
    if mostrar == 999:
        break
    else:        
        print(f' -- LEVANTAMENTO DO JOGADOR {jogador[mostrar]["nome"]}:')
        for indice, valor in enumerate(jogador[mostrar]["gols"]):
            print(f'   -->no jogo {indice+1} fez {valor} gols')
                
        
