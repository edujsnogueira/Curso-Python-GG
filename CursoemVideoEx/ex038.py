# Exercício 038:

"""Esrcreva um program que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- o primeiro valor é maior;
- o segundo valor é maior; ou
- não exite valor maior, os dois são iguais."""

numero1 = int(input('Digite o primeiro número inteiro:'))
numero2 = int(input('Digite o segundo número inteiro:'))
print(f'O primeiro número digitado foi {numero1} e o segundo número digitado foi {numero2}.')
if numero1 > numero2:
    print('O primeiro valor é maior.')
elif numero1 < numero2:
    print('O segundo valor é maior.')
else:
    print('Não exite valor maior, os dois valores são iguais.')
