binario = input("Ingresa un número binario de maximo 8 digitos: ")
decimal = 0
i=0
for cont in binario:
    i+=1

if i == 8:
    for bit in binario:
        decimal = decimal * 2 + int(bit)

    print("El número binario a decimal es:", decimal)
else:
    print("el numero no cumple con la cantidad de bits")