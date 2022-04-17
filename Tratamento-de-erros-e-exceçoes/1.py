def leiaInt(entry="0"):
    while True:
        try:
            entry = input('NÚMERO INTEIRO: ')
            if entry.isnumeric() == True:
                print('ENTRADA ACEITA')
                return entry
            elif entry.isnumeric() == False:
                print('ENTRADA RECUSADA')
                continue
        except (TypeError, ValueError):
            print('ENTRADA RECUSADA')
            continue
        except KeyboardInterrupt:
            print()
            print('O Usuário não quis informar os dados')
            return entry


def leiaFloat(entry="0"):
    while True:
        try:
            entry = input('NÚMERO REAL: ')
            if ((entry.replace(',', '')).replace('.', '')).strip().isnumeric() == False:
                print('ENTRADA RECUSADA: ')
                continue
            entry = float(entry.replace(',', '.'))
            print('ENTRADA ACEITA')
            return entry
        except (TypeError, ValueError):
            print('ENTRADA RECUSADA')
            continue
        except KeyboardInterrupt:
            print()
            print('O Usuário não quis informar os dados')
            return entry



print(f'O número inteiro digitado foi: {leiaInt()} e o número real foi {leiaFloat()}')