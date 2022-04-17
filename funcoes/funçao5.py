from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 15)
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    sleep(.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(.5)
            cont += p
        print('FIM!!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(.5)
            cont -= p
        print('FIM!!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 15)
print('Agora e sua vez!!! :)')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
