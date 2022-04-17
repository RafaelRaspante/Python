from random import randint
from time import sleep
computador = randint(0, 2)
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print(''' Suas opçãoes:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
opcao = int(input('Qual e sua jogada: '))
if opcao < 3:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('=-' * 13)
    print(f'O computador jogou {itens[computador]}')
    print(f'O Jogador jogou {itens[opcao]}')
    print('=-' * 13)
    if computador == 0:
        if opcao == 1:
            print('JOGADOR VENCEU')
        elif opcao == 2:
            print('COMPUTADOR VENCEU')
        else:
            print('EMPATE')
    elif computador == 1:
        if opcao == 0:
            print('COMPUTADOR VENCEU')
        elif opcao == 2:
            print('JOGADOR VENCEU')
        else:
            print('EMPATE')
    elif computador == 2:
        if opcao == 0:
            print('JOGADOR VENCEU')
        elif opcao == 1:
            print('COMPUTADOR VENCEU')
        else:
            print('EMPATE')
else:
    print('VALOR INVÁLIDO')


