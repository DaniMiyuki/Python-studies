# crie um programa que leia daus notas de um aluno e calcule sua media,
#mostrando uma mensagem no final, de acordo com a media atingida:
#media abaixo de 5.0: reprovado
#media entre 5.0 e 6.9: recuperacao:
# media 7.0 ou superior: aprovado

nota1 = float(input('digite sua primeira nota: ')) 
nota2 = float(input('digite sua seg nota: '))

res = (nota1 + nota2)/2

if res < 5.0:
    print('sua nota e {} e vc foi reprovado'.format(res))
elif 7.0 > res >= 5:
    print('sua nota e {} e vc esta de recuperacao.'.format(res))
elif res >= 7.0:
    print('sua nota e {} e foi aprovado'.format(res))
