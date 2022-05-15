def leiaInt(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric():
            print(f'vc acabou de digitar o numero {num}')
            break          
        else:
            print('Erro! Digite um número inteiro válido.')   


# programa principal:
num = leiaInt('digite um numero: ')
