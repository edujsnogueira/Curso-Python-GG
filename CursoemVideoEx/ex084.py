# Exercício 084:

'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

# Compliquei a solução colocando várias listas no início e tendo que realizar operações com elas. O ideal
# seria somente guardar o peso maior e menor em variáveis simples e depois varrer a lista comparando com os
# valores salvos.

# pessoas = []
# dados = []
# pesados = []
# leves = []
# while True:
#     dados.append(str(input('Digite o nome da pessoa: ')).strip().capitalize())
#     dados.append(float(input('Digite o peso da pessoa: ')))
#     pessoas.append(dados[:])
#     if len(pessoas) == 1:
#         maior = menor = dados[1]
#         leves.append(dados[0])
#         pesados.append(dados[0])
#     dados.clear()
#     continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
#     while continuar not in 'SN':
#         continuar = str(input('Comando inválido! Digite apenas [S/N]! ')).strip().upper()[0]
#     if continuar in 'N':
#         break
# for pessoa in pessoas:
#     if pessoa[1] > maior:
#         maior = pessoa[1]
#         pesados.clear()
#         pesados.append(pessoa[0])
#     elif pessoa[1] == maior:
#         pesados.append(pessoa[0])
#     elif pessoa[1] < menor:
#         menor = pessoa[1]
#         leves.clear()
#         leves.append(pessoa[0])
#     elif pessoa[1] == menor:
#         leves.append(pessoa[0])
# print(f'Foram cadastradas {len(pessoas)} pessoas ao todo.')
# print(f'O maior peso cadastrado foi de {maior} kg de {pesados}.')
# print(f'O menor peso cadastrado foi de {menor} kg de {leves}.')


# Solução mais simples:

pessoas = []
dados = []
pesados = []
leves = []
maior = menor = 0
while True:
    dados.append(str(input('Digite o nome da pessoa: ')).strip().capitalize())
    dados.append(float(input('Digite o peso da pessoa: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Comando inválido! Digite apenas [S/N]! ')).strip().upper()[0]
    if continuar in 'N':
        break
for pessoa in pessoas:
    if pessoa[1] == maior:
        pesados.append(pessoa[0])
    if pessoa[1] == menor:
        leves.append(pessoa[0])
print(f'Foram cadastradas {len(pessoas)} pessoas ao todo.')
print(f'O maior peso cadastrado foi de {maior} kg de {pesados}.')
print(f'O menor peso cadastrado foi de {menor} kg de {leves}.')
