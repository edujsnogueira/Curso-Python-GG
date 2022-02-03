# Exercício 013:

# Faça um programa que leia o salário de um funcionário de  mostre seu novo salário, com 15% de aumento.

# s = float(input('Digite o salário do funcionário em Reais:'))
# print(f'O novo salário do funcionário, com 15% de aumento, deve ser R$ {s * 1.15:.2f}.')

# Obs: Se quiser deixar a porcentagem de aumento customizável:

s = float(input('Digite o salário do funcionário em Reais:'))
p = float(input('Digite a porcentagem do aumento em %:'))
print(f'O salário anterior do funcionário era {s:.2f} e novo salário do funcionário,'
      f'com {p}% de aumento, deve ser R$ {s * (1 + p / 100):.2f}.')
