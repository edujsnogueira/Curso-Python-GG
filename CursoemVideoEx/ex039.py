# Exercício 039:

"""Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com a sua idade:
- se ele ainda vai se alistar ao serviço militar;
- se está na hora dele se alistar ao serviço militar; ou
- se já passou da hora dele se alistar ao serviço militar.
O programa também deve mostra o tempo que fala ou que passou do prazo."""

nascimento = int(input('Digite seu ano de nascimento:'))
from datetime import date
ano = date.today().year
idade = ano - nascimento
if idade < 18:
    print(f'Você ainda vai se alistar! Faltam {abs(idade - 18)} anos para o alistamento!') # poderia ser "18 - idade"
    print(f'O ano de alistamento é {nascimento + 18}.')
elif idade > 18:
    print(f'Você já se alistou! Já passou {idade - 18} anos do alistamento!')
    print(f'O ano de alistamento foi {nascimento + 18}.')
else:
    print('Está na hora de se alistar!')
