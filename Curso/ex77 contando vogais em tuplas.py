'''crie um programa que tenha uma tupla com varias palavras(nao usar acentos) depois disso, voce deve mostrar 
para cada palavra, quais sao as suas vogais'''

tupla = ('aprende', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar')

for palavras in tupla:
    print(f'\nem {palavras} tem ', end='')  
    for letra in palavras:
        if letra in 'aeiou':
            print(letra, end='')