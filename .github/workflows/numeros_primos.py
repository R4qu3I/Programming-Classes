numero=int(input("Digite um número: "))
if numero > 1:
    for i in range (2,numero):
        if (numero % i) == 0:
            print(f"O número {numero} não é primo!")
            break
        else:
            print(f"O número {numero} é primo!")
            break
else:
    print(f"O número {numero} não é primo!")
