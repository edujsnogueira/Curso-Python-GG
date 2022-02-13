# Exercício 043:

"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o IMC e mostre se status, de acordo com a
tabela abaixo:
- abaixo de 18:5 abaixo do peso;
- entre 18.5 e 25: peso ideal;
- entre 25 e 30: sobrepeso;
- entre 30 e 40: obesidade; e
- acima de 40: obesidade mórbida."""

altura = float(input('Digite a sua altura em metros:'))
peso = float(input('Digite o seu peso em quilos:'))
imc = peso / altura ** 2
if imc < 18.5:
    print(f'Seu Índice de Massa Corpórea é {imc:.1f} e você está \033[1;91mABAIXO DO PESO\033[m!')
elif imc < 25:
    print(f'Seu Índice de Massa Corpórea é {imc:.1f} e você está com \033[1;92mPESO IDEAL\033[m!')
elif imc < 30:
    print(f'Seu Índice de Massa Corpórea é {imc:.1f} e você está com \033[1;93mSOBREPESO\033[m!')
elif imc < 40:
    print(f'Seu Índice de Massa Corpórea é {imc:.1f} e você está com \033[1;31mOBESIDADE\033[m!')
else:
    print(f'Seu Índice de Massa Corpórea é {imc:.1f} e você está com \033[1;95mOBESIDADE MÓRBIDA\033[m!')
