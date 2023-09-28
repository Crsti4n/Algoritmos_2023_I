# factura.py

from datetime import datetime  # Importa la clase datetime desde el módulo datetime

class Factura:
    venta = 0  # Atributo para almacenar la venta relacionada con la factura
    fecha = datetime.now()  # Atributo para almacenar la fecha y hora de la factura (inicializado con la fecha y hora actual)

    def __init__(self, venta):
        self.venta = venta  # Inicializa el atributo venta con la venta proporcionada
        self.fecha = datetime.now()  # Inicializa la fecha de la factura con la fecha y hora actual
    
    def imprimir_factura(self):
        # Imprime los detalles de la factura
        print("\n" + "=" * 20)
        print("Factura de compra:")
        print(f"Fecha de venta: {self.fecha}")
        print(f"Cliente: {self.venta.get_cliente().get_nombre()}")
        print("Productos comprados:")
        total = 0
        descuento = self.venta.get_cliente().calcular_descuento(total)

        for producto in self.venta.get_productos_vendidos():
            print(f"{producto.get_nombre()}: ${producto.get_precio():.2f}")
            total += producto.get_precio()

        print(f"Total: ${total:.2f}")

        if descuento > 0:
            print(f"Descuento aplicado: ${descuento:.2f}")
            total_con_descuento = total - descuento
            print(f"Total con descuento: ${total_con_descuento:.2f}")
        else:
            print("No se aplicó ningún descuento.")

        print("\n¡Gracias por su compra!")

    def imprimir_reporte_factura(self):
        # Retorna una representación en formato de cadena de la factura (similar a imprimir_factura, pero en lugar de imprimir, construye una cadena)
        factura_str = ""
        factura_str += "\n" + "=" * 20 + "\n"
        factura_str += "Factura de compra:\n"
        factura_str += f"Fecha de venta: {self.fecha}\n"
        factura_str += f"Cliente: {self.venta.get_cliente().get_nombre()}\n"
        factura_str += "Productos comprados:\n"
        total = 0
        descuento = self.venta.get_cliente().calcular_descuento(total)

        for producto in self.venta.get_productos_vendidos():
            factura_str += f"{producto.get_nombre()}: ${producto.get_precio():.2f}\n"
            total += producto.get_precio()

        factura_str += f"Total: ${total:.2f}\n"

        if descuento > 0:
            factura_str += f"Descuento aplicado: ${descuento:.2f}\n"
            total_con_descuento = total - descuento
            factura_str += f"Total con descuento: ${total_con_descuento:.2f}\n"
        else:
            factura_str += "No se aplicó ningún descuento.\n"

        factura_str += "\n¡Gracias por su compra!\n"
        
        return factura_str  # Retorna la representación en formato de cadena de la factura

    def get_venta(self):
        return self.venta  # Retorna la venta relacionada con la factura

    def set_venta(self, venta):
        self.venta = venta  # Establece la venta relacionada con la factura

    def get_fecha(self):
        return self.fecha  # Retorna la fecha de la factura

    def set_fecha(self, fecha):
        self.fecha = fecha  # Establece la fecha de la factura
