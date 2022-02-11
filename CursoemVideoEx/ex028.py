# Exercício 028:

# Escreva um programa que faça o computador "pensar" e mum número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

print('O computador está escolhendo um número entre 0 e 5...')
import random
computador = random.randint(0, 5)
jogador = int(input('Escolha um número inteiro entre 0 e 5:'))
if computador == jogador:
    print("Parabéns, você venceu!")
else:
    print(f"Você perdeu! Você escolheu o número {jogador} e o computador escolheu o número {computador}!")
