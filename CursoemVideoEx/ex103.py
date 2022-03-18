# Exercício 103:

'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um
jogador e quantos gols ele marcou. O programa deverá conseguir mostrar a ficha do jogador, mesmo que algum
dado não tenha sido informado corretamente.'''


def ficha(nome='desconhecido', gols=0):
    """
    => Função que exibe a ficha do jogador.
    :param nome: (opcional) exibe o nome do jogador.
    :param gols: (opcional) exibe quantos gols o jogador fez.
    :return: retorna o nome do jogador e a quantidade de gols.
    => Se nada for digitado o programa ainda deve apresentar resposta.
    """

    nome = str(input('Nome do jogador: ')).strip().capitalize()
    if not nome:
        nome = '<desconhecido>'
    gols = str(input('Número de gols: ')).strip()
    if not gols.isnumeric():
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


print(ficha())
