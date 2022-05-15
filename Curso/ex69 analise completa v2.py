'''crie um programa que leia a idade e o sexo de varias pessoas.
a cada pessoa cadastrada, o programa devera perguntar se o USUARIO quer ou nao continuar.
no final, mostre:
A) quantas pessoas tem mais de 18 anos. // B) quantos homens foram cadastrados. // C) quantas mulheres tem menos de 20 anos. '''


print('*' * 20)
print('CADASTRO DE PESSOAS')
print('*' * 20)

homem = mulher = maior18 = menor20 = 0

while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'fm':
        sexo = str(input('SEXO [M/F]: ')).strip().lower()
    if sexo == 'm':
        homem += 1
    if sexo == 'f':
        mulher += 1
    if idade >= 18:
        maior18 += 1       
    if  idade <= 20 and sexo == 'f': 
        menor20 += 1
    resposta = ' '
    while resposta not in 'sn':
        resposta = str(input('Deseja continuar [S/N]: ')).strip().lower()
    if resposta == 'n':
        break

print(f'total de pessoas com mais de 18 anos: {maior18}')
print(f'homens cadastrados: {homem}')
print(f'mulheres cadastradas: {mulher}')
print(f'mulheres menor de 20 anos: {menor20}')