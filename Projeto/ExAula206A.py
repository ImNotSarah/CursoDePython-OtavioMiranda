import json


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Luiz', 'Otávio')

with open('ExAula206.json', 'w', encoding='utf8') as arquivo:
    json.dump(vars(p1), arquivo, ensure_ascii = False, indent=2)

