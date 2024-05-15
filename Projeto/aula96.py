string = 'abc'
lista = ['Maria', 'Helena', 1,2,3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

print(*salas, sep='\n')
""""
print('Maria', 'Helena', 1,2,3, 'Eduarda')
print(*lista)
print(*string)
print(*tupla)
"""