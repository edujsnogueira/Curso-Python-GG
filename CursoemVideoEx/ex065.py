# Exercício 065:

'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar se o usuário quer ou não
continuar a digitar mais valores.'''

novo = 'S'
lista = []
while novo == 'S':
    numero = int(input('Digite um número inteiro: '))
    lista.append(numero)
    novo = str(input('Quer digitar outro número [S/N]: ')).strip().upper()[0]
print(f'Você digitou {len(lista)} números, a média foi {sum(lista)/len(lista):.2f}, o maior foi {max(lista)} e o '
      f'menor foi {min(lista)}.')
