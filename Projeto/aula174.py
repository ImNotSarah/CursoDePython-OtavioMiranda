from itertools import combinations, permutations, product
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]
print_iter(product(*camisetas))