import json

def inserir(diccionario):
    nome = input("Digite seu nome: ")
    contato = {
        nome: {
            "email": input("Digite seu email: "),
            "telefone": input("Digite seu telefone: "),
            "Twitter": input("Digite seu Twitter: "),
            "Instragram": input("Digite o Instagram: ")
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
    pass


def listar():
    pass


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


principal()
