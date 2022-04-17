soma = 0
cont = 0
for c in range(1, 7):
    nun = int(input("Digite um numero: "))
    if nun % 2 == 0:
        cont += 1
        soma += nun
print(f'A soma dos {cont} numeros pares e {soma}')