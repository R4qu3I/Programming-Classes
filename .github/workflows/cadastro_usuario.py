import sys

def exibir_menu():
    print("\n+++ MENU DE CADASTRO +++\n")
    print("1. Cadastrar usuário")
    print("2. Mostrar dados cadatrados")
    print("3. Sair")

def cadastrar_usuario():
    print("\n+++ COMPLETE AS INFORMAÇÕES ABAIXO +++\n ")
    global nome
    nome=input("Digite o seu nome: ")
    global idade
    idade=int(input("Digite a sua idade: "))
    global genero
    genero=input("Digite o seu gênero: ")
    global cpf
    cpf=input("Digite o seu CPF: ")
    global email
    email=input("Digite o seu e-mail: ")
    global tel
    tel=input("Digite o seu número de telefone: ")

def dados_cadastrados():
    print("\n+++ DADOS CADASTRADOS +++ \n ")
    print("Nome: ",nome)
    print("Idade: ",idade)
    print("Genero: ",genero)
    print("CPF: ",cpf)
    print("E-mail: ",email)
    print("Telefone:",tel)

def main():
    while True:
        exibir_menu()

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            dados_cadastrados()
        elif opcao == "3":
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
