# Exercício 063:

'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os "n" primeiros elementos de uma
Sequência de Fibonacci.'''


print('Calculadora de Sequência de Fibonacci')
fibo = int(input('Digite quantos termos da sequência você quer conhecer: '))
anterior = 0
atual = 1
soma = 0
contador = 2
if fibo < 1:
    print('Você deve escolher um número inteiro maior que zero. Tente outra vez!')
if fibo == 1:
    print(anterior)
elif fibo == 2:
    print(anterior, atual, end=' ')
elif fibo > 2:
    print(anterior, atual, end=' ')
    while contador < fibo:
        soma = anterior + atual
        anterior = atual
        atual = soma
        contador += 1
        print(soma, end=' ')
print('Fim!')
