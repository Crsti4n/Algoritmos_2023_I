import tkinter as tk
from tkinter import ttk
from negocio.empleado_negocio import EmpleadoNegocio
from negocio.cliente_negocio import ClienteNegocio
from negocio.producto_negocio import ProductoNegocio

#clase principal de la aplicación
class MainMenuApp:
    # Variables de clase para almacenar instancias de negocios y listas
    empleado_negocio = EmpleadoNegocio()
    cliente_negocio = ClienteNegocio()
    producto_negocio = ProductoNegocio()
    lista_empleados = []
    lista_clientes = []
    lista_productos = []
    treeview = []  # Lista para almacenar un objeto Treeview
    detalle_label = []  # Lista para almacenar un objeto Label

    # Constructor de la clase
    def __init__(self, root):
        # Configuración inicial de la ventana principal
        self.root = root
        self.root.title("Interfaz Sistema de ventas y facturas")
        self.root.config(bg='white')
        self.root.geometry('800x650')
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        # Crear el contenedor principal
        self.container = ttk.Frame(root)
        self.container.pack(fill="both", expand=True)

        # Crear el panel de opciones en el lado izquierdo
        self.options_panel = ttk.Frame(self.container, width=150)
        self.options_panel.pack(side="left", fill="y")

        # Crear el área de contenido en el lado derecho
        self.content_frame = ttk.Frame(self.container)
        self.content_frame.pack(side="right", fill="both", expand=True)

        # Crear el menú en el panel de opciones
        self.opciones_menu = tk.Menu(self.root)
        self.root.config(menu=self.opciones_menu)
        self.opciones_menu.add_command(label="Empleados", command=self.mostrar_contenido_opcion_empleado)
        self.opciones_menu.add_command(label="Clientes", command=self.mostrar_contenido_opcion_cliente)
        self.opciones_menu.add_command(label="Productos", command=self.mostrar_contenido_opcion_producto)

