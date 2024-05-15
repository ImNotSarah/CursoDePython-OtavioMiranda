# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
citys = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states = ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(lista1, lista2):
    if len(lista1)> len(lista2):
        lista = lista1
        lista1 = lista2
        lista2 = lista
    resultado = []
    for i in range(len(lista1)):
        states_and_citys = (lista1[i], lista2[i])
        resultado.append(states_and_citys)
    return resultado

print(zipper(citys, states))
print(zipper(states, citys))
