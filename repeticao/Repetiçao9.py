from datetime import date
atual = date.today().year
totma = 0
totme = 0
for c in range(1, 8, 1):
    ano = int(input(f'Em que ano a {c}º pessoa nasceu: '))
    idade = atual - ano
    if idade >= 21:
        totma += 1
    else:
        totme += 1
print(f'{totma} pessoas e maior de idade ')
print(f'{totme} pessoas  e menor de idade ')

