# crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome "santo".

c = str(input('digite sua ciade natal: ')).strip()
print(c[:5].upper == 'SANTO')