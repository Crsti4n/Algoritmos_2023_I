# stock.py

from datetime import datetime  # Importa la clase datetime desde el módulo datetime

class Stock:
    producto = ''  # Atributo para almacenar el producto relacionado con el stock
    cantidad = 0  # Atributo para almacenar la cantidad de unidades en stock
    fecha_ultimo_reabastecimiento = datetime.now()  # Atributo para almacenar la fecha y hora del último reabastecimiento

    def __init__(self, producto, cantidad):
        self.producto = producto  # Inicializa el atributo producto con el producto proporcionado
        self.cantidad = cantidad  # Inicializa el atributo cantidad con la cantidad proporcionada
        
        self.fecha_ultimo_reabastecimiento = datetime.now()  # Inicializa la fecha de último reabastecimiento con la fecha y hora actual
    
    def get_producto(self):
        return self.producto  # Retorna el producto relacionado con el stock

    def set_producto(self, producto):
        self.producto = producto  # Establece el producto relacionado con el stock

    def get_cantidad(self):
        return self.cantidad  # Retorna la cantidad de unidades en stock

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad  # Establece la cantidad de unidades en stock

    def get_ubicacion(self):
        return self.ubicacion  # Retorna la ubicación del stock 

    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion  # Establece la ubicación del stock 

    def agregar_stock(self, cantidad):
        self.cantidad += cantidad  # Incrementa la cantidad de unidades en stock con la cantidad proporcionada
        self.fecha_ultimo_reabastecimiento = datetime.now()  # Actualiza la fecha de último reabastecimiento a la fecha y hora actual

    def reducir_stock(self, cantidad):
        if self.cantidad >= cantidad:
            self.cantidad -= cantidad  # Reduce la cantidad de unidades en stock con la cantidad proporcionada
            self.fecha_ultimo_reabastecimiento = datetime.now()  # Actualiza la fecha de último reabastecimiento a la fecha y hora actual
        else:
            print("No hay suficiente stock disponible.")  # Imprime un mensaje si no hay suficiente stock para reducir

    def actualizar_stock(self, cantidad):
        self.cantidad += cantidad  # Actualiza la cantidad de unidades en stock con la cantidad proporcionada
        self.fecha_ultimo_reabastecimiento = datetime.now()  # Actualiza la fecha de último reabastecimiento a la fecha y hora actual

    def get_fecha_ultimo_reabastecimiento(self):
        return self.fecha_ultimo_reabastecimiento  # Retorna la fecha y hora del último reabastecimiento
