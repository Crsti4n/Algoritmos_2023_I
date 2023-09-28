# producto.py

class Producto:
    # Atributos de clase para almacenar valores predeterminados
    id = 0  # Identificador del producto
    nombre = ''  # Nombre del producto
    precio = 0  # Precio del producto
    marca = ''  # Marca del producto
    modelo = ''  # Modelo del producto
    descripcion = ''  # Descripción del producto
    disponible = False  # Indicador de disponibilidad del producto

    # Constructor de la clase para inicializar objetos Producto   
    def __init__(self, id, nombre, precio, marca, modelo, descripcion, disponible):
        # Inicializando los atributos del objeto con los valores proporcionados
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        self.modelo = modelo
        self.descripcion = descripcion
        self.disponible = disponible

    # Métodos para obtener y establecer el ID
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id
    
    # Métodos para obtener y establecer el nombre
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    # Métodos para obtener y establecer el precio
    def get_precio(self):
        return self.precio
    
    def set_precio(self, precio):
        self.precio = precio
    
    # Métodos para obtener y establecer la marca
    def get_marca(self):
        return self.marca
    
    def set_marca(self, marca):
        self.marca = marca
    
    # Métodos para obtener y establecer el modelo
    def get_modelo(self):
        return self.modelo
    
    def set_modelo(self, modelo):
        self.modelo = modelo
    
    # Métodos para obtener y establecer la descripción
    def get_descripcion(self):
        return self.descripcion
    
    def set_descripcion(self, descripcion):
        self.descripcion = descripcion
    
    # Métodos para obtener y establecer la disponibilidad
    def get_disponible(self):
        return self.disponible
    
    def set_disponible(self, disponible):
        self.disponible = disponible

    # Método para obtener información del producto
    def obtener_informacion(self):
        return f"ID: {self.id}, Marca: {self.marca}, Modelo: {self.modelo} - {self.nombre}: ${self.precio:.2f}"
