# Exercício 045:

"""Crie um program que faça o computador jogar jokenpô com você!"""

print('Vamos jogar JOKENPÔ? \nVocê deve escolher PEDRA, PAPEL ou TESOURA!')
lista = ['PEDRA', 'PAPEL', 'TESOURA']
import random
computador = random.choice(lista)
jogador = str(input('O computador já escolheu! Qual é a sua escolha?')).strip().upper()
if jogador in lista:
    from time import sleep
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ!!!')
    if jogador == computador:
        print(f'Deu empate! Ambos escolheram {jogador}!')
    elif computador == 'PEDRA' and jogador == 'PAPEL':
        print(f'Parabéns, você \033[1;32mGANHOU\033[m! Você escolheu {jogador} e o computador escolheu {computador}!')
    elif computador == 'PAPEL' and jogador == 'TESOURA':
        print(f'Parabéns, você \033[1;32mGANHOU\033[m! Você escolheu {jogador} e o computador escolheu {computador}!')
    elif computador == 'TESOURA' and jogador == 'PEDRA':
        print(f'Parabéns, você \033[1;32mGANHOU\033[m! Você escolheu {jogador} e o computador escolheu {computador}!')
    else:
        print(f'Que pena, você \033[1;31mPERDEU\033[m! Você escolheu {jogador} e o computador escolheu {computador}!')
else:
    print('\033[1;31mVocê deve escolher PEDRA, PAPEL ou TESOURA! Tente novamente!')
