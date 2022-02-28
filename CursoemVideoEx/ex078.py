# Exercício 078:

'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior
e o menor valor digitado e as suas respectivas posições na lista.'''

valores = []
for pos in range(1, 6):
    valores.append(int(input(f'Digite um valor para a posição {pos}: ')))
print(valores)
maior = max(valores)
menor = min(valores)
maiores = []
menores = []
for pos, valor in enumerate(valores):
    if valor == maior:
        maiores.append(pos + 1)
    if valor == menor:
        menores.append(pos + 1)
print(f'O maior valor digitado foi {maior} nas posições {maiores}.')
print(f'O menor valor digitado foi {menor} nas posições {menores}.')
