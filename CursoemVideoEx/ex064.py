# Exercício 064:

'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999,
que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles,
desconsiderando o "flag".'''

numero = soma = contador = 0
while numero != 999:
    numero = int(input('''Digite um número inteiro para saber a soma e a quantidade de números digitados ao final. 
Se for digitado "999" o programa vai encerrar e apresentar o resultado: '''))
    if numero == 999:
        print('Você digitou o comando de parada e o programa vai encerrar.')
    else:
        soma += numero
        contador += 1
print(f'Você digitou {contador} números e a soma entre eles foi {soma}.')
