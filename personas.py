class Personas:

    def __init__(self, nombre, apellido, fn):

        self. nombre = nombre
        self. apellido = apellido
        self. fn = fn

    def caminar(self):
        print("Unos Pokémon vuelan al cielo, pero yo puedo CAMINAR, CAMINAR")

    def estudiar(self, materia, notas):
        print(f"Estoy perdiendo {materia}")
        return notas