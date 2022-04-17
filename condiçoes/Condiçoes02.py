from random import randint
from time import sleep
n = randint(0,5)
print('Jogo do advinha')
n1 = int(input('Digite um numero: '))
print('PROCESSANDO....')
sleep(2)
if n == n1:
    print('Voce acertou')
else:
    print('Voce errou')
    print(f'O numero correto e {n}')
