# Exercício 046:

'''Faça um programa que mostre uma contagem regressiva na tela para o estouro de fogos de artifício, indo de dez
até zero, com uma pause de um segundo entre eles.'''

from time import sleep
import emoji
for contagem in range(10, -1, -1):
    print(contagem)
    sleep(1)
print(emoji.emojize('Feliz ano novo! :fireworks:'))
