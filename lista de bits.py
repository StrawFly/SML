binario = input("Ingresa un número binario de máximo 8 dígitos: ").strip()

if 1 <= len(binario) <= 8 and all(bit in "01" for bit in binario) :
    decimal = 0
    longitud = len(binario)  # Determinar cuántos bits tiene la entrada

    for i, bit in enumerate(binario):
        decimal += int(bit) * (2 ** i)

    print("El número binario leído de izquierda a derecha en decimal es:", decimal)
else:
    print("Error: Ingresa un número binario válido de hasta 8 dígitos.")