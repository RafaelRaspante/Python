km = float(input('Digite quantos KM tem o percuso desejado:'))
if km <= 200:
    preco = km * 0.5
else:
    preco = km * 0.45
print(f'O valor da sua viagem e de {preco} reais')