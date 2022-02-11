# Exercício 034:

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para salários inferiores ou iguais a R$ 1.250,00, o aumento é de 15%.

salario = float(input('Digite o salário do funcionário em R$:'))
if salario > 1250.00:
    print(f'O novo salário do funcionário, com aumento de 10% é R$ {salario * 1.1:.2f}.')
else:
    print(f'O novo salário do funcionário, com aumento de 15% é R$ {salario * 1.15:.2f}.')

# Esse exercício poderia ser feito com condicional simmplificada porque só existe uma bifurcação.
