print('=' * 20)
print('10 termos de um PA')
print('=' * 20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (11 - 1) * razao
for c in range(primeiro, decimo, razao):
    print(c, end="➾ ")
print('ထ')
