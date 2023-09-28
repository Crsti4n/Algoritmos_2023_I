# persona.py

class Persona:
    # Atributos de clase para almacenar valores predeterminados
    id = 0
    nombre = ''
    direccion = ''
    telefono = ''

    # Constructor de la clase para inicializar objetos Persona
    def __init__(self, id, nombre, direccion, telefono):
        # Inicializando los atributos del objeto con los valores proporcionados
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    # Métodos para obtener los valores de los atributos
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_direccion(self):
        return self.direccion

    def get_telefono(self):
        return self.telefono

    # Métodos para establecer los valores de los atributos
    def set_id(self, id):
        self.id = id

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_direccion(self, direccion):
        self.direccion = direccion

    def set_telefono(self, telefono):
        self.telefono = telefono