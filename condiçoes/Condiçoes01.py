n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A media do aluno e {m:.1f}')
if m >= 6.0:
    print('Esta acima da media')
else:
    print('Abaixo da media ')
