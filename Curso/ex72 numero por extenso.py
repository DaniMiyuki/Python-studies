'''crie um programa que tenha uma tupla totalmente preenchida com contagem por extenso, de zero ate vinte.
seu programa devera ler um numero pelo teclado(entre 0 e 20) e mostra-lo porextenso'''

print(f'{"=" *20} LEITOR DE NUMERO {"="*20}')

n = int(input('digite um numero de [0 ~ 5]: '))
nextenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco')    
while 0 < n > 5:
    print('tente novamente!')
    n = int(input('digite um numero de [0 ~ 5]: '))
print(f'o numero digitado foi {nextenso[n]}')