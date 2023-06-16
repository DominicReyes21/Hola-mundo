from producto import Producto

class Pelicula(Producto):
    def __init__(self, titulo, actor_principal, director, año):
        super().__init__(titulo)
        self.actor_principal = actor_principal
        self.director = director
        self.año = año
        self.costo_renta = 0
        self.costo_venta = 0
