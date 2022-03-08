# Exercício 093:

'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

aproveitamento = dict()
gols = list()
aproveitamento['nome'] = str(input('Digite o nome do jogador: ')).strip().capitalize()
partidas = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou? '))
for p in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {p + 1}? ')))
aproveitamento['gols'] = gols[:]
aproveitamento['total'] = sum(gols)
print('-=' * 30)
print(aproveitamento)
print('-=' * 30)
for k, v in aproveitamento.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {aproveitamento["nome"]} jogou {partidas} partidas.')
for n in range(1, len(gols) + 1):
    print(f' => Na partida {n}, fez {gols[n - 1]} gols.')
print(f'Foi um total de {aproveitamento["total"]} gols.')
print('-=' * 30)
