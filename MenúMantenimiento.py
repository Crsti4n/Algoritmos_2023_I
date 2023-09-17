from negocio.BibliotecaNegocio import BibliotecaNegocio


class MenuBiblioteca:
    def __init__(self):
        self.biblioteca = BibliotecaNegocio()
        self.opciones = {
            "1": self.biblioteca.registrar_autor,
            "2": self.biblioteca.listar_autores,
            "3": self.biblioteca.editar_autor,
            "4": self.biblioteca.eliminar_autor,
            "5": self.biblioteca.registrar_libro,
            "6": self.biblioteca.listar_libros,
            "7": self.biblioteca.editar_libro,
            "8": self.biblioteca.eliminar_libro,
            "9": self.biblioteca.registrar_categoria,
            "10": self.biblioteca.listar_categorias,
            "11": self.biblioteca.editar_categoria,
            "12": self.biblioteca.eliminar_categoria,
            "13": self.biblioteca.asignar_autores_libros,
            "14": self.biblioteca.asignar_categoria_libro,
            "15": self.biblioteca.reporte_libro,
            "16": exit
        }

    def mostrar_menu(self):
        while True:
            print("Menú:")
            print("1. Registrar autor")
            print("2. Listar autores")
            print("3. Editar autor")
            print("4. Eliminar autor")
            print("5. Registrar libro")
            print("6. Listar libros")
            print("7. Editar libro")
            print("8. Eliminar libro")
            print("9. Registrar categoría")
            print("10. Listar categorías")
            print("11. Editar categoría")
            print("12. Eliminar categoría")
            print("13. Asignar autores a libros")
            print("14. Asignar categorías a libros")
            print("15. Generar reporte de los libros")
            print("16. Salir")

            seleccion = input("Seleccione una opción: ")

            if seleccion in self.opciones:
                self.opciones[seleccion]()
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

def main():
    menu = MenuBiblioteca()
    menu.mostrar_menu()

if __name__ == "__main__":
    main()