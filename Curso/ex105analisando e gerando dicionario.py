def notas(*num, sit=False):
    aprovacao={}
    aprovacao['total'] = len(num)
    aprovacao['maior'] = max(num)
    aprovacao['menor'] = min(num)
    aprovacao['media'] = sum(num)/len(num)

    if sit == True:
        if aprovacao['media'] < 7:
            aprovacao['situacao'] = 'RUIM'
        if aprovacao['media'] >= 7 or aprovacao['media'] <= 9:
            aprovacao['situacao'] = 'BOM'
        else:
            aprovacao['situacao'] = 'ÓTIMO'

    return aprovacao
    


#programa principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)