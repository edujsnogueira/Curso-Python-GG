# Exercício 019:

# Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude o professor,
# lendo o nome deles e escretendo o nome do escolhido.

'''import random
aluno1 = input('Digite o nome do primeiro aluno:')
aluno2 = input('Digite o nome do segundo aluno:')
aluno3 = input('Digite o nome do terceiro aluno:')
aluno4 = input('Digite o nome do quarto aluno:')
print(f'O nome do aluno sorteado é {random.choice([aluno1, aluno2, aluno3, aluno4])}.')'''

# Para rodar esse programa precisamos criar uma lista. No caso inicial fizemos uma lista direto dentro do choice,
# mas poderíamos ter feito uma lista antes e só ter sorteado a lista.

import random
aluno1 = input('Digite o nome do primeiro aluno:')
aluno2 = input('Digite o nome do segundo aluno:')
aluno3 = input('Digite o nome do terceiro aluno:')
aluno4 = input('Digite o nome do quarto aluno:')
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print(f'O nome do aluno sorteado é {escolhido}.')
