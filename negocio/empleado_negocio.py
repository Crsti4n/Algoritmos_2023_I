import pandas as pd #Importa la librería pandas

from modelo.empleado import Empleado  # Importa la clase Empleado desde un módulo llamado empleado

class EmpleadoNegocio:
    listado_empleados = []  # Lista para almacenar objetos Empleado
    registros_empleados = 'listado_empleados.xlsx'  # Nombre del archivo de registros de empleados en formato Excel

    def __init__(self):
        self.listado_empleados = []  # Inicializa la lista de empleados al crear una instancia de la clase

    def obtener_empleados(self):
        try:
            # Intenta leer los datos de empleados desde un archivo Excel
            df = pd.read_excel(self.registros_empleados)
            listado_empleados = []
            for index, row in df.iterrows():
                # Crea objetos Empleado a partir de los datos leídos y los agrega a la lista
                empleado = Empleado(row['ID'], row['Nombre'], row['Dirección'], row['Teléfono'], row['Cargo'])
                empleado.set_ventas_realizadas(row['Ventas_Realizadas'])
                listado_empleados.append(empleado)
            return listado_empleados  # Retorna la lista de objetos Empleado
        except FileNotFoundError:
            return []  # Si el archivo no se encuentra, retorna una lista vacía

    def registrar_empleado(self, id, nombre, direccion, telefono, cargo):
        self.listado_empleados = self.obtener_empleados()  # Obtiene la lista de empleados existentes desde el archivo
        empleado = Empleado(id, nombre, direccion, telefono, cargo)  # Crea un nuevo objeto Empleado
        self.listado_empleados.append(empleado)  # Agrega el nuevo empleado a la lista
        self.guardar_empleados()  # Guarda la lista actualizada en el archivo
        print(f'Se ha registrado al empleado {nombre} correctamente.')

    def guardar_empleados(self):
        if len(self.listado_empleados) > 0:
            data = []
            for empleado in self.listado_empleados:
                # Prepara los datos de los empleados para guardar en un DataFrame de pandas
                data.append([empleado.id, empleado.nombre, empleado.direccion, empleado.telefono, empleado.cargo, empleado.ventas_realizadas])
            columnas = ['ID', 'Nombre', 'Dirección', 'Teléfono', 'Cargo', 'Ventas_Realizadas']
            df = pd.DataFrame(data, columns=columnas)
            df.to_excel(self.registros_empleados, index=False, engine='openpyxl')  # Guarda los datos en el archivo Excel
            return f'Se registraron correctamente los datos del empleado'
        else:
            return f'Se generó un error al registrar el empleado'

    def editar_empleado(self, indice, nombre, direccion, telefono, cargo):
        try:
            df = pd.read_excel(self.registros_empleados)  # Lee los datos existentes desde el archivo
            df.loc[indice, 'Nombre'] = nombre  # Actualiza el nombre del empleado en el DataFrame
            df.loc[indice, 'Dirección'] = direccion  # Actualiza la dirección del empleado
            df.loc[indice, 'Teléfono'] = telefono  # Actualiza el teléfono del empleado
            df.loc[indice, 'Cargo'] = cargo  # Actualiza el cargo del empleado
            df.to_excel(self.registros_empleados, index=False, engine='openpyxl')  # Guarda los datos actualizados
            return f'Actualización correcta'
        except FileNotFoundError:
            return []  # Si el archivo no se encuentra, retorna una lista vacía
    
    def eliminar_empleado(self, indice):
        try:
            df = pd.read_excel(self.registros_empleados)  # Lee los datos existentes desde el archivo
            df.drop(indice, inplace=True)  # Elimina el empleado con el índice proporcionado
            df.to_excel(self.registros_empleados, index=False, engine='openpyxl')  # Guarda los datos actualizados
            return f'Empleado eliminado correctamente'
        except FileNotFoundError:
            return []  # Si el archivo no se encuentra, retorna una lista vacía