# Aula 008:

'''Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python.
 Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando
 módulos built-in e módulos externos, oferecidos no Pypi.'''

# Módulos:

# Podemos importar bibliotecas e funcionalidades no Python.

# Normalmente usamos o comando 'import', que importa todas as funcionalidades (ou bibliotecas) dos programas que queremos
# instalar.

# Também é possível usar o comando 'from X import'para importar funcionalidades específicas.

# Práitca:

# import math
# num = int(input('Digite um número inteiro:'))
# raiz = math.sqrt(num)
# print(f'A raiz de {num} é {math.ceil(raiz)}.')

# Obs: 'math.ceil' arredonda para cima e 'math.floor'arredonda para baixo.

# Também é possível importar apenas algumas funcionalidades. Quando importar apenas as funcionalidades não é
# necessário referenciar o caminho antes.

# from math import ceil, sqrt

# num = int(input('Digite um número inteiro:'))
# raiz = sqrt(num)
# print(f'A raiz de {num} é {ceil(raiz)}.')

# A documentação com a explicação das funções pode ser encontrada na página oficial do Python:
# https://docs.python.org/3/library/index.html

# Também é possível digitar import e apertat ctrl e espaço para ver uma lista na tela.

# Outra possibilidade é importar pacotes feitos por desenvolvedores pelo 'PyPI': https://pypi.org

import emoji
print(emoji.emojize('Olá, Mundo! :earth_americas:', use_aliases=True))

# Também é possível instalar pelas preferências / interpretadores do projeto.

# Fim!
