#faca um programa que leia um ano qualquer e mostre se ele eh bissexto
from datetime import date
ano = int(input('digite uma data ou coloque zero para o ano atual: '))

if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 !=0) or ano % 400 == 0:
    print('{} e um ano bissexto'.format(ano))
else:
    print('{} nao e um ano bissexto'.format(ano))    