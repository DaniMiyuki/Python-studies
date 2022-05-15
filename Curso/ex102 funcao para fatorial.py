
def fatorial(n, show=False):
    c = 1
    for x in range(n, 0, -1):
        print(f'{x}', end='')
        if x > 1:
            print(' x ', end='')
        c*=x
    return f' = {c}'


# programa principal
print('=.'*15)
print(F'{"FATORANDO":^30}')
print('=.'*15)
print(fatorial(int(input('digite um nunmero: ')), show=True))
