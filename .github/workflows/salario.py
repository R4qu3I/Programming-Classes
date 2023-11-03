## CADASTRAR USUARIO E MOSTRAR DADOS
import sys

def exibir_menu():
    print("Menu:")
    print("1. Adicionar novo usuário:")
    print("2. Exibir usuários cadastrados:")
    print("3. Exibir descontos:")
    print("4. Sair")

def adicionar_usuario():
    print("Complete as informações abaixo:")
    global nome
    nome=input("Digite seu nome: ")
    global salario
    salario=float(input("Digite o seu salário: "))
    global cargo
    cargo=input("Digite seu cargo: ")
    global setor
    setor=input("Digite o seu setor: ")
    global faltas
    faltas=int(input("Digite a quantidade de faltas: "))
    print("Nova usuário adicionado!")

def usuarios_cadastrados():
    print("Usuários cadastrados:")
    print("- Raquel")
    
def exibir_descontos():
    print("Descontos existentes:")    

    desc_falt=((salario/30)*faltas)
    print("- Faltas: ",desc_falt)
    
    vt=float((6/100)*salario)
    print("- Vale transporte: ",vt)

    fgts=float((8/100)*salario)
    print("- FGTS: ",fgts)
    
    irpf=float((9/100)*salario)
    if salario <= 1903.99:
        irpf=0

    elif salario <= 2826.66:
        irpf=7.5/100

    elif salario <= 3751.05:
        irpf=15/100
    
    elif salario <= 4664.68:
        irpf=22.5/100

    else:
        irpf=27.5/100
    print("- IRPF: ",fgts)

    medico=float((1/100)*salario)
    print("- Convênio médico: ",medico)

    odonto=float((0.5/100)*salario)
    print("- Plano odontológico: ",odonto)

    descontos=(desc_falt+vt+fgts+irpf+medico+odonto)
    print("Todal de descontos: ",descontos)

    liquido=salario-descontos
    print("O seu salário líquido é de: ",liquido)
        

def main():
    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_usuario()
        elif opcao == "2":
            usuarios_cadastrados()
        elif opcao == "3":
            exibir_descontos()
        elif opcao == "4":
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
