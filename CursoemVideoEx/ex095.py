# Exercício 095:

'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador.'''


aproveitamento = dict()
gols = list()
jogadores = list()
while True:
    print('-=' * 30)
    aproveitamento['nome'] = str(input('Digite o nome do jogador: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou? '))
    for p in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {p + 1}? ')))
    aproveitamento['gols'] = gols[:]
    aproveitamento['total'] = sum(gols)
    jogadores.append(aproveitamento.copy())
    gols.clear()
    continuar = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida! Quer continuar? [S/N]:')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print('cod'.center(5), 'nome'.center(15), 'gols'.center(30), 'total'.center(5))
for chave, valor in enumerate(jogadores):
    print(f'{(chave + 1):^5} {valor["nome"].center(15)} {str(valor["gols"]).center(30)} {valor["total"]:^5}')
print('-=' * 30)
while True:
    busca = int(input('Digite o código do jogador que deseja detalhar? (999 para sair) '))
    if busca == 999:
        break
    if busca - 1 >= len(jogadores):
        print('Opção inválida! O código deve estar na lista ou ser 999 para sair!')
    else:
        print(f'  Levantamento do Jogador: {jogadores[busca - 1]["nome"]}  '.center(60, '-'))
        for i, g in enumerate(jogadores[busca - 1]["gols"]):
            print(f'- No jogo {i + 1} fez {g} gols.')
    print('-=' * 30)
print('  Volte sempre!  '.center(60))
