import pandas as pd #Importa la librería pandas


from modelo.producto import Producto  # Importa la clase Producto desde un módulo llamado producto

class ProductoNegocio:
    listado_productos = []  # Lista para almacenar objetos Producto
    registros_productos = 'listado_productos.xlsx'  # Nombre del archivo de registros de productos en formato Excel

    def __init__(self):
        self.listado_productos = []  # Inicializa la lista de productos al crear una instancia de la clase

    def obtener_productos(self):
        try:
            # Intenta leer los datos de productos desde un archivo Excel
            df = pd.read_excel(self.registros_productos)
            listado_productos = []
            for index, row in df.iterrows():
                # Crea objetos Producto a partir de los datos leídos y los agrega a la lista
                producto = Producto(row['ID'], row['Nombre'], row['Precio'], row['Marca'], row['Modelo'], row['Descripción'], row['Disponible'])
                listado_productos.append(producto)
            return listado_productos  # Retorna la lista de objetos Producto
        except FileNotFoundError:
            return []  # Si el archivo no se encuentra, retorna una lista vacía

    def registrar_producto(self, id, nombre, precio, marca, modelo, descripcion, disponible):
        self.listado_productos = self.obtener_productos()  # Obtiene la lista de productos existentes desde el archivo
        producto = Producto(id, nombre, precio, marca, modelo, descripcion, disponible)  # Crea un nuevo objeto Producto
        self.listado_productos.append(producto)  # Agrega el nuevo producto a la lista
        self.guardar_productos()  # Guarda la lista actualizada en el archivo
        print(f'Se ha registrado el producto "{nombre}" correctamente.')

    def guardar_productos(self):
        if len(self.listado_productos) > 0:
            data = []
            for producto in self.listado_productos:
                # Prepara los datos de los productos para guardar en un DataFrame de pandas
                data.append([producto.id, producto.nombre, producto.precio, producto.marca, producto.modelo, producto.descripcion, producto.disponible])
            columnas = ['ID', 'Nombre', 'Precio', 'Marca', 'Modelo', 'Descripción', 'Disponible']
            df = pd.DataFrame(data, columns=columnas)
            df.to_excel(self.registros_productos, index=False, engine='openpyxl')  # Guarda los datos en el archivo Excel
            return f'Se registraron correctamente los datos del producto'
        else:
            return f'Se generó un error al registrar el producto'

    def editar_producto(self, indice, nombre, precio, marca, modelo, descripcion, disponible):
        try:
            df = pd.read_excel(self.registros_productos)  # Lee los datos existentes desde el archivo
            df.loc[indice, 'Nombre'] = nombre  # Actualiza el nombre del producto en el DataFrame
            df.loc[indice, 'Precio'] = precio  # Actualiza el precio del producto
            df.loc[indice, 'Marca'] = marca  # Actualiza la marca del producto
            df.loc[indice, 'Modelo'] = modelo  # Actualiza el modelo del producto
            df.loc[indice, 'Descripción'] = descripcion  # Actualiza la descripción del producto
            df.loc[indice, 'Disponible'] = disponible  # Actualiza la disponibilidad del producto
            df.to_excel(self.registros_productos, index=False, engine='openpyxl')  # Guarda los datos actualizados
            return f'Actualización correcta'
        except FileExistsError:
            return []

    def eliminar_producto(self, indice):
        try:
            df = pd.read_excel(self.registros_productos)  # Lee los datos existentes desde el archivo
            df.drop(indice, inplace=True)  # Elimina el producto con el índice proporcionado
            df.to_excel(self.registros_productos, index=False, engine='openpyxl')  # Guarda los datos actualizados
            return f'Producto eliminado correctamente'
        except FileExistsError:
            return []

    