somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'========== {p}º PESSOA ==========')
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Qual e sua idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A media da idades do grupo e {mediaidade} anos')
print(f'O homem mais velho e {nomevelho} e sua idade e {maioridadehomem}')
print(f'Ao todo sao {totmulher20} mulheres com menos de 20 anos')