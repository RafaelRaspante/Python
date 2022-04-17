from math import hypot
co = int(input('Qual e o cateto oposto: '))
ca = int(input('Qual e o cateto adjacente: '))
h = hypot(co,ca)
print(f'O cateto oposto e {co} o cateto ajacente e {ca} e a Hipotenusa e {h:.2f}')