from datetime import date
nasacimento = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasacimento
print(f'Quem nasceu em {nasacimento} tem {idade} anos em {atual}')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda falta {saldo} anos para o alistamento')
    ano = atual + saldo
    print(f'Seu ano de alistamento e {ano}')
elif idade > 18:
    saldo = idade - 18
    print(f'Seu alistamento ja passou {saldo} anos')
    ano = atual - saldo
    print(f'Seu ano de alistamento foi em {ano}')






