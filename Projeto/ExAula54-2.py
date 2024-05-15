"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = input('Que horas são? (numeros inteiros)')

try:
    horario = int(horario)
    if horario >= 0 and horario <= 11:
        print('Bom dia!')
    elif horario >= 12 and horario <= 17:
        print('Boa tarde!')
    elif horario >= 18 and horario <= 23:
        print('Boa noite!')
    else:
        print('A hora digitada não é válida')
except:
    print('Erro! Digite um horario valido')
