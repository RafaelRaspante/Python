print('-=' * 13)
print('ANALIZADOR DE TRIÂNGULOS')
print('-=' * 13)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b+c and b < a+c and c < a+b:
    print('PODE formar um Triângulo')
    if a == b == c:
        print('Equilátero')
    elif a != b != c != a:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('NÃO PODE formar um Triângulo')