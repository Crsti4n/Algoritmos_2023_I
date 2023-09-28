# venta.py

class Venta:
    cliente = ''  # Atributo para almacenar información del cliente
    productos_vendidos = []  # Lista para almacenar los productos vendidos en la venta

    def __init__(self, cliente):
        self.cliente = cliente  # Inicializa el atributo cliente con el cliente proporcionado
        self.productos_vendidos = []  # Inicializa la lista de productos vendidos como una lista vacía

    def agregar_producto(self, producto):
        self.productos_vendidos.append(producto)  # Agrega un producto a la lista de productos vendidos

    def get_productos_vendidos(self):
        return self.productos_vendidos  # Retorna la lista de productos vendidos en la venta

    def set_productos_vendidos(self, productos_vendidos):
        self.productos_vendidos = productos_vendidos  # Establece la lista de productos vendidos

    def get_cliente(self):
        return self.cliente  # Retorna la información del cliente asociado a la venta

    def set_cliente(self, cliente):
        self.cliente = cliente  # Establece la información del cliente asociado a la venta

