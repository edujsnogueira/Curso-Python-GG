# Exercício 066:

'''Crie um programa que leia vários números pelo teclado. O programa só vai parar quando o usuário digitar o valor
999, sendo a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles,
desconsiderando o "flag".'''

soma = contador = 0
while True:
    numero = int(input('Digite um número inteiro. \n'
                       'Se digitar 999 o programa irá encerrar: '))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f'Você digitou {contador} números e a soma deles é {soma}.')
