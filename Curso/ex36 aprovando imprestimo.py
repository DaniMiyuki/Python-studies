# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.Pergunte o valor da casa, o salario do comprador
# e em quantos anos ele vai pagar. a prestacao mensal, nao pode exceder 30% do salario ou entao o emprestimo e negado.

c = float(input('digite o valor da casa que deseja comprar: '))
s = float(input('digite o valor do salario: '))
i = int(input('digite sua idade: '))

id = 65 - i
p = c / (12 * id)
ps = s * 0.30

if p <= ps:
    print('parabens seu emprestimo foi aprovado e vc pagara {:.2f} por mes. durante {} anos'.format(p, id))
else:
    print('seu emprestimo foi negado!')