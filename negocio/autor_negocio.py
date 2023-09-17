import pandas as pd
from modelo.autor import Autor  # Importa la clase autor desde el módulo Autor.py

class AutorNegocio:
    # Propiedades de la clase
    listado_autores = []  # Lista para almacenar los objetos Autor
    registros_autores = 'listado_autores.xlsx'  # Nombre del archivo Excel

    def __init__(self):
        self.listado_autores = []  # Inicializa la lista de autores al crear una instancia de la clase
           
    def obtener_autores(self):
        # Función para obtener la lista de libros desde el archivo Excel
        try:
            df = pd.read_excel(self.registros_autores)  # Lee el archivo Excel y crea un DataFrame
            listado_autores = []

            # Itera a través de las filas del DataFrame para crear objetos Autor
            for index, row in df.iterrows():
                autor = Autor(row['Código de Persona'],row['Código del Autor'],row['Nombre del Autor'],row['Apellido paterno'],row['Apellido materno'],row['fecha de nacimiento'], row['Pais'], row['Editorial'])
                listado_autores.append(autor)

            return listado_autores  # Retorna la lista de autores

        except FileNotFoundError:
            return []  # Retorna una lista vacía si el archivo no se encuentra

    def registrar_autor(self,_cod_persona, _cod_autor,_nombre,_apellido_paterno,_apellido_materno,_fecha_nacimiento, _pais, _editorial):
        # Función para registrar un autor
        self.listado_autores = self.obtener_autores()  # Obtiene la lista de autores existente

        autor= Autor(_cod_persona,_cod_autor,_nombre,_apellido_paterno,_apellido_materno,_fecha_nacimiento, _pais, _editorial)  # Crea un objeto Autor

        self.listado_autores.append(autor)  # Agrega al autor a la lista
        print(f'Se agregó un autor. Total de autores: {len(self.listado_autores)}')

    def guardar_autores(self):
        # Función para guardar la lista de autores en el archivo Excel
        if len(self.listado_autores) > 0:
            data = []
            for autor in self.listado_autores:
                data.append([autor.get_cod_persona(),autor.get_cod_autor(),autor.get_nombre(),autor.get_apellido_paterno(),autor.get_apellido_materno(),autor.get_fecha_nacimiento(), autor.get_pais(), autor.get_editorial()])
            
            columnas = ['Código de Persona','Código del Autor','Nombre del Autor','Apellido paterno','Apellido materno','fecha de nacimiento', 'Pais', 'Editorial']
            df = pd.DataFrame(data, columns=columnas)  # Crea un DataFrame con los datos de los autores
            df.to_excel(self.registros_autores, index=False, engine='openpyxl')  # Guarda el DataFrame en el archivo Excel
            return 'Se registraron los autores correctamente'
        else:
            return 'No hay autores para guardar'

    def editar_autor(self, _indice,_cod_persona,_cod_autor,_nombre,_apellido_paterno,_apellido_materno,_fecha_nacimiento, _pais, _editorial):
        # Función para editar un autor
        df = pd.read_excel(self.registros_autores)  # Lee el archivo Excel

        # Actualiza los valores en el DataFrame
        df.loc[_indice, 'Código de Persona'] = _cod_persona
        df.loc[_indice, 'Nombre del Autor'] = _nombre
        df.loc[_indice, 'Código del Autor'] = _cod_autor
        df.loc[_indice, 'Apellido paterno'] = _apellido_paterno
        df.loc[_indice, 'Apellido materno'] = _apellido_materno
        df.loc[_indice, 'fecha de nacimiento'] = _fecha_nacimiento
        df.loc[_indice, 'Pais'] = _pais
        df.loc[_indice, 'Editorial'] = _editorial
        


        df.to_excel(self.registros_autores, index=False, engine='openpyxl')  # Guarda el DataFrame actualizado en el archivo Excel
        return 'Actualización del autor correcta'

    def eliminar_autor(self, _indice):
        # Función para eliminar un autor
        df = pd.read_excel(self.registros_autores)  # Lee el archivo Excel

        # Elimina la fila correspondiente al índice indicado
        df.drop(_indice, inplace=True)

        df.to_excel(self.registros_autores, index=False, engine='openpyxl')  # Guarda el DataFrame actualizado en el archivo Excel
        return 'Autor eliminado correctamente'