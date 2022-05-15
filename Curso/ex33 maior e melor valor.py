# faca um programa uqe leia tres numeros e mmostre qual e o maior e qual eo menor.

print('digite 3 numeros: ')
n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o se num: '))
n3 = int(input('digite o terc num: '))

l = [n1, n2, n3]

print('o menor numero foi {}'.format(min(l)))
print('o maior numero foi {}'.format(max(l)))
print(sorted(l))
