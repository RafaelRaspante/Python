sal = float(input('Qual e o salario do empregado: R$ '))
if sal <= 1250.00:
    sal = sal + (sal * 15/100)
else:
    sal = sal + (sal * 10/100)
print(f'O novo salario do empregador e R$ {sal}')