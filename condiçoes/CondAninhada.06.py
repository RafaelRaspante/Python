from datetime import date
nascimento = int(input('ANO DE NASCIMENTO: '))
ano = date.today().year
idade = ano - nascimento

if idade <= 9:
    print(f'Esse acleta tem {idade} anos e sua categoria e MIRIM')
elif idade <= 14:
    print(f'Esse acleta tem {idade} anos e sua categoria e INFANTIL')
elif idade <= 19:
    print(f'Esse acleta tem {idade} anos e sua categoria e JÚNIOR')
elif idade <= 25:
    print(f'Esse acleta tem {idade} anos e sua categoria e SÊNIOR')
else:
    print(f'Esse acleta tem {idade} anos e sua categoria e MASTER')
    