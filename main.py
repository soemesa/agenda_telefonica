import json


def inserir(diccionario):
    contatos = abrir_agenda()

    diccionario.update(contatos)

    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    telefone = input("Digite seu telefone: ")
    twitter = input("Digite seu Twitter: ")
    instagram = input("Digite o Instagram: ")

    contato = {
        nome: {
            "email": email,
            "telefone": telefone,
            "Twitter": twitter,
            "Instagram": instagram
        }
    }
    diccionario.update(contato)
    print(f"O contato {nome} foi cadastrado com sucesso!")

    arquivo = open("agenda_telefonica.json", "w")
    json.dump(diccionario, arquivo)
    arquivo.close()


def alterar():
    pass


def remover():
    pass


def pesquisar():
    contato_encontrado = False
    nome = input("Digite seu nome: ")

    contatos = abrir_agenda()
    for contato in contatos.keys():
        if contato == nome:
            contato_encontrado = True
            imprimir_contato(contato, contatos)
    if not contato_encontrado:
        print("Contato não encontrado!Tente novamente!")


def listar():
    contatos = abrir_agenda()
    for contato in contatos.keys():
        imprimir_contato(contato, contatos)


def principal():
    diccionario = {}

    while True:
        print(" === Agenda Telefônica === ")
        print(" 1- Inserir contato")
        print(" 2- Alterar contato")
        print(" 3- Remover contato")
        print(" 4- Consultar contato")
        print(" 5- Listar contatos")
        print(" 6- Sair")
        opcao = int(input(" > "))

        if opcao == 1:
            inserir(diccionario)
        elif opcao == 2:
            alterar()
        elif opcao == 3:
            remover()
        elif opcao == 4:
            pesquisar()
        elif opcao == 5:
            listar()
        elif opcao == 6:
            print("Saindo da agenda...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


def abrir_agenda():
    with open("agenda_telefonica.json", encoding='utf-8') as meu_json:
        contatos = json.load(meu_json)
    return contatos


def imprimir_contato(contato, contatos):
    return print('-------------------------\n'
                 f'nome: {contato}\n'
                 f'email: {contatos[contato]["email"]}\n'
                 f'telefone: {contatos[contato]["telefone"]}\n'
                 f'Twitter: {contatos[contato]["Twitter"]}\n'
                 f'Instagram: {contatos[contato]["Instagram"]}\n'
                 '-------------------------')


principal()
