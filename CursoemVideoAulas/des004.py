# Desafio 004:

# Depois da versão 3.7 do python não precisa mais usar ".format ()",
# apenas coloque um f antes das aspas ' ' e escreva o nome da variável
# dentro dos colchetes {}  exemplo: print (f'A soma de {n1} e {n2} é {s}')

n = input('Digite algo:')
print('Segue abaixo as informações:')
print('Tipo primitivo:', type(n))
print(f'Só tem espaços? {n.isspace()}')
print(f'É numérico? {n.isnumeric()}')
print(f'É alfabético? {n.isalpha()}')
print(f'É alfanumérico? {n.isalnum()}')
print(f'Está em letras maiúsculas?{n.isupper()}')
print(f'Está em letras minúsculas? {n.islower()}')
print(f'Está capitalizada? {n.istitle()}')
