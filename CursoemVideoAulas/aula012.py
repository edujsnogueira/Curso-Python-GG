# Aula 012:

# Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos
# "if", "elif" e "else" em programas Python.

# Condição simples:
"""
nome = str(input('Qual é o seu nome?')).strip().capitalize()
if nome == 'Gustavo':
    print('Que nome bonito!')
print(f'Tenha um bom dia, {nome}!')
"""

# Condição composta
"""
nome = str(input('Qual é o seu nome?')).strip().capitalize()
if nome == 'Gustavo':
    print('Que nome bonito!')
else:
    print('Que nome normal!')
print(f'Tenha um bom dia, {nome}!')
"""

# Condição aninhada (sempre tem que ter um único "if", podem existir vários "elif", o "else" é opicional.)

nome = str(input('Qual é o seu nome?')).strip().capitalize()
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'João' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Paula Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Que nome normal!')
print(f'Tenha um bom dia, {nome}!')

# Fim
