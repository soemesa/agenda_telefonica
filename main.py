import json


def inserir(diccionario):
    contatos = abrir_agenda()
    diccionario.update(contatos)

    nome = input("Digite seu nome: ").strip()
    email = input("Digite seu email: ").strip()
    telefone = input("Digite seu telefone: ").strip()
    twitter = input("Digite seu Twitter: ").strip()
    instagram = input("Digite o Instagram: ").strip()

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
    contato_encontrado = False
    nome = input("Digite um nome: ")

    contatos = abrir_agenda()

    contatos.pop(nome)

    # TODO Guardar en una funcion
    arquivo = open("agenda_telefonica.json", "w")
    json.dump(contatos, arquivo)
    arquivo.close()


def pesquisar():
    contato_encontrado = False
    nome = input("Digite um nome: ")

    contatos = abrir_agenda()
    # TODO botar en funcion procura_contato
    try:
        for contato in contatos.keys():
            if contato.lower() == nome.lower():
                contato_encontrado = True
                imprimir_contato(contato, contatos)
    except AttributeError:
        print("Não tem dados salvados! ")
    if not contato_encontrado:
        print("Contato não encontrado!Tente novamente!")


def listar():
    contatos = abrir_agenda()
    try:
        for contato in contatos.keys():
            imprimir_contato(contato, contatos)
    except AttributeError:
        print("Não tem dados salvados! ")


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
    try:
        with open("agenda_telefonica.json", encoding='utf-8') as meu_json:
            contatos = json.load(meu_json)
        return contatos
    except FileNotFoundError:
        return ''

def imprimir_contato(contato, contatos):
    return print('-------------------------\n'
                 f'nome: {contato}\n'
                 f'email: {contatos[contato]["email"]}\n'
                 f'telefone: {contatos[contato]["telefone"]}\n'
                 f'Twitter: {contatos[contato]["Twitter"]}\n'
                 f'Instagram: {contatos[contato]["Instagram"]}\n'
                 '-------------------------')


principal()
