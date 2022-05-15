#escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a base de conversao
#1 para bianrio
#2 para octal
#3 para hexadecimal

n = int(input('digite um numero: '))
print('''escolha uma das bases para conversao:
[1] para binario
[2] para octal
[3]  para hexadecimal
''')
opcao = int(input('digite uma opcao: '))
if opcao == 1:
    print('em binario e igual a {}'.format(bin(n)))
elif opcao == 2:
    print('convertendo para octal sera  {}'.format(oct(n)))    
elif opcao == 3:
    print('em hexadeciamal sera {}'.format(hex(n)))    
