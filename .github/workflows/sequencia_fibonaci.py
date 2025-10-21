n=int(input("Digite a quantidade de termos você quer mostrar: "))
n1=1
n2=1
print("{}".format(n1)) # .format retorna a string formatada com o valor passado no lugar das chaves
print("{}".format(n2))
cont=3
while cont <= n:
    n3=n1+n2
    print("{}".format(n3))
    n1=n2
    n2=n3
    cont += 1 # += vai somar e substituir o valor
