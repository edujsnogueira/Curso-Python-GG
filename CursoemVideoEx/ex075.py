# Exercício 075:

'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

# n1 = int(input('Digite um número unteiro: '))
# n2 = int(input('Digite outro número unteiro: '))
# n3 = int(input('Digite mais um número unteiro: '))
# n4 = int(input('Digite o último número unteiro: '))
# valores = (n1, n2, n3, n4)
valores = tuple(int(input('Digite um número: ')) for c in range(0, 4))
print(f'Você digitou os seguintes valores: {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O valor 3 apareceu pela primeira vez na {valores.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram: ')
impar = 0
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
    else:
        impar += 1
if impar == 4:
    print('nenhum número par encontrado')
