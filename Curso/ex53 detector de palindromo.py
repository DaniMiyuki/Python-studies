# crie um programa que leia uma frase qualquer e diga se ela e um palindromo, desconsiderando os espacos.

f = str(input('digite uma frase: ')).upper()
a = f.strip().split()
x = ''.join(a)
inverso = x[::-1]  # : ~dois pontos comeca no inicio : ~dois pontos termina no fim e o um negativo VOLTA de 1 em 1
                      #podem ser substituidas por :
                      #inverso = ''
                      #for letra in range(len(x) -1,-1,-1): 
                      #    inverso += x [letra]
if inverso == x:
        print ('o inverso e \"{}\" entao e um palindromo'.format(f))
else:
        print('\"{}\" nao e um palindromo')