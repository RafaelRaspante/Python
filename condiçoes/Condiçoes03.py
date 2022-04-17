print('Radar eletrônico')
v = float(input('Qual a velocidade do carro? '))
if v > 80:
    print(f'MULTADO! Voce excedeu o limite de 80KM/h. Voce foi multado em {(v - 80) * 7} R$')
print('Tenha um Bom dia dirija com seguraça')