def calcular_punto_equidistante(panaderia, cafeteria, cine):
    """
    Calcula el punto equidistante a tres ubicaciones dadas.
    
    Args:
        panaderia (tuple): Coordenadas (x, y) de la panadería
        cafeteria (tuple): Coordenadas (x, y) de la cafetería
        cine (tuple): Coordenadas (x, y) del cine
    
    Returns:
        tuple: Coordenadas (x, y) del punto equidistante o None si no existe
    """
    a, b = panaderia
    c, d = cafeteria
    e, f = cine
    
    # Calculamos coeficientes para las ecuaciones
    A = 2 * (c - a)
    B = 2 * (d - b)
    C = a**2 + b**2 - c**2 - d**2
    
    D = 2 * (e - a)
    E = 2 * (f - b)
    F = a**2 + b**2 - e**2 - f**2
    
    denominador = A * E - B * D
    
    if denominador == 0:
        return None
    
    x = (C * E - B * F) / denominador
    y = (A * F - C * D) / denominador
    
    return (x, y)

def ingresar_coordenada(nombre_punto):
    """
    Función para ingresar coordenadas con validación
    """
    while True:
        try:
            x = float(input(f"Ingrese coordenada x para {nombre_punto}: "))
            y = float(input(f"Ingrese coordenada y para {nombre_punto}: "))
            return (x, y)
        except ValueError:
            print("Por favor ingrese números válidos.")

if __name__ == "__main__":
    print("Calculador de punto equidistante a tres ubicaciones")
    print("Por favor ingrese las coordenadas de cada lugar\n")
    
    # Ingreso de coordenadas
    print("== Panadería ==")
    panaderia = ingresar_coordenada("la panadería (a,b)")
    
    print("\n== Cafetería ==")
    cafeteria = ingresar_coordenada("la cafetería (c,d)")
    
    print("\n== Cine ==")
    cine = ingresar_coordenada("el cine (e,f)")
    
    # Cálculo del punto equidistante
    resultado = calcular_punto_equidistante(panaderia, cafeteria, cine)
    
    # Mostrar resultados
    print("\n" + "="*40)
    print("\nUbicaciones ingresadas:")
    print(f"- Panadería (a,b): {panaderia}")
    print(f"- Cafetería (c,d): {cafeteria}")
    print(f"- Cine (e,f): {cine}")
    
    if resultado:
        g, h = resultado
        print(f"\nEl punto equidistante (g,h) es: ({g:.2f}, {h:.2f})")
    else:
        print("\nLos tres puntos están alineados, no existe un punto equidistante único.")
    
    input("\nPresione Enter para salir...")