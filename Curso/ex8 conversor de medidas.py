# escreva um programa que leia um valor em metros e exiba convertido em cenimetros e milimetros.

m = float(input('digite uma medida: '))
print ('{} metros e {:.0f}mm, {:.0f}cm, {:.0f}dm, {:.1f}dam, {:.2f}hm, {:.3f}km '.format(m, m*1000, m*100, m*10, m*0.1, m*0.01, m*0.001))
