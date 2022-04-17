vc = float(input('VALOR da casa: R$ '))
vs = float(input('Qual e o seu salario: R$ '))
f = int(input('Em quantos anos quer finaciar: '))
vp = vc / (f * 12)
minimo = vs * 30/100
print(f'Para pagar uma casa de {vc} em {f} anos a prestaçao é de {vp:.2f}')

if vp >= minimo:
    print("\033[;31m" 'EMPRÉSTIMO NEGADO' "\033[m")
else:
    print("\033[;34m" 'EMPRÉSTIMO APROVADO' "\033[m")
