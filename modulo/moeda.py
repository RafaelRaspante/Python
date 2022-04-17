def metade(num=0.0, formato=False):
    res = num / 2
    return res if not formato else moeda(res)


def dobro(num=0.0, formato=False):
    res = num * 2
    return res if not formato else moeda(res)


def aumentar(num=0.0, aum=0, formato=False):
    aumento = ((num * aum) / 100) + num
    return aumento if formato is False else moeda(aumento)


def diminuir(num=0.0, aum=0, formato=False):
    resultado = num - ((num * aum) / 100)
    return resultado if formato is False else moeda(resultado)


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:>8.2f}'.replace('.', ',')


def resumo(num=0, taxaa=10, taxar=5):
    print('~' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('~' * 30)
    print(f'Preço Analisado:\t{moeda(num)}')
    print(f'O Dobro do preço:\t{dobro(num, True)}')
    print(f'A metade do preço:\t{metade(num, True)}')
    print(f'{taxaa}% de aumento:\t\t{aumentar(num, taxaa, True)}')
    print(f'{taxar}% de redução:\t\t{aumentar(num, taxar, True)}')
    print('~' * 30)



