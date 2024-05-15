p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

seila = p1.keys()
teste = list(seila)

print(seila)

print(teste[0])



print()
#Primeira Maneira
p1.update({
     'nome': 'novo valor',
     'idade': 30,
})
#Segunda maneira
p1.update(nome='novo valor', idade=30)
#Terceira maneira
tupla = (('nome', 'novo valor'), ('idade', 30))
p1.update(tupla)
#Quarta Maneira
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)