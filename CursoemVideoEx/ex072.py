# exercício 072:

'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte.
Seu programa deverá ler um número pelo teclado entre (0 e 20) e mostrá-lo por extenso.'''

numero = 0
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número inteiro entre 0 e 20 para ser mostrado por extenso: '))
    if 0 <= numero <= 20:
        print(f'Você digitou o número {extenso[numero]}!')
        resposta = ' '
        while resposta not in 'SN':
            resposta = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        if resposta in 'N':
            break
    else:
        print('Você deve digitar um número inteiro entre 0 e 20!')
print('Fim!')
