# escreva um programa que leia a velociade de um carro.
#se ela ultrapassar 80km/h mostre uma msg dizendo que ele foi multado.
#a multa vai custar R$7,00 por cada km acima do limite.

v = float(input('digite a velocidade: '))
    
if v > 80:
     print('vc excedeu o limeite de 80km/h epagara uma multa de {:.2f}'.format((v -80) * 7))
print('parabens vc esta dentro da velocidade permitida!')