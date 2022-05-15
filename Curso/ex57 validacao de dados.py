# faca um programa que leia o sexo de uma pesoa,
# mas so aceite valores 'M' e 'F'.
#caso esteja errado, peca a digitacao novamente ate ter um valor correto.

sexo = str(input('sexo [F/M]: ')).lower().strip() [0] # o 0 eh para mostrar a primeira letra caso a pessoa digite a palavara inteira (masculino)

while sexo != 'm' and sexo!= 'f':   
    sexo = str(input('digite o valor corretamente: '))
print(f'vc digitou [{sexo.upper()}] e seu dado foi registrado com sucesso')