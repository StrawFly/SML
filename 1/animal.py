# animal.py
class Animal:
    def __init__(self, especie: str, raza: str, edad: int, peso: float):
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso

    # Getters y Setters
    @property
    def especie(self):
        return self.__especie
    
    @especie.setter
    def especie(self, value):
        self.__especie = value

    # ... Repetir para otros atributos (raza, edad, peso)

    def calcular_produccion(self):
        return self.__peso  # Ejemplo básico