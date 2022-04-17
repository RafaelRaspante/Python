peso = float(input('Qual é seu peso: '))
altura = float(input('Qual é sua altura: '))
iMC = peso / (altura ** 2)
print(f'Seu IMC é {iMC:.1f}')
if iMC < 18.5:
    print('Você está ABAIXO DO PESO ')
elif 18.5 <= iMC < 25:
    print('Você está PESO IDEAL')
elif 25 <= iMC < 30:
    print('Você está SOBREPESO')
elif 30 <= iMC < 40:
    print('Você está com OBSIDADE')
else:
    print('Você está com OBSIDADE MÒRBIDA')
