# Exercício 104:

'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input()
do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')'''


def teste():

    valor = str(input('Digite um número: ')).strip()
    while not valor.isnumeric():
        print('\033[0;31mErro! Digite um número inteiro válido!\033[m')
        valor = input('Digite um número: ')
    return f'Você acabou de digitar o número {valor}!'


print(teste())
