# Exercício 100:

'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los na lista e a segunda função mostra a soma entre
todos os valores pares sorteados.'''

from random import sample
from time import sleep

valores = list()


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    valores.extend(sample(range(0, 10), 5))
    for v in valores:
        print(v, end=' ')
        sleep(0.5)
    print('Pronto!')


def soma():
    par = 0
    for v in valores:
        if v % 2 == 0:
            par += v
    print(f'Somando os valores pares de {valores}, temos {par}.')


sorteia()
soma()
