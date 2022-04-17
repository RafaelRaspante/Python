expressao = str(input('Digite a expressão: '))
for char in expressao:
    if char == '(':
        abre_p += 1
    if char == ')':
        fecha_p += 1
if abre_p == fecha_p:
    print('Expressão Válida!')
else:
    print('Expressão Inválida')