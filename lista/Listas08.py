temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Digite seu nome: ')))
    temp.append(float(input("Digite seu peso: ")))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar [S/N]'))
    if resp in 'Nn':
        break
print(f'Ao todo, você cadastrou {len(princ)}')
print(f'O maior peso foi {mai} Kg.Peso de', end=' ')
for p in princ:
    if p[1] == mai:
        print(p[0], end=' ')
print()
print(f'O menor peso foi {men} KG', end=' ')
for p in princ:
    if p[1] == men:
        print(p[0], end=' ')

