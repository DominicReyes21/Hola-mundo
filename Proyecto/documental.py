from producto import Producto

class Documental(Producto):
    def __init__(self, titulo, director, tema, año):
        super().__init__(titulo)
        self.director = director
        self.tema = tema
        self.año = año
        self.costo_renta = 0
        self.costo_venta = 0
