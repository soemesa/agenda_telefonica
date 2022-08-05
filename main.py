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
                criar()
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


def criar():
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
            "twitter": twitter,
            "instagram": instagram
        }
    }
    contatos.update(contato)
    print(f"O contato {nome} foi cadastrado com sucesso!")

    salvar_arquivo(contatos)


def alterar():
    nome = input("Digite o nome a ser alterado: ")

    contatos = procura_contato_em_arquivo(nome)
    try:

        for chave in contatos.keys():
            # TODO editar contato
            nome = input("Digite um novo nome: ").strip()
            email = input("Digite um novo email: ").strip()
            telefone = input("Digite um novo telefone: ").strip()
            twitter = input("Digite um novo Twitter: ").strip()
            instagram = input("Digite um novo Instagram: ").strip()

            contatos[chave]['email'] = email
            contatos[chave]['telefone'] = telefone
            contatos[chave]['twitter'] = twitter
            contatos[chave]['instagram'] = instagram
        contatos[nome] = contatos.pop(chave)
        salvar_arquivo(contatos)
        print("Contato atualizado com sucesso!!")

    except AttributeError:
        print("Contato inexistente!!")


def remover():
    nome = input("Digite um nome: ")

    contatos = procura_contato_em_arquivo(nome)

    for nome in contatos.keys():
        pass
    contatos.pop(nome)
    print(f"O contato {nome} foi removido com sucesso!")

    salvar_arquivo(contatos)


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
