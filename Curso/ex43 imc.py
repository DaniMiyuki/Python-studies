# desenvolva uma logica que leia o peso e a altura de uma pessoa, 
#calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#abaixo de 18.5: abaixo de peso
#entre 18.5 e 25: peso ideal
#25 ate 30 : sobrepeso
#30 ate 40: obsidade
#acima de 40: obesidade morbida

p = float(input('digite seu peso: '))
h = float(input('digite sua altura: '))

imc = p/(h**2)
print('seu imc e {:.1f}'.format(imc))

if imc < 18.5:
    print('abaixo do peso')
elif 18.5 <= imc < 25:
    print('peso ideal')
elif 25 <= imc < 30:
    print('sobrepeso')
elif 30 <= imc < 40:
    print('obesidade')
else:
    print('obeside morbida')

