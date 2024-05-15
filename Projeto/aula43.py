#nome = 'Sarah'
#print(nome[2])
#print(nome[-3])
#print('r' in nome)
#print('z' in nome)
#print('ra' in nome)
#print(10*'-')
#print('ra' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encntontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else: 
    print(f'{encontrar} não está em {nome}')