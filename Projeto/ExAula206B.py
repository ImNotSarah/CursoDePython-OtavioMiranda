import json

with open('ExAula206.json', 'r', encoding='utf8') as arquivo:
        dados = json.load(arquivo)

print(dados)
nome = dados['nome']
sobrenome = dados['sobrenome']
