"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
def soma (*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma_123 = soma(1,2,3)
print(soma_123)