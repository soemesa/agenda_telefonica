import csv


def principal():
    while True:
        print(" === Agenda Telefônica === ")
        print(" 1- Criar contato")
        print(" 2- Pesquisar contato")
        print(" 3- Listar contato")
        print(" 4- Alterar contato")
        print(" 5- Remover contatos")
        print(" 6- Sair")

        opcao = input(" > ")
        if opcao not in '123456':
            print('Opção inválida. Insira um numero da lista.')
        elif opcao == '1':
            criar_contatos()
        elif opcao == '2':
            pesquisar()
        elif opcao == '3':
            listar()
        elif opcao == '4':
            alterar()
        # elif opcao == '5':
        #     remover()
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
    try:
        with open('agenda_telefonica.csv', 'r') as arquivo:
            for line in csv.DictReader(arquivo):
                contatos.append(line)
        return contatos
    except FileNotFoundError:
        return {}


def mudar_minuscula(lista):
    for nome in range(len(lista)):
        lista[nome] = lista[nome].lower()
    return lista


# TODO retornar como se guarda
def pesquisar():
    nome = input('Digite um nome: ')
    encontrado = False

    with open('agenda_telefonica.csv', 'r') as arquivo:
        arquivo = csv.reader(arquivo, delimiter=',')

        for linha in arquivo:
            if nome.lower() in mudar_minuscula(linha):
                print(f'nome \t\t email \t\t telefone \t\t'
                      f'twitter \t\t instagram')
                print(f'{linha[0]} \t\t {linha[1]} \t\t\t {linha[2]} \t\t'
                      f'{linha[3]} \t\t {linha[4]}')
                encontrado = True
    if not encontrado:
        print('Contato não encontrado!')


def imprimir_contato(contato):
    contato = contato_existe(contato)
    print('loco')


def listar():
    with open('agenda_telefonica.csv', 'r') as arquivo:
        arquivo = csv.reader(arquivo, delimiter=',')

        num = 0
        for linha in arquivo:
            num += 1
            # print(linha)
            if not 'nome' or 'email' in linha:
                print(f"{'num':^3} | {'nome':^8} | {'email':^16} | {'telefone':^8} | {'twitter':^8} | {'instagram':^8}")
            print(f'{num:^3} | {linha[0]:^8} | {linha[1]:^16} | {linha[2]:^8} | {linha[3]:^8} | {linha[4]:^8}')
            print(f"{'-' * 3} | {'-' * 8} | {'-' * 16} | {'-' * 8} | {'-' * 8} | {'-' * 8}")


# def testando_listar():
#     with open('agenda_telefonica.csv', 'r') as arquivo:
#         arquivo = csv.reader(arquivo, delimiter=',')
#
#         print(f"{'nome':^10} | {'email':^16} | {'telefone':^12} | {'twitter':^10} | {'instagram':^10}")
#         print(f"{'-'*10} | {'-'*16} | {'-'*12} | {'-'*10} | {'-'*10}")
#
#         for linha in arquivo:
#

# TODO Ver como se comporta si el nombre tiene espacios
def alterar():
    nome = input('Digite o nome que deseja alterar: ')
    contatos = abrir_agenda()
    for contato in contatos:
        if nome.lower() == contato['nome'].lower():
            nome = input('Digite um novo nome: ')
            email = input('Digite um novo email: ')
            telefone = input('Digite um novo telefone: ')
            twitter = input('Digite um novo twitter: ')
            instagram = input('Digite um novo instagram: ')

            contato_entrada = f"{contato['nome']},{contato['email']},{contato['telefone']},{contato['twitter']},{contato['instagram']}"
            contato_saida = f'{nome},{email},{telefone},{twitter},{instagram}'

            text = open("agenda_telefonica.csv", "r")
            text = ''.join([i for i in text]).replace(contato_entrada, contato_saida)
            x = open("agenda_telefonica.csv", "w")
            x.writelines(text)
            x.close()


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


listar()
