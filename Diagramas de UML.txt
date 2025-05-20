# cultivo.py
class Cultivo:
    def __init__(self, nombre: str, tipo: str, area: float, rendimiento: float):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__area = area
        self.__rendimiento = rendimiento

    # Getters y Setters
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    # ... Repetir para otros atributos (tipo, area, rendimiento)

    def calcular_produccion(self):
        return self.__area * self.__rendimiento