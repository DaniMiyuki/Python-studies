'''crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista.
   caso o numero ja exista la dentro, ele nao sera adicionado.no final, serao exibidos todos os valores uicos digitados, em ordem crescente'''

lista = []
while True:
    n = int(input('digite um numero: '))
    if n not in lista:
        lista += [n]
        print('valor adicionado com sucesso!!!')
    else:
        print('valor duplicado, nao sera adicionado na lista...')
        continue
    denovo = str(input('deseja continuar [S/N]? ')).strip().lower()
    if denovo == 's':
        pass
    else:
        break
lista.sort()
print(f'a lista e {lista}')