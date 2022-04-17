try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que voce digitou')
except ZeroDivisionError:
    print('Nao e possivel dividir um numero por 0')
except KeyboardInterrupt:
    print('O usuario nao quis informar os dados')
except Exception as erro:
    print(f'O erro encontado foi {erro.__cause__}')
else:
    print(f'O resulado e {r:.1f}')
finally:
    print('Volte sempre muito obrigado')