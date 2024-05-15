# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [(l1[i], l2[i]) for i in range(intervalo)]

# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']
# print(list(zip(l1, l2)))


# print()
listaA = [1,2,3,4,5,6,7]
listaB = [1,2,3,4]



def zipper(lista1, lista2):
    if len(lista1)> len(lista2):
        lista = lista1
        lista1 = lista2
        lista2 = lista
    resultado = []
    for i in range(len(lista1)):
        soma = lista1[i] + lista2[i]
        resultado.append(soma)
    return resultado

print(zipper(listaA, listaB))
print(zipper(listaB, listaA))