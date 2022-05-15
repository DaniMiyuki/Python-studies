'''crie um programa que simule o funcionamento de um caixa eletronico
no inicio, pergunte ao usuario qual sera o VALOR A SER SACADO(numero inteiro)
e o programa vai informar quantas cedulas de cada valor serao entregues.'''

print('{:^30}'.format('BANCO KANE'))
valor = int(input('qual o valor que deseja sacar: '))
while True:
    if valor >= 50:
        n1 = valor // 50
        n1resto = valor % 50
        valor = n1resto
        print(f'total de {n1} cedulas de R$50') 
        if n1resto == 0:
            break        
    if valor >= 20:
        n2 = valor // 20
        n2resto = valor % 20
        valor = n2resto
        print(f'total de {n2} cedulas de R$20')
        if n2resto == 0:
            break            
    if valor >= 10:
        n3 = valor // 10
        n3resto = valor % 10
        valor = n3resto
        print(f'total de {n3} cedulas de R$10')
        if n3resto == 0:
            break                
    else:
        print(f'total de {valor} cedulas de R$1')
        break            
print('VOLTE SEMPRE AO BANCO KANE!!')

'''
            OUTRA FORMA DE ESCREVER
valor = int(input('qual o valor que deseja sacar: '))
total = valor
cedula = 50
totced = 0
while True*
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula ==20:
            cedula = 10
        elif cedula == 10
            cedula = 1
        totced = 0
        if total == 0:
            break
print('volte sempre')

            OUTRA FORMA com FOR
valor = int(input('qual o valor que deseja sacar: '))
for nota in [50, 20, 10, 1]
    quantidade = valor // nota
    valor = valor % nota
    if quantidade > 0:
    print(f'Total de {totced} cedulas de R${cedula}')    
'''