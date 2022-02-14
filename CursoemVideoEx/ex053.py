# Exercício 053:

'''Crie um programa que leia um afrase e diga se ela é um palíndromo, desconsiderando os espaços.'''

import unidecode
frase = str(input('Digite uma frase para verificar se ela é um palíndromo:')).strip().upper()
frasevazia = frase.replace(" ", "")
frasevazia = unidecode.unidecode(frasevazia)
inverso = frasevazia[:: -1]
if frasevazia == inverso:
    print(f"Parabéns, você descobriu um palíndromo! A frase {frase} pode ser lida de trás para frente.")
else:
    print(f"A frase {frase} não é um palíndromo!")
