'''crie um programa que leia dois valores e mostre um menu como o ao lado na tela:
seu programa devera realizar a operacao solicita em cada caso.
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa'''


n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))




while True:
    print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair do programa')
    op = int(input('qual a sua opcao: '))
    
    if op == 1:
        print(f'a soma de {n1} e {n2} e {n1 + n2}')
    elif op == 2:
        print(f'a multiplicacao de {n1} e {n2} e {n1 * n2}')
    elif op == 3:
        if n1 > n2:
            print(f'o maior valor entre {n1} e {n2} e {n1}')
        if n2 > n1:
            print(f'o maior numero entre {n1} e {n2} e {n2}')
        else:
            print(f'ambos sao iguas.')
    elif op == 4:
        n1 = int(input('digite o primeiro valor: '))
        n2 = int(input('digite o segundo valor: '))
    elif op == 5:
        print('finalizando programa....')
        break    
    else:
        print('opcao invalida!')  

'''from time import sleep
n1 = int(input("Digite o Valor 1: "))
n2 = int(input("Digite o Valor 2: "))
while True:
	print("\033[35m=\033[m"*53)
	sleep(1.5)
	print('QUADRO DE OPÇÕES
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS VALORES
[5] ENCERRAR PROGRAMA')
	print("QUAL A SUA OPÇÃO? ")
	op = int(input())
	if op == 1:
		print("O resultado de {} + {} = {}".format(n1, n2, n1+n2))
	elif op == 2:
		print("O resultado de {} × {} = {}".format(n1, n2, n1*n2))
	elif op == 3:
		print("O maior número entre {} e {} é {}".format(n1, n2, max(n1,n2)))
	elif op == 4:
		n1 = int(input("Digite o Valor 1: "))
		n2 = int(input("Digite o Valor 2: "))
	elif op == 5:
		print("Programa encerrado. Volte Sempre.^~^")
		break 
	else:
		print("Opção Inválida. Tente Novamente.")'''
        
