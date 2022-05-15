# Crie um programa que leia o ano de nascimento de sete pessoas
# No final, mostre quantas pessoas ainda nao atingiram a 
# maioridade e quantas ja sao maiores
import datetime
#ano = date.today().year
data = datetime.datetime.now()
ano = (data.year)

qtdi = 0
qtd = 0
for x in range(1, 8):
    nascimento = int(input('qual o ano de nascimeto da {} pessoa: '.format(x)))
    idade = ano - nascimento

    if idade <= 18:
        qtdi += 1
    else:
        qtd += 1
print('neste ano de {}'.format(ano))
print('das sete pessoas {} atingiram a maioridade e {} ainda sao de menor!!'.format(qtdi,qtd))