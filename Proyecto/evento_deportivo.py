from producto import Producto

class EventoDeportivo(Producto):
    def __init__(self, titulo, deporte, fecha, hora, lugar):
        super().__init__(titulo)
        self.deporte = deporte
        self.fecha = fecha
        self.hora = hora
        self.lugar = lugar
        self.costo_venta = 0
