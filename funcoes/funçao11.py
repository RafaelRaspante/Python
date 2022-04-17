def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31m ERRRO! Digite um numero inteiro valido. \033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')