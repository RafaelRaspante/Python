number=[ ]
for count in range(0, 5):
    number.append(int(input(f'Digite um número na posição {count}: ')))
print()
maior=max(number)
menor=min(number)
print(f'Os Valores Digitados Foram {number}')
print(f'O maior número é {maior} está na posição ', end='')
for i, v in enumerate(number):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor número é {menor} está na posição ', end='')
for i, v in enumerate(number):
    if v == menor:
        print(f'{i}...', end='')
print()
