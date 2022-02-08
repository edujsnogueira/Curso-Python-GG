# Aula 009:

''' Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são
o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(),
capitalize(), title(), strip(), junção com join().'''

# Manipulando texto:

# Cadeia de caracteres ou cadeia de string é apresentada entre aspas simples ou duplas (ou triplas, para comentários).


### Fatiamento de string


# Toda string é armazenada em ordem de escrita, começando com índice "0" e seguindo até o tamanho final.

frase = 'Curso em vídeo Python'
print(frase)

# podemos imprimir apenas uma letra específica:
print(frase[9])

# podemos fatiar um intervalo:
print(frase[9:13])

# Obs: o Python não pega o último caractere do intervalo!!!
print(frase[9:21])

# Também podemos pular intervalos fixos:
print(frase[9:21:2])

# Se o início for omitido o intervalo começa do 0:
print(frase[:6])

# Se o final for omitido o intervalo pega até o final:
print(frase[15:])

# O mesmo pode ser aplicado pulando caracteres:
print(frase[9::3])



### Análise de string:


# Podemos descobrir o comprimento da string com a função "len":
print(len(frase))

# Podemos contar quantas vezes um caractere aparece dentro de uma string com a função "count"
print(frase.count('o'))

# Obs: O puthon difencia letras maiúscalas de minúsculas.

# Podemos usar a contagem junto com o fatiamento:
print(frase.count('o', 0, 13))

# Obs: lembrar que o final não entra na contagem, por isso o segundo 'o' não foi contado.

# Podemos buscar um dado específico com o comando 'find'. O resultado apresentado é o primeiro caractere onde
# o resultado foi encontrado.
print(frase.find('deo'))

# Obs: Se o valor procurado não for encontrado o Python retorna '-1'como resultado.
print(frase.find('Android'))

# Também é possível usar o operador 'in'para verificar se existe um caracter ou grupo de caracteres na string,
# mas a resposta é verdadeira ou falsa.
print('Curso' in frase)
print('Android' in frase)



### Transformação


# Podemos trocar caracteres com 'replace'
print(frase.replace('Python', 'Android'))

# Obs: Vimos que o replace não grava a alteração (se pedir para imprimir a frase, continuaremos com Python, e não
# Android), mas ele faz uma substituição secundária.

# Podemos transformar todas as letras em maiúsculas:
print(frase.upper())

# Obs: Confirmamos que a palavra 'Pithon' continua na frase e que a frase continua com maiúsculos e minúsculos.
print(frase)

# Podemos fazer o contrário com 'lower'
print(frase.lower())

# O comando 'capitalize' transforma tudo em minúscula e somente o primeiro caractere fica em maiúsculo.
print(frase.capitalize())

# O comando 'title' é semelhante, mas transforma cada início de palavra em maiúscula.
print(frase.title())

frase2 = '   Aprenda Python  '
print(frase2)
print(len(frase2))

# o comando 'strip' remove os espaços inúteis antes e depois das strings.
print(frase2.strip())
print(len(frase2))

# Obs: O comando também não reescreve sobre a string anterior. Repare que o tamanho continuou o mesmo.

# Obs: Existem variações como o 'rstrip'que remove apenas espaços em branco na direita (ao final) da string,
# assim como o 'lstrip'que remove os espaços na esquerda (no início) da string.



### Divisão


# O comando 'split' divide uma string em uma lista de strings, usando os espaços como referência, para criar uma
# lista de palavras relacionadas com a string original. De forma semelhante, cada palavra individual e a contagem
# das palavras na lista de strings começa com o indicador "0".
print(frase.split())
dividido = frase.split()
print(dividido)
print(dividido[2])
print(dividido[2][3])

# A junção de nomes de uma lista em uma frase é possível com o comando 'join'.
print(' '.join(frase))
print(' '.join(dividido))

# Obs: Como o objeto 'frase' não foi reescrito no split, a utilização do 'join' separou letra a letra!
# Obs2: Qualquer coisa que for colocada entre as aspas do join vai ser usada no comando.

# E no final das contas, como faz para trocar o efetivamente com o comando 'replace'? Somente atribuindo o resultado.
print(frase)
frase = frase.replace('Python', 'Android')
print(frase)

# Fim!
