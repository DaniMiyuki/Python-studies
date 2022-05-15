# desenvolva um proghrama que pergunte a distancai de uma viagem em km.
#calcule o preco da passagem, cobrando R$0,50 por KM para viagens de ate 200Km
# e R$ 0,45 para viagens mais longas.

d = float(input('digite a distancia de sua viagem: '))

if d <= 200:
    print('sua viagem custara {:.2f} reais.'.format(d * 0.50))
else:
    print('sua viagem custara {:.2f} reais.'.format(d * 0.45))    