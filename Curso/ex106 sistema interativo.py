c = ('')
def ajuda(com):
    help(com)


def titulo(msg, cor = 0):
    tam = len(msg)
    print('~' * tam)
    print(msg)
    print('~' * tam)


#programa principal
comando = ''
while True:
    titulo('Sistema de Ajuda PyHELP')
    comando = str(input('funcao ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Ate Logo')