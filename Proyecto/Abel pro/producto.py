# Clase para representar los productos
class Producto:
    def __init__(self, tipo, titulo, actor_director, costo_renta=None, costo_venta=None, otros_datos=None):
        self.tipo = tipo
        self.titulo = titulo
        self.actor_director = actor_director
        self.costo_renta = costo_renta
        self.costo_venta = costo_venta
        self.otros_datos = otros_datos

    def __str__(self):
        return f"{self.tipo}: {self.titulo} - {self.actor_director}"
