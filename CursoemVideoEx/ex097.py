# exercício 097:

'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e
mostre uma mensagem com tamanho adaptável.'''


def escreva(msg):
    print('~' * len(msg))
    print(msg.center(len(msg)))
    print('~' * len(msg))


escreva(str(input('Digite a sua mensagem: ').strip()))
