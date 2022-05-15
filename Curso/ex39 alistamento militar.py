# faca um programa que leia o ano de nascimento de um jovem e informe 
#de acordo com sua idade, se ele ainda vai se alistar ao servico militar, se
#e a hora de se alistar ou se ja passou do tempo do alistamento.
#seu programa tbm devera mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano = int(input('digite o ano em que nasceu: '))
data = date.today().year


id = data - ano


if id < 18:
    print('faltam {} anos para seu alistamento'.format(18 - id))
elif id > 18:
    print('ja se passaram {} anos para vc se alistar'.format(id - 18))
elif id == 18:
    print('vc deve se alistar imediatamente!!!')