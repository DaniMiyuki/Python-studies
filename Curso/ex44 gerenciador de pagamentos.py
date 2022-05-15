# elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preco normal e condicao de pagamento:

# a vista dinheiro/cheque: 10% de desconto
# a vista no cartao: 5% de desconto
# em ate 2x no cartao: preco normal
# 3x ou mais no cartao: 20% de juros

vp = float(input('digite o valor da compra: '))
print('Formas de pagamento')
print('[1] a vista dinheiro/cheque /n [2] a vista no cartao /n [3] 2x no cartao /n [4] 3x ou mais no cartao')
op = int(input('qual e a opcao: '))

d = vp - (vp * 0.10)
c = vp - (vp*0.05)
c3 = vp + (vp*0.20)

if op == 1:
    print('vc escolheu pagar a vista e o valor ficara R${:.2f}'.format(d))
elif op == 2:
    print('vc escolheu pagar a vista no cartao e o valor ficara R${:.2f}'.format(c))
elif op == 3:
    print('nao ha desconto, o valor sera R${:.2f} com parcelas de R${:.2f}'.format(vp, vp/2))
elif op == 4:
    print('vc escolheu pagar em 3x, e o valor sera R${:.2f} com parcelas de R${:.2f}'.format(c3, c3/3))