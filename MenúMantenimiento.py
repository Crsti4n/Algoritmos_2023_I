from negocio.mantenimientoNegocio import MantenimientoNegocio #Importar la clase mantenimientoNegocio

#Clase para crear el menú
class MenuBiblioteca:
    def __init__(self):
        self.biblioteca=MantenimientoNegocio()
        # Diccionario de opciones del menú
        self.opciones = {
            "1": self.biblioteca.registrar_empleados,  # Opción para registrar empleados
            "2": self.biblioteca.obtener_empleados,   # Opción para obtener empleados
            "3": self.biblioteca.editar_empleado,     # Opción para editar empleados
            "4": self.biblioteca.eliminar_empleado,   # Opción para eliminar empleados
            "5": self.biblioteca.registrar_clientes,  # Opción para registrar clientes
            "6": self.biblioteca.obtener_clientes,    # Opción para obtener clientes
            "7": self.biblioteca.editar_clientes,     # Opción para editar clientes
            "8": self.biblioteca.eliminar_cliente,    # Opción para eliminar clientes
            "9": self.biblioteca.registrar_productos, # Opción para registrar productos
            "10": self.biblioteca.obtener_productos,  # Opción para obtener productos
            "11": self.biblioteca.editar_productos,   # Opción para editar productos
            "12": self.biblioteca.eliminar_producto,  # Opción para eliminar productos
            "13": self.biblioteca.actualizar_stock,   # Opción para actualizar el stock de productos
            "14": self.biblioteca.disponibilidad_producto,  # Opción para verificar disponibilidad de productos
            "15": self.biblioteca.realizar_ventas,    # Opción para realizar ventas
            "16": self.biblioteca.actualizar_ventas_realizadas,  # Opción para actualizar ventas realizadas
            "17": self.biblioteca.realizar_descuento, # Opción para aplicar descuentos a clientes
            "18": self.biblioteca.generar_factura,    # Opción para generar facturas
            "19": self.biblioteca.reporte_factura,    # Opción para generar reportes de facturas
            "20": exit,  # Opción para salir del programa
        }
    def mostrar_menu(self):       
        while True:
            print("\nMenú:")
            print("1. Registrar empleados")
            print("2. Obtener empleados")
            print("3. Editar empleados")
            print("4. Eliminar empleados")
            print("5. Registrar clientes")
            print("6. Obtener clientes")
            print("7. Editar clientes")
            print("8. Eliminar clientes")
            print("9. Registrar productos")
            print("10. Obtener productos")
            print("11. Editar productos")
            print("12. Eliminar productos")
            print("13. Actualizar stock")
            print("14. Disponibilidad del producto")
            print("15. Realizar ventas")
            print("16. Actualizar ventas realizadas")
            print("17. Realizar descuento")
            print("18. Generar factura")
            print("19. Generar reporte de factura")
            print("20. Salir")
                
            opcion =input("Seleccione una opción: ")
            
            # Verificar si la selección del usuario está en el diccionario de opciones
            if opcion in self.opciones:
                self.opciones[opcion]()  # Ejecutar la función correspondiente a la opción seleccionada
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
def main():
    menu = MenuBiblioteca()
    menu.mostrar_menu()

if __name__ == "__main__":
    main()       