# Exercício 089:

'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente.'''


boletim = []
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = float(f'{(nota1 + nota2) / 2:.1f}')
    boletim.append([nome, nota1, nota2, media])
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida! Quer continuar? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break
print('-=' * 20)
print('BOLETIM'.center(40))
print('Nº'.center(5), 'NOME'.center(28), 'MÉDIA'.center(5))
print('-=' * 20)
for c in range(0, len(boletim)):
    print(f'{c:^5} {boletim[c][0].center(28)} {boletim[c][3]:^5}')
print('-=' * 20)
while True:
    notas = int(input(f'Mostrar notas de qual aluno? Escolha entre 0 e {len(boletim) - 1}, ou 999 para interromper: '))
    if notas == 999:
        print('Finalizando...')
        break
    elif 0 <= notas < len(boletim):
        print(f'As notas de {boletim[notas][0]} são {boletim[notas][1]} e {boletim[notas][2]}.')
    else:
        continue
print(' VOLTE SEMPRE! '.center(40, '-'))
