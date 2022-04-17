frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count("A")}')
print(f'A letra A apareceu a primeira vez na posição: {frase.find("A")+1}')
print(f'A letra A apareceu a ultima vez na posição: {frase.rfind("A")+1}')