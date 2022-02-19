# Exercício 060:

'''Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex: 5! = 5 * 4 * 3 * 2 * 1 = 120.'''


# Fazendo com o método interno do Python:

'''
from math import factorial

numero = int(input('Digite um número para saber seu fatorial:'))
fatorial = factorial(numero)
print(f'O fatorial de {numero} é {fatorial}.')
'''


# fazendo com "while":

'''
numero = int(input('Digite um número para saber seu fatorial:'))
contador = numero
fatorial = 1 # o número 1 é o elemento nulo da multiplicação
print(f'Calculando {numero}! = ', end="")
while contador > 0:
    print(f'{contador}', end="")
    print(' x ' if contador > 1 else ' = ', end='')  # restrição simplificada dentro de "print"
    fatorial *= contador
    contador -= 1
print(f'{fatorial}')
'''


# Fazendo com "for":

numero = int(input('Digite um número para saber seu fatorial:'))
contador = numero
fatorial = 1 # o número 1 é o elemento nulo da multiplicação
print(f'Calculando {numero}! = ', end="")
for contador in range (numero, 0, -1):
    print(f'{contador}', end="")
    print(' x ' if contador > 1 else ' = ', end='')  # restrição simplificada dentro de "print"
    fatorial *= contador
    contador -= 1
print(f'{fatorial}')
