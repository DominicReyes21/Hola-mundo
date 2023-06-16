from producto import Producto
from pelicula import Pelicula
from serie import Serie
from documental import Documental
from evento_deportivo import EventoDeportivo

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("El producto se ha agregado correctamente.")

    def buscar_producto(self, palabra_clave):
        resultados = []
        for producto in self.productos:
            if palabra_clave.lower() in producto.titulo.lower():
                resultados.append(producto)

        if resultados:
            print("Resultados de búsqueda:")
            for producto in resultados:
                if isinstance(producto, Pelicula):
                    print(f"Película: {producto.titulo}")
                elif isinstance(producto, Serie):
                    print(f"Serie: {producto.titulo}")
                elif isinstance(producto, Documental):
                    print(f"Documental: {producto.titulo}")
                elif isinstance(producto, EventoDeportivo):
                    print(f"Evento deportivo en vivo: {producto.titulo}")
        else:
            print("No se encontraron productos que coincidan con la búsqueda.")

    def eliminar_producto(self, titulo):
        for producto in self.productos:
            if producto.titulo.lower() == titulo.lower():
                self.productos.remove(producto)
                print("El producto se ha eliminado correctamente.")
                return

        print("No se encontró el producto especificado.")

    def mostrar_catalogo(self, opcion):
        if opcion == "1":
            self.mostrar_peliculas()
        elif opcion == "2":
            self.mostrar_series()
        elif opcion == "3":
            self.mostrar_documentales()
        elif opcion == "4":
            self.mostrar_eventos_deportivos()
        elif opcion == "5":
            self.mostrar_todo()
        else:
            print("Opción inválida.")

    def mostrar_peliculas(self):
        peliculas = [producto for producto in self.productos if isinstance(producto, Pelicula)]
        self.mostrar_productos(peliculas, "Películas")

    def mostrar_series(self):
        series = [producto for producto in self.productos if isinstance(producto, Serie)]
        self.mostrar_productos(series, "Series")

    def mostrar_documentales(self):
        documentales = [producto for producto in self.productos if isinstance(producto, Documental)]
        self.mostrar_productos(documentales, "Documentales")

    def mostrar_eventos_deportivos(self):
        eventos_deportivos = [producto for producto in self.productos if isinstance(producto, EventoDeportivo)]
        self.mostrar_productos(eventos_deportivos, "Eventos deportivos")

    def mostrar_todo(self):
        self.mostrar_productos(self.productos, "Catálogo completo")

    def mostrar_productos(self, productos, categoria):
        if productos:
            print(f"{categoria}:")
            for producto in productos:
                print(f"- {producto.titulo}")
        else:
            print(f"No hay {categoria} disponibles.")

    def cargar_catalogo(self, nombre_archivo):
        try:
            with open(nombre_archivo, "r") as archivo:
                # Lógica para cargar los productos desde el archivo
                print("El catálogo se ha cargado correctamente.")
        except FileNotFoundError:
            print("No se encontró el archivo especificado.")
        except:
            print("Ocurrió un error al cargar el catálogo.")

    def guardar_catalogo(self, nombre_archivo):
        try:
            with open(nombre_archivo, "w") as archivo:
                # Lógica para guardar los productos en el archivo
                print("El catálogo se ha guardado correctamente.")
        except:
            print("Ocurrió un error al guardar el catálogo.")

# Función para mostrar el menú principal
def mostrar_menu_principal():
    print("Menú principal")
    print("1. Agregar un producto")
    print("2. Buscar producto")
    print("3. Eliminar un producto")
    print("4. Mostrar el catálogo")
    print("5. Cargar catálogo")
    print("6. Guardar catálogo")
    print("7. Salir")

# Función para mostrar el menú de agregar producto
def mostrar_menu_agregar_producto():
    print("Menú agregar producto")
    print("1. Película")
    print("2. Serie")
    print("3. Documental")
    print("4. Evento deportivo en vivo")
    print("5. Regresar")

# Función para mostrar el menú de mostrar catálogo
def mostrar_menu_mostrar_catalogo():
    print("Menú mostrar catálogo")
    print("1. Películas")
    print("2. Series")
    print("3. Documentales")
    print("4. Eventos deportivos")
    print("5. Todo")
    print("6. Regresar")

# Función principal
def main():
    catalogo = Catalogo()

    while True:
        mostrar_menu_principal()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":  # Agregar un producto
            mostrar_menu_agregar_producto()
            opcion_agregar = input("Ingrese una opción: ")

            if opcion_agregar == "1":  # Agregar una película
                titulo = input("Ingrese el título: ")
                actor_principal = input("Ingrese el actor o actriz principal: ")
                director = input("Ingrese el director: ")
                año = input("Ingrese el año: ")
                pelicula_obj = Pelicula(titulo, actor_principal, director, año)
                catalogo.agregar_producto(pelicula_obj)
            elif opcion_agregar == "2":  # Agregar una serie
                titulo = input("Ingrese el título: ")
                actor_principal = input("Ingrese el actor o actriz principal: ")
                director = input("Ingrese el director: ")
                temporadas = input("Ingrese el número de temporadas: ")
                serie_obj = Serie(titulo, actor_principal, director, temporadas)
                catalogo.agregar_producto(serie_obj)
            elif opcion_agregar == "3":  # Agregar un documental
                titulo = input("Ingrese el título: ")
                director = input("Ingrese el director: ")
                tema = input("Ingrese el tema: ")
                año = input("Ingrese el año: ")
                documental_obj = Documental(titulo, director, tema, año)
                catalogo.agregar_producto(documental_obj)
            elif opcion_agregar == "4":  # Agregar un evento deportivo en vivo
                titulo = input("Ingrese el título: ")
                deporte = input("Ingrese el deporte: ")
                fecha = input("Ingrese la fecha: ")
                hora = input("Ingrese la hora: ")
                lugar = input("Ingrese el lugar: ")
                evento_deportivo_obj = EventoDeportivo(titulo, deporte, fecha, hora, lugar)
                catalogo.agregar_producto(evento_deportivo_obj)
            elif opcion_agregar == "5":  # Regresar
                continue
            else:
                print("Opción inválida.")
        elif opcion == "2":  # Buscar producto
            palabra_clave = input("Ingrese una palabra clave para la búsqueda: ")
            catalogo.buscar_producto(palabra_clave)
        elif opcion == "3":  # Eliminar un producto
            titulo = input("Ingrese el título del producto que desea eliminar: ")
            catalogo.eliminar_producto(titulo)
        elif opcion == "4":  # Mostrar el catálogo
            mostrar_menu_mostrar_catalogo()
            opcion_mostrar = input("Ingrese una opción: ")
            catalogo.mostrar_catalogo(opcion_mostrar)
        elif opcion == "5":  # Cargar catálogo
            nombre_archivo = input("Ingrese el nombre del archivo del catálogo: ")
            catalogo.cargar_catalogo(nombre_archivo)
        elif opcion == "6":  # Guardar catálogo
            nombre_archivo = input("Ingrese el nombre del archivo para guardar el catálogo: ")
            catalogo.guardar_catalogo(nombre_archivo)
        elif opcion == "7":  # Salir
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
