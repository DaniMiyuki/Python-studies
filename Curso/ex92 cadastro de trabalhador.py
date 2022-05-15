from datetime import date
from time import sleep

cadastro = {}
cadastroM = []
while True:
    print(F'{" ":<5}','CADASTRO')
    cadastro["nome"] = str(input('Nome: '))
    cadastro["nascimento"] = int(input('Ano de Nascimento: '))
    cadastro["ctps"] = int(input('Carteira de Trabalho (0 se nao tem): '))
    cadastro["contratacao"] = int(input('Ano de contratacao: '))
    cadastro["salario"] = float(input('Salario: R$'))
    cadastro["aposentadoria"] = (cadastro["contratacao"] +35) - (cadastro["nascimento"])
    cadastroM.append(cadastro.copy())
    print('-=-'*15)
    for key in cadastro.keys():
        sleep(1)
        if key == "nascimento":
            print(f'{key} tem o valor {(date.today().year)-(cadastro[key])}')
        elif cadastro["ctps"] == 0:
            break
        else:
            print(f'{key} tem o valor {cadastro[key]}')
    print('-=-'*15)
    pergunta = str(input('deseja fzr mais cadastro? [S/N] '))
    if pergunta in 'nN':
        break
print(cadastroM)