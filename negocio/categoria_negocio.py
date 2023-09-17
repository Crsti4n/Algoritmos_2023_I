import pandas as pd
from modelo.categoria import Categoria  # Importa la clase categoria desde el módulo categoria.py

class CategoriaNegocio:
    # Propiedades de la clase
    listado_categorias = []  # Lista para almacenar los objetos categoria
    registros_categorias= 'listado_categorias.xlsx'  # Nombre del archivo Excel

    def __init__(self):
        self.listado_categorias = []  # Inicializa la lista de categorias al crear una instancia de la clase

    def obtener_categorias(self):
        # Función para obtener la lista de categorias desde el archivo Excel
        try:
            df = pd.read_excel(self.registros_categorias)  # Lee el archivo Excel y crea un DataFrame
            listado_categorias = []

            # Itera a través de las filas del DataFrame para crear objetos categoria
            for index, row in df.iterrows():
                categoria = Categoria(row['Código de Categoría'], row['Categoría'])
                listado_categorias.append(categoria)

            return listado_categorias  # Retorna la lista de categorias

        except FileNotFoundError:
            return []  # Retorna una lista vacía si el archivo no se encuentra

    def registrar_categoria(self,_cod_categoria, _categoria):
        # Función para registrar una categoria
        self.listado_categorias = self.obtener_categorias()  # Obtiene la lista de categorias existente

        categoria = Categoria(_cod_categoria, _categoria)  # Crea un objeto categoria

        self.listado_categorias.append(categoria)  # Agrega el categoria a la lista
        print(f'Se agregó una categoría. Total de categorías: {len(self.listado_categorias)}')

    def guardar_categorias(self):
        # Función para guardar la lista de categorias en el archivo Excel
        if len(self.listado_categorias) > 0:
            data = []
            for categoria in self.listado_categorias:
                data.append([categoria.get_cod_categoria(), categoria.get_categoria()])
            
            columnas = ['Código de Categoría', 'Categoría']
            df = pd.DataFrame(data, columns=columnas)  # Crea un DataFrame con los datos de las categorías
            df.to_excel(self.registros_categorias, index=False, engine='openpyxl')  # Guarda el DataFrame en el archivo Excel
            return 'Se registraron las categorías correctamente'
        else:
            return 'No hay categorías para guardar'

    def editar_categoria(self, _indice,_cod_categoria, _categoria):
        # Función para editar una categoria
        df = pd.read_excel(self.registros_categorias)  # Lee el archivo Excel

        # Actualiza los valores en el DataFrame
        df.loc[_indice, 'Código de Categoría'] = _cod_categoria
        df.loc[_indice, 'Categoria'] = _categoria

        df.to_excel(self.registros_categorias, index=False, engine='openpyxl')  # Guarda el DataFrame actualizado en el archivo Excel
        return 'Actualización de la categoria correcta'

    def eliminar_categoria(self, _indice):
        # Función para eliminar una categoria
        df = pd.read_excel(self.registros_categorias)  # Lee el archivo Excel

        # Elimina la fila correspondiente al índice indicado
        df.drop(_indice, inplace=True)

        df.to_excel(self.registros_categorias, index=False, engine='openpyxl')  # Guarda el DataFrame actualizado en el archivo Excel
        return 'Categoria eliminado correctamente'