#faca um programa que jogue par ou impar com o computador.o jogo so sera interrompido quando 
# o jogador PERDER mostrando o total de vitorias consecutivas que ele conquistou no final do jogo,

from random import randint
soma = cont = 0

while True:
    computador = randint(1,10)
    n = int(input('digite um valor: '))
    resposta = str(input('par ou impar [P/I]: ')).strip().lower()
    total = (computador + n)
    
    if total % 2 == 0:
        print(f'vc jogou {n} e o computador {computador}.total foi {total} e deu PAR')
        if resposta == 'p':
            print('vc venceu!!!')
            print('vamos jogar novamente!!!')
        else:
            print('vc perdeu!!')
            break
    else:
        print(f'vc jogou {n} e o computador {computador}.total foi {total} e deu IMPAR')
        if resposta == 'i':
            print('vc venceu!!!')
            print('vamos jogar novamente!!!')
        else:
            print('vc perdeu!!')
            break
    cont += 1
print(f'game over!! vc venceu {cont}')