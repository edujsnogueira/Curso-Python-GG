# Exercício 030:

# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

numero = int(input('Digite um número inteiro:'))
if numero % 2 == 0:
    print(f'Você digitou o número {numero} que é par!')
else:
    print(f'Você digitou o número {numero} que é ímpar!')
