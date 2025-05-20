from personas import Personas
from calculadora import CalculadoraDeNotas

personas1 = Personas ("Miguel", "Paez", "24-05-2011")

print("el nombris de la persona 1 es: ", {personas1. nombre})

personas1.caminar()

notas = personas1.estudiar ("Programación ", [3.3, 2.2, 3.0, 1.0] )
print(f"mira esas notas {notas}")

promedio = sum (notas) / len(notas)
print (promedio)

calcularpersona1 = CalculadoraDeNotas(notas)

calcularpersona1. calcularpromedio()
calcularpersona1. notamaxima()
calcularpersona1. notaminima()
calcularpersona1. validaraprobación(promedio)