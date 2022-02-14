# Exercício 050:

'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digita do for ínpar, desconsidere-o.'''

soma = 0
contador = 0
for c in range(0, 6):
    numero = int(input('Digite um número inteiro:'))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print(f'A soma dos {contador} números pares digitados foi: {soma}.')
