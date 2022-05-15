def metades(preço=0, formato=False):
    met = preço / 2
    return met if formato is False else moedas(met)

def dobros(preço=0, formato=False):
    dob = preço * 2
    return dob if formato is False else moedas(dob)

def aumenta(preço=0, taxa=0, formato=False):
    aum = preço + (preço*taxa/100)
    return aum if formato is False else moedas(aum)

def diminui(preço=0,taxa=0, formato=False):
    dim = preço - (preço*taxa/100)
    return dim if not formato else moedas(dim)

def moedas(preço = 0, moe = 'R$', formato=False):
    return f'{moe}{preço:.2f} '.replace(".", ",")

def resumo(preço=0, aum=0, dim=0):
    print('~'*30)
    print(F'{"RESUMO DO VALOR":^30}')
    print('~'*30)
    print(f'a metade de {moedas(preço)} é {metades(preço,True)} ')
    print(f'o dobro de {moedas(preço)} é {dobros(preço,True)} ')
    print(f'aumentando {aum}% é {aumenta(preço,aum,True)} ')
    print(f'diminuindo {dim}% é {diminui(preço,dim,True)} ')