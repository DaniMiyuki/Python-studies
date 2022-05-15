def leiaDinheiro(resposta):
    while True:
        resposta = float(input('digite um valor: '))
        if type(resposta) != float or int:
            print('valor invalido!!digite novamente!')
        else:
            return resposta