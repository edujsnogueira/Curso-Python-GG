# Exercício 027:

# Faça um programa que leia o nome competo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
'''Exemplo:
nome: Ana Maria de Souza
primeiro nome: Ana
último nome: Souza'''

nome = str(input('Digite seu nome completo:')).strip()
separado = nome.split()
print(f'Seu nome é {nome}.')
print(f'Seu primeiro nome é: {separado[0]}.')
print(f'Seu último nome é: {separado[-1]}.')

# Obs: O comando [-1] pega o último elemento da lista, o [-2] pegaria o penúltimo, e assim por diante.
# Obs: Uma outra alternativa menos elegante seria contar a quantidade de elementos da lista com o comando "len" e
# tirar uma unidade, já que o primeiro é sempre a posição zero.
