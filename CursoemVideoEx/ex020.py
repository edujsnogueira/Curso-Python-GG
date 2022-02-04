# Exercício 020:

# O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça
# um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
aluno1 = input('Digite o nome do primeiro aluno:')
aluno2 = input('Digite o nome do segundo aluno:')
aluno3 = input('Digite o nome do terceiro aluno:')
aluno4 = input('Digite o nome do quarto aluno:')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print(f'A ordem de sorteio dos alunos é {lista}.')
