from time import sleep

def contagem(n1,n2,r):
    print('-=-' * 15)
    cont = n1
    while cont != n2:
        if n1 < n2 and r < 0:
            print('impossible Run!!!')
            break
        elif n1 > n2 and r > 0:
            print('impossible Run!!!')
            break
        else:
            print(f'{cont}', end=' ')
            cont += r
            sleep(0.5)
    print(f'{n2} FIM!')
    print('-=-' * 15)

# programa principal
contagem(10,0,-2)
contagem(-2,3,1)
print('Agora e sua vez de personalizar a contagem!')
contagem(int(input('Inicio: ')),int(input('Fim: ')),int(input('Razao: ')))

