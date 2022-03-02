# Exercício 087:

'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

pares = terceira = segunda = 0
matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para a posição [{l, c}]: ')))
print('-=' * 25)
for l in range(0, 3):
    terceira += matriz[l][2]
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if matriz[1][c] > segunda:
            segunda = matriz[1][c]
        print(f'[{matriz[l][c]:^6}]', end='')
    print()
print('-=' * 25)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {terceira}.')
print(f'O maior valor da da segunda linha é {segunda}.')
