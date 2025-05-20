# granja.py
from cultivo import Cultivo
from animal import Animal
from produccion import Produccion

class Granja:
    def __init__(self):
        self.__cultivos = []
        self.__animales = []
    
    # Métodos CRUD para cultivos
    def agregar_cultivo(self, cultivo: Cultivo):
        self.__cultivos.append(cultivo)
    
    def eliminar_cultivo(self, index: int):
        del self.__cultivos[index]
    
    # ... Métodos similares para editar y consultar
    
    # Métodos CRUD para animales
    def agregar_animal(self, animal: Animal):
        self.__animales.append(animal)
    
    # ... Métodos similares para editar y eliminar
    
    def generar_reporte(self):
        total_cultivos = Produccion.calcular_total_cultivos(self.__cultivos)
        total_ganado = Produccion.calcular_total_ganado(self.__animales)
        total = Produccion.calcular_total_granja(self.__cultivos, self.__animales)
        
        print(f"Reporte de Producción:\n"
              f"Cultivos: {total_cultivos} kg\n"
              f"Ganado: {total_ganado} kg\n"
              f"Total: {total} kg")