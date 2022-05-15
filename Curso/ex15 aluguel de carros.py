# escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidades de dias pelos quais el foi alugado.
  #calcule o preco a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

t = float(input(' digite a distacia percorrida: '))
di= float(input('digite quantidade de dias usado: '))
print('o valor a pagar sera de {:.2f}'.format((di * 60)+(t * 0.15)))