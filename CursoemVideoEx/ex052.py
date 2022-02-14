# Exercício 052:

'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

numero = int(input('Digite um número para testar se ele é um número primo:'))

soma = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        soma += 1
if soma == 2: # para ser um número primo ele só pode ser divisível por dois números, um e ele mesmo.
    print(f'Parabéns! O número {numero} é um número primo!')
else:
    print(f'O número {numero} não é um número primo!')
