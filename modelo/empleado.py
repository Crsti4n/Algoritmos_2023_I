# empleado.py

from modelo.persona import Persona  # Importa la clase Persona desde el módulo persona

class Empleado(Persona):
    cargo = ''  # Atributo para almacenar el cargo del empleado
    ventas_realizadas = 0  # Atributo para almacenar el número de ventas realizadas por el empleado

    def __init__(self, id, nombre, direccion, telefono, cargo):
        super().__init__(id, nombre, direccion, telefono)  # Llama al constructor de la clase base (Persona)
        self.cargo = cargo  # Inicializa el atributo cargo con el valor proporcionado
        self.ventas_realizadas = 0  # Inicializa el atributo ventas_realizadas como 0

    def actualizar_ventas(self, cantidad_ventas):
        self.ventas_realizadas += cantidad_ventas  # Actualiza el número de ventas realizadas por el empleado

    def registrar_venta(self, producto, cliente):
        self.ventas_realizadas += 1  # Incrementa el número de ventas realizadas por 1
        print(f"Venta realizada por {self.nombre} a {cliente.get_nombre()}: {producto.obtener_informacion()}")
        # Imprime un mensaje indicando la venta realizada por el empleado a un cliente con los detalles del producto

    def get_cargo(self):
        return self.cargo  # Retorna el cargo del empleado

    def set_cargo(self, cargo):
        self.cargo = cargo  # Establece el cargo del empleado

    def get_salario(self):
        return self.salario  # Retorna el salario del empleado 

    def set_salario(self, salario):
        self.salario = salario  # Establece el salario del empleado

    def get_ventas_realizadas(self):
        return self.ventas_realizadas  # Retorna el número de ventas realizadas por el empleado

    def set_ventas_realizadas(self, ventas_realizadas):
        self.ventas_realizadas = ventas_realizadas  # Establece el número de ventas realizadas por el empleado

    def imprimir(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}, Cargo: {self.cargo}, Ventas Realizadas: {self.ventas_realizadas}"
        # Retorna una cadena que representa la información del empleado, incluyendo su ID, nombre, dirección, teléfono, cargo y ventas realizadas