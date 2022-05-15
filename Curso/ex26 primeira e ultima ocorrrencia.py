# faca um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra "A"
#em que posicao ela aporece a primeira vez
#           "        "      a ultima vez

nome = str(input('digite seu nome: ')).upper().strip()

print(' a letra A aparece {} vezes'.format(nome.count('A')))
print('a letra A aparece {} a primeira vez'.format(nome.find('A')))
print('a letra A aparece {} a primeira vez'.format(nome.rfind('A')))
