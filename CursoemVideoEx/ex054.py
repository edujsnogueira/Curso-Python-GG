# Exercício 054:

'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantos já são maiores.'''

from datetime import date
maior = 0
menor = 0
ano = date.today().year
for contador in range(0, 7):
    nascimento = int(input('Digite o ano de nascimento de uma pessoa:'))
    idade = ano - nascimento
    if idade < 21:
        menor += 1
    else:
        maior += 1
print(f'De acordo com as datas digitadas, {maior} pessoas já atingiram a maioridade e {menor} pessoas '
       f'ainda são menores de idade.')
