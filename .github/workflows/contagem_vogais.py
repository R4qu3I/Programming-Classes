frase=input("Escreva uma frase aleatória: ")


def conta_vogais(string):
    string = string.lower() # .lower vai transformar maiúsculas p/ minúsculas para contar
    resultado = 0
    vogais = 'aeiou'
    for i in vogais:
        resultado += string.count(i) # .count irá contar
    return resultado


print(conta_vogais(frase))
