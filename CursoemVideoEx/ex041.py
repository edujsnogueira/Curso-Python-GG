# Exercício 041:

"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, conforme a sua idade:
- até 9 anos: mirim;
- até 14 anos: infantil;
- até 19 ano: junior;
- até 25 anos: sênior; e
- acima: master."""

nascimento = int(input('Digite o ano de nascimento do nadador:'))
from datetime import date
ano = date.today().year
idade = ano - nascimento
if idade < 10:
    print(f'O nadador tem {idade} anos e a categoria dele é MIRIM.')
elif idade < 15:
    print(f'O nadador tem {idade} anos e a categoria dele é INFANTIL.')
elif idade < 20:
    print(f'O nadador tem {idade} anos e a categoria dele é JUNIOR.')
elif idade < 26:
    print(f'O nadador tem {idade} anos e a cattegoria dele é SÊNIOR.')
else:
    print(f'O nadador tem {idade} anos e a categoria dele é MASTER.')
