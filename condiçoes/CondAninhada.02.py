num = int(input('Digite um número inteiro: '))
print('''Escolha umas das bases para conversão
[1] para converter para BINÁRIO
[2] para converter para OCTAL
[3] para converter para HEXADECIMAL''')
opçao = int(input('Sua opção e: '))
if opçao == 1:
    print(f'{num} convertido para BINÁRIO é {bin(num)[2:]}')
elif opçao == 2:
    print(f'{num} convertido para OCTAL é {oct(num)[2:]}')
elif opçao == 3:
    print(f'{num} convertido para HEXADECIMAL é {hex(num)[2:]}')
else:
    print("\033[;31m" 'COMANDO INVÁLIDO'"\033[m")