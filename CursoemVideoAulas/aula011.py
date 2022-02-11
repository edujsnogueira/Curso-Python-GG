# Aula 011:

# Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus
# programas em Python. Veja como utilizar o código "\033[m" com todas as suas principais possibilidades.

# Cores no terminal

# Código ANSI para corres com "escape sequence" que é a barra invertida.


# 3 estrutura: \033[estilo; texto; fundo m

'''
Estilo:
- **0**: (Nome) sem cor.
- **1**: (Bold) Negrito.
- **4**: (Underline) Sublinhado.
- **7**: (Negative) Inverte letra e fundo.

Cor do texto (fg):
- **30**: Branco.
- **31**: Vermelho.
- **32**: Verde.
- **33**: Amarelo.
- **34**: Azul.
- **35**: Magenta.
- **36**: Cyan (azul claro).
- **37**: Cinza.

Cor de fundo (bg):
- **40**: Branco.
- **41**: Vermelho.
- **42**: Verde.
- **43**: Amarelo.
- **44**: Azul.
- **45**: Magenta.
- **46**: Cyan (azul claro).
- **47**: Cinza.

**OBS**: Para limpar/limitar a formatação deve-se utilizar "\033[m"
'''

# Praticando:

print('Olá, Mundo!')

# trocando a cor da letra para vermelho:
print('\033[31mOlá, Mundo!')

# alterando o fundo para amarelo:
print('\033[31;43mOlá, Mundo!')

# colocando em negrito:
print('\033[1;31;43mOlá, Mundo!')

# terminddo com a formatação após a frase:
print('\033[1;31;43mOlá, Mundo!\033[m')

# pode ser feito com variáveis também:
a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m!')


# Coleção (dicionário):

# É possível escrever uma coleção de cores que eu pretendo utilizar e já deixar previamente estabelecido.
# Depois é só chamar a cor escolhida.

nome = 'Guanabara'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

print(f'Olá, muito prazer em te conhecer, {cores["azul"]}{nome}{cores["limpa"]}!')

# Fim
