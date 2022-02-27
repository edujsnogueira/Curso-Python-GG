# Exercício 077:

'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
para cada palavra, quais são as suas vogais.'''

from unidecode import unidecode

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'grátis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')
c = 0
while c < len(palavras):
    print(f'\nNa palavra {palavras[c].upper()}, temos as seguintes vogais:', end=' ')
    # if 'a' in palavras[c]:
    #     print('a', end=' ')
    # if 'e' in palavras[c]:
    #     print('e', end=' ')
    # if 'i' in palavras[c]:
    #     print('i', end=' ')
    # if 'o' in palavras[c]:
    #     print('o', end=' ')
    # if 'u' in palavras[c]:
    #     print('u', end=' ')
    for letra in palavras[c]:
        if unidecode(letra.lower()) in 'aeiou':
            print(letra, end=' ')
    c += 1
