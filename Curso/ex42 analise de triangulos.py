# refaca o desafio 35 doa triangulos acrescentando o recurso de mostrar que tipo de triangulo sera formado:
#equilatero: todos os lados iguais
#isosceles dois lados iguais
#escalenos todos os lado diferentes

s1 = float(input('digite primeira medida: '))
s2 = float(input('digite seg mediada: '))
s3 = float(input('digite a ter media: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == s2 == s3:
        print('formara um triangulo EQUILATERO')
    elif s1 == s2 !=s3 or s1 == s3 != s2 or s2 == s3 != s1:
        print('forma um triangulo isosceles')
    elif s1 != s2 != s3:
        print('formara um triangulo escaleno')
else:
    print('n forma um triangulo')
    