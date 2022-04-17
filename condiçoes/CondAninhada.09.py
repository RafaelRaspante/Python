valor = float(input('Qual e o valor do produto: '))
print('''FORMAS DE PAGAMENTO:
[1] Á vista dinheiro/cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Digite umas das opçoes acima: '))

if opcao == 1:
    total = valor - (valor * 0.10)
    print(f'Sua compra de R${valor:.2f} vai custar R${total}')
elif opcao == 2:
    total = valor - (valor * 0.05)
    print(f'Sua compra de R${valor:.2f} vai custar R${total}')
elif opcao == 3:
    total = valor
    parcela = total / 2
    print(f'Sua compra  sera parcelada de 2x de R${parcela:.2f} e de R${total:.2f} SEM JUROS')
elif opcao == 4:
    totaldeparcelas = int(input('Quantas parcelas? '))
    total = valor + (valor * 0.20)
    vdaparcela = total / totaldeparcelas
    print(f'Sua compra sera parcelada de {totaldeparcelas}x de R${vdaparcela:.2f} COM JUROS')
    print(f'Sua compra de R${valor:.2f} vai custar R${total:.2f}')
else:
    print("\033[;31m"'COMANDO INVÀLIDO'"\033[m")
    