# Exercício 056:

'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo;
- Qual é o nome do homem mais velho;
- Quantas mulheres têm menos de 21 anos.'''

soma = 0
homem = 0
velho = 0
idoso = 0
mulher = 0
for c in range(1, 5):
    nome = str(input(f'Digite o nome da {c}ª pessoa:')).strip().capitalize()
    idade = int(input(f'Digite a idade de {nome}:'))
    sexo = str(input(f'Qual o sexo de {nome}? Digite [ M ] para masculino e [ F ] para feminino.')).strip().upper()
    soma = soma + idade
    if sexo == 'M':
        if idade > velho:
            velho = idade
            idoso = nome
    else:
        if idade < 21:
            mulher = mulher + 1
print(f'A média de idade do grupo é {soma / 4:.2f}.')
if idoso == 0:
    print('Você não digitou o nome de nenhum homem.')
else:
    print(f'O nome do homem mais velho é {idoso} e ele tem {velho} anos.')
if mulher == 0:
    print('Você não digitou nenhuma mulher menor de idade.')
else:
    print(f'Você digitou {mulher} mulheres menores de 21 anos de idade.')
