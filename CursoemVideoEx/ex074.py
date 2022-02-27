# Exercício 074:

'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a
listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''


# from random import randint
# tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
# print(f'Os valores sorteados foram: {tupla}')
# print(f'O maior valor sorteado foi: {max(tupla)} e o menor valor foi {min(tupla)}')

from random import sample
tupla = tuple(sample(range(10), 5))
print(f'Os valores sorteados foram: {tupla}')
print(f'O maior valor sorteado foi {max(tupla)} e o menor valor foi {min(tupla)}.')
