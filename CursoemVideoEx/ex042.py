# Exercício 042:

"""Refaça o exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- equilátero: todos os lados iguais;
- isósceles: dois lados iguais;
- escaleno: todos os lados diferentes."""

r1 = float(input('Digite o comprimento da primeira reta:'))
r2 = float(input('Digite o comprimento da segunda reta:'))
r3 = float(input('Digite o comprimento da terceira reta:'))
lista = [r1, r2, r3]
lista_ordenada = sorted(lista)
if lista_ordenada[0] + lista_ordenada[1] > lista_ordenada[2]:
    if lista[0] == lista[1] and lista[0] == lista[2]:
        print(f'As retas {r1}, {r2} e {r3} conseguem formar um triângulo EQUILÁTERO!')
    elif lista[0] != lista[1] and lista[0] != lista[2] and lista[1] != lista[2]:
        print(f'As retas {r1}, {r2} e {r3} conseguem formar um triângulo ESCALENO!')
    else:
        print(f'As retas {r1}, {r2} e {r3} conseguem formar um triângulo ISÓSCELES!')
else:
    print(f'As retas {r1}, {r2} e {r3} não conseguem formar um triângulo!')

'''Obs: no python podemos colocar direto os sinais de == ou != sem o comando de "and". Lembrar que se for usar o 
diferente, tem que testar todas as possibilidades.'''
