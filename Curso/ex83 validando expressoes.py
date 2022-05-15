#crie um programa onde o usuario digite uma expressao qualquer que
#use parenteses.seu aplicativo devera analisar se a expressao
#passada esta com os parenteses abertos e fechados na ordem correta...


expressao = str(input('digite uma expressao: '))
if expressao.count('(') != expressao.count(')'):
    print('expressao incorreta, faltam completar o "()" !!')
else:
    print('expressao correta')


'''

expr = str(input('digite expressao: ')
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) >0:    
        pilha.pop()
    else:
        pilha.append(')')
        break
if le(pilha) == 0:
    print('expressao valida')
else:
    print('invalida')

'''