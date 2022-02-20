# Exercício 068:

'''Faça um programa para jogar PAR ou ÍMPAR com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que o jogador conquistou ao final do jogo.'''

from random import randint

print('-=-' * 10)
print('Vamos jogar par ou ímpar?')
print('-=-' * 10)
contador = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Escolha um número inteiro para jogar: '))
    soma = computador + jogador
    jogada = " "
    while jogada not in 'PI':
        jogada = str(input('Escolha Par ou Ímpar [P/I]: ')).strip().upper()[0]
    print('-=-' * 10)
    if jogada in 'P':
        if soma % 2 == 0:
            print(f'Parabéns, você ganhou! Você escolheu {jogador}, o computador escolheu {computador}, a soma'
                  f' foi {soma} e deu PAR.')
            contador += 1
        else:
            print(f'Você perdeu! Você escolheu {jogador}, o computador escolheu {computador}, a soma'
                  f' foi {soma} e deu ÍMPAR.')
            break
    else:
        if soma % 2 != 0:
            print(f'Parabéns, você ganhou! Você escolheu {jogador}, o computador escolheu {computador}, a soma'
                  f' foi {soma} e deu ÍMPAR.')
            contador += 1
        else:
            print(f'Você perdeu! Você escolheu {jogador}, o computador escolheu {computador}, a soma'
                  f' foi {soma} e deu PAR.')
            break
print(f'GAME OVER! Você venceu {contador} vezes!')
