# CLASES: HERENCIA Y MULTIHERENCIA

class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def describir(self):
        return f"{self.nombre} (Especie: {self.especie})"

class Mamifero(Animal):
    def __init__(self, nombre, especie, pelaje):
        super().__init__(nombre, especie)
        self.pelaje = pelaje

    def amamantar(self):
        return f" {self.nombre} amamanta a sus crías (Pelaje: {self.pelaje})"

class Ave(Animal):
    def __init__(self, nombre, especie, envergadura):
        super().__init__(nombre, especie)
        self.envergadura = envergadura

    def volar(self):
        return f" {self.nombre} vuela con {self.envergadura} cm de envergadura"

# Multiherencia: Murciélago es Mamífero + Ave
class Murcielago(Mamifero, Ave):
    def __init__(self, nombre, pelaje, envergadura):
        Mamifero.__init__(self, nombre, "Murciélago", pelaje)
        Ave.__init__(self, nombre, "Murciélago", envergadura)

    def ecolocalizacion(self):
        return f" {self.nombre} usa SONAR para orientarse"

# INTERACCIÓN CON USUARIO

zoo = []  # Base de datos de animales

def agregar_animal():
    print("\n TIPOS DE ANIMALES:")
    print("1. Mamífero\n2. Ave\n3. Murciélago")
    tipo = input("Selecciona el tipo (1/2/3): ")

    nombre = input("Nombre del animal: ")
    especie = input("Especie: ")

    if tipo == "1":
        pelaje = input("Tipo de pelaje: ")
        animal = Mamifero(nombre, especie, pelaje)
    elif tipo == "2":
        envergadura = input("Envergadura (cm): ")
        animal = Ave(nombre, especie, envergadura)
    elif tipo == "3":
        pelaje = input("Pelaje: ")
        envergadura = input("Envergadura (cm): ")
        animal = Murcielago(nombre, pelaje, envergadura)
    else:
        print("Opción inválida")
        return

    zoo.append(animal)
    print(f" {animal.describir()} agregado al zoológico!")

def listar_animales():
    if not zoo:
        print("\n El zoológico está vacío")
        return

    print("\n ANIMALES EN EL ZOOLÓGICO:")
    for animal in zoo:
        print(f"\n{animal.describir()}")
        if isinstance(animal, Mamifero):
            print(animal.amamantar())
        if isinstance(animal, Ave):
            print(animal.volar())
        if isinstance(animal, Murcielago):
            print(animal.ecolocalizacion())

# MENÚ PRINCIPAL

while True:
    print("\n" + "="*30)
    print(" ZOOLÓGICO ")
    print("="*30)
    print("1. Agregar animal")
    print("2. Listar animales")
    print("3. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_animal()
    elif opcion == "2":
        listar_animales()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print(" Opción no válida")