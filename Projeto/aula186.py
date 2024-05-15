caminho_arquivo = 'C:\\Users\\sarah\\OneDrive\\Área de Trabalho\\Python\\Projeto\\'
caminho_arquivo += 'aula186.txt'

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

# with open(caminho_arquivo, 'w') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 1\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     # print(arquivo.read())

# print('#'*10)


# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 1\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )