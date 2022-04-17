def area (larg, comp):
    a = larg * comp
    print(f'A area do terreno e {a} m²')


print('-=-' * 9)
print('   Controlre de Terrenos   ')
print('-=-' * 9)
l = float(input('Digite a largura [m]: '))
c = float(input('Digite a comprimento [m]: '))
area(l, c)
