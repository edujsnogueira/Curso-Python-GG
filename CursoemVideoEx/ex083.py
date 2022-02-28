# Exercício 083:

''' Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

expr = str(input('Digite uma expressão para verificarmos a validade: ')).strip()
pilha = []
for symbol in expr:
    if symbol == '(':
        pilha.append('(')
    elif symbol == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
