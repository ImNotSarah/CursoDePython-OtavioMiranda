def sauda2(nome):
    print('Como vai ' + nome + '?')

def tchau():
    print('ok, tchau!')

def sauda(nome):
    print('Olá, ' + nome + '!')
    sauda2(nome)
    print('preparando para dizer tchau...')
    tchau()

print(sauda('Sarah'))