# Exercício 055:

'''Faça um program que leia o peso de cinco pessoas e ao final mostre qual foi o maior e o menor peso lido.'''


'''
# Solução complicada fazendo por loop

maior = 0
menor = 0
for contador in range(1, 6):
    peso = float(input(f'Digite o peso da {contador}ª pessoa em kg:'))
    if contador == 1: # isso aqui é uma solução para não ter que atribuir um número muito alto ao inicializar o menor.
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso digitado foi Kg {maior} e o menor peso foi Kg {menor}.')
'''

# Solução muito mais simples fazendo por listas:

lista = []  # lista vazia
for contador in range(1, 6):
    peso = float(input(f'Digite o peso da {contador}ª pessoa em kg:'))
    lista += [peso]   # adiciona os valores de peso na lista
print(f'O maior peso digitado foi Kg {max(lista)} e o menor peso digitado foi Kg {min(lista)}')
