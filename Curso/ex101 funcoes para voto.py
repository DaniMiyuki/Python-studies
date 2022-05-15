from datetime import date

def voto(nasc):    
    idade = (date.today().year) - nasc 
    if 18 <= idade <= 65:
        print(F'    Com {idade} anos: VOTO OBRIGATORIO.')
    elif idade < 18:
        print(f'      com {idade} anos: NAO VOTA.')
    else:
        print(f'     com {idade} anos: voto opcional')
    print()


#programa principal
print()
print('~.~'*12)
print(f'{"Verificacao para votar":^36}')
print('~.~'*12)
voto(int(input('      Ano de nascimento: ')))


'''
# USANDO RETURN
def voto(nasc):
    from datetime import date    
    idade = (date.today().year) - nasc 
    if 18 <= idade <= 65:
        return(F'    Com {idade} anos: VOTO OBRIGATORIO.')
    elif idade < 18:
        return(f'      com {idade} anos: NAO VOTA.')
    else:
        return(f'     com {idade} anos: voto opcional')
    print()


#programa principal
print()
print('~.~'*12)
print(f'{"Verificacao para votar":^36}')
print('~.~'*12)
pergunta =int(input('      Ano de nascimento: '))
print(voto(pergunta))
'''