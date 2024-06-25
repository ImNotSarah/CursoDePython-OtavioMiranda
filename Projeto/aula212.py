class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
    
    @property
    def cor(self):
        print('Poperty')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123456


caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)
print(caneta.cor_tampa)

####

# class Caneta:
#     def __init__(self, cor):
#         self.cor = cor
    
#     def get_cor(self):
#         print('Get cor')
#         return self.cor
    


# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())