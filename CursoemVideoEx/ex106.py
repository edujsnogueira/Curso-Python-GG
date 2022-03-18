# Exercício 106:

'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual
vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.'''

from time import sleep

cores = (
    '\033[m', # sem cor = 0
    '\033[0;30;41m', # fundo vermelho = 1
    '\033[0;30;42m', # fundo verde = 2
    '\033[0;30;43m', # fundo amarelo = 3
    '\033[0;30;44m', # fundo azul = 4
    '\033[0;30;45m', # fundo magenta = 5
    '\033[0;30;46m', # fundo ciano = 6
    '\033[0;30;47m'  # fundo branco = 7
        )


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(cores[7], end='')
    help(com)
    print(cores[0], end='')
    sleep(1)


def título(msg, cor=0):
    print(cores[cor], end='')
    tam = len(msg) + 4
    print('~' * tam)
    print(msg.center(tam))
    print('~' * tam)
    print(cores[0], end='')
    sleep(1)


# Programa principal:
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP!', 2)
    comando = str(input('Escolha uma função ou biblioteca para receber ajuda: ')).strip()
    if comando.upper() in 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)
