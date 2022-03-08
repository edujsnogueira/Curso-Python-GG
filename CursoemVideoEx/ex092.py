# Exercício 092:

''' Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import date

inss = dict()
inss['nome'] = str(input('Digite o nome: ')).strip().capitalize()
hoje = date.today().year
ano = int(input('Digite o ano de nascimento: '))
inss['idade'] = hoje - ano
inss['ctps'] = int(input('Digite o nº da carteira de trabalho (0 para não tem): '))
if inss['ctps'] != 0:
    inss['contrato'] = int(input('Digite o ano de contratação: '))
    inss['renda'] = float(input('Digite o salário R$: '))
    inss['aposentadoria'] = inss['contrato'] + 35 - ano
print('-=' * 30)
for k, v in inss.items():
    print(f'{k} tem o valor {v}.')
print('-=' * 30)
