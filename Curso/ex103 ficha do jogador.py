def arm_dados(jogador='<desconhecido>', gols=0):
    print(f'o jogador {jogador} fez {gols} gols no campeonato')
            

#programa principal
print('~.'*15)
print(f'{"VALIDACAO":^30}')
print('~.'*15)

x = input('nome: ')
y = input('gols: ')

if y.isnumeric():
    y = int(y)
else:
    y = 0
if x.strip() == '':
    arm_dados(gols=y)
else:
    arm_dados(x, y)


'''
def ficha(jog='<desconhecido>', gol=0):
    print(f'o jogador {jog} fez {gol} no campeonato.')


#programa principal
n = str(input("nome do jogador"))
g = str(input("num de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol = g)
else:
    ficha(n,g)
'''