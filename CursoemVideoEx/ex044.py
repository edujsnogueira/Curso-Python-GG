# Exercício 044:

"""Elabore um programa que calcule o valor a ser pado por um produto, considerando o seu preço normal e a
condição de pagamento:
- à vista dinheiro ou cheque: 10% de desconto;
- à vista cartão: 5% de desconto;
- em 2x no cartão: preço normal; e
- 3x ou mais no cartão: 20% de juros."""

print('{:-^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Digite o preço do produto em R$:'))
print('''Formas de pagamento:
[ 1 ] para pagamento à vista dinheiro ou cheque;
[ 2 ] para pagamento à vista no cartão;
[ 3 ] para pagamento em 2x no cartão; ou
[ 4 ] para pagamento em 3x ou mais.''')
pagamento = int(input('Digite a forma de pagamento escolhida:'))
if pagamento == 1:
    print(f'Você vai pagar à vista com dinheiro ou cheque, ganhou 10% de desconto, e o valor do produto com desconto '
          f'é de R$ {preco * 0.9:.2f}.')
elif pagamento == 2:
    print(f'Você escolheu pagamento à vista no cartão, ganhou 5% de desconto, e o valor do produto com desconto '
          f'é de R$ {preco * 0.95:.2f}.')
elif pagamento == 3:
    print(f'Você escolheu pagamento em 2x no cartão, não ganhou desconto, e o valor do produto sem desconto '
          f'é de R$ {preco:.2f} em duas parcelas de R$ {preco / 2}.')
elif pagamento == 4:
    parcela = int(input('Digite o número de parcelas (maior ou igual a três parcelas):'))
    if parcela > 2:
        print(f'Você escolheu pagamento em 3x ou mais no cartão, terá um acréscimo de 20% de juros, e o valor do '
              f'produto com juros é de R$ {preco * 1.2:.2f} em {parcela} parcelas de R$ {preco / parcela:.2f}.')
    else:
        print('\033[1;31mVocê não escolheu corretamente a forma de pagamento.')
else:
    print('\033[1;31mVocê não escolheu corretamente a forma de pagamento.')
