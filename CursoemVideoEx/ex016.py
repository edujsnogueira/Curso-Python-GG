# Exercício 016:

# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

# import math
# num = float(input('Digite um número real qualquer:'))
# print(f'O número digitado foi {num} e a sua parte inteira é {math.trunc(num)}.')

# Uma alternativa é importar somente a função que é utilizada e não o pacote todo. Nesse caso, lembrar de
#  só fazer referência para a função importada:

# from math import trunc
# num = float(input('Digite um número real qualquer:'))
# print(f'O número digitado foi {num} e a sua parte inteira é {trunc(num)}.')

# A maneira mais simples nem demandaria a importação de nenhuma biblioteca:

num = float(input('Digite um número real:'))
print(f'O número digitado foi {num} e a sua parte inteira é {int(num)}.')
