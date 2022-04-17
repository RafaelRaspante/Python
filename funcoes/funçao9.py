def fatorial(num, show=False):
    """
     -> Calcula o fatorial de um número.
     :param num: O número a ser calculado.
     :param show: (opcional) Mostrar ou não  a conta.
     :return: O valor do fatorial de um número num.
     """
    f = 1
    if show == True:
        for c in range(num, 1, -1):
            f *= c
            print(f'{c} X ', end='')
        print(f'1 = ', end='')
        return f
    if show == False:
        for c in range(num, 1, -1):
            f *= c
        return f'O fatorial de {num} é igual a {f}'


número = int(input('Digite o número que quer o calculo fatorial? '))
detalhe = input('Deseja resultado detalhado [S/N}? ').upper()[0]
while detalhe not in 'SN':
    detalhe = input('Deseja detalhado [S/N}? ').upper()[0]
if detalhe in 'Ss':
    detalhe = True
else:
    detalhe = False
print(fatorial(número, detalhe))
