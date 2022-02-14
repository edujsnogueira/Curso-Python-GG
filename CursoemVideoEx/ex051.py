# Exercício 051:

'''Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética.
No final, mostre os dez primeiros termo dessa progressão.'''

primeiro = int(input('Digite o primeiro termo de uma progressão aritmética:'))
razao = int(input('Digite a razão da progressão aritmética'))
soma = primeiro
print(f'O 1° termo é {soma}.')
for c in range(2, 11):
    soma += razao
    print(f'O {c}° termo é {soma}.')
