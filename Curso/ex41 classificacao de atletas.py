#a confederacao nacional de natacao precisa de um programa que leia o ano de anscimento
# de um atleta e mostre sua categoria, de acordo com a idade:
# ate 9 anos : mirim
#ate 14 anos : infantil
#ate 19 anos : junior
#ate 25 anos : senior
#acima: master

from datetime import date

ano = int(input('digite seu ano de nascimento: '))

data = date.today().year

id = data - ano

if id <= 9:
    print('vc tem {} anos e sua categoria e MIRIM'.format(id))
elif id <= 14:
    print('sua idade e {} anos e sua categoria e INFANTIL'.format(id))
elif id <= 19:
    print('sua idade e {} anos e sua categoria e JUNIOR'.format(id))
elif id <= 25:
    print('sua idade e {} e sua categoria e SENIOR'.format(id))
else:
    print('sua idade e {} e sua categoria e MASTER'.format(id))