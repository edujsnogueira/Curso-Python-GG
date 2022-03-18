# Exercício 105:

'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings dessa função para consulta pelo desenvolvedor.'''


notas = list()
provas = dict()


def turma(notas, situação=False):
    """
    => Função para analisar notas e desempenho da turma.
    :param notas: lista com as notas obtidas pelos alunos da turma (>= 7 é boa, >= 5 é razoável e < 5 é ruim).
    :param situação: (opcional) padrão é falso, quando verdadeiro mostra situação da turma.
    :return: dicionário contendo: quantidade de notas, maior not, menor nota, média da turma e situação (opcional).
    """
    while True:
        notas.append(float(input('Digite uma nota: ')))
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
        if continuar in 'N':
            break
    mostrar = str(input('Deseja mostrar a situação da turma? [S/N] ')).strip().upper()[0]
    if mostrar in 'S':
        situação = True
    provas['total'] = len(notas)
    provas['maior'] = max(notas)
    provas['menor'] = min(notas)
    provas['média'] = float(sum(notas)/len(notas))
    if situação:
        if provas['média'] >= 7:
            provas['situação'] = 'BOA'
        elif provas['média'] < 5:
            provas['situação'] = 'RUIM'
        else:
            provas['situação'] = 'REGULAR'
    print(provas)


turma(notas)
help(turma)
