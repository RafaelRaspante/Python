a = [int(input('Insira um número: ')) for i in range(0, 5)]
print(f'Foram digitados {len(a)} números!')
print(f'Em ordem decrescente {sorted(a, reverse=True)}')
print(f'O valor 5{" " if  5 in a else " não"} está na lista')
