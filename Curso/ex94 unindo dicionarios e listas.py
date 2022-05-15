cadastro = {}
pessoas = []
soma = 0
mulheres = ' '
while True:
    cadastro["nome"] = str(input('nome: '))
    sexo = str(input('Sexo: [M/F] '))
    while sexo not in 'MmFf':
        print('ERRO!! Por favor, digite apenas M ou F.')
        sexo = str(input('Sexo: [M/F] '))
    cadastro["sexo"] = sexo   
    cadastro["idade"] = int(input('idade:' ))
    soma += cadastro["idade"]
    pessoas.append(cadastro.copy())

    pergunta = str(input('quer continuar? [S/N] '))
    while pergunta not in 'SsNn':
        print('ERRO!! Responda apenas S ou N.')
        pergunta = str(input('quer continuar? [S/N] '))
    if pergunta in 'Nn':
        break

print('-=-'*15)
print(pessoas)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')
media = (soma/len(pessoas))
print(f'B) A media de idade e de {media:.0f} anos')
for p in range(len(pessoas)):
    if pessoas[p]["sexo"] in 'Ff':
        mulheres += pessoas[p]["nome"]
print(f'C) As mulheres cadastradas foram {mulheres}')
print('D) Listas das pessoas acima da media:')
for cada_dic in pessoas:    # ---> cada_dic sera cada dicionario na lista pessoas
    if cada_dic["idade"] > media:
        print('primeira opcao, usando apenas IF')
        print(f'nome = {cada_dic["nome"]}; sexo = {cada_dic["sexo"]}; idade = {cada_dic["idade"]}')
        for key, valor in cada_dic.items():
            print('segunda opcao, usando FOR com items')
            print(f'{key} = {valor};', end=' ')
            

print('<<ENCERRADO>>')
