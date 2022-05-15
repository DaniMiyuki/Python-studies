# faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivivo e todas as informacoes possiveis sobre ela

a = input('digite algo')
print('o tipo primitivo desse valor e ', type(a))
print('so tem espacos? ', a.isspace())
print('e um numerico? ', a.isnumeric())
print('e alfabetico? ', a.isalpha())
print('e alfanumerico? ', a.isalnum())
print('e identificavel? ', a.isidentifier())