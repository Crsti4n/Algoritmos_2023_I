import pandas as pd
from modelo.libro import Libro  # Importa la clase Libro desde el módulo libro.py

class LibroNegocio:
    # Propiedades de la clase
    listado_libros = []  # Lista para almacenar los objetos Libro
    registros_libros = 'listado_libros.xlsx'  # Nombre del archivo Excel

    def __init__(self):
        self.listado_libros = []  # Inicializa la lista de libros al crear una instancia de la clase

    def obtener_libros(self):
        # Función para obtener la lista de libros desde el archivo Excel
        try:
            df = pd.read_excel(self.registros_libros)  # Lee el archivo Excel y crea un DataFrame
            listado_libros = []

            # Itera a través de las filas del DataFrame para crear objetos Libro
            for index, row in df.iterrows():
                libro = Libro(row['Código del libro'], row['Título'], row['Año de Publicación'], row['Tomo'])
                listado_libros.append(libro)

            return listado_libros  # Retorna la lista de libros

        except FileNotFoundError:
            return []  # Retorna una lista vacía si el archivo no se encuentra

    def registrar_libro(self, _cod_libro, _titulo, _anyo, _tomo):
        # Función para registrar un libro
        self.listado_libros = self.obtener_libros()  # Obtiene la lista de libros existente

        libro = Libro(_cod_libro, _titulo, _anyo, _tomo)  # Crea un objeto Libro

        self.listado_libros.append(libro)  # Agrega el libro a la lista
        print(f'Se agregó un libro. Total de libros: {len(self.listado_libros)}')

    def guardar_libros(self):
        # Función para guardar la lista de libros en el archivo Excel
        if len(self.listado_libros) > 0:
            data = []
            for libro in self.listado_libros:
                data.append([libro.get_codigo_libro(), libro.get_titulo(), libro.get_año(), libro.get_tomo()])
            
            columnas = ['Código del libro', 'Título', 'Año de Publicación', 'Tomo']
            df = pd.DataFrame(data, columns=columnas)  # Crea un DataFrame con los datos de los libros
            df.to_excel(self.registros_libros, index=False, engine='openpyxl')  # Guarda el DataFrame en el archivo Excel
            return 'Se registraron los libros correctamente'
        else:
            return 'No hay libros para guardar'

    def editar_libro(self, _indice, _cod_libro, _titulo, _anyo, _tomo):
        # Función para editar un libro
        df = pd.read_excel(self.registros_libros)  # Lee el archivo Excel

        # Actualiza los valores en el DataFrame
        df.loc[_indice, 'Código del libro'] = _cod_libro
        df.loc[_indice, 'Título'] = _titulo
        df.loc[_indice, 'Año de Publicación'] = _anyo
        df.loc[_indice, 'Tomo'] = _tomo


        df.to_excel(self.registros_libros, index=False, engine='openpyxl')  # Guarda el DataFrame actualizado en el archivo Excel
        return 'Actualización del libro correcta'

    def eliminar_libro(self, _indice):
        # Función para eliminar un libro
        df = pd.read_excel(self.registros_libros)  # Lee el archivo Excel

        # Elimina la fila correspondiente al índice indicado
        df.drop(_indice, inplace=True)

        df.to_excel(self.registros_libros, index=False, engine='openpyxl')  # Guarda el DataFrame actualizado en el archivo Excel
        return 'Libro eliminado correctamente'