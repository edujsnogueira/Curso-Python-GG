# Exercício 032:

# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

'''
ano = int(input('Digite um ano para saber se ele é bissexto:'))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'O ano {ano} é bissexto!')
        else:
            print(f'O ano {ano} não é bissexto!')
    else:
        print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
'''


# Podemos simplificar a análise juntado todas as condições com "and" e "or":

ano = int(input('Digite um ano para saber se ele é bissexto:'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')

# Obs1: o módulo "calendar" já tem a função "isleap" que verifica se o ano é bissexto.
# Obs2: o módulo "datetime" tem a função "date.today().year" que lê o ano atual.
