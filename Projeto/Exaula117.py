def multiplicar_numero(numero):
    def duplicar(multiplicador):
        return f'{numero} vezes {multiplicador} é {numero * multiplicador}'
    return duplicar

conta = multiplicar_numero(2)
duplicar = conta(2)
triplicar = conta(3)
quadriplicar = conta(4)

print(f'{duplicar} \n{triplicar} \n{quadriplicar}')
