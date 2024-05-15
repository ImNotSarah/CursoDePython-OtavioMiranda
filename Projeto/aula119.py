pessoa = {
    'nome': 'Sarah',
    'sobrenome': 'Lima',
    'idade': 19,
    'altura': 1.70,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
print(pessoa['nome'])

for chave in pessoa:
    print(chave, pessoa[chave])
