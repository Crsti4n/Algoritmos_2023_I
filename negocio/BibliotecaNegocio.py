from datetime import datetime # Importamos la clase datetime para trabajar con fechas
from negocio.libro_negocio import LibroNegocio # Importamos la clase libro_negocio 
from negocio.autor_negocio import AutorNegocio # Importamos la clase autor_negocio
from negocio.categoria_negocio import CategoriaNegocio # Importamos la categoria_negocio
negocio = LibroNegocio() #Importamos la clase LibroNegocio
negocio2 = AutorNegocio() #Importamos la clase AutorNegocio
negocio3=CategoriaNegocio() #Importamos la clase CategoriaNegocio
from modelo.autor import Autor
from modelo.libro import Libro
from modelo.categoria import Categoria

#Clase que contiene todas funciones que se usaran en el menú
class BibliotecaNegocio:
    def __init__(self):
        #Arreglos para almacenar los autores, libros y categorías ingresadas
        self.lista_autores = []
        self.lista_libros = []
        self.lista_categorias = []
    #Función para registrar a los autores
    def registrar_autor(self):
        cod_persona = input('Ingrese el código de la persona: ')
        cod_autor = input('Ingrese el código del autor: ')
        nombre = input('Ingrese el nombre del autor: ')
        apellido_paterno = input('Ingrese el apellido paterno del autor: ')
        apellido_materno = input('Ingrese el apellido materno del autor: ')
        fecha_nacimiento = input('Ingrese la fecha de nacimiento del autor: ')
        pais = input('Ingrese el pais del autor: ')
        editorial = input('Ingrese el la editorial: ')

        # Llama al método de la instancia de AutorNegocio para registrar el autor
        negocio2.registrar_autor(cod_persona,cod_autor,nombre,apellido_paterno,apellido_materno,fecha_nacimiento, pais, editorial)
        nuevo_autor =Autor(cod_persona, cod_autor, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, pais, editorial)
        self.lista_autores.append(nuevo_autor)
        # Guardar los cambios en el archivo
        negocio2.guardar_autores()

    # Función para listar los autores
    def listar_autores(self):
        listado_autores = negocio2.obtener_autores()
        for autor in listado_autores:
            print(autor.mostrar_datos())

