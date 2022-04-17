value = list()
for cont in range(0, 5):
    value.append(int(input('Digite um valor: ')))

for c, v in enumerate(value):
    print(f'Na posiçao {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')