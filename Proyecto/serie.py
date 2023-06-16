from producto import Producto

class Serie(Producto):
    def __init__(self, titulo, actor_principal, director, temporadas):
        super().__init__(titulo)
        self.actor_principal = actor_principal
        self.director = director
        self.temporadas = temporadas
        self.costo_renta = 0
        self.costo_venta = 0
