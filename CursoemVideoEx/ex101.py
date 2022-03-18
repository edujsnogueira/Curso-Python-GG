# Exercício 101:

'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
OBRIGATÓRIO nas eleições.'''

# Nessa solução abaixo eu não estou retornando o valor litoral e sim imprimindo.

# def voto():
#     from datetime import datetime
#
#     print('_' * 30)
#     ano = int(input('Em que ano você nasceu? '))
#     idade = datetime.today().year - ano
#     if idade < 16:
#         print(f'Você tem {idade} anos e o voto é NEGADO!')
#     if 16 <= idade < 18 or idade > 65:
#         print(f'Você tem {idade} anos e o voto é OPCIONAL!')
#     else:
#         print(f'Você tem {idade} anos e o voto é OBRIGATÓRIO!')
#
#
# voto()

# Solução com a função "return":


def voto(ano):
    """
    => A função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor
    literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições:
    :param ano: ano de nascimento lido no programa principal.
    :return: situação do voto.
    """
    from datetime import datetime

    idade = datetime.today().year - ano
    if idade < 16:
        return f'Você tem {idade} anos e o voto é NEGADO!'
    if 16 <= idade < 18 or idade > 65:
        return f'Você tem {idade} anos e o voto é OPCIONAL!'
    else:
        return f'Você tem {idade} anos e o voto é OBRIGATÓRIO!'


print('_' * 30)
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
help(voto)
