import csv


def principal():
    while True:
        print(" === Agenda Telefônica === ")
        print(" 1- Criar contato")
        print(" 2- Alterar contato")
        print(" 3- Remover contato")
        print(" 4- Pesquisar contato")
        print(" 5- Listar contatos")
        print(" 6- Sair")

        opcao = input(" > ")
        if opcao not in '123456':
            print('Opção inválida. Insira um numero da lista.')
        elif opcao == '1':
            criar_contatos()
        # elif opcao == '2':
        #     alterar()
        # elif opcao == '3':
        #     remover()
        # elif opcao == '4':
        #     pesquisar()
        # elif opcao == '5':
        #     listar()
        elif opcao == '6':
            print("Saindo da agenda...")
            break


def criar_contatos():
    while True:
        try:
            quantidade_contatos = input('Quantidade de contatos a criar: ')
            for contato in range(int(quantidade_contatos)):
                criar_contato()
            principal()
        except ValueError:
            print("Caracter inválido!! Digite um número por favor!!")


def criar_contato():
    nome = input('Digite um nome: ')
    while nome.lower() in mudar_minuscula(lista_nomes()):
        print(f'O contato {nome} já existe. Cadastre outro')
        nome = input('Digite um nome: ')

    email = input("Digite um email: ")
    while not validar_email(email):
        print(f'Email [{email}] não válido. Bota email certo pfv!')
        email = input('Digite um novo email: ')

    telefone = input("Digite um telefone, números só: ")
    while not validar_telefone(telefone):
        print(f'O telefone [{telefone}] tá errado bota telefone certo pfv!')
        telefone = input("Digite um telefone: ")

    twitter = input("Digite um Twitter: ")
    instagram = input("Digite um Instagram: ")

    etiquetas = ['nome', 'email', 'telefone', 'twitter', 'instagram']

    contato = {
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "twitter": twitter,
        "instagram": instagram
    }

    with open('agenda_telefonica.csv', 'a') as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=etiquetas)
        if abrir_cabeceira() != etiquetas:
            writer.writeheader()
        writer.writerow(contato)
    print(f"O contato {nome} foi cadastrado com sucesso!")


# TODO borrar si no se ua
def contato_existe(nome):
    contatos = abrir_agenda()
    for contato in contatos:
        for chave, valor in contato.items():
            if chave == 'nome' and valor == nome:
                return contato


def lista_nomes():
    contatos = abrir_agenda()
    nomes = []
    for contato in contatos:
        nomes.append(contato['nome'])
    return nomes


def abrir_cabeceira():
    with open('agenda_telefonica.csv', 'r') as ficheiro:
        reader = csv.reader(ficheiro)
        for linha in reader:
            return linha


def abrir_agenda():
    contatos = []
    with open('agenda_telefonica.csv', 'r') as arquivo:
        for line in csv.DictReader(arquivo):
            contatos.append(line)
    return contatos


def mudar_minuscula(lista):
    for nome in range(len(lista)):
        lista[nome] = lista[nome].lower()
    return lista


def validar_email(email):
    import re

    formato = '^[^@\s]+@[^@\s]+\.[^@\s]+$'
    if re.match(formato, email):
        return True
    return False


def validar_telefone(telefone):
    try:
        int(telefone)
        return True
    except ValueError:
        return False


principal()
