import json


def principal():
    try:
        while True:
            print(" === Agenda Telefônica === ")
            print(" 1- Criar contato")
            print(" 2- Alterar contato")
            print(" 3- Remover contato")
            print(" 4- Pesquisar contato")
            print(" 5- Listar contatos")
            print(" 6- Sair")

            opcao = int(input(" > "))
            if opcao == 1:
                criar_contatos()
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
    except ValueError:
        print("Opção inválida!! Selecione uma opçao da lista!!")


def criar_contato():
    contatos = abrir_agenda()

    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    telefone = input("Digite seu telefone: ")
    twitter = input("Digite seu Twitter: ")
    instagram = input("Digite o Instagram: ")

    contato = {
        nome: {
            "email": email,
            "telefone": telefone,
            "twitter": twitter,
            "instagram": instagram
        }
    }
    contatos.update(contato)
    print(f"O contato {nome} foi cadastrado com sucesso!")

    salvar_arquivo(contatos)


def criar_contatos():
    quantidade_contatos = int(input('Quantidade de contatos a criar: '))

    for contato in range(quantidade_contatos):
        criar_contato()

def alterar():
    nome = input("Digite o nome a ser alterado: ")
    contatos = abrir_agenda()
    contato_alterado = False
    try:
        for chave, valor in contatos.items():
            if chave.lower() == nome.lower():
                nome = input("Digite um novo nome: ")
                email = input("Digite um novo email: ")
                telefone = input("Digite um novo telefone: ")
                twitter = input("Digite um novo Twitter: ")
                instagram = input("Digite um novo Instagram: ")

                valor['email'] = email
                valor['telefone'] = telefone
                valor['twitter'] = twitter
                valor['instagram'] = instagram

                contatos[nome] = contatos.pop(chave)
                salvar_arquivo(contatos)
                contato_alterado = True
                print("Contato atualizado com sucesso!!")
        if contato_alterado == False:
            print('Contato inexistente!')
    except AttributeError:
        print("Contato inexistente!!")


def remover():
    nome = input("Digite um nome: ")
    contatos = procura_contato_em_arquivo(nome)

    try:
        for nome in contatos.keys():
            pass
        contatos.pop(nome)
        print(f"O contato {nome} foi removido com sucesso!")
        salvar_arquivo(contatos)
    except AttributeError:
        print('Não existem contatos crie um')


def pesquisar():
    nome = input("Digite um nome: ")
    contato = procura_contato_em_arquivo(nome)
    imprimir_contato(contato)


def listar():
    contatos = abrir_agenda()
    if len(contatos) == 0:
        return print('Não existem contatos cadastrados!!')
    imprimir_contato(contatos)


def abrir_agenda():
    try:
        with open("agenda_telefonica.json", encoding='utf-8') as meu_json:
            contatos = json.load(meu_json)
        return contatos
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}


def imprimir_contato(contato):
    try:
        for nome, valor in contato.items():
            print('-------------------------\n'
                  f'nome: {nome}\n'
                  f'email: {valor["email"]}\n'
                  f'telefone: {valor["telefone"]}\n'
                  f'Twitter: {valor["twitter"]}\n'
                  f'Instagram: {valor["instagram"]}\n'
                  '-------------------------')
    except AttributeError:
        print(f"Contato não encontrado!! Tente novamente!!")


def salvar_arquivo(contatos):
    arquivo = open("agenda_telefonica.json", "w")
    json.dump(contatos, arquivo)
    arquivo.close()


def procura_contato_em_arquivo(nome):
    contatos = abrir_agenda()

    for contato, valor in contatos.items():
        if contato.lower() == nome.lower():
            return {contato: valor}
        if contato == '':
            return {}


principal()
