# Exercício 088:

'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from random import sample
from time import sleep

linha = '-=' * 20
lista = []
print(linha)
print('JOGO DA MEGA SENA'.center(40))
print(linha)
jogos = int(input('Quantos jogos você quer sortear? '))
print(f'  SORTEANDO {jogos} JOGOS!  '.center(40, "="))
for c in range(1, jogos + 1):
    lista = sample(range(1, 61), 6)
    lista.sort()
    print(f'{c}º JOGO: {lista}')
    sleep(0.5)
    lista.clear()
print(f'  BOA SORTE!  '.center(40, "="))
