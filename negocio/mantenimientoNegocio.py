# Importa las clases necesarias desde sus respectivos módulos

from datetime import datetime
from modelo.stock import Stock
from modelo.cliente import Cliente
from modelo.empleado import Empleado
from modelo.venta import Venta
from modelo.factura import Factura
from modelo.producto import Producto
from negocio.empleado_negocio import EmpleadoNegocio
from negocio.cliente_negocio import ClienteNegocio
from negocio.producto_negocio import ProductoNegocio

# Instancia objetos de las clases de negocios para empleados, clientes y productos

negocio_empleado=EmpleadoNegocio()
negocio_cliente=ClienteNegocio()
negocio_producto=ProductoNegocio()

# Define la clase MantenimientoNegocio que contiene las operaciones para gestionar empleados, clientes y productos

class MantenimientoNegocio:
    def __init__(self):
        self.lista_empleados = [] #Lista para almacenar los empleados registrados
        self.lista_clientes = [] #Lista para almacenar los clientes registrados
        self.lista_productos = [] #Lista para almacenar los eproductos registrados
        self.lista_ventas = [] #Lista para almacenar las ventas registradas
        self.lista_facturas = [] #Lista para almacenar las facturas realizadas


    # Métodos para gestionar empleados
    def registrar_empleados(self):
        id = input('Ingrese el ID: ')
        nombre = input('Ingrese el nombre: ')
        direccion = input('Ingrese la dirección: ')
        telefono = input('Ingrese el teléfono: ')
        cargo = input('Ingrese el cargo: ')
        negocio_empleado.registrar_empleado(id, nombre, direccion, telefono, cargo)
        nuevo_empleado=Empleado(id, nombre, direccion, telefono, cargo)
        self.lista_empleados.append(nuevo_empleado)
        negocio_empleado.guardar_empleados()

    # Metódo para obtiene y muestra la lista de empleados
    def obtener_empleados(self):
        listado_empleados = negocio_empleado.obtener_empleados()
        for empleado in listado_empleados:
            print(empleado.imprimir())

    # Método para editar la información de un empleado existente
    def editar_empleado(self):
        indice = int(input('Ingrese el índice del empleado a editar: ')) - 1
        nombre = input('Ingrese el nuevo nombre: ')
        direccion = input('Ingrese la nueva dirección: ')
        telefono = input('Ingrese el nuevo teléfono: ')
        cargo = input('Ingrese el nuevo cargo: ')
        negocio_empleado.editar_empleado(indice, nombre, direccion, telefono, cargo)
        
    # Método para eliminar un empleado existente
    def eliminar_empleado(self):
        self.obtener_empleados()
        indice = int(input('Ingrese el índice del empleado a eliminar: ')) - 1
        negocio_empleado.eliminar_empleado(indice)

    # # Métodos para gestionar clientes
    def registrar_clientes(self):
        id = input('Ingrese el ID: ')
        nombre = input('Ingrese el nombre: ')
        direccion = input('Ingrese la dirección: ')
        telefono = input('Ingrese el teléfono: ')
        negocio_cliente.registrar_cliente(id, nombre, direccion, telefono)
        nuevo_cliente=Cliente(id, nombre, direccion, telefono)
        self.lista_clientes.append(nuevo_cliente)
        negocio_cliente.guardar_clientes()

    # Metódo para obtiene y muestra la lista de clientes
    def obtener_clientes(self):
        listado_clientes = negocio_cliente.obtener_clientes()
        for cliente in listado_clientes:
            print(cliente.imprimir())
    
    # Método para editar la información de un cliente existente
    def editar_clientes(self):
        indice = int(input('Ingrese el índice del cliente a editar: ')) - 1
        nombre = input('Ingrese el nuevo nombre: ')
        direccion = input('Ingrese la nueva dirección: ')
        telefono = input('Ingrese el nuevo teléfono: ')
        negocio_cliente.editar_cliente(indice, nombre, direccion, telefono)
    
    # Método para eliminar un cliente existente
    def eliminar_cliente(self):
        self.obtener_clientes()
        indice = int(input('Ingrese el índice del cliente a eliminar: ')) - 1
        negocio_cliente.eliminar_cliente(indice)

    # Métodos para gestionar productos
    def registrar_productos(self):
        id = input('Ingrese el ID: ')
        nombre = input('Ingrese el nombre: ')
        precio = float(input('Ingrese el precio: '))
        marca = input('Ingrese la marca: ')
        modelo = input('Ingrese el modelo: ')
        descripcion = input('Ingrese la descripción: ')
        disponible = input('¿Está disponible? (S/N): ').strip().lower() == 's'
        negocio_producto.registrar_producto(id, nombre, precio, marca, modelo, descripcion, disponible)
        nuevo_producto=Producto(id, nombre, precio, marca, modelo, descripcion, disponible)
        self.lista_productos.append(nuevo_producto)
        negocio_producto.guardar_productos()
    
    # Metódo para obtiene y muestra la lista de productos
    def obtener_productos(self):
        listado_productos = negocio_producto.obtener_productos()
        for producto in listado_productos:
            print(producto.obtener_informacion())
    
    # Método para editar la información de un producto existente
    def editar_productos(self):
        indice = int(input('Ingrese el índice del producto a editar: ')) - 1
        nombre = input('Ingrese el nuevo nombre: ')
        precio = float(input('Ingrese el nuevo precio: '))
        marca = input('Ingrese la nueva marca: ')
        modelo = input('Ingrese el nuevo modelo: ')
        descripcion = input('Ingrese la nueva descripción: ')
        disponible = input('¿Está disponible? (S/N): ').strip().lower() == 's'
        negocio_producto.editar_producto(indice, nombre, precio, marca, modelo, descripcion, disponible)
    
    # Método para eliminar un empleado existente
    def eliminar_producto(self):
        self.obtener_productos()
        indice = int(input('Ingrese el índice del producto a eliminar: ')) - 1
        negocio_producto.eliminar_producto(indice)

    #Método para actualizar el stock
    def actualizar_stock(self):
        # Muestra la lista actual de productos disponibles
        self.obtener_productos()
        
        # Verifica si la lista de productos está vacía
        if not self.lista_productos:
            print("No hay productos en la lista.")
            return
        
        # Solicita al usuario el índice del producto que desea actualizar
        indice = int(input('Ingrese el índice del producto a actualizar el stock: ')) - 1
        
        # Verifica si el índice proporcionado es válido
        if 0 <= indice < len(self.lista_productos):
            
            # Solicita al usuario la cantidad que desea agregar al stock
            cantidad = int(input('Ingrese la cantidad a agregar al stock: '))
            
            # Obtiene el producto seleccionado
            producto = self.lista_productos[indice]
        
            # Crear una instancia de Stock con los argumentos necesarios
            stock = Stock(producto, cantidad)
        
            # Llamar al método para agregar stock
            stock.agregar_stock(cantidad)
        
            # Guardar los cambios en la base de datos o donde corresponda
            negocio_producto.editar_producto(indice, producto.nombre, producto.precio, producto.marca, producto.modelo, producto.descripcion, producto.disponible)
        else:
            print("El índice ingresado no es válido.")
          
          
    #Método para mostrar los productos que estén disponibles       
    def disponibilidad_producto(self):
        
        # Obtener la lista actual de productos disponibles
        self.obtener_productos()
        if not self.lista_productos:
            print("No hay productos en la lista.")
            return
        
        # Solicitar al usuario el índice del producto para verificar su disponibilidad
        indice = int(input('Ingrese el índice del producto para verificar disponibilidad: ')) - 1
        
        # Verificar si el índice proporcionado es válido
        if 0 <= indice < len(self.lista_productos):
            
            # Obtener el producto seleccionado
            producto = self.lista_productos[indice]
            
            # Verificar si el producto está disponible
            if producto.disponible:
                print(f'El producto "{producto.nombre}" está disponible.')
            else:
                print(f'El producto "{producto.nombre}" no está disponible.')
        else:
            print("El índice ingresado no es válido.")
    
    #Método para registrar ventas
    def realizar_ventas(self):
        
        # Obtener la lista de clientes registrados
        self.obtener_clientes()
        
        # Verificar si no hay productos registrados
        if not self.lista_productos:
            print("No hay productos registrados en la lista.")
            return
        
        # Verificar si no hay clientes registrados
        if not self.lista_clientes:
            print("No hay clientes en la lista.")
            return
        # Solicitar al usuario que ingrese el índice del cliente que realiza la compra
        cliente_indice = int(input('Ingrese el índice del cliente que realiza la compra: ')) - 1
        
        # Obtener el cliente seleccionado
        cliente = self.lista_clientes[cliente_indice]
        
        # Crear una instancia de Venta asociada al cliente
        venta = Venta(cliente)
        while True:
            # Mostrar el listado de productos disponibles
            self.obtener_productos()
            
            # Solicitar al usuario que ingrese el índice del producto a agregar a la venta
            producto_indice = int(input('Ingrese el índice del producto a agregar a la venta (0 para terminar): '))
            if producto_indice == 0:
                break # El usuario ingresa 0 para terminar la venta
            producto = self.lista_productos[producto_indice - 1]
            venta.agregar_producto(producto)
            
        # Agregar la venta a la lista de ventas registradas
        self.lista_ventas.append(venta)
        
        # Guardar los cambios en la base de datos de productos
        negocio_producto.guardar_productos()
        print('Venta realizada con éxito.')

    #Método para actualizar la contibilidad de las ventas
    def actualizar_ventas_realizadas(self):
        
        # Obtener la lista de empleados registrados
        self.obtener_empleados()
        
        # Verificar si no hay empleados registrados
        if not self.lista_empleados:
            print("No hay empleados disponibles para actualizar ventas.")
            return
        
        # Solicitar al usuario que ingrese el índice del empleado para actualizar sus ventas
        empleado_indice = int(input('Ingrese el índice del empleado para actualizar sus ventas: ')) - 1
        
        # Obtener el empleado seleccionado
        empleado = self.lista_empleados[empleado_indice]
        
        # Solicitar al usuario que ingrese la cantidad de ventas realizadas por el empleado
        cantidad_ventas = int(input('Ingrese la cantidad de ventas realizadas por el empleado: '))
        
        # Actualizar el número de ventas realizadas por el empleado
        empleado.actualizar_ventas(cantidad_ventas)
        
        # Guardar los cambios en la base de datos de empleados
        negocio_empleado.editar_empleado(empleado_indice, empleado.nombre, empleado.direccion, empleado.telefono, empleado.cargo)
    
    #Método para realizar un descuento
    def realizar_descuento(self):
        
        # Obtener la lista de clientes registrados
        self.obtener_clientes()
        
        # Verificar si no hay clientes registrados
        if not self.lista_clientes:
            print("No hay clientes disponibles para aplicar descuentos.")
            return
        
        # Solicitar al usuario el índice del cliente para aplicar el descuento
        cliente_indice = int(input('Ingrese el índice del cliente para aplicar el descuento: ')) - 1
        # Verificar si el índice ingresado es válido
        if 0 <= cliente_indice < len(self.lista_clientes):
            # Obtener el cliente seleccionado
            cliente = self.lista_clientes[cliente_indice]

            # Solicitar al usuario el precio total de la compra
            precio_total = float(input('Ingrese el precio total de la compra: '))

            # Calcular el descuento usando el método calcular_descuento del cliente
            descuento = cliente.calcular_descuento(precio_total)
            
            # Imprimir el monto del descuento aplicado
            print(f"Descuento aplicado: ${descuento:.2f}")
        else:
            print("El índice del cliente ingresado no es válido.")

    #Método para generar una factura
    def generar_factura(self):
        
         # Verificar si no hay ventas registradas
        if not self.lista_ventas :
            print("No hay ventas registradas.")
            return
        
        # Mostrar las ventas registradas para que el usuario elija una
        print("Ventas registradas:")
        for i, venta in enumerate(self.lista_ventas, start=1):
                print(f"{i}. Venta de {venta.get_cliente().get_nombre()}")  
        # Solicita al usuario el índice de la venta que desea facturar
        venta_indice = int(input('Ingrese el índice de la venta a facturar: ')) - 1
        
        #Verificar que el índice ingresado sea correcto
        if 0 <= venta_indice < len(self.lista_ventas):
            
            # Obtener la venta seleccionada
            venta = self.lista_ventas[venta_indice]
            for i, venta in enumerate(self.lista_ventas, start=1):
                print(f"{i}. Venta de {venta.get_cliente().get_nombre()}")
                
            # Solicitar al usuario el índice de la venta que desea facturar 
            venta_indice = int(input('Ingrese el índice de la venta para generar la factura: ')) - 1
            venta = self.lista_ventas[venta_indice]
            
             # Crear una instancia de Factura con la venta seleccionada
            factura = Factura(venta)
            
            # Agregar la factura a la lista de facturas
            self.lista_facturas.append(factura)
            
            # Imprimir la factura
            factura.imprimir_factura()
        else:
            print("El índice de la venta ingresado no es válido.")
            
    "Método para generar una factura en formato .txt"
    def reporte_factura(self):
        
        # Obtener la fecha actual
        fecha_actual = datetime.now()
        
        # Formatear la fecha en el formato deseado (día_mes_año)
        formato = fecha_actual.strftime("%d_%m_%Y")
        # Crear el nombre del archivo de reporte
        nom_reporte = 'reporte_facturas_' + formato + '.txt'
        
        # Abrir el archivo en modo escritura ('w')
        with open(nom_reporte, 'a') as archivo:
            
             # Escribir una cabecera en el archivo
            archivo.write("*******Listado de Facturas*******************.\n")
            
            # Iterar sobre las facturas registradas en la lista
            for factura in self.lista_facturas:
                
                # Escribir los detalles de la factura en el archivo
                archivo.write(factura.imprimir_reporte_factura())
                archivo.write("\n") # Agregar una línea en blanco entre facturas
            archivo.write("*************************************************.\n")
