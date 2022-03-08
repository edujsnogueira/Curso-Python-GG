# Exercício 090:

'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''


aluno = dict()
aluno['Nome'] = str(input('Digite o nome do aluno: ')).strip().capitalize()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO'
elif aluno['Média'] >= 5:
    aluno['Situação'] = 'RECUPERAÇÃO'
else:
    aluno['Situação'] = 'REPROVADO'
print('-=' * 20)
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