#CONTENIDO EMPLEADO ---------------------------------------------------------

    def mostrar_contenido_opcion_empleado(self):
        self.limpiar_contenido()# Limpia el contenido anterior
        # Crea un objeto Treeview para mostrar datos
        self.treeview = ttk.Treeview(self.content_frame)
        self.treeview.pack(fill="both", expand=True)

        # Configuración de columnas y encabezados del Treeview
        self.treeview["columns"] = ("ID", "Nombre", "Dirección", "Teléfono", "Cargo", "Ventas Realizadas")
        self.treeview.column("#0", width=50)
        self.treeview.column("ID", width=100)
        self.treeview.column("Nombre", width=200)
        self.treeview.column("Dirección", width=200)
        self.treeview.column("Teléfono", width=150)
        self.treeview.column("Cargo", width=150)
        self.treeview.column("Ventas Realizadas", width=150)

        self.treeview.heading("#0", text="Índice")
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Dirección", text="Dirección")
        self.treeview.heading("Teléfono", text="Teléfono")
        self.treeview.heading("Cargo", text="Cargo")
        self.treeview.heading("Ventas Realizadas", text="Ventas Realizadas")

        # Obtención de datos de EMPLEADOS y llenado del Treeview
        empleados = self.empleado_negocio.obtener_empleados()

        for i, empleado in enumerate(empleados):
            self.treeview.insert("", "end", text=i, values=(empleado.id, empleado.nombre, empleado.direccion, empleado.telefono, empleado.cargo, empleado.ventas_realizadas))

        # Creación de botones y etiquetas
        detalle_button = ttk.Button(self.content_frame, text="Mostrar Detalle", command=self.mostrar_detalle_empleado)
        detalle_button.pack(pady=10)

        nuevo_empleado_button = ttk.Button(self.content_frame, text="Nuevo Registro", command=self.nuevo_empleado)
        nuevo_empleado_button.pack(pady=10)

        editar_empleado_button = ttk.Button(self.content_frame, text="Editar Registro", command=self.editar_empleado)
        editar_empleado_button.pack(pady=10)

        eliminar_empleado_button = ttk.Button(self.content_frame, text="Eliminar Registro", command=self.eliminar_empleado)
        eliminar_empleado_button.pack(pady=10)

        # Etiqueta para mostrar detalles de EMPLEADOS
        self.detalle_label = ttk.Label(self.content_frame, text="")
        self.detalle_label.pack(padx=20, pady=20)

    # Función para mostrar el detalle de un EMPLEADO seleccionado
    def mostrar_detalle_empleado(self):
        seleccionado = self.treeview.selection()
        if seleccionado:
            indice = int(self.treeview.item(seleccionado)['text'])
            empleado = self.empleado_negocio.obtener_empleados()[indice]
            self.detalle_label.config(text=f"ID: {empleado.id}\nNombre: {empleado.nombre}\nDirección: {empleado.direccion}\nTeléfono: {empleado.telefono}\nCargo: {empleado.cargo}\nVentas Realizadas: {empleado.ventas_realizadas}")
        else:
            self.detalle_label.config(text="Seleccione un empleado")

    # Función para agregar un nuevo EMPLEADO
    def nuevo_empleado(self):
        self.limpiar_contenido()

        # Etiquetas y campos de entrada
        self.id_label = ttk.Label(self.content_frame, text="ID:")
        self.id_label.pack()
        self.id_entry = ttk.Entry(self.content_frame)
        self.id_entry.pack()

        self.nombre_label = ttk.Label(self.content_frame, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = ttk.Entry(self.content_frame)
        self.nombre_entry.pack()

        self.direccion_label = ttk.Label(self.content_frame, text="Dirección:")
        self.direccion_label.pack()
        self.direccion_entry = ttk.Entry(self.content_frame)
        self.direccion_entry.pack()

        self.telefono_label = ttk.Label(self.content_frame, text="Teléfono:")
        self.telefono_label.pack()
        self.telefono_entry = ttk.Entry(self.content_frame)
        self.telefono_entry.pack()

        self.cargo_label = ttk.Label(self.content_frame, text="Cargo:")
        self.cargo_label.pack()
        self.cargo_entry = ttk.Entry(self.content_frame)
        self.cargo_entry.pack()

        guardar_button = ttk.Button(self.content_frame, text="Guardar", command=self.guardar_empleado)
        guardar_button.pack()

        salir_button = ttk.Button(self.content_frame, text="Cancelar")
        salir_button.pack()

    # Función para editar un EMPLEADO existente
    def editar_empleado(self):
        seleccionado = self.treeview.selection()
        if seleccionado:
            self.indice_empleado = int(self.treeview.item(seleccionado)['text'])
            self.editar_empleado_fr()
        else:
            self.detalle_label.config(text="Seleccione un empleado")

    # Función para mostrar el formulario de edición de EMPLEADO
    def editar_empleado_fr(self):
        self.limpiar_contenido()
        empleado = self.listado_empleados[self.indice_empleado]

        self.id_label = ttk.Label(self.content_frame, text="ID:")
        self.id_label.pack()
        self.id_entry = ttk.Entry(self.content_frame)
        self.id_entry.pack()
        self.id_entry.insert(0, empleado.id)

        self.nombre_label = ttk.Label(self.content_frame, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = ttk.Entry(self.content_frame)
        self.nombre_entry.pack()
        self.nombre_entry.insert(0, empleado.nombre)

        self.direccion_label = ttk.Label(self.content_frame, text="Dirección:")
        self.direccion_label.pack()
        self.direccion_entry = ttk.Entry(self.content_frame)
        self.direccion_entry.pack()
        self.direccion_entry.insert(0, empleado.direccion)

        self.telefono_label = ttk.Label(self.content_frame, text="Teléfono:")
        self.telefono_label.pack()
        self.telefono_entry = ttk.Entry(self.content_frame)
        self.telefono_entry.pack()
        self.telefono_entry.insert(0, empleado.telefono)

        self.cargo_label = ttk.Label(self.content_frame, text="Cargo:")
        self.cargo_label.pack()
        self.cargo_entry = ttk.Entry(self.content_frame)
        self.cargo_entry.pack()
        self.cargo_entry.insert(0, empleado.cargo)

        self.ventas_label = ttk.Label(self.content_frame, text="Ventas Realizadas:")
        self.ventas_label.pack()
        self.ventas_entry = ttk.Entry(self.content_frame)
        self.ventas_entry.pack()
        self.ventas_entry.insert(0, empleado.ventas_realizadas)

        editar_button = ttk.Button(self.content_frame, text="Guardar", command=self.editar_registro_empleado)
        editar_button.pack()

        salir_button = ttk.Button(self.content_frame, text="Cancelar")
        salir_button.pack()

    # Función para guardar un nuevo EMPLEADO o actualizar uno existente
    def guardar_empleado(self):
        id = self.id_entry.get()
        nombre = self.nombre_entry.get()
        direccion = self.direccion_entry.get()
        telefono = self.telefono_entry.get()
        cargo = self.cargo_entry.get()

        # Llama a la función registrar_empleado
        reg = self.empleado_negocio.registrar_empleado(id, nombre, direccion, telefono, cargo)
        reg = self.empleado_negocio.guardar_empleados()
        print(f"Guardado en el Excel: {reg}")
        # Actualiza la lista de autores
        self.listado_empleados = self.empleado_negocio.obtener_empleados()
        self.mostrar_contenido_opcion_empleado()         # Muestra el contenido de la opción "Autores"

    # Función para editar un registro de EMPLEADO
    def editar_registro_empleado(self):
        id = self.id_entry.get()
        nombre = self.nombre_entry.get()
        direccion = self.direccion_entry.get()
        telefono = self.telefono_entry.get()
        cargo = self.cargo_entry.get()
        ventas_realizadas = self.ventas_entry.get()

        reg = self.empleado_negocio.editar_empleado(self.indice_empleado, id, nombre, direccion, telefono, cargo, ventas_realizadas)
        print(f"Editado en el Excel: {reg}")
        self.listado_empleados = self.empleado_negocio.obtener_empleados()
        self.mostrar_contenido_opcion_empleado()

    # Función para eliminar un EMPLEADO
    def eliminar_empleado(self):
        seleccionado = self.treeview.selection()
        if seleccionado:
            indice = int(self.treeview.item(seleccionado)['text'])
            mensaje = self.empleado_negocio.eliminar_empleado(indice)
            self.detalle_label.config(text=mensaje)
            self.mostrar_contenido_opcion_empleado()
        else:
            self.detalle_label.config(text="Seleccione un empleado")


#CONTENIDO CLIENTE---------------------------------------------------------

    def mostrar_contenido_opcion_cliente(self):
        self.limpiar_contenido()# Limpia el contenido anterior
        # Crea un objeto Treeview para mostrar datos
        self.treeview = ttk.Treeview(self.content_frame)
        self.treeview.pack(fill="both", expand=True)

        # Configuración de columnas y encabezados del Treeview
        self.treeview["columns"] = ("ID", "Nombre", "Dirección", "Teléfono", "Compras Realizadas")
        self.treeview.column("#0", width=50)
        self.treeview.column("ID", width=100)
        self.treeview.column("Nombre", width=200)
        self.treeview.column("Dirección", width=200)
        self.treeview.column("Teléfono", width=150)
        self.treeview.column("Compras Realizadas", width=150)

        self.treeview.heading("#0", text="Índice")
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Dirección", text="Dirección")
        self.treeview.heading("Teléfono", text="Teléfono")
        self.treeview.heading("Compras Realizadas", text="Compras Realizadas")

        # Obtención de datos de CLIENTES y llenado del Treeview
        clientes = self.cliente_negocio.obtener_clientes()

        for i, cliente in enumerate(clientes):
            self.treeview.insert("", "end", text=i, values=(cliente.id, cliente.nombre, cliente.direccion, cliente.telefono, cliente.compras_realizadas))

        # Creación de botones y etiquetas
        detalle_button = ttk.Button(self.content_frame, text="Mostrar Detalle", command=self.mostrar_detalle_cliente)
        detalle_button.pack(pady=10)

        nuevo_cliente_button = ttk.Button(self.content_frame, text="Nuevo Registro", command=self.nuevo_cliente)
        nuevo_cliente_button.pack(pady=10)

        editar_cliente_button = ttk.Button(self.content_frame, text="Editar Registro", command=self.editar_cliente)
        editar_cliente_button.pack(pady=10)

        eliminar_cliente_button = ttk.Button(self.content_frame, text="Eliminar Registro", command=self.eliminar_cliente)
        eliminar_cliente_button.pack(pady=10)

        # Etiqueta para mostrar detalles de CLIENTES
        self.detalle_label = ttk.Label(self.content_frame, text="")
        self.detalle_label.pack(padx=20, pady=20)

    # Función para mostrar el detalle de un CLIENTE seleccionado
    def mostrar_detalle_cliente(self):
        seleccionado = self.treeview.selection()
        if seleccionado:
            indice = int(self.treeview.item(seleccionado)['text'])
            cliente = self.cliente_negocio.obtener_clientes()[indice]
            self.detalle_label.config(text=f"ID: {cliente.id}\nNombre: {cliente.nombre}\nDirección: {cliente.direccion}\nTeléfono: {cliente.telefono}\nCompras Realizadas: {cliente.compras_realizadas}")
        else:
            self.detalle_label.config(text="Seleccione un cliente")

    # Función para agregar un nuevo CLIENTE
    def nuevo_cliente(self):
        self.limpiar_contenido()
        # Etiquetas y campos de entrada
        self.id_label = ttk.Label(self.content_frame, text="ID:")
        self.id_label.pack()
        self.id_entry = ttk.Entry(self.content_frame)
        self.id_entry.pack()

        self.nombre_label = ttk.Label(self.content_frame, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = ttk.Entry(self.content_frame)
        self.nombre_entry.pack()

        self.direccion_label = ttk.Label(self.content_frame, text="Dirección:")
        self.direccion_label.pack()
        self.direccion_entry = ttk.Entry(self.content_frame)
        self.direccion_entry.pack()

        self.telefono_label = ttk.Label(self.content_frame, text="Teléfono:")
        self.telefono_label.pack()
        self.telefono_entry = ttk.Entry(self.content_frame)
        self.telefono_entry.pack()

        guardar_button = ttk.Button(self.content_frame, text="Guardar", command=self.guardar_cliente)
        guardar_button.pack()

        salir_button = ttk.Button(self.content_frame, text="Cancelar")
        salir_button.pack()
        
    # Función para editar un CLIENTE existente
    def editar_cliente(self):
        seleccionado = self.treeview.selection()
        if seleccionado:
            self.indice_cliente = int(self.treeview.item(seleccionado)['text'])
            self.editar_cliente_fr()
        else:
            self.detalle_label.config(text="Seleccione un cliente")

    # Función para mostrar el formulario de edición de CLIENTE
    def editar_cliente_fr(self):
        self.limpiar_contenido()
        cliente = self.listado_clientes[self.indice_cliente]

        self.id_label = ttk.Label(self.content_frame, text="ID:")
        self.id_label.pack()
        self.id_entry = ttk.Entry(self.content_frame)
        self.id_entry.pack()
        self.id_entry.insert(0, cliente.id)

        self.nombre_label = ttk.Label(self.content_frame, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = ttk.Entry(self.content_frame)
        self.nombre_entry.pack()
        self.nombre_entry.insert(0, cliente.nombre)

        self.direccion_label = ttk.Label(self.content_frame, text="Dirección:")
        self.direccion_label.pack()
        self.direccion_entry = ttk.Entry(self.content_frame)
        self.direccion_entry.pack()
        self.direccion_entry.insert(0, cliente.direccion)

        self.telefono_label = ttk.Label(self.content_frame, text="Teléfono:")
        self.telefono_label.pack()
        self.telefono_entry = ttk.Entry(self.content_frame)
        self.telefono_entry.pack()
        self.telefono_entry.insert(0, cliente.telefono)

        editar_button = ttk.Button(self.content_frame, text="Guardar", command=self.editar_registro_cliente)
        editar_button.pack()

        salir_button = ttk.Button(self.content_frame, text="Cancelar")
        salir_button.pack()

    # Función para guardar un nuevo Cliente o actualizar uno existente
    def guardar_cliente(self):
        id = self.id_entry.get()
        nombre = self.nombre_entry.get()
        direccion = self.direccion_entry.get()
        telefono = self.telefono_entry.get()

        # Llama a la función registrar_cliente
        reg = self.cliente_negocio.registrar_cliente(id, nombre, direccion, telefono)
        reg = self.cliente_negocio.guardar_clientes()
        print(f"Guardado en el Excel: {reg}")

        self.listado_clientes = self.cliente_negocio.obtener_clientes()
        self.mostrar_contenido_opcion_cliente()         # Muestra el contenido de la opción "Clientes"

    # Función para editar un registro de CLIENTE
    def editar_registro_cliente (self):
        id = self.id_entry.get()
        nombre = self.nombre_entry.get()
        direccion = self.direccion_entry.get()
        telefono = self.telefono_entry.get()

        reg = self.cliente_negocio.editar_cliente(self.indice_cliente, id, nombre, direccion, telefono)
        print(f"Editado en el Excel: {reg}")
        self.listado_clientes = self.cliente_negocio.obtener_clientes()
        self.mostrar_contenido_opcion_cliente()

    # Función para eliminar un CLIENTE
    def eliminar_cliente(self):
        seleccionado = self.treeview.selection()
        if seleccionado:
            indice = int(self.treeview.item(seleccionado)['text'])
            mensaje = self.cliente_negocio.eliminar_cliente(indice)
            self.detalle_label.config(text=mensaje)
            self.mostrar_contenido_opcion_cliente()
        else:
            self.detalle_label.config(text="Seleccione un cliente")


#CONTENIDO PRODUCTO---------------------------------------------------------

    def mostrar_contenido_opcion_producto(self):
        self.limpiar_contenido()# Limpia el contenido anterior
        # Crea un objeto Treeview para mostrar datos
        self.treeview = ttk.Treeview(self.content_frame)
        self.treeview.pack(fill="both", expand=True)

        # Configuración de columnas y encabezados del Treeview
        self.treeview["columns"] = ("ID", "Nombre", "Precio", "Marca", "Modelo", "Descripción", "Disponible")
        self.treeview.column("#0", width=50)
        self.treeview.column("ID", width=100)
        self.treeview.column("Nombre", width=200)
        self.treeview.column("Precio", width=100)
        self.treeview.column("Marca", width=100)
        self.treeview.column("Modelo", width=100)
        self.treeview.column("Descripción", width=200)
        self.treeview.column("Disponible", width=100)

        self.treeview.heading("#0", text="Índice")
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Precio", text="Precio")
        self.treeview.heading("Marca", text="Marca")
        self.treeview.heading("Modelo", text="Modelo")
        self.treeview.heading("Descripción", text="Descripción")
        self.treeview.heading("Disponible", text="Disponible")

        # Obtención de datos de PRODUCTOS y llenado del Treeview
        productos = self.producto_negocio.obtener_productos()

        for i, producto in enumerate(productos):
            self.treeview.insert("", "end", text=i, values=(producto.id, producto.nombre, producto.precio, producto.marca, producto.modelo, producto.descripcion, producto.disponible))

        # Creación de botones y etiquetas
        detalle_button = ttk.Button(self.content_frame, text="Mostrar Detalle", command=self.mostrar_detalle_producto)
        detalle_button.pack(pady=10)

        nuevo_producto_button = ttk.Button(self.content_frame, text="Nuevo Registro", command=self.nuevo_producto)
        nuevo_producto_button.pack(pady=10)

        editar_producto_button = ttk.Button(self.content_frame, text="Editar Registro", command=self.editar_producto)
        editar_producto_button.pack(pady=10)

        eliminar_producto_button = ttk.Button(self.content_frame, text="Eliminar Registro", command=self.eliminar_producto)
        eliminar_producto_button.pack(pady=10)

        # Etiqueta para mostrar detalles de PRODUCTO
        self.detalle_label = ttk.Label(self.content_frame, text="")
        self.detalle_label.pack(padx=20, pady=20)

    # Función para mostrar el detalle de un PRODUCTO seleccionado
    def mostrar_detalle_producto(self):
        seleccionado = self.treeview.selection()
        if seleccionado:
            indice = int(self.treeview.item(seleccionado)['text'])
            producto = self.producto_negocio.obtener_productos()[indice]
            self.detalle_label.config(text=f"ID: {producto.id}\nNombre: {producto.nombre}\nPrecio: {producto.precio}\nMarca: {producto.marca}\nModelo: {producto.modelo}\nDescripción: {producto.descripcion}\nDisponible: {producto.disponible}")
        else:
            self.detalle_label.config(text="Seleccione un producto")

    # Función para agregar un nuevo PRODUCTO
    def nuevo_producto(self):
        self.limpiar_contenido()
        # Etiquetas y campos de entrada
        self.id_label = ttk.Label(self.content_frame, text="ID:")
        self.id_label.pack()
        self.id_entry = ttk.Entry(self.content_frame)
        self.id_entry.pack()

        self.nombre_label = ttk.Label(self.content_frame, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = ttk.Entry(self.content_frame)
        self.nombre_entry.pack()

        self.precio_label = ttk.Label(self.content_frame, text="Precio:")
        self.precio_label.pack()
        self.precio_entry = ttk.Entry(self.content_frame)
        self.precio_entry.pack()

        self.marca_label = ttk.Label(self.content_frame, text="Marca:")
        self.marca_label.pack()
        self.marca_entry = ttk.Entry(self.content_frame)
        self.marca_entry.pack()

        self.modelo_label = ttk.Label(self.content_frame, text="Modelo:")
        self.modelo_label.pack()
        self.modelo_entry = ttk.Entry(self.content_frame)
        self.modelo_entry.pack()

        self.descripcion_label = ttk.Label(self.content_frame, text="Descripción:")
        self.descripcion_label.pack()
        self.descripcion_entry = ttk.Entry(self.content_frame)
        self.descripcion_entry.pack()

        self.disponible_label = ttk.Label(self.content_frame, text="Disponible:")
        self.disponible_label.pack()
        self.disponible_entry = ttk.Entry(self.content_frame)
        self.disponible_entry.pack()

        guardar_button = ttk.Button(self.content_frame, text="Guardar", command=self.guardar_producto)
        guardar_button.pack()

        salir_button = ttk.Button(self.content_frame, text="Cancelar")
        salir_button.pack()

    # Función para editar un PRODUCTO existente
    def editar_producto(self):
        seleccionado = self.treeview.selection()
        if seleccionado:
            self.indice_producto = int(self.treeview.item(seleccionado)['text'])
            self.editar_producto_fr()
        else:
            self.detalle_label.config(text="Seleccione un producto")

    # Función para mostrar el formulario de edición de PRODUCTO
    def editar_producto_fr(self):
        self.limpiar_contenido()
        producto = self.listado_productos[self.indice_producto]

        self.id_label = ttk.Label(self.content_frame, text="ID:")
        self.id_label.pack()
        self.id_entry = ttk.Entry(self.content_frame)
        self.id_entry.pack()
        self.id_entry.insert(0, producto.id)

        self.nombre_label = ttk.Label(self.content_frame, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = ttk.Entry(self.content_frame)
        self.nombre_entry.pack()
        self.nombre_entry.insert(0, producto.nombre)

        self.precio_label = ttk.Label(self.content_frame, text="Precio:")
        self.precio_label.pack()
        self.precio_entry = ttk.Entry(self.content_frame)
        self.precio_entry.pack()
        self.precio_entry.insert(0, producto.precio)

        self.marca_label = ttk.Label(self.content_frame, text="Marca:")
        self.marca_label.pack()
        self.marca_entry = ttk.Entry(self.content_frame)
        self.marca_entry.pack()
        self.marca_entry.insert(0, producto.marca)

        self.modelo_label = ttk.Label(self.content_frame, text="Modelo:")
        self.modelo_label.pack()
        self.modelo_entry = ttk.Entry(self.content_frame)
        self.modelo_entry.pack()
        self.modelo_entry.insert(0, producto.modelo)

        self.descripcion_label = ttk.Label(self.content_frame, text="Descripción:")
        self.descripcion_label.pack()
        self.descripcion_entry = ttk.Entry(self.content_frame)
        self.descripcion_entry.pack()
        self.descripcion_entry.insert(0, producto.descripcion)

        self.disponible_label = ttk.Label(self.content_frame, text="Disponible:")
        self.disponible_label.pack()
        self.disponible_entry = ttk.Entry(self.content_frame)
        self.disponible_entry.pack()
        self.disponible_entry.insert(0, producto.disponible)

        guardar_button = ttk.Button(self.content_frame, text="Guardar Cambios", command=self.editar_registro_producto)
        guardar_button.pack()

        salir_button = ttk.Button(self.content_frame, text="Cancelar", command=self.mostrar_contenido_opcion_producto)
        salir_button.pack()

    # Función para guardar un nuevo PRODUCTO o actualizar uno existente
    def guardar_producto(self):
        id = self.id_entry.get()
        nombre = self.nombre_entry.get()
        precio = self.precio_entry.get()
        marca = self.marca_entry.get()
        modelo = self.modelo_entry.get()
        descripcion = self.descripcion_entry.get()
        disponible = self.disponible_entry.get()

        # Llama a la función registrar_producto
        self.producto_negocio.registrar_producto(id, nombre, precio, marca, modelo, descripcion, disponible)
        self.producto_negocio.guardar_productos()
        # Muestra el contenido de la opción "Producto"
        self.mostrar_contenido_opcion_producto()

    # Función para editar un registro de PRODUCTO
    def editar_registro_producto(self):
        id = self.id_entry.get()
        nombre = self.nombre_entry.get()
        precio = self.precio_entry.get()
        marca = self.marca_entry.get()
        modelo = self.modelo_entry.get()
        descripcion = self.descripcion_entry.get()
        disponible = self.disponible_entry.get()

        self.producto_negocio.editar_producto(self.indice_producto, id, nombre, precio, marca, modelo, descripcion, disponible)
        self.producto_negocio.guardar_productos()
        self.mostrar_contenido_opcion_producto()

    # Función para eliminar un autor
    def eliminar_producto(self):
        seleccionado = self.treeview.selection()
        if seleccionado:
            indice = int(self.treeview.item(seleccionado)['text'])
            mensaje = self.producto_negocio.eliminar_producto(indice)
            self.detalle_label.config(text=mensaje)
            self.mostrar_contenido_opcion_producto()
        else:
            self.detalle_label.config(text="Seleccione un producto")

#-------------------------------------------------------------------------------------------#
    # Limpiar el contenido actual
    def limpiar_contenido(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        self.treeview = None
        self.detalle_label = ttk.Label(self.content_frame, text="")
        self.detalle_label.pack(padx=10, pady=10, fill="both", expand=True)


# Crear la ventana principal
root = tk.Tk()
app = MainMenuApp(root)
root.mainloop()
