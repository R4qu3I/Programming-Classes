# GABARITO 1-D/ 2-B/ 3-C/ 4-A/ 5-D/ 6-B


#QUESTÃO 4
A=10
B=20
print(B)
B=5
print(A,B)


#QUESTÃO 5
A=30
B=20
C=A+B
print(C)
B=10
print(B,C)
C=A+B
print(A,B,C)


#QUESTÃO 6 - não tem o mesmo resultado
A=4/(2+4)/4
a=(4/2+2/4)
print(A,a)
B=4/(2+2)/4
b=4/2+2/4
print(B,b)


#QUESTÃO 7 - algoritmo que leia N1, N2 de um aluno. Calcular média e exibir. Usar menu e fila
import sys
n1=[]
n2=[]


def exibir_menu():
    print("¨¨¨¨MENU¨¨¨¨")
    print("1. Cadastrar notas: ")
    print("2. Verificar média: ")
    print("3. Sair")


def cadastrar_notas():


    n_1=float(input("Digite a nota da primeira prova: "))
    n1.append(n_1)
    n_2=float(input("Digite a nota da segunda prova: "))
    n2.append(n_2)
    print("Notas cadastradas!")


def verificar_media():
    media=((n1[0]+n2[0])/2) #colchetes para saber a posição que está gravada
    print(f"Sua média é igual a: {media}")


def main():
    while True:
        exibir_menu()


        opcao=input("Escolha uma opção: ")


        if opcao == "1":
            cadastrar_notas()
        elif opcao == "2":
            verificar_media()
        elif opcao == "3":
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()


#QUESTÃO 8 - algoritmo p/ determinar que se o aluno tem média acima de 75%, está aprovado, senão, retido
nome=input("Digite o nome do aluno: ")
aulas_tt=float(input("Digite a quantidade total de aulas do curso: "))
qtd_presenca=int(input("Digite a quantidade de aulas frequentadas: "))


frequencia=float((qtd_presenca/aulas_tt)*100)


if frequencia > 75:
    print(f"Você está aprovado com a frequência igual a {frequencia}")
else:
    print(f"Você está reprovado com a frequência igual a {frequencia}!")
