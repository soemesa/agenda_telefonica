import csv


# Função que ejecuta e mostra na tela o menu principal com as opções(criar, pesquisar, listar, alterar, remover e sair)
# Ao escolher lança uma função
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
        elif opcao == '5':
            remover()
        elif opcao == '6':
            print("Saindo da agenda...")
            break


# Função que pergunta ao usuario a quantidade de contatos a criar e finaliza quando o numero de contatos atingiu ao limite
def criar_contatos():
    while True:
        try:
            quantidade_contatos = input('Quantidade de contatos a criar: ')
            for contato in range(int(quantidade_contatos)):
                criar_contato()
            principal()
        except ValueError:
            print("Caracter inválido!! Digite um número por favor!!")


# Função que pergunta ao usuário o nome, o telefone, e-mail, Twitter e Instagram e salva um contato em arquivo csv
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


# Função que retorna tudos os nomes dos contatos cadastrados e os armaneza numa lista
def lista_nomes():
    contatos = abrir_agenda()
    nomes = []
    for contato in contatos:
        nomes.append(contato['nome'])
    return nomes


# Função para obter primeira linha do arquivo que contem encabeçado
def abrir_cabeceira():
    with open('agenda_telefonica.csv', 'r') as ficheiro:
        reader = csv.reader(ficheiro)
        for linha in reader:
            return linha


# Função que retorna uma lista de dicionarios com todas as linhas do arquivo CSV
def abrir_agenda():
    contatos = []
    try:
        with open('agenda_telefonica.csv', 'r') as arquivo:
            for line in csv.DictReader(arquivo):
                contatos.append(line)
        return contatos
    except FileNotFoundError:
        return {}


# Função que pega uma lista como parámetro e retorna ela em minusculas
def mudar_minuscula(lista):
    for item in range(len(lista)):
        lista[item] = lista[item].lower()
    return lista


# Função que pega um nombre por consola e procura em arquivo CSV.
# Se o nome existe imprime na tela.
def pesquisar():
    nome = input('Digite um nome: ')
    encontrado = False

    try:
        with open('agenda_telefonica.csv', 'r') as arquivo:
            arquivo = csv.reader(arquivo, delimiter=',')

            for linha in arquivo:
                if nome.lower() in mudar_minuscula(linha):
                    print(f"{'nome':^8} | {'email':^16} | {'telefone':^10} | {'twitter':^10} | {'instagram':^10}")
                    print(f"{'-' * 8} | {'-' * 16} | {'-' * 10} | {'-' * 10} | {'-' * 10}")
                    print(f'{linha[0]:^8} | {linha[1]:^16} | {linha[2]:^10} | {linha[3]:^10} | {linha[4]:^10}')
                    print(f"{'-' * 8} | {'-' * 16} | {'-' * 10} | {'-' * 10} | {'-' * 10}")
                    encontrado = True
            if not encontrado:
                print('Contato não encontrado!')
    except FileNotFoundError:
        print('Contato não encontrado!')


# Função que mostra na tela todos os contatos que exitem no arquivo CSV.
def listar():
    try:
        with open('agenda_telefonica.csv', 'r') as arquivo:
            arquivo = csv.reader(arquivo, delimiter=',')

            num = -1
            etiquetas = ['nome', 'email', 'telefone', 'twitter', 'instagram']

            for linha in arquivo:
                num += 1
                if etiquetas == linha:
                    print(
                        f"{'num':^3} | {'nome':^8} | {'email':^16} | {'telefone':^10} | {'twitter':^10} | {'instagram':^10}")
                    print(f"{'-' * 3} | {'-' * 8} | {'-' * 16} | {'-' * 10} | {'-' * 10} | {'-' * 10}")
                else:
                    print(
                        f'{num:^3} | {linha[0]:^8} | {linha[1]:^16} | {linha[2]:^10} | {linha[3]:^10} | {linha[4]:^10}')
        print(f"{'-' * 3} | {'-' * 8} | {'-' * 16} | {'-' * 10} | {'-' * 10} | {'-' * 10}")
    except FileNotFoundError:
        print('Não existem contatos cadastrados! \n')


# Função que pega nome pasado e procura no arquivo mudando todos seus elementos e savando em arquivo CSV.
def alterar():
    nome = input('Digite o nome que deseja alterar: ')
    alterado = False
    contatos = abrir_agenda()
    for contato in contatos:
        if nome.lower() == contato['nome'].lower():
            nome = input('Digite um novo nome: ')
            while nome.lower() in mudar_minuscula(lista_nomes()):
                print(f'O contato {nome} já existe. Cadastre outro')
                nome = input('Digite um nome: ')

            email = input('Digite um novo email: ')
            while not validar_email(email):
                print(f'Email [{email}] não válido. Bota email certo pfv!')
                email = input('Digite um novo email: ')

            telefone = input('Digite um novo telefone: ')
            while not validar_telefone(telefone):
                print(f'O telefone [{telefone}] tá errado bota telefone certo pfv!')
                telefone = input("Digite um telefone: ")

            twitter = input('Digite um novo twitter: ')
            instagram = input('Digite um novo instagram: ')

            contato_entrada = f"{contato['nome']},{contato['email']},{contato['telefone']},{contato['twitter']},{contato['instagram']}"
            contato_saida = f'{nome},{email},{telefone},{twitter},{instagram}'

            text = open("agenda_telefonica.csv", "r")
            text = ''.join([i for i in text]).replace(contato_entrada, contato_saida)
            x = open("agenda_telefonica.csv", "w")
            x.writelines(text)
            x.close()
            alterado = True
            print('Contato atualizado com sucesso!')
    if not alterado:
        print('Contato não encontrado!')


# Função que apaga contato do arquivo CSV usando o nome pasado pela consola.
def remover():
    nome_in = input('Digite o nome a remover: ')
    try:
        # Abrir arquivo em modo leitura e salva em lista.
        with open("agenda_telefonica.csv", "r") as arquivo:
            arquivo = csv.reader(arquivo, delimiter=',')
            lista = list(arquivo)

        # Abrir arquivo em modo escritura e salva linha a linha se é distinto do nome.
        with open("agenda_telefonica.csv", "w") as file:
            writer = csv.writer(file, delimiter=',', lineterminator='\n')
            elementos = []
            for linha in lista:
                for item in linha:
                    elementos.append(item)
                nome, email, telefone, twitter, instagram = linha
                if nome_in.lower() != nome.lower():
                    writer.writerow(linha)
                else:
                    print('Contato apagado com sucesso!')

        if not nome_in in elementos:
            print('O Contato não existe')
    except FileNotFoundError:
        print('Não existem contatos cadastrados!')


# Função para validar se o email é correto
def validar_email(email):
    import re
    formato = '^[^@\s]+@[^@\s]+\.[^@\s]+$'
    if re.match(formato, email):
        return True
    return False


# Função para valir se o telefone pasado é um número.
def validar_telefone(telefone):
    try:
        int(telefone)
        return True
    except ValueError:
        return False


remover()
