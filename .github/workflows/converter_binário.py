num = float(input("Digite o número que deseja converter para binário: "))

partes = str(num).split(".")

parte_int = int(partes[0])
parte_dec = float("0." + partes[1])

binario_int = ""

while parte_int:
    binario_int = str(parte_int % 2) + binario_int
    parte_int //= 2

binario_dec = []

while parte_dec:
    parte_dec *= 2
    x = int(parte_dec)
  
    if x == 1:
        parte_dec -= x
        binario_dec.append("1") # .append acrescenta dentro da lista

    else:
        binario_dec.append("0")

binario = binario_int + "." + "".join(binario_dec) # .join vai adicionar o resultado na string
print(binario)
