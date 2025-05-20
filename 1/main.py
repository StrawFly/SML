# main.py
from granja import Granja
from cultivo import Cultivo
from animal import Animal

# Ejemplo de uso
mi_granja = Granja()

# Agregar cultivos
mi_granja.agregar_cultivo(Cultivo("Maíz", "Cereal", 50.0, 10.5))
mi_granja.agregar_cultivo(Cultivo("Trigo", "Cereal", 30.0, 8.2))

# Agregar animales
mi_granja.agregar_animal(Animal("Vaca", "Holstein", 3, 650.0))
mi_granja.agregar_animal(Animal("Cerdo", "Duroc", 2, 120.0))

# Generar reporte
mi_granja.generar_reporte()