def solicitar_cita():
    respuesta = input("¿Desea solicitar una cita médica? (si/no): ").strip().lower()
    if respuesta not in ["si", "sí", "s"]:
        print("Gracias, que tenga un buen día.")
        return
    
    nombre = input("Ingrese su nombre completo: ").strip()
    numero_id = input("Ingrese su número de identificación: ").strip()
    
    print("Seleccione una opción:")
    print("1. Quiero una cita en un día y hora específica")
    print("2. Estoy disponible para cualquier día")
    
    while True:
        try:
            opcion = int(input("Ingrese 1 o 2: "))
            if opcion in [1, 2]:
                break
            print("Por favor, seleccione una opción válida.")
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")
    
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    momentos = ["mañana", "tarde", "noche"]
    
    if opcion == 1:
        print("Días disponibles para cita médica:")
        for i, dia in enumerate(dias_semana, start=1):
            print(f"{i}. {dia}")
        
        while True:
            try:
                dia_elegido = int(input("Seleccione el número del día: "))
                if 1 <= dia_elegido <= len(dias_semana):
                    dia_seleccionado = dias_semana[dia_elegido - 1]
                    break
                print("Por favor, seleccione una opción válida.")
            except ValueError:
                print("Entrada inválida. Ingrese un número válido.")
        
        print("Seleccione el horario:")
        for i, momento in enumerate(momentos, start=1):
            print(f"{i}. {momento}")
        
        while True:
            try:
                momento_elegido = int(input("Seleccione el número del horario: "))
                if 1 <= momento_elegido <= len(momentos):
                    momento_seleccionado = momentos[momento_elegido - 1]
                    break
                print("Por favor, seleccione una opción válida.")
            except ValueError:
                print("Entrada inválida. Ingrese un número válido.")
        
    else:
        dia_seleccionado = dias_semana[len(nombre) % len(dias_semana)]
        momento_seleccionado = momentos[len(numero_id) % len(momentos)]
    
    print(f"La cita médica ha sido asignada para el {dia_seleccionado} en la {momento_seleccionado} para {nombre}.")

if __name__ == "__main__":
    solicitar_cita()
