def multiplicacao(*args):
     total = 1
     for numero in args:
         total *= numero
     return total

multiplicacao_152 = multiplicacao(1,5,2)
print(multiplicacao_152)

def par_ou_impar(numero):
    resto = numero % 2 
    if resto == 0:
        return f'{numero} é par'
    return f'{numero} é impar'


print(par_ou_impar(5))

 