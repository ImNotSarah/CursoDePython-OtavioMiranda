produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
import copy

novos_produtos = copy.deepcopy(produtos)

novos_precos = [
    {**produto,'preco': round(produto['preco']*1.1,2)}
    for produto in novos_produtos
]

print('Com aumento de 10%:',*novos_precos, sep='\n')
print()

print('Produtos em ordem decrescente:')
produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome.sort(key=lambda item: item['nome'], reverse=True)

print(*produtos_ordenados_por_nome, sep='\n')
print()

produtos_ordenados_por_preco =copy.deepcopy(produtos)
produtos_ordenados_por_preco.sort(key=lambda item: item['preco'])

print('Produtos por ordem crescente de preço')
print(*produtos_ordenados_por_preco, sep='\n')

