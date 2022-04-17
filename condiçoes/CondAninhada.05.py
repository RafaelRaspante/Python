n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a media e {media:.1f} ')
if media < 5:
    print('O aluno está ' "\033[;31m"'REPROVADO'"\033[m")
elif 7 > media >= 5:
    print('O aluno está ' "\033[;33m"'RECUPERAÇAO'"\033[m")
elif media >= 7:
    print('O aluno está ' "\033[;32m"'APROVADO'"\033[m")