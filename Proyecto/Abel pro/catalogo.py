import csv
from producto import Producto

class Catalogo:
    def __init__(self):
        self.catalogo = []

    def agregar_producto(self):
        print("\nMenú agregar producto")
        print("1. Película")
        print("2. Serie")
        print("3. Documental")
        print("4. Evento deportivo en vivo")
        print("5. Regresar")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            producto = self.crear_pelicula()
        elif opcion == "2":
            producto = self.crear_serie()
        elif opcion == "3":
            producto = self.crear_documental()
        elif opcion == "4":
            producto = self.crear_evento_deportivo()
        elif opcion == "5":
            return
        else:
            print("Opción inválida.")
            return

        self.catalogo.append(producto)
        print("Producto agregado correctamente.")

    def crear_pelicula(self):
        tipo = "Película"
        titulo = input("Ingresa el título: ")
        actor_director = input("Ingresa el actor o director: ")
        año = input("Ingresa el año: ")
        costo_renta, costo_venta = self.obtener_costos()

        return Producto(tipo, titulo, actor_director, costo_renta=costo_renta, costo_venta=costo_venta,
                        otros_datos=año)

    def crear_serie(self):
        tipo = "Serie"
        titulo = input("Ingresa el título: ")
        actor_director = input("Ingresa el actor o director: ")
        temporadas = input("Ingresa el número de temporadas: ")
        costo_renta, costo_venta = self.obtener_costos()

        return Producto(tipo, titulo, actor_director, costo_renta=costo_renta, costo_venta=costo_venta,
                        otros_datos=temporadas)

    def crear_documental(self):
        tipo = "Documental"
        titulo = input("Ingresa el título: ")
        director = input("Ingresa el director: ")
        tema = input("Ingresa el tema: ")
        año = input("Ingresa el año: ")
        costo_renta, costo_venta = self.obtener_costos()

        return Producto(tipo, titulo, director, costo_renta=costo_renta, costo_venta=costo_venta, otros_datos=tema)

    def crear_evento_deportivo(self):
        tipo = "Evento deportivo en vivo"
        titulo = input("Ingresa el título: ")
        deporte = input("Ingresa el deporte: ")
        fecha = input("Ingresa la fecha: ")
        hora = input("Ingresa la hora: ")
        lugar = input("Ingresa el lugar: ")
        costo_venta = input("Ingresa el costo de venta: ")

        return Producto(tipo, titulo, deporte, costo_venta=costo_venta, otros_datos=(fecha, hora, lugar))

    def obtener_costos(self):
        costo_renta = None
        costo_venta = None

        renta_venta = input("¿El producto está disponible para renta, venta o ambos? (Renta/Venta/Ambos): ")
        if renta_venta.lower() == "renta":
            costo_renta = input("Ingresa el costo de renta: ")
        elif renta_venta.lower() == "venta":
            costo_venta = input("Ingresa el costo de venta: ")
        elif renta_venta.lower() == "ambos":
            costo_renta = input("Ingresa el costo de renta: ")
            costo_venta = input("Ingresa el costo de venta: ")
        else:
            print("Opción inválida.")

        return costo_renta, costo_venta

    def buscar_producto(self):
        busqueda = input("Ingresa las palabras clave para buscar: ")
        resultados = []
        for producto in self.catalogo:
            if busqueda.lower() in producto.titulo.lower():
                resultados.append(producto)

        if resultados:
            print("\nResultados de la búsqueda:")
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con esa búsqueda.")

    def eliminar_producto(self):
        titulo = input("Ingresa el título del producto a eliminar: ")
        encontrado = False

        for producto in self.catalogo:
            if producto.titulo.lower() == titulo.lower():
                self.catalogo.remove(producto)
                print("Producto eliminado correctamente.")
                encontrado = True
                break

        if not encontrado:
            print("No se encontró un producto con ese título.")

    def mostrar_catalogo(self):
        print("\nMenú mostrar catálogo")
        print("1. Películas")
        print("2. Series")
        print("3. Documentales")
        print("4. Eventos deportivos")
        print("5. Todo")
        print("6. Regresar")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            self.mostrar_productos("Película")
        elif opcion == "2":
            self.mostrar_productos("Serie")
        elif opcion == "3":
            self.mostrar_productos("Documental")
        elif opcion == "4":
            self.mostrar_productos("Evento deportivo en vivo")
        elif opcion == "5":
            self.mostrar_productos()
        elif opcion == "6":
            return
        else:
            print("Opción inválida.")

    def mostrar_productos(self, tipo=None):
        if tipo:
            productos = [producto for producto in self.catalogo if producto.tipo == tipo]
            if not productos:
                print("No hay productos de ese tipo en el catálogo.")
                return
        else:
            productos = self.catalogo

        for producto in productos:
            print(producto)

    def cargar_catalogo(self):
        nombre_archivo = input("Ingresa el nombre del archivo de catálogo: ")
        try:
            with open(nombre_archivo, "r") as archivo:
                lector_csv = csv.reader(archivo)
                for fila in lector_csv:
                    tipo = fila[0]
                    titulo = fila[1]
                    actor_director = fila[2]
                    otros_datos = fila[3]
                    producto = Producto(tipo, titulo, actor_director, otros_datos)
                    self.catalogo.append(producto)
            print("Catalogo cargado")
        except FileNotFoundError:
            print("El archivo no existe.")
        except:
            print("Ocurrio un error.")

    def guardar_catalogo(self):
        nombre_archivo = input("Ingresa el nombre del archivo para guardar el catálogo: ")
        try:
            with open(nombre_archivo, "w") as archivo:
                escritor_csv = csv.writer(archivo)
                for producto in self.catalogo:
                    fila = [producto.tipo, producto.titulo, producto.actor_director, producto.otros_datos]
                    escritor_csv.writerow(fila)
            print("Catálogo guardado correctamente.")
        except:
            print("Ocurrió un error al guardar el catálogo.")

