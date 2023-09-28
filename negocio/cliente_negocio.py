import pandas as pd #Importa la librería pandas

from modelo.cliente import Cliente  # Importa la clase Cliente desde un módulo llamado cliente

class ClienteNegocio:
    listado_clientes = []  # Lista para almacenar objetos Cliente
    registros_clientes = 'listado_clientes.xlsx'  # Nombre del archivo de registros de clientes en formato Excel

    def __init__(self):
        self.listado_clientes = []  # Inicializa la lista de clientes al crear una instancia de la clase

    def obtener_clientes(self):
        try:
            # Intenta leer los datos de clientes desde un archivo Excel
            df = pd.read_excel(self.registros_clientes)
            listado_clientes = []
            for index, row in df.iterrows():
                # Crea objetos Cliente a partir de los datos leídos y los agrega a la lista
                cliente = Cliente(row['ID'], row['Nombre'], row['Direccion'], row['Telefono'])
                cliente.set_compras_realizadas(row['Compras_Realizadas'])
                listado_clientes.append(cliente)
            return listado_clientes  # Retorna la lista de objetos Cliente
        except FileNotFoundError:
            return []  # Si el archivo no se encuentra, retorna una lista vacía

    def registrar_cliente(self, id, nombre, direccion, telefono):
        self.listado_clientes = self.obtener_clientes()  # Obtiene la lista de clientes existentes desde el archivo
        cliente = Cliente(id, nombre, direccion, telefono)  # Crea un nuevo objeto Cliente
        self.listado_clientes.append(cliente)  # Agrega el nuevo cliente a la lista
        self.guardar_clientes()  # Guarda la lista actualizada en el archivo
        print(f'Se ha registrado al cliente {nombre} correctamente.')

    def guardar_clientes(self):
        if len(self.listado_clientes) > 0:
            data = []
            for cliente in self.listado_clientes:
                # Prepara los datos de los clientes para guardar en un DataFrame de pandas
                data.append([cliente.id, cliente.nombre, cliente.direccion, cliente.telefono, cliente.compras_realizadas])
            columnas = ['ID', 'Nombre', 'Direccion', 'Telefono', 'Compras_Realizadas']
            df = pd.DataFrame(data, columns=columnas)
            df.to_excel(self.registros_clientes, index=False, engine='openpyxl')  # Guarda los datos en el archivo Excel
            return f'se registraron correctamente los datos del cliente'
        else:
            return f'se generó un error al registrar el cliente'

    def editar_cliente(self, indice, nombre, direccion, telefono):
        try:
            df = pd.read_excel(self.registros_clientes)  # Lee los datos existentes desde el archivo
            df.loc[indice, 'Nombre'] = nombre  # Actualiza el nombre del cliente en el DataFrame
            df.loc[indice, 'Direccion'] = direccion  # Actualiza la dirección del cliente
            df.loc[indice, 'Telefono'] = telefono  # Actualiza el teléfono del cliente
            df.to_excel(self.registros_clientes, index=False, engine='openpyxl')  # Guarda los datos actualizados
            return f'Actualización correcta'
        except FileNotFoundError:
            return []  # Si el archivo no se encuentra, retorna una lista vacía
    
    def eliminar_cliente(self, indice):
        try:
            df = pd.read_excel(self.registros_clientes)  # Lee los datos existentes desde el archivo
            df.drop(indice, inplace=True)  # Elimina el cliente con el índice proporcionado
            df.to_excel(self.registros_clientes, index=False, engine='openpyxl')  # Guarda los datos actualizados
            return f'Cliente eliminado correctamente'
        except FileNotFoundError:
            return []  # Si el archivo no se encuentra, retorna una lista vacía

        
