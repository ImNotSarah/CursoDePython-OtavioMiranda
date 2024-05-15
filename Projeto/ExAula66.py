""" Calculadora com while """
while True:
    N1 = input('Digite um número: ')
    N2 = input('Digite outro número: ')
    operador = input('digite o operador [+][-][/][*]: ')

    if N1.isdigit and N2.isdigit():
        operadores_permitidos = '+-/*'
        N1 = float(N1)
        N2 = float(N2)

        if len(operador) > 1:
            print('<ERRO> Digite apenas um operador!')
            continue

        if operador not in operadores_permitidos:
            print('<ERRO> Digite um operador válido!')
            continue

        if operador == '+':
            print(f'{N1} + {N2} = {N1+N2}')

        elif operador == '-':
            print(f'{N1} - {N2} = {N1-N2}')

        elif operador == '/':
            print(f'{N1} / {N2} = {N1/N2}')

        else:
            print(f'{N1} * {N2} = {N1*N2}')

        sair = input('Quer sair? [s]im: ').lower().startswith('s')

        if sair is True:
            break
    else: 
        print('<ERRO> Um ou ambos dos números digitados são inválidos!')