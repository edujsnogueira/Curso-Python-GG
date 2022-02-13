# Exercício 036:

"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, ou então o empréstimo
será negado."""

casa = float(input('Digite qual o valor da casa que você deseja comprar em R$?'))
salario = float(input('Digite qual o valor do seu salário mensal em R$?'))
tempo = int(input('Digite em quanto anos você pretende financiar a casa?'))
prestacao = casa / tempo / 12
margem = salario * 0.3
print(f'Você tem uma margem consignável de R$ {margem:.2f} para comprar uma casa de R$ {casa:.2f}, '
      f'com um financiamento de {tempo} anos.')
if prestacao > margem:
    print(f'Empréstimo \033[1;31mNEGADO\033[m! Infelizmente a prestação de R$ {prestacao:.2f} é maior que a sua margem!')
else:
    print(f'Empréstimo \033[1;32mCONCEDIDO\033[m! Você pode comprar a casa, e o valor da prestação é de R$ {prestacao:.2f}!')
