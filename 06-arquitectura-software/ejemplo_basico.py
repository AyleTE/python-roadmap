# Simulación de MVC simple
class Modelo:
    def datos(self): return 'datos'
class Vista:
    def mostrar(self, datos): print(f'Mostrar: {datos}')
class Controlador:
    def __init__(self): self.modelo = Modelo(); self.vista = Vista()
    def ejecutar(self): self.vista.mostrar(self.modelo.datos())

Controlador().ejecutar()