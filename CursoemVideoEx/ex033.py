# Exercício 033:

# Faça um programa que leia três números e moste qual é o maior e qual é o menor.

# Fazendo por função sorted:

n1 = int(input('Digite o primeiro número inteiro:'))
n2 = int(input('Digite o segundo número inteiro:'))
n3 = int(input('Digite o terceiro número inteiro:'))
lista = [n1, n2, n3]
lista_ordenada = sorted(lista)
print(f'Você digitou os números {n1}, {n2} e {n3}, o maior número é {lista_ordenada[2]} e '
      f'o menor número é {lista_ordenada[0]}.')

# Obs: outra opção era usar o max e min direto na lista mesmo sem sortear!
# O python vem com vários comandos que facilitam muito para quem conhece.
