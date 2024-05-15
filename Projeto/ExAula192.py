import json
lista_de_tarefas = []

def mostrar_lista_json(lista):
    for item in lista:
        print(item)
    
def salvar_no_json():

    with open('ExAula192.json', 'w', encoding='utf8') as arquivo:
            json.dump(lista_de_tarefas, arquivo, ensure_ascii = False, indent=2)

def puxar_do_json():
    with open('ExAula192.json', 'r', encoding='utf8') as arquivo:
        lista_de_tarefas_json = json.load(arquivo)
        return lista_de_tarefas_json

while True:

    print('Comandos: listar, desfazer, refazer')
    escolha = input('Digite uma tarefa ou um comando: ')
    print()
    escolha = escolha.lower()

    if escolha not in ['listar', 'desfazer', 'refazer']:

        lista_de_tarefas.append(escolha)
        salvar_no_json()
        mostrar_lista_json(puxar_do_json())
        print()

    elif escolha == 'listar':

        print('TAREFAS:\n')
        salvar_no_json()
        mostrar_lista_json(puxar_do_json())
        print()

    elif escolha == 'desfazer':

        ultimo_valor_removido = lista_de_tarefas.pop()
        salvar_no_json()
        mostrar_lista_json(puxar_do_json())
        print()
    
    elif escolha == 'refazer':

        lista_de_tarefas.append(ultimo_valor_removido)
        salvar_no_json()
        mostrar_lista_json(puxar_do_json())
        print()

    