# Exercício 057:

'''Faça um programa que leia o sexo da pessoa, mas só leia "M" ou "F".
Caso esteja errado, peça a digitação novamente até aparecer um valor correto.'''


sexo = str(input('Digite o sexo da pessoa, sendo [ M ] para masculino e [ F ] para feminino:')).strip().upper()
'''Com o [0] no final o programa utiliza somente a primeira letra, se o operador digitar masculino por extenso, 
por exemplo. O problema é que qualquer coisa digitada que comece com M ou F vai ser aceita.'''
while sexo not in 'MF':
    sexo = str(input('Dados inválidos! Por favor digite o sexo corretamente! [ M / F ]:')).strip().upper()
print(f'Sexo {sexo} registado com sucesso!')
