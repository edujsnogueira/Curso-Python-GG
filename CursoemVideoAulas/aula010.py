# Aula 010:

# Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.
# Veja como aplicar os comandos if: e else: no Python.

# Estruturas condicionais:


# Condição simples: (não tem "else")

'''
nome = str(input('Qual é o seu nome:')).strip().capitalize()
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
print(f'Bom dia, {nome}!')
'''


# Condição composta: (com "else")

'''
nome = str(input('Qual é o seu nome:')).strip().capitalize()
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')
'''


# Condições simplificadas: (com "if" e "else" na mesma linha)

'''
nome = str(input('Qual é o seu nome:')).strip().capitalize()
print('Que nome lindo você tem!' if nome == 'Gustavo' else 'Seu nome é tão normal!')
print(f'Bom dia, {nome}!')
'''


# Exemplo de aplicação:

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1 + nota2) / 2
print(f'A sua média é {media:.1f}!')
if media >= 6.0:
    print('Sua média foi boa! Você está aprovado! parabéns!')
else:
    print('Sua média foi ruim! Você está de recuperação! Estude mais!')

# FIM
