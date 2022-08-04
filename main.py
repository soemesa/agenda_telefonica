import json


def inserir():
    contatos = abrir_agenda()

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
    contatos.update(contato)
    print(f"O contato {nome} foi cadastrado com sucesso!")

    salvar_arquivo(contatos)


def alterar():
    pass


def remover():
    nome = input("Digite um nome: ")

    contatos = abrir_agenda()

    contatos.pop(nome)
    print(f"O contato {nome} foi removido com sucesso!")

    salvar_arquivo(contatos)

def pesquisar():
    contato_encontrado = False
    nome = input("Digite um nome: ")

    contato = procura_contato_em_arquivo(nome)

    imprimir_contato(contato)

    # except AttributeError:
    #     print("Não tem dados salvados! ")
    # if not contato_encontrado:
    #     print("Contato não encontrado!Tente novamente!")


def listar():
    contatos = abrir_agenda()
    try:
        for contato in contatos.keys():
            imprimir_contato(contato, contatos)
    except AttributeError:
        print("Não tem dados salvados! ")


def principal():
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
            inserir()
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
        return {}


def imprimir_contato(contato):
    for nome, valor in contato.items():
        return print('-------------------------\n'
                     f'nome: {nome}\n'
                     f'email: {valor["email"]}\n'
                     f'telefone: {valor["telefone"]}\n'
                     f'Twitter: {valor["Twitter"]}\n'
                     f'Instagram: {valor["Instagram"]}\n'
                     '-------------------------')


def salvar_arquivo(contatos):
    arquivo = open("agenda_telefonica.json", "w")
    json.dump(contatos, arquivo)
    arquivo.close()

def procura_contato_em_arquivo(nome):
    contatos = abrir_agenda()
    for contato, valor in contatos.items():
        if contato.lower() == nome.lower():
            return {contato: valor}


principal()
