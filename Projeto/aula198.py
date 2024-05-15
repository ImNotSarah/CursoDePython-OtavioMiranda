class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Luiz', 'Otávio')

# p1.nome = 'Sarah'
# p1.sobrenome = 'Lima'

print(p1.nome)
print(p1.sobrenome)