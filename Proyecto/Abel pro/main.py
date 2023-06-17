from catalogo import Catalogo

if __name__ == "__main__":
    catalogo = Catalogo()

    while True:
        print("\nMenú principal")
        print("1. Agregar producto al catálogo")
        print("2. Buscar producto en el catálogo")
        print("3. Eliminar producto del catálogo")
        print("4. Mostrar catálogo")
        print("5. Cargar catálogo desde archivo")
        print("6. Guardar catálogo en archivo")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            catalogo.agregar_producto()
        elif opcion == "2":
            catalogo.buscar_producto()
        elif opcion == "3":
            catalogo.eliminar_producto()
        elif opcion == "4":
            catalogo.mostrar_catalogo()
        elif opcion == "5":
            catalogo.cargar_catalogo()
        elif opcion == "6":
            catalogo.guardar_catalogo()
        elif opcion == "7":
            break
        else:
            print("Opción inválida.")
