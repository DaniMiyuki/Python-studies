from modi107 import moeda
n = float(input('digite o preço: R$'))
print(f'a metade de R${n:.2f} é R${moeda.metade(n):.2f} ')
print(f'o dobro de R${n:.2f} é R${moeda.dobro(n):.2f} ')
print(f'aumentando 10% é R${moeda.aumentar(n,10):.2f} ')
print(f'diminuindo 13% é R${moeda.diminuir(n,13):.2f} ')