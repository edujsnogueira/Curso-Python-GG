# Exercício 024:

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cidade = str(input('Digite o nome da cidade que você nasceu:')).strip().upper().split()
print(f'A cidade que você nasceu começa com Santo? {"SANTO" == cidade[0]}')
# Uma possível solução é jogar tudo para maiúscula e comparar com 'SANTO' em maiúscula.
# O comando "in" também seria uma boa solução, mas esbarra no problema da cidade de 'Santos'.
