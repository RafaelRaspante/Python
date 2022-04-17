aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Media de {aluno["Nome"]}: '))
if aluno['Media'] >= 7:
    aluno['Situaçâo'] = 'Aprovado'
elif 5<= aluno['Media'] < 7:
    aluno['Situaçâo'] = 'Recuperação'
else:
    aluno['Situaçâo'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} e igual a {v}')
