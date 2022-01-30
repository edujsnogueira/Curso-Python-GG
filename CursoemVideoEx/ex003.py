# Existem 4 tipos primitivos básicos no Python:
# int = números inteiros;
# float = números reais;
# bool = números boleanos (True ou False). Obs: a primeira letra tem que ser maiúscula; e
# str = palavras. Obs: tem que vir entre aspas. Os números entres aspas são strings.

# Para descobrir o tipo de primitivo:
# n1 = input('Digite um valor: ')
# print(type(n1))

# Colocando o int na frente conseguimos transformar o string em número:
# n1 = int(input('Digite um valor: '))
# print(type(n1))

# Se não colocarmos o int na frente o sinal de soma vai concatenar as variáveis ao invés de somar:
# n1 = input('Digite um valor: ')
# n2 = input('Digite outro valor: ')
# s = n1 + n2
# print('A soma vale:', s)

# SCom o int na frente o sinal de soma vai somar as variáveis:
# n1 = int(input('Digite um valor: '))
# n2 = int(input('Digite outro valor: '))
# s = n1 + n2
# print('A soma vale:', s)

# Podemos utilizar os colchetes e o comando format para deixar o código mais elegante!
# n1 = int(input('Digite um valor: '))
# n2 = int(input('Digite outro valor: '))
# s = n1 + n2
# print('A soma entre', n1, 'e', n2, 'vale:', s)
# print('A soma entre {} e {} vale {}'.format(n1, n2, s))

# Podemos transformar o valor recebido em outras variáveis também:
# n = float(input('Digite um valor:'))
# print(n)

# Se declararmos a variável como boleano o resultado será true se tiver algum valor declarado e false se estiver vazio:
# n = bool(input('Digite um valor:'))
# print(type(n))
# print(n)

# o comando isnumeric declara se é possível converter a variável em número inteiro.
# Também apresenta como resposta somente verdaddeiro ou falso:

# n = input('Digite algo: ')
# print(type(n))
# print(n.isnumeric())

# Também é possível saber se a variável é letra (alfabeto):
# n = input('Digite algo: ')
# print(type(n))
# print(n.isalpha())

# Também é possível saber se a variável é alfanumérica (letra ou número ou combinação dos dois):
# n = input('Digite algo: ')
# print(type(n))
# print(n.isalnum())

# Existem vários "is alguma coisa", podemos testar depois.
# Lembrando que sempre que usamos o comando "input" estamos criando uma variável string
