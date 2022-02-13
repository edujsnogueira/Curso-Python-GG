# Exercício 037:

"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a
base da conversão:
- 1 para binário;
- 2 para octal; e
- 3 para hexadecimal."""

numero = int(input('Digite um numero inteiro a ser convertido para outra base:'))
base = int(input('Digite 1 para binário, 2 para octal e 3 para hexadecimal:'))
if base == 1:
    print(f'O número {numero} na base binária é {format(numero, "b")}!')
elif base == 2:
    print(f'O número {numero} na base octal é {format(numero, "o")}!')
elif base == 3:
    print(f'O número {numero} na base hexadecimal é {format(numero, "x")}!')
else:
    print('Você não digitou uma base válida!')