# Función para editar un autor
    def editar_autor(self):
        self.listar_autores()
        indice = int(input('Ingrese el índice del libro a editar: ')) - 1
        cod_persona = input('Ingrese el nuevo código de la persona: ')
        cod_autor = input('Ingrese el nuevo código del autor: ')
        nombre = input('Ingrese el nuevo nombre del autor: ')
        apellido_paterno = input('Ingrese el nuevo apellido paterno del autor: ')
        apellido_materno = input('Ingrese el nuevo apellido materno del autor: ')
        fecha_nacimiento = input('Ingrese la nueva fecha de nacimiento del autor: ')
        pais = input('Ingrese el nuevo pais del autor: ')
        editorial = input('Ingrese la nueva editorial: ')

        # Llama al método de la instancia de AutorNegocio para editar el autor
        print(negocio2.editar_autor(indice,cod_persona,cod_autor,nombre,apellido_paterno,apellido_materno,fecha_nacimiento, pais, editorial))

    # Función para eliminar un autor
    def eliminar_autor(self):
        self.listar_autores()
        indice = int(input('Ingrese el índice del autor a eliminar: ')) - 1

        # Llama al método de la instancia de AutorNegocio para eliminar el autor
        print(negocio2.eliminar_autor(indice))


    # Función para registrar un nuevo libro
    def registrar_libro(self):
        cod_libro = input('Ingrese el código del libro: ')
        titulo = input('Ingrese el título del libro: ')
        año = input('Ingrese el Año de publicación del libro: ')
        tomo = input('Ingrese el número de tomo del libro: ')

        # Llama al método de la instancia de LibroNegocio para registrar el libro
        negocio.registrar_libro(cod_libro, titulo, año, tomo)
        nuevo_libro =Libro(cod_libro, titulo, año, tomo)
        self.lista_libros.append(nuevo_libro)
        # Guardar los cambios en el archivo
        negocio.guardar_libros()

    # Función para listar los libros
    def listar_libros(self):
        listado_libros = negocio.obtener_libros()
        for libro in listado_libros:
            print(libro.imprimir())

    # Función para editar un libro
    def editar_libro(self):
        self.listar_libros()
        indice = int(input('Ingrese el índice del libro a editar: ')) - 1
        cod_libro = input('Ingrese el nuevo código del libro: ')
        titulo = input('Ingrese el nuevo título del libro: ')
        año = input('Ingrese el nuevo año de publicación del libro: ')
        tomo = input('Ingrese el nuevo número de tomo del libro: ')

        # Llama al método de la instancia de LibroNegocio para editar el libro
        print(negocio.editar_libro(indice, cod_libro, titulo, año, tomo))

    # Función para eliminar un libros
    def eliminar_libro(self):
        self.listar_libros()
        indice = int(input('Ingrese el índice del libro a eliminar: ')) - 1

        # Llama al método de la instancia de LibroNegocio para eliminar el libro
        print(negocio.eliminar_libro(indice))
 

    # Función para registrar una nueva categoria
    def registrar_categoria(self):
        cod_categoria = input('Ingrese el código de la categoría: ')
        categoria = input('Ingrese el hombre de la categoría: ')

        # Llama al método de la instancia de CategoriaNegocio para registrar el categoria
        negocio3.registrar_categoria(cod_categoria, categoria)
        nuevo_categoria =Categoria(cod_categoria, categoria)
        self.lista_categorias.append(nuevo_categoria)
        # Guardar los cambios en el archivo
        negocio3.guardar_categorias()

    # Función para listar las categorías
    def listar_categorias(self):
        listado_categorias = negocio3.obtener_categorias()
        for categoria in listado_categorias:
            print(categoria.mostra_datos())

    # Función para editar una categoria
    def editar_categoria(self):
        self.listar_categorias()
        indice = int(input('Ingrese el índice del libro a editar: ')) - 1
        cod_categoria = input('Ingrese el nuevo código de la categoria: ')
        categoria = input('Ingrese la nueva categoría de la categoria: ')

        # Llama al método de la instancia de CategoriaNegocio para editar la categoria
        print(negocio3.editar_categoria(indice, cod_categoria, categoria))

    # Función para eliminar una categoria
    def eliminar_categoria(self):
        self.listar_categorias()
        indice = int(input('Ingrese el índice de la categoria a eliminar: ')) - 1

        # Llama al método de la instancia de LibroNegocio para eliminar el libro
        print(negocio3.eliminar_categoria(indice))

    #Función para asignar autores a los libros
    def asignar_autores_libros(self):
        
         # Verificar si hay autores y libros disponibles.
        if not self.lista_autores:
            print("No hay autores en la lista para asignar.")
            return

        if not self.lista_libros:
            print("No hay libros en la lista para asignar autores.")
            return
        # Iterar a través de la lista de libros.
        for libro in self.lista_libros:
            print(f"Libro: {libro.titulo}")
            
            print("Autores disponibles:")
            # Enumerar y mostrar autores disponibles al usuario.
            for i, autor in enumerate(self.lista_autores, start=1):
                print(f"{i}. {autor.nombre} {autor.apellido_paterno}")

            while True:
                try:
                    # Solicitar al usuario seleccionar un autor.
                    seleccion = int(input(f"Seleccione el autor para '{libro.titulo}' (1-{len(self.lista_autores)}): "))
                    if 1 <= seleccion <= len(self.lista_autores):
                        autor_seleccionado = self.lista_autores[seleccion - 1]
                        libro.asignar_autor(autor_seleccionado.cod_autor)
                        print(f"Autor '{autor_seleccionado.nombre} {autor_seleccionado.apellido_paterno}' asignado a '{libro.titulo}' con éxito.")
                        break
                    else:
                        print("Selección inválida. Intente de nuevo.")
                except ValueError:
                    print("Entrada inválida. Ingrese un número válido.")

        print("Autores asignados a todos los libros con éxito.")
    
    #Función para asignar categorías a los libros
    def asignar_categoria_libro(self):
        # Verificar si hay categorías y libros disponibles.
        if not self.lista_categorias:
            print("No hay categorías en la lista para asignar.")
            return

        if not self.lista_libros:
            print("No hay libros en la lista para asignar categorías.")
            return
        
        # Iterar a través de la lista de libros.
        for libro in self.lista_libros:
            print(f"Libro: {libro.titulo}")
            
            # Enumerar y mostrar categorías disponibles al usuario.
            print("Categorías disponibles:")
            for i, categoria in enumerate(self.lista_categorias, start=1):
                print(f"{i}. {categoria.categoria}")

            while True:
                try:
                    # Solicitar al usuario seleccionar una categoría.
                    seleccion = int(input(f"Seleccione la categoría para '{libro.titulo}' (1-{len(self.lista_categorias)}): "))
                    if 1 <= seleccion <= len(self.lista_categorias):
                        categoria_seleccionada = self.lista_categorias[seleccion - 1]
                        libro.asignar_categoria(categoria_seleccionada.cod_categoria)
                        print(f"Categoría '{categoria_seleccionada.categoria}' asignada a '{libro.titulo}' con éxito.")
                        break
                    else:
                        print("Selección inválida. Intente de nuevo.")
                except ValueError:
                    print("Entrada inválida. Ingrese un número válido.")

        print("Categorías asignadas a todos los libros con éxito.")
    
    def reporte_libro(self):
        print("Generando el Reporte del libro")
        fecha_actual = datetime.now()
        formato = fecha_actual.strftime("%d_%m_%Y")
        print("Fecha actual en formato 'día_mes_año':", formato)
        nom_reporte = 'reporte_'+ formato + '.txt'
        with open(nom_reporte, 'a') as archivo:
            archivo.write("*******Reporte de los libros******************.\n")
            for libro in self.lista_libros:
                archivo.write(libro.imprimir())
                archivo.write("Datos del libro.\n")
            archivo.write("*************************************************.\n")
