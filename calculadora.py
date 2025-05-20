class CalculadoraDeNotas:

    def __init__(self, notas):

        self. notas = notas

    def calcularpromedio(self):
        print(f"El promedio es: {sum(self.notas)/len(self.notas)}")

    def notamaxima(self):
        print(f"La nota maxima es: {max(self.notas)}")

    def notaminima(self):
        print(f"La nota minima es: {min(self.notas)}")

    def validaraprobación(self, promedio):
        if promedio >= 3.0:
            print("aprobastes felicidad")

        else:
            print("No aprobastes triste")