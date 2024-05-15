perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

primeira_pergunta = perguntas[0]['Pergunta']

opcoes_primeira_pergunta = perguntas[0]['Opções']

acertos = 0

print(f'Pergunta: {primeira_pergunta}\n\nOpções:')


for sequencia_1 in range(len(opcoes_primeira_pergunta)):
    print(f'{sequencia_1}) {opcoes_primeira_pergunta[sequencia_1]}')
    
resposta1 = input('Escolha uma opção: ')

if resposta1 == '2':
    print('ACERTOU ✔\n')
    acertos += 1
    
else:
    print('ERROU ❌\n')

segunda_pergunta = perguntas[1]['Pergunta']
opcoes_segunda_pergunta = perguntas[1]['Opções']

print(f'Pergunta: {segunda_pergunta}\n\nOpções:')

for sequencia_2 in range(len(opcoes_segunda_pergunta)):
    print(f'{sequencia_2}) {opcoes_segunda_pergunta[sequencia_2]}')

resposta2 = input('Escolha uma opção: ')

if resposta2 == '0':
    print('ACERTOU ✔\n')
    acertos += 1
    
else:
    print('ERROU ❌\n')

terceira_pergunta = perguntas[2]['Pergunta']
opcoes_terceira_pergunta = perguntas[2]['Opções']

print(f'Pergunta: {terceira_pergunta}\n\nOpções:')

for sequencia_3 in range(len(opcoes_terceira_pergunta)):
    print(f'{sequencia_3}) {opcoes_terceira_pergunta[sequencia_3]}')

resposta3 = input('Escolha uma opção: ')

if resposta3 == '1':
    print('ACERTOU ✔\n')
    acertos += 1
    
else:
    print('ERROU ❌\n')

print(f'Você acertor {acertos} de 3 perguntas.\n')