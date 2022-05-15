# crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiusculas e minusculas
#quantas letras ao todo (sem considerar espacos)
#quantas letras tem o primeiro nome.

n = str(input('digite seu nome completo: ')).strip()
print('lmaiu {}'.format(n.upper()))
print('lminus {}'.format(n.lower()))
print('qunt de letra e {}'.format(len(n)-n.count(' ')))
s = n.split()
print('o prim nome tem {} letras'.format(len(s[0])))