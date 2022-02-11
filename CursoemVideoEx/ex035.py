# Exercício 035:

# desenvolva um programa que leio o comprimento de três retas e diga ao usuário se elas podem
# ou não formar um triângulo.

r1 = float(input('Digite o comprimento da primeira reta:'))
r2 = float(input('Digite o comprimento da segunda reta:'))
r3 = float(input('Digite o comprimento da terceira reta:'))
lista = [r1, r2, r3]
lista_ordenada = sorted(lista)
if lista_ordenada[0] + lista_ordenada[1] > lista_ordenada[2]:
    print(f'As retas {r1}, {r2} e {r3} conseguem formar um triângulo!')
else:
    print(f'As retas {r1}, {r2} e {r3} não conseguem formar um triângulo!')
