lista_de_compras = []

while True:
    opcao = input('\nSelecione uma ação: \n[i]nserir [a]pagar [l]istar:')

    if opcao == 'i':
        valor = input('\nValor: ')
        lista_de_compras.append(valor)

    elif opcao == 'a':
        indice = int(input('\nEscolha um indice para apagar: '))
        
        if indice > len(lista_de_compras):
            print('\nNão foi possivel apagar esse indice')
            
        else: 
            lista_de_compras.pop(indice)

    elif opcao == 'l':
        for item in enumerate(lista_de_compras):
            print(item)

    else:
        print('\nOpção inválida!')
