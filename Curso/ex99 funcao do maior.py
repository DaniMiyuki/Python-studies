def analisador(*num):
    print('-=-' * 15)
    print('Analisando os valores digitados...')
    for cada_numero in num:
        print(cada_numero, end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) > 0:
        print(f'O maior numero informado foi {max(num)}!')
    


# programm principal
analisador(2,9,4,5,7,1)
analisador(4,7,0)
analisador()

''' resolucao professor:
def analisador(*num):
    cont = maior = 0
    print('-=-' * 15)
    print('Analisando os valores digitados...')
    for cada_numero in num:
        print(cada_numero, end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior numero informado foi {maior}!')
    

# programm principal
analisador(2,9,4,5,7,1)
analisador(4,7,0)
analisador()
'''