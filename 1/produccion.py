# produccion.py
class Produccion:
    @staticmethod
    def calcular_total_cultivos(cultivos: list):
        return sum(c.calcular_produccion() for c in cultivos)
    
    @staticmethod
    def calcular_total_ganado(animales: list):
        return sum(a.calcular_produccion() for a in animales)
    
    @staticmethod
    def calcular_total_granja(cultivos: list, animales: list):
        return Produccion.calcular_total_cultivos(cultivos) + Produccion.calcular_total_ganado(animales)