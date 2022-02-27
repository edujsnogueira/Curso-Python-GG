# Exercício 073:

'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

brasileirao = ('Atlético Mineiro - MG', 'Flamengo - RJ', 'Palmeiras - SP', 'Fortaleza - CE', 'Corinthians - SP',
               'Red Bull Bragantino - SP', 'Fluminense - RJ', 'América - MG', 'Atlético - GO', 'Santos - SP',
               'Ceará - CE', 'Internacional - RS', 'São Paulo - SP', 'Athletico Paranaense - PR', 'Cuiabá - MT',
               'Juventude - RS', 'Grêmio - RS', 'Bahia - BA', 'Sport - PE', 'Chapecoense - SC')
print(f'Os times do Brasileirão 2021 são: {brasileirao}')
print(f'Os 5 primeiros times são: {brasileirao[0:5]}')
print(f'Os 4 últimos times são: {brasileirao[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(brasileirao)}')
print(f'O time da Chapecoense - SC está na {brasileirao.index("Chapecoense - SC") + 1}ª posição')
