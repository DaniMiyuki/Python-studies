def area(larg,comp):
    a = larg*comp
    print(f'A area de um terreno {larg:.1f} x {comp:.1f} e de {area}m2.')


#programa principal
print(f'{"Controle de terrenos":^50}')
print('=-='*15)
l = float(input('largura (m): '))
c = float(input('comprimento(m): '))
area(l,c)