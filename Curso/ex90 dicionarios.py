aluno = {}

while True:
    aluno['nome'] = str(input('nome: '))
    aluno['media'] = float(input(f'media de {aluno["nome"]}: '))    
    print('.・'*10)
    print(f'nome: {aluno["nome"]}')
    print(f'media: {aluno["media"]}')
    if aluno["media"] <= 5:
        aluno['situacao'] = 'reprovado'
    elif 5 < aluno["media"] < 7:
        aluno['situacao'] = 'recuperacao'
    else:
        aluno['situacao'] = 'aprovado'
    print(f'situacao de {aluno["nome"]}: {aluno["situacao"]}')
    print('.・'*10)
    print()
    print('=-'*15)
    pergunta = str(input('adicionar mais boletim? [S/N] '))
    if pergunta in 'Nn':
        break
    print('=-'*15)
    print()


'''aluno = dict()
aluno['nome'] = str(input('nome: '))
aluno['media'] = float(input(f'media de {aluno["nome"]}'))
if aluno["media"] <= 5:
        aluno["situacao"] = 'reprovado'
elif 5 < aluno["media"] < 7:
    aluno["situacao"] = 'recuperacao'
else:
    aluno["situacao"] = 'aprovado'
print('-='*30)
for k, v in aluno.items():
    print(f' - {k} e igual a {v}')
'''

'''
aluno = {'nome': str(input('Nome: '))}
aluno['média'] = float(input(f'Digite a média de {aluno["nome"]}: '))
aluno['situação'] = 'aprovado' if aluno['média'] >= 7 else 'reprovado' if aluno['média'] <6 else 'recuperação'
for key, value in aluno.items():
	print(f'{key}:', value)
'''