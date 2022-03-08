# Exercício 091:

'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.'''


from random import sample
from time import sleep

dados = dict()
print(' VALORES SORTEADOS '.center(30, '='))
for n in range(1, 5):
    dados[f'jogador{n}'] = sample(range(1, 7), 1)
for k, v in dados.items():
    print(f'O {k} tirou {v}.'.center(30))
    sleep(0.5)
print(' RANKING DOS JOGADORES '. center(30, '='))
c = 1
for i in sorted(dados, key=dados.get, reverse=True):
    print(f'{c}º lugar: {i} com {dados[i]}.'.center(30))
    sleep(0.5)
    c += 1
print('=' * 30)
