# Exercício 094:

'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas;
B) A média de idade;
C) Uma lista com as mulheres;
D) Uma lista de pessoas com idade acima da média.'''

pessoas = list()
pessoa = dict()
mulheres = list()
soma = media = 0
while True:
    pessoa['nome'] = str(input('Digite o nome: ')).strip().capitalize()
    pessoa['sexo'] = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Opção inválida! Digite o sexo [M/F]: ')).strip().upper()[0]
    if pessoa['sexo'] in 'F':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Digite a idade: '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())
    continuar = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida! Quer continuar? [S/N]:')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print(f'O grupo tem {len(pessoas)} pessoas.')
media = soma / len(pessoas)
print(f'A média de idades é {media:.1f} anos.')
print(f'As mulheres cadastradas foram: {mulheres}.')
print('Lista das pessoas acima da média:')
for n in range(0, len(pessoas)):
    if pessoas[n]['idade'] > media:
        print(pessoas[n])
print('-=' * 30)
