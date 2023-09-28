from modelo.persona import Persona  # Importa la clase Persona de un módulo llamado persona

class Cliente(Persona):
    compras_realizadas = []  # Lista para almacenar compras realizadas por el cliente

    def __init__(self, id, nombre, direccion, telefono):
        super().__init__(id, nombre, direccion, telefono)  # Llamando al constructor de la clase base Persona
        self.compras_realizadas = []  # Inicializa la lista de compras realizadas como una lista vacía

    def get_compras_realizadas(self):
        return self.compras_realizadas  # Retorna la lista de compras realizadas por el cliente

    def set_compras_realizadas(self, compras_realizadas):
        self.compras_realizadas = compras_realizadas  # Establece la lista de compras realizadas

    def realizar_compra(self, producto):
        self.compras_realizadas.append(producto)  # Agrega un producto a la lista de compras realizadas

    def calcular_descuento(self, precio_total):
        if precio_total > 10000:
            return precio_total * 0.20  # Aplica un descuento del 20% si el precio total es mayor a 10000
        else:
            return 0  # No se aplica descuento

    def imprimir(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}, Compras Realizadas: {', '.join(self.compras_realizadas)}"
        # Devuelve una cadena que representa los datos del cliente y las compras realizadas